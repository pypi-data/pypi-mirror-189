
""" Headline: Anomaly Processing Inline Inspection Anomaly Growth Calculation tool
    Calls:  pimsilitool, pimsilitool.config
    inputs: ILI Feature class(Which is calibrated and imported)
    Description: This tool calculates Anomaly Growth.  
    Output: The output of this tool.
   """

import arcpy
import pimsilitool
import os
from pimsilitool import config
import sys
from datetime import datetime
from pimsilitool.license.validate_license.license_operation import LicenseOperation


class AnomalyGrowthCalculator(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ILI Anomaly Growth Calculator"
        self.description = "This Tool Calculates Anomaly Growth"
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):

        # Input ILI point featuere - Parameter [0]
        in_anomaly_matches_rows = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_ANOMALY_MATCHES,
                                        displayName="Input ILI Anomaly Matches Rows",
                                        name="in_ili_features",
                                        datatype=["GPFeatureLayer","GPTableView"],
                                        parameterType="Required",
                                        direction="Input")

        # Parameter [0]
        in_parent_features = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES,
                                            displayName="Input ILI Anomaly Parent Features",
                                            name="in_parent_features",
                                            datatype="GPFeatureLayer",
                                            parameterType="Required",
                                            direction="Input")
        # Parameter [0]
        in_parent_uniqueid_field = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES,
                                            displayName="ILI Anomaly Parent Unique ID Field",
                                            name="in_parent_uniqueid_field",
                                            datatype="Field", parameterType="Required", direction="Input")
        in_parent_uniqueid_field.parameterDependencies = [in_parent_features.name]

        # Parameter [0]
        in_parent_depth_field = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES,
                                             displayName="ILI Anomaly Parent Depth Percent Field",
                                             name="in_parent_depth_field",
                                             datatype="Field", parameterType="Required", direction="Input")
        in_parent_depth_field.parameterDependencies = [in_parent_features.name]
        in_parent_depth_field.filter.list = ['int', 'long', 'double']

        # Parameter [0]
        in_parent_tool_accuracy = arcpy.Parameter(category=config.ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES,
                                                displayName="Parent Tool Accuracy (%)",
                                                name="in_parent_tool_accuracy",
                                                datatype="GPDouble", parameterType="Optional", direction="Input")
        in_parent_tool_accuracy.value = 0

        # Parameter [0]
        in_parent_tool_run_date = arcpy.Parameter(category=config.ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES,
                                                  displayName="Parent Tool Run Date",
                                                  name="in_parent_tool_run_date",
                                                  datatype="GPDate", parameterType="Optional", direction="Input")

        # in_parent_tool_run_date.filter.list = ['int', 'long', 'double']

        # Parameter [0]
        in_child_features = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES,
                                                displayName="Input ILI Anomaly Child Features",
                                                name="in_child_features",
                                                datatype="GPFeatureLayer",
                                                parameterType="Required",
                                                direction="Input")
        # Parameter [0]
        in_child_uniqueid_field = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES,
                                            displayName="ILI Anomaly Child Unique ID Field",
                                            name="in_child_uniqueid_field",
                                            datatype="Field", parameterType="Required", direction="Input")
        in_child_uniqueid_field.parameterDependencies = [in_child_features.name]

        # Parameter [0]
        in_child_depth_field = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES,
                                             displayName="ILI Anomaly Child Depth Percent Field",
                                             name="in_child_depth_field",
                                             datatype="Field", parameterType="Required", direction="Input")
        in_child_depth_field.parameterDependencies = [in_child_features.name]
        in_child_depth_field.filter.list = ['int', 'long', 'double']

        # Parameter [0]
        in_child_tool_accuracy = arcpy.Parameter(category=config.ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES,
                                                  displayName="Child Tool Accuracy (%)",
                                                  name="in_child_tool_accuracy",
                                                  datatype="GPDouble", parameterType="Optional", direction="Input")
        in_child_tool_accuracy.value = 0

        # Parameter [0]
        in_child_tool_run_date = arcpy.Parameter(category=config.ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES,
                                                  displayName="Child Tool Run Date",
                                                  name="in_child_tool_run_date",
                                                  datatype="GPDate", parameterType="Optional", direction="Input")

        # Parameter [0]
        in_calc_direction = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_DEFAULT,
                                            displayName="ILI Anomaly Direction of Calculations",
                                            name="in_calc_direction",
                                            datatype="GPString", parameterType="Required", direction="Input")

        in_calc_direction.filter.list = config.ANOMALY_GROWTH_CALC_DIRECTION
        in_calc_direction.value = config.ANOMALY_GROWTH_CALC_DIRECTION[0]

        in_is_unmatched_child = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_DEFAULT,
                                            displayName="Generate Unmatched Child Anomaly Growth Table",
                                            name="in_is_unmatched_child",
                                            datatype="GPBoolean", parameterType="Optional", direction="Input")
        in_is_unmatched_child.value = False

        # Parameter [0]
        out_growth_table = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_OUTPUT,
                                            displayName="Output Anomaly Growth Table",
                                            name="out_growth_table",
                                            datatype="GPTableView", parameterType="Required", direction="Output")

        out_unmatched_child_table = arcpy.Parameter(category = config.ANOMALY_GROWTH_CATEGORY_OUTPUT,
                                            displayName="Output Unmatched Child Anomaly Growth Table",
                                            name="out_unmatched_child_table",
                                            datatype="GPTableView", parameterType="Optional", direction="Output")
        out_unmatched_child_table.enabled = False

        parameters = [in_anomaly_matches_rows,
                      in_parent_features, in_parent_uniqueid_field, in_parent_depth_field, in_parent_tool_accuracy, in_parent_tool_run_date,
                      in_child_features, in_child_uniqueid_field, in_child_depth_field, in_child_tool_accuracy, in_child_tool_run_date,
                      in_calc_direction, in_is_unmatched_child, out_growth_table, out_unmatched_child_table
                      ]

        return parameters

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):

        # output feature class names
        if parameters[0].value and not parameters[0].hasBeenValidated:
            catalogPath = arcpy.da.Describe(parameters[0].value)["catalogPath"]
            if not parameters[13].value:
                parameters[13].value = os.path.join(os.path.dirname(catalogPath), config.ANOMALY_GROWTH_OUTPUT_TABLE_NAME)

        if parameters[0].value is None:
            parameters[13].value = None

        # parent unique id, depth fields
        if parameters[1].value and not parameters[1].hasBeenValidated:
            if not parameters[2].value:
                parameters[2].value = config.ANOMALY_GROWTH_ANOMALY_FIELDS[0]
            if not parameters[3].value:
                parameters[3].value = config.ANOMALY_GROWTH_ANOMALY_FIELDS[1]
        if parameters[1].value is None:
            parameters[2].value = parameters[3].value = None

        # child unique id, depth fields
        if parameters[6].value and not parameters[6].hasBeenValidated:
            if not parameters[7].value:
                parameters[7].value = config.ANOMALY_GROWTH_ANOMALY_FIELDS[0]
            if not parameters[8].value:
                parameters[8].value = config.ANOMALY_GROWTH_ANOMALY_FIELDS[1]

        if parameters[6].value is None:
            parameters[7].value = parameters[8].value = None

        if parameters[12].value:
            if parameters[0].value:
                catalogPath = arcpy.da.Describe(parameters[0].value)["catalogPath"]
                if not parameters[14].value:
                    parameters[14].value = os.path.join(os.path.dirname(catalogPath), config.ANOMALY_GROWTH_OUTPUT_UNMATCHED_TABLE_NAME)
            parameters[14].enabled = True
        else:
            parameters[14].value = None
            parameters[14].enabled = False
        # parameters[14].enabled = parameters[12].value

        return

    def updateMessages(self, parameters):

        if parameters[12].value and not parameters[14].value:
            parameters[14].setErrorMessage("Output table cab not be empty.")

        return

    def execute(self, parameters, messages):
               
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting Anomaly Growth Calculator process...")

        try:
            in_anomaly_matches_rows  = parameters[0].value
            in_parent_features  = parameters[1].value
            in_parent_uniqueid_field  = parameters[2].valueAsText
            in_parent_depth_field = parameters[3].valueAsText
            in_parent_tool_accuracy = float(parameters[4].valueAsText)
            in_parent_tool_run_date = parameters[5].value
            in_child_features  = parameters[6].value
            in_child_uniqueid_field = parameters[7].valueAsText
            in_child_depth_field = parameters[8].valueAsText
            in_child_tool_accuracy = float(parameters[9].valueAsText)
            in_child_tool_run_date = parameters[10].value
            in_calc_direction = parameters[11].valueAsText
            in_is_unmatched_child = parameters[12].value
            out_growth_table  = parameters[13].valueAsText
            out_unmatched_child_table = parameters[14].valueAsText

            parent_unique_fld = "PARENT_" + in_parent_uniqueid_field
            parent_depth_fld = "PARENT_" + in_parent_depth_field

            child_unique_fld = "CHILD_" + in_child_uniqueid_field
            child_depth_fld = "CHILD_" + in_child_depth_field

            flds = []
            flds += [f.name.upper() for f in arcpy.ListFields(in_anomaly_matches_rows)]

            # check if parent unique id fields exit in the input anomaly matches table
            if parent_unique_fld.upper() not in flds:
                pimsilitool.AddMessage("Field {} does not exist in the input ILI Anomaly Matches Rows".format(parent_unique_fld))
                return

            # check if child unique id fields exit in the input anomaly matches table
            if child_unique_fld.upper() not in flds:
                pimsilitool.AddMessage("Field {} does not exist in the input ILI Anomaly Matches Rows".format(child_unique_fld))
                return

            temp_rows1 = os.path.join(arcpy.env.scratchGDB, "TempRows1")
            if arcpy.Exists(temp_rows1):
                arcpy.Delete_management(temp_rows1)

            arcpy.CopyRows_management(in_anomaly_matches_rows, temp_rows1)

            # delete fields if exist
            for fld in [in_parent_depth_field, in_child_depth_field]:
                if fld.upper() in flds:
                    arcpy.DeleteField_management(temp_rows1, fld)

            # join parent dataset
            pimsilitool.AddMessage("Join parent features to input anomaly matches...")
            arcpy.JoinField_management(temp_rows1, parent_unique_fld, in_parent_features, in_parent_uniqueid_field, [in_parent_depth_field])
            arcpy.AlterField_management(temp_rows1, in_parent_depth_field, parent_depth_fld, parent_depth_fld)

            # join child dataset
            pimsilitool.AddMessage("Join child features input anomaly matches...")

            arcpy.JoinField_management(temp_rows1, child_unique_fld, in_child_features, in_child_uniqueid_field, [in_child_depth_field])
            arcpy.AlterField_management(temp_rows1, in_child_depth_field, child_depth_fld, child_depth_fld)
            # flds = []
            # flds += [f.name.upper() for f in arcpy.ListFields(temp_rows1)]

            temp_rows2 = os.path.join(arcpy.env.scratchGDB, "TempRows2")
            if arcpy.Exists(temp_rows2):
                arcpy.Delete_management(temp_rows2)
            arcpy.CopyRows_management(temp_rows1, temp_rows2)

            # generate statistics
            stats = []
            temp_rows3 = os.path.join(arcpy.env.scratchGDB, "TempRows3")
            if arcpy.Exists(temp_rows3):
                arcpy.Delete_management(temp_rows3)

            arcpy.CopyRows_management(temp_rows2, temp_rows3)

            if in_calc_direction == config.ANOMALY_GROWTH_CALC_DIRECTION[1]:
                casefield = child_unique_fld

                # Loop through all fields in the Input Table
                # for field in stat_field_list:
                stats.append([child_depth_fld, "FIRST"])
                stats.append([parent_depth_fld, "MIN"])
                stats.append([parent_depth_fld, "MAX"])
                stats.append([parent_depth_fld, "MEAN"])
                stats.append([parent_depth_fld, "STD"])
                stats.append([parent_depth_fld, "COUNT"])
                in_fields = ["FIRST_CHILD_" + in_child_depth_field,
                               "MAX_PARENT_"+ in_parent_depth_field,
                               "MEAN_PARENT_"+ in_parent_depth_field
                               ]
            else:
                casefield = parent_unique_fld
                # Loop through all fields in the Input Table
                # for field in stat_field_list:
                stats.append([parent_depth_fld, "FIRST"])
                stats.append([child_depth_fld, "MIN"])
                stats.append([child_depth_fld, "MAX"])
                stats.append([child_depth_fld, "MEAN"])
                stats.append([child_depth_fld, "STD"])
                stats.append([child_depth_fld, "COUNT"])
                in_fields = ["FIRST_PARENT_" + in_parent_depth_field,
                               "MAX_CHILD_" + in_child_depth_field,
                               "MEAN_CHILD_"+ in_child_depth_field
                               ]

            # Run the Summary Statistics tool with the stats list
            pimsilitool.AddMessage("Calculating statistics...")

            temp_rows4 = os.path.join(arcpy.env.scratchGDB, "TempRows4")
            if arcpy.Exists(temp_rows4):
                arcpy.Delete_management(temp_rows4)

            arcpy.Statistics_analysis(temp_rows3, temp_rows4, stats, casefield)

            pimsilitool.AddMessage("Calculating anomaly percent growth...")

            anomaly_growth_fields = [
                                    ["PARENT_TOOL_ACCURACY", "DOUBLE", "Parent Tool Accuracy (%)", None],
                                    ["PARENT_DEPTH_UNCERTAINTY", "DOUBLE", "Parent Depth Uncertainty (%)", None],
                                    ["PARENT_TOOL_RUN_DATE", "DATE", "Parent Tool Run Date", None],

                                    ["CHILD_TOOL_ACCURACY", "DOUBLE", "Child Tool Accuracy (%)", None],
                                    ["CHILD_DEPTH_UNCERTAINTY", "DOUBLE", "Child Depth Uncertainty (%)", None],
                                    ["CHILD_TOOL_RUN_DATE", "DATE", "Child Tool Run Date", None],

                                    ["PERCENTAGE_GROWTH", "DOUBLE", "Percentage Growth (%)", None],
                                    ["MEAN_PERCENTAGE_GROWTH", "DOUBLE", "Mean Percentage Growth (%)", None],
                                    ["ANNUAL_GROWTH_RATE", "DOUBLE", "Annual Growth Rate (%)", None],
                                    ["MEAN_ANNUAL_GROWTH_RATE", "DOUBLE", "Mean Annual Growth Rate (%)", None],

                                    ["WORST_CASE_GROWTH", "DOUBLE", "Worst Case Growth (%)", None],
                                    ["WORST_CASE_MEAN_GROWTH", "DOUBLE", "Worst Case Mean Growth (%)", None],
                                    ["WORST_CASE_ANNUAL_GROWTH", "DOUBLE", "Worst Case Annual Growth (%)", None],
                                    ["WORST_CASE_MEAN_ANNUAL_GROWTH", "DOUBLE", "Worst Case Mean Annual Growth (%)", None]
                                    ]

            arcpy.AddFields_management(temp_rows4, anomaly_growth_fields)
            # new_field_alias
            added_fields = [
                            "PARENT_TOOL_ACCURACY", "PARENT_DEPTH_UNCERTAINTY", "PARENT_TOOL_RUN_DATE",
                            "CHILD_TOOL_ACCURACY", "CHILD_DEPTH_UNCERTAINTY", "CHILD_TOOL_RUN_DATE",
                            "PERCENTAGE_GROWTH", "MEAN_PERCENTAGE_GROWTH", "ANNUAL_GROWTH_RATE", "MEAN_ANNUAL_GROWTH_RATE",
                            "WORST_CASE_GROWTH", "WORST_CASE_MEAN_GROWTH", "WORST_CASE_ANNUAL_GROWTH","WORST_CASE_MEAN_ANNUAL_GROWTH"
                            ]

            field_names = in_fields + added_fields

            d1 = datetime.strptime(str(in_parent_tool_run_date).split(" ")[0], "%Y-%m-%d")
            d2 = datetime.strptime(str(in_child_tool_run_date).split(" ")[0], "%Y-%m-%d")

            run_date_diff = abs((d2 - d1).days)
            run_date_diff_years = float(run_date_diff / 365)

            with arcpy.da.UpdateCursor(temp_rows4, field_names) as cursor:
                for row in cursor:
                    # parent tool accuracy
                    row[3] = in_parent_tool_accuracy

                    # parent depth uncertainty
                    try:
                        parent_depth = float(row[0])
                        child_depth = float(row[1])
                        child_mean_depth = float(row[2])
                    except Exception as e:
                        pimsilitool.AddError("Something went wrong in joining the Input Anomaly Matches Rows and Anomaly Parent/Child Features using Unique ID Field values.")
                        pimsilitool.AddError("Please check Unique ID values in Anomaly Matches Rows, ILI Anomaly Parent Features and ILI Anomaly Child Features.")
                        raise

                    parent_depth = float(row[0])
                    parent_depth_uncertainity = parent_depth * in_parent_tool_accuracy / 100
                    row[4] = parent_depth_uncertainity

                    # parent tool run date
                    row[5] = in_parent_tool_run_date

                    # child tool accuracy
                    row[6] = in_child_tool_accuracy

                    # child depth uncertainty
                    child_depth = float(row[1])
                    child_depth_uncertainity = child_depth * in_child_tool_accuracy / 100
                    row[7] = child_depth_uncertainity

                    # child tool run date
                    row[8] = in_child_tool_run_date

                    # percentage growth
                    pct_growth = ((child_depth - parent_depth) / parent_depth) * 100
                    row[9] = pct_growth

                    # annual growth rate
                    row[11] = float(pct_growth) / run_date_diff_years

                    # calculated mean percent
                    child_mean_depth = float(row[2])
                    pct_growth_mean = ((child_mean_depth - parent_depth) / parent_depth) * 100
                    row[10] = pct_growth_mean

                    # annual growth rate mean
                    row[12] = float(pct_growth_mean) / run_date_diff_years

                    # worst case growth
                    worst_pct_growth = (((child_depth + child_depth_uncertainity) - (parent_depth - parent_depth_uncertainity)) / (parent_depth - parent_depth_uncertainity)) * 100
                    row[13] = worst_pct_growth

                    # annual worst case growth
                    row[15] = float(worst_pct_growth) / run_date_diff_years

                    # worst case mean growth
                    worst_pct_mean_growth = (((child_mean_depth + child_depth_uncertainity) - (parent_depth - parent_depth_uncertainity)) / (parent_depth - parent_depth_uncertainity)) * 100
                    row[14] = worst_pct_mean_growth

                    # annual worst case mean growth
                    row[16] = float(worst_pct_mean_growth) / run_date_diff_years

                    cursor.updateRow(row)

            arcpy.CopyRows_management(temp_rows4, out_growth_table)

            flds = []
            flds += [f.name.upper() for f in arcpy.ListFields(out_growth_table)]

            pimsilitool.AddMessage("Altering statistics field names...")

            # Fields used in ILI Anomaly Direction: Calculate statistics for child anomalies
            if parent_unique_fld.upper() in flds:
                arcpy.AlterField_management(out_growth_table, parent_unique_fld, parent_unique_fld[0:30], "Parent Unique ID")
            if "FREQUENCY" in flds:
                arcpy.AlterField_management(out_growth_table, "FREQUENCY", new_field_alias="Frequency")
            if ("FIRST_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, "FIRST_PARENT_" + in_parent_depth_field, ("PARENT_" + in_parent_depth_field)[0:30], "Parent Depth (%)")

            if ("MIN_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("MIN_CHILD_" + in_child_depth_field), ("MIN_CHILD_" + in_child_depth_field)[0:30], "Minimum Child Depth %")
            if ("MAX_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, "MAX_CHILD_" + in_child_depth_field, ("MAX_CHILD_" + in_child_depth_field)[0:30], "Maximum Child Depth %")
            if ("MEAN_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("MEAN_CHILD_" + in_child_depth_field), ("MEAN_CHILD_" + in_child_depth_field)[0:30], "Mean Child Depth %")
            if ("STD_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("STD_CHILD_" + in_child_depth_field), ("StdDev_CHILD_" + in_child_depth_field)[0:30], "Child Depth % Std. Deviation")
            if ("COUNT_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("COUNT_CHILD_" + in_child_depth_field), "Child_Count", "Child Count")

            # Fields used in ILI Anomaly Direction: Calculate statistics for parent anomalies
            if child_unique_fld.upper() in flds:
                arcpy.AlterField_management(out_growth_table, child_unique_fld, child_unique_fld[0:30], "Child Unique ID")
            if ("FIRST_CHILD_" + in_child_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, "FIRST_CHILD_" + in_child_depth_field, ("CHILD_" + in_child_depth_field)[0:30], "Child Depth (%)")

            if ("MIN_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("MIN_PARENT_" + in_parent_depth_field), ("MIN_PARENT_" + in_parent_depth_field)[0:30], "Minimum Parent Depth %" )
            if ("MAX_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("MAX_PARENT_" + in_parent_depth_field), ("MAX_PARENT_" + in_parent_depth_field)[0:30], "Maximum Parent Depth %")
            if ("MEAN_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("MEAN_PARENT_" + in_parent_depth_field), ("MEAN_PARENT_" + in_parent_depth_field)[0:30],  "Mean Parent Depth %")
            if ("STD_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("STD_PARENT_" + in_parent_depth_field), ("StdDev_PARENT_" + in_parent_depth_field)[0:30], "Parent Depth % Std. Deviation")
            if ("COUNT_PARENT_" + in_parent_depth_field).upper() in flds:
                arcpy.AlterField_management(out_growth_table, ("COUNT_PARENT_" + in_parent_depth_field), "PARENT_Count", "Parent Count")

            if in_is_unmatched_child:
                self.create_output_unmatched_child_table(in_child_features, in_anomaly_matches_rows, out_unmatched_child_table,
                                                         child_unique_fld, child_depth_fld,
                                                         in_child_uniqueid_field, in_child_depth_field,
                                                         in_child_tool_accuracy, in_child_tool_run_date, run_date_diff_years)

            arcpy.Delete_management(temp_rows1)
            arcpy.Delete_management(temp_rows2)
            arcpy.Delete_management(temp_rows3)
            arcpy.Delete_management(temp_rows4)

            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def create_output_unmatched_child_table(self, in_child_features, in_anomaly_matches_rows, out_unmatched_child_table, child_unique_fld, child_depth_fld,
                                            in_child_uniqueid_field, in_child_depth_field, in_child_tool_accuracy, in_child_tool_run_date, run_date_diff_years
                                            ):
        try:

            unmatched_child_fields = [
                [child_unique_fld, "GUID", "Child Unique ID", None],
                [child_depth_fld, "DOUBLE", "Child Depth %", None],
                ["CHILD_TOOL_ACCURACY", "DOUBLE", "Child Tool Accuracy (%)", None],
                ["CHILD_DEPTH_UNCERTAINTY", "DOUBLE", "Child Depth Uncertainty (%)", None],
                ["WORST_CASE_" + child_depth_fld, "DOUBLE", "Worst Case Child Depth %", None],
                ["CHILD_TOOL_RUN_DATE", "DATE", "Child Tool Run Date", None],
                ["ANNUAL_GROWTH_RATE", "DOUBLE", "Annual Growth Rate (%)", None],
                ["WORST_CASE_ANNUAL_GROWTH", "DOUBLE", "Worst Case Annual Growth (%)", None]

            ]

            if arcpy.Exists(out_unmatched_child_table):
                arcpy.Delete_management(out_unmatched_child_table)
            arcpy.CreateTable_management(os.path.dirname(out_unmatched_child_table), os.path.basename(out_unmatched_child_table))

            arcpy.AddFields_management(out_unmatched_child_table, unmatched_child_fields)

            pimsilitool.AddMessage("Creating output unmatched child anomaly growth table...")

            # get unique id values in in_anomaly_matches_rows
            unique_values = self.unique_values(in_anomaly_matches_rows, child_unique_fld)


            pimsilitool.AddMessage("Populating output unmatched child anomaly growth table...")
            guids = "(" + ",".join("'" + x + "'" for x in unique_values) + ")"
            sql = "{} NOT IN {}".format(in_child_uniqueid_field, guids)

            unmatched_flds = [child_unique_fld, child_depth_fld, "CHILD_TOOL_ACCURACY", "CHILD_DEPTH_UNCERTAINTY",
                    "WORST_CASE_" + child_depth_fld, "CHILD_TOOL_RUN_DATE",  "ANNUAL_GROWTH_RATE", "WORST_CASE_ANNUAL_GROWTH"]

            in_child_flds = [in_child_uniqueid_field, in_child_depth_field]

            with arcpy.da.InsertCursor(out_unmatched_child_table, unmatched_flds) as cursor:
                with arcpy.da.SearchCursor(in_child_features, in_child_flds, sql) as c_cursor:
                    for row in c_cursor:
                        uid = row[0]
                        depth = float(row[1])
                        depth_uncert = depth * in_child_tool_accuracy / 100
                        worst_case_depth = depth + depth_uncert
                        annual_growth = depth / (run_date_diff_years / 2)
                        worst_case_annual_growth = worst_case_depth / (run_date_diff_years /2)

                        c_row = (uid, depth, in_child_tool_accuracy, depth_uncert,
                                 worst_case_depth, in_child_tool_run_date, annual_growth, worst_case_annual_growth)
                        cursor.insertRow(c_row)

        except Exception as e:
            raise

    def unique_values(self, in_fc , field):
        try:
            with arcpy.da.SearchCursor(in_fc, [field]) as cursor:
                return sorted({row[0] for row in cursor})

        except Exception as e:
            raise
