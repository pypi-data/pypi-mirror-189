
""" Headline: Anomaly Processing Inline Inspection Anomaly Matching tool 
    Calls:  inlineinspection, inlineinspection.config
    inputs: ILI Anomaly Ellipse from current and previous years.
    Description: This tool Compares Anomaly.  
    Output: The output of this tool.
   """

# from logging import exception
import arcpy
import pimsilitool
import os
# import datetime as dt
# import math
from pimsilitool import config
# import traceback
import sys
# from arcpy import env
import sqlite3
import uuid
from pimsilitool.license.validate_license.license_operation import LicenseOperation


class AnomalyComparer(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ILI Anomaly Matching"
        self.description = "This Tool Compares ILI Anomalies"
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):
            
        in_dataset121_features = arcpy.Parameter(category =config.ANOMALY_MATCHING_CLOCK_POSITION[1],
                                                 displayName="Input ILI Anomaly Ellipse Dataset 1 Features",
                                                name="in_dataset121_features",
                                                datatype="GPFeatureLayer",
                                                parameterType="Required",
                                                direction="Input")
        # in_dataset121_features.filter.list = ["Polygon"]

        in_dataset122_features = arcpy.Parameter(category =config.ANOMALY_MATCHING_CLOCK_POSITION[1],
                                                 displayName="Input ILI Anomaly Ellipse Dataset 2 Features",
                                                name="in_dataset122_features",
                                                datatype="GPFeatureLayer",
                                                parameterType="Required",
                                                direction="Input")
        # in_dataset122_features.filter.list = ["Polygon"]

        in_dataset61_features = arcpy.Parameter(category =config.ANOMALY_MATCHING_CLOCK_POSITION[0],
                                                displayName="Input ILI Anomaly Ellipse Dataset 1 Features",
                                                name="in_dataset61_features",
                                                datatype="GPFeatureLayer",
                                                parameterType="Required",
                                                direction="Input")
        # in_dataset61_features.filter.list = ["Polygon"]

        in_dataset62_features = arcpy.Parameter(category =config.ANOMALY_MATCHING_CLOCK_POSITION[0],
                                                displayName="Input ILI Anomaly Ellipse Dataset 2 Features",
                                                name="in_dataset62_features",
                                                datatype="GPFeatureLayer",
                                                parameterType="Required",
                                                direction="Input")
        # in_dataset62_features.filter.list = ["Polygon"]

        in_uniqueid_field = arcpy.Parameter(
                                                displayName="Anomaly Unique ID Field", name="in_uniqueid_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_uniqueid_field.parameterDependencies = [in_dataset121_features.name]
        in_uniqueid_field.filter.list = ['guid']
                
        in_search_distance = arcpy.Parameter(
                                                displayName="Search Distance",
                                                name="in_search_distance",
                                                datatype="GPLinearUnit",
                                                parameterType="Required",
                                                direction="Input")
        in_search_distance.value = '.25 Feet'        
        in_search_distance.filter.list = ['Kilometers', 'Miles', 'Meters', 'Feet']     
                
        out_comparer_features = arcpy.Parameter(displayName="Output Anomaly Comparer Table",
                                                name="out_comparer_features",
                                                datatype="GPTableView",
                                                parameterType="Optional",
                                                direction="Output")
        # out_comparer_features.value ="%scratchGDB%\AnomalyMatches"
               
        parameters = [in_dataset121_features, in_dataset122_features,
                        in_dataset61_features, in_dataset62_features,
                        in_uniqueid_field,
                        in_search_distance,
                        out_comparer_features                        
                      ]

        return parameters

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):

        # Fill the fields after feature selection.
        if self.param_changed(parameters[0]):
            # flds = []
            # fc=parameters[3].value
            # if(fc):
            #     fls = []
            #     fls += [f.name.upper() for f in arcpy.ListFields (fc)]
            #
            #     flds=[]
            #     for f in fls:
            #         x=f.split('.')
            #         if len(x)>1:
            #             x1=x[1]
            #             flds.append(x1)
            #         else:
            #             flds.append(f)
              
            if not parameters[4].value:
                parameters[4].value = config.ANOMALY_MATCHING_ANOMALY_FIELDS[0]

        if parameters[0].value:
            catalogPath = arcpy.da.Describe(parameters[0].value)["catalogPath"]
            if not parameters[6].value:
                parameters[6].value = os.path.join(os.path.dirname(catalogPath), config.ANOMALY_MATCHING_OUTPUT_TABLE_NAME)
        else:
            parameters[6].value = None

        return

    def updateMessages(self, parameters):  
        return

    def param_changed(self, param):
        changed = param.value and not param.hasBeenValidated
        return changed

    def execute(self, parameters, messages):
               
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting Anomaly Compare process...")

        try:
            arcpy.env.overwriteOutput = True
            searchTolarance = parameters[5].valueAsText
            parent_anomaly_12 = parameters[0].value
            child_anomaly_12 = parameters[1].value
            parent_anomaly_6 = parameters[2].value
            child_anomaly_6 = parameters[3].value
            unique_field = parameters[4].valueAsText
            out_table = parameters[6].valueAsText

            for i in range(0, 4):
                if not arcpy.Exists(parameters[i].value):
                    pimsilitool.AddError("Input features does not exist: " + parameters[i].valueAsText)
                    return

                if int(arcpy.GetCount_management(parameters[i].value).getOutput(0)) < 1:
                    pimsilitool.AddError("There are no features in the input feature class.")
                    return

            pimsilitool.AddMessage("Generating near tables...")

            neartable12 = os.path.join(arcpy.env.scratchGDB, config.ANOMALY_MATCHING_NEAR_TABLE_NAMES[0])
            neartable6 = os.path.join(arcpy.env.scratchGDB, config.ANOMALY_MATCHING_NEAR_TABLE_NAMES[1])

            self.generate_near_table(parent_anomaly_12, child_anomaly_12, neartable12, searchTolarance)
            self.generate_near_table(parent_anomaly_6, child_anomaly_6, neartable6, searchTolarance)

            out_union_table = os.path.join(arcpy.env.scratchGDB, "Union_Table")
            if arcpy.Exists(out_union_table):
                arcpy.Delete_management(out_union_table)

            arcpy.Merge_management([neartable12, neartable6], out_union_table)

            sort_fc = os.path.join(arcpy.env.scratchGDB, "Sorted_Table")
            if arcpy.Exists(sort_fc):
                arcpy.Delete_management(sort_fc)
            arcpy.Sort_management(out_union_table, sort_fc, "IN_FID ASCENDING; NEAR_FID ASCENDING; NEAR_RANK DESCENDING")

            pimsilitool.AddMessage("Removing duplicate rows...")
            arcpy.DeleteIdentical_management(sort_fc, "IN_FID;NEAR_FID", None, 0)

            pimsilitool.AddMessage("Joining unique id columns...")

            self.join_field(sort_fc, "IN_FID", parent_anomaly_12, "OBJECTID", unique_field)
            self.alter_field(sort_fc, unique_field, ("PARENT_" + unique_field)[0:30], "Parent Unique ID")

            self.join_field(sort_fc, "NEAR_FID", child_anomaly_12, "OBJECTID", unique_field)
            self.alter_field(sort_fc, unique_field, ("CHILD_" + unique_field)[0:30], "Child Unique ID")

            arcpy.TableToTable_conversion(sort_fc, os.path.dirname(out_table), os.path.basename(out_table))

            for fc in [neartable12,neartable6,out_union_table, sort_fc]:
                if arcpy.Exists(fc):
                    arcpy.Delete_management(fc)

            pimsilitool.AddMessage("Completed Anomaly Compare process.")
            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def generate_near_table(self, parent_anomaly_12, child_anomaly_12, neartable12, searchTolarance):
        try:
            arcpy.analysis.GenerateNearTable(parent_anomaly_12, child_anomaly_12, neartable12,
                                             searchTolarance, "LOCATION", "NO_ANGLE", "ALL", 1000, "PLANAR")
        except Exception as e:
            raise

    def join_field(self, in_table, in_fld, join_table, join_fld, flds):
        try:
            arcpy.JoinField_management(in_table, in_fld, join_table,join_fld, flds)

        except Exception as e:
            raise

    def alter_field(self, in_table, in_fld, alter_fld, alias_name):

        try:
            arcpy.AlterField_management(in_table, in_fld, alter_fld, alias_name)

        except Exception as e:
            raise

