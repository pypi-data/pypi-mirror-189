
""" Headline: Anomaly Processing Inline Inspection pressure calculation tool
    Calls:  pimsilitool, pimsilitool.config
    inputs: ILI Feature class(Which is calibrated and imported)
    Description: This tool calculates severity ratios, burst/safe pressures, according to B31G and Modified B31G.  
    Output: The output of this tool estimates burst pressure values for Metal Loss anomalies based on depth, length and pressure.
   """


import arcpy
import pimsilitool
import os
import math
from pimsilitool import config
import sys
import arcpy.cim
from pimsilitool.license.validate_license.license_operation import LicenseOperation


class PressureCalculator(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = config.PRESSURE_CALCULATOR_TOOL_LABEL
        self.description = config.PRESSURE_CALCULATOR_TOOL_DESC
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):
        params = []
        # ************************* ILI Anomaly Data ***************

        # Parameter [0]
        in_ili_features = arcpy.Parameter(category = config.PRESSURE_CALCULATOR_CATEGORY_ANOMALY,
                                                displayName="Input ILI Features",
                                                name="in_ili_features",
                                                datatype=["GPFeatureLayer","GPTableView"],
                                                parameterType="Required",
                                                direction="Input")

        # Parameter [1]
        in_pc_length_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_ANOMALY,
                                                displayName="Anomaly Length Field", name="in_pc_length_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_pc_length_field.parameterDependencies = [in_ili_features.name]       
        in_pc_length_field.filter.list = ['int', 'long', 'double']
        
        # Parameter [2]
        in_pc_MaxDepthMeasured_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_ANOMALY,
                                                displayName="Anomaly Depth Percent Field", name="in_pc_MaxDepthMeasured_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_pc_MaxDepthMeasured_field.parameterDependencies = [in_ili_features.name]
        in_pc_MaxDepthMeasured_field.filter.list = ['int', 'long', 'double']

        # Parameter [3]
        in_pc_MeasuredWallThickness_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_ANOMALY,
                                                displayName="Measured Wall Thickness Field",
                                                name="in_pc_MeasuredWallThickness_field",
                                                datatype="Field", parameterType="Required",
                                                direction="Input")
        in_pc_MeasuredWallThickness_field.parameterDependencies = [in_ili_features.name]
        in_pc_MeasuredWallThickness_field.filter.list = ['int', 'long', 'double']

        params += [in_ili_features, in_pc_length_field, in_pc_MaxDepthMeasured_field, in_pc_MeasuredWallThickness_field]

        # ************************* Diameter ***************

        # Parameter [4]
        in_diameter_source = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                  displayName="Input Pipe Outside Diameter Source",
                                                  name="in_diameter_source",
                                                  datatype="GPString",
                                                  parameterType="Required",
                                                  direction="Input")
        in_diameter_source.filter.list = config.PRESSURE_CALCULATOR_DIAMETER_SOURCE
        in_diameter_source.value = config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[0]

        # Parameter [5]
        in_diameter_features = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                   displayName="Input Outside Diameter Features",
                                                   name="in_diameter_features",
                                                   datatype="GPFeatureLayer",
                                                   parameterType="optional",
                                                   direction="Input")
        in_diameter_features.filter.list = ["Polyline"]

        # Parameter [6]
        in_diameter_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                 displayName="Input Outside Diameter Field", name="in_diameter_field",
                                                 datatype="Field", parameterType="optional", direction="Input")
        in_diameter_field.parameterDependencies = [in_ili_features.name]
        in_diameter_field.filter.list = ['int', 'long', 'double']

        # Parameter [7]
        in_diameter_value = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                 displayName="Input Outside Diameter Value", name="in_diameter_value",
                                                 datatype="GPDouble", parameterType="optional", direction="Input")

        params += [in_diameter_source, in_diameter_features, in_diameter_field, in_diameter_value]

        # ************************* SMYS ***************

        # Parameter [8]
        in_smys_source = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                 displayName="Input Material SMYS Source",
                                                 name="in_smys_source",
                                                 datatype="GPString",
                                                 parameterType="optional",
                                                 direction="Input")
        in_smys_source.filter.list = config.PRESSURE_CALCULATOR_SMYS_SOURCE
        in_smys_source.value = config.PRESSURE_CALCULATOR_SMYS_SOURCE[0]

        # Parameter [9]
        in_smys_features = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                   displayName="Input Material SMYS Features",
                                                   name="in_smys_features",
                                                   datatype="GPFeatureLayer",
                                                   parameterType="optional",
                                                   direction="Input")
        in_smys_features.filter.list = ["Polyline"]

        # Parameter [10]
        in_smys_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                displayName="Input Material SMYS Field", name="in_smys_field",
                                                datatype="Field", parameterType="optional", direction="Input")
        in_smys_field.parameterDependencies = [in_ili_features.name]
        in_smys_field.filter.list = ['int', 'long', 'double']

        # Parameter [11]
        in_smys_value = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                displayName="Input Material SMYS Value", name="in_smys_value",
                                                datatype="GPDouble", parameterType="optional", direction="Input")

        params += [in_smys_source, in_smys_features, in_smys_field, in_smys_value]

        # ************************* MAOP ***************

        # Parameter [12]
        in_maop_source = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                 displayName="Input Pipe MAOP or MOP Source",
                                                 name="in_maop_source",
                                                 datatype="GPString",
                                                 parameterType="Required",
                                                 direction="Input")
        in_maop_source.filter.list = config.PRESSURE_CALCULATOR_MAOP_SOURCE
        in_maop_source.value = config.PRESSURE_CALCULATOR_MAOP_SOURCE[0]

        # Parameter [13]
        in_maop_features = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                   displayName="Input MAOP or MOP Features",
                                                   name="in_maop_features",
                                                   datatype="GPFeatureLayer",
                                                   parameterType="optional",
                                                   direction="Input")
        in_maop_features.filter.list = ["Polyline"]

        # Parameter [14]
        in_maop_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                    displayName="Input MAOP or MOP Field", name="in_maop_field",
                                                    datatype="Field", parameterType="optional", direction="Input")
        in_maop_field.parameterDependencies = [in_ili_features.name]
        in_maop_field.filter.list = ['int', 'long', 'double']

        # Parameter [15]
        in_maop_value = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                    displayName="Input MAOP or MOP Value", name="in_maop_value",
                                                    datatype="GPDouble", parameterType="optional", direction="Input")

        params += [in_maop_source, in_maop_features, in_maop_field, in_maop_value]

        # ************************* Design Factor ***************

        # Parameter [16]
        in_design_factor_source = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                      displayName="Input Design Factor Source",
                                                      name="in_design_factor_source",
                                                      datatype="GPString",
                                                      parameterType="Required",
                                                      direction="Input")
        in_design_factor_source.filter.list = config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE
        in_design_factor_source.value = config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[0] # value

        # Parameter [17]
        in_design_factor_features = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                       displayName="Input Design Factor Features",
                                                       name="in_design_factor_features",
                                                       datatype="GPFeatureLayer",
                                                       parameterType="optional",
                                                       direction="Input")
        in_design_factor_features.filter.list = ["Polyline"]

        # Parameter [18]
        in_design_factor_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                         displayName="Input Design Factor Field",
                                                         name="in_design_factor_field",
                                                         datatype="Field", parameterType="optional", direction="Input")
        in_design_factor_field.parameterDependencies = [in_ili_features.name]
        in_design_factor_field.filter.list = ['int', 'long', 'double']

        # Parameter [19]
        in_design_factor_value = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA,
                                                         displayName="Input Design Factor Value",
                                                         name="in_design_factor_value",
                                                         datatype="GPDouble", parameterType="optional", direction="Input")
        in_design_factor_value.value = 0.72

        params += [in_design_factor_source, in_design_factor_features, in_design_factor_field, in_design_factor_value]

        # ************************* Output Calculated Fields ***************

        # Parameter [22]
        in_pc_pipeBurstPressure_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                displayName="B31G Pipe Burst Pressure Field", name="in_pc_pipeBurstPressurer_field",
                                datatype="GPString", parameterType="Required", direction="Input")

       
        # Parameter [23]
        in_pc_calculatePressure_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                displayName="B31G Calculated Safety Pressure Field", name="in_pc_calculatePressure_field",
                                datatype="GPString", parameterType="Required", direction="Input")
      
        # Parameter [24]
        in_pc_safetyFactor_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                displayName="B31G Safety Factor Field", name="in_pc_safetyFactor_field",
                                datatype="GPString", parameterType="Required", direction="Input")

       
        # Parameter [25]
        in_pc_pressureReferencedRatio_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                    displayName="B31G Pressure Reference Ratio Field", name="in_pc_pressureReferenceRatio_field",
                                    datatype="GPString", parameterType="Required", direction="Input")

        # Parameter [26]
        in_pc_estimatedRepairFactor_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                    displayName="B31G Estimated Repair Factor Field", name="in_pc_estimatedRepairFactor_field",
                                    datatype="GPString", parameterType="Required", direction="Input")

        # Parameter [27]
        in_pc_rupturePressureRatio_field = arcpy.Parameter(category =config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                    displayName="B31G Rupture Pressure Ratio Field", name="in_pc_rupturePressureRatio_field",
                                    datatype="GPString", parameterType="Required", direction="Input")

        # Parameter [28]
        in_pc_modPipeBurstPressure_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                           displayName="Modified B31G Pipe Burst Pressure Field",
                                                           name="in_pc_modPipeBurstPressure_field",
                                                           datatype="GPString", parameterType="Required",
                                                           direction="Input")

        # Parameter [29]
        in_pc_modCalculatePressure_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                        displayName="Modified B31G Calculated Safety Pressure Field",
                                                        name="in_pc_modCalculatePressure_field",
                                                        datatype="GPString", parameterType="Required",
                                                        direction="Input")

        # Parameter [30]
        in_pc_modSafetyFactor_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                   displayName="Modified B31G Safety Factor Field",
                                                   name="in_pc_modSafetyFactor_field",
                                                   datatype="GPString", parameterType="Required", direction="Input")

        # Parameter [31]
        in_pc_modPressureReferencedRatio_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                              displayName="Modified B31G Pressure Reference Ratio Field",
                                                              name="in_pc_modPressureReferencedRatio_field",
                                                              datatype="GPString", parameterType="Required",
                                                              direction="Input")

        # Parameter [32]
        in_pc_modEstimatedRepairFactor_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                            displayName="Modified B31G Estimated Repair Factor Field",
                                                            name="in_pc_modEstimatedRepairFactor_field",
                                                            datatype="GPString", parameterType="Required",
                                                            direction="Input")

        # Parameter [33]
        in_pc_modRupturePressureRatio_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                           displayName="Modified B31G Rupture Pressure Ratio Field",
                                                           name="in_pc_modRupturePressureRatio_field",
                                                           datatype="GPString", parameterType="Required",
                                                           direction="Input")
        # Parameter [20]
        in_pc_outside_diameter_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                   displayName="Outside Diameter Field",
                                                   name="in_pc_outside_diameter_field",
                                                   datatype="GPString", parameterType="optional",
                                                   direction="Input")

        # Parameter [21]
        in_pc_smys_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                        displayName="Material SMYS Field",
                                                        name="in_pc_smys_field",
                                                        datatype="GPString", parameterType="optional",
                                                        direction="Input")

        # Parameter [21]
        in_pc_referencePressure_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                        displayName="Reference Pressure Field",
                                                        name="in_pc_referencePressure_field",
                                                        datatype="GPString", parameterType="optional",
                                                        direction="Input")
        # Parameter [20]
        in_pc_designFactor_field = arcpy.Parameter(category=config.PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS,
                                                   displayName="Design Factor Field",
                                                   name="in_pc_designFactor_field",
                                                   datatype="GPString", parameterType="optional",
                                                   direction="Input")

        params += [in_pc_pipeBurstPressure_field, in_pc_calculatePressure_field,
                    in_pc_safetyFactor_field, in_pc_pressureReferencedRatio_field, in_pc_estimatedRepairFactor_field,
                    in_pc_rupturePressureRatio_field, in_pc_modPipeBurstPressure_field, in_pc_modCalculatePressure_field,
                    in_pc_modSafetyFactor_field, in_pc_modPressureReferencedRatio_field,
                    in_pc_modEstimatedRepairFactor_field, in_pc_modRupturePressureRatio_field,
                    in_pc_outside_diameter_field, in_pc_smys_field,
                    in_pc_referencePressure_field, in_pc_designFactor_field]

        return params

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):

        # metal loss anomaly
        idx = 0
        idx2 = 4
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.PRESSURE_CALCULATOR_ANOMALY_FIELDS)

        pipe_param_idxs = [4, 8, 12, 16]
        start_idx = 20

        if parameters[0].value and not parameters[0].hasBeenValidated:

            flds = self.get_fields(parameters[0].value)

            for i in range(start_idx, 36):
                if not parameters[i].value:
                    j = i - start_idx
                    comparevalue = config.PRESSURE_CALCULATOR_ADDING_FIELDS[j]
                    self.populate_add_field(flds, parameters, i, comparevalue)

        elif not parameters[0].value or not arcpy.Exists(parameters[0].value):
            parameters[1].value = parameters[2].value = parameters[3].value = None
            for i in range(start_idx, 36):
                parameters[i].value = None

        if parameters[0].value:
            des = arcpy.Describe(parameters[0].value)
            if des.datatype == 'FeatureClass' or des.datatype == 'FeatureLayer':
                parameters[4].filter.list = config.PRESSURE_CALCULATOR_DIAMETER_SOURCE
                parameters[8].filter.list = config.PRESSURE_CALCULATOR_SMYS_SOURCE
                parameters[12].filter.list = config.PRESSURE_CALCULATOR_MAOP_SOURCE
                parameters[16].filter.list = config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE
            else:
                parameters[4].filter.list = config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[:2]
                parameters[8].filter.list = config.PRESSURE_CALCULATOR_SMYS_SOURCE[:2]
                parameters[12].filter.list = config.PRESSURE_CALCULATOR_MAOP_SOURCE[:2]
                parameters[16].filter.list = config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[:2]

        else:
            parameters[4].filter.list = config.PRESSURE_CALCULATOR_DIAMETER_SOURCE
            parameters[8].filter.list = config.PRESSURE_CALCULATOR_SMYS_SOURCE
            parameters[12].filter.list = config.PRESSURE_CALCULATOR_MAOP_SOURCE
            parameters[16].filter.list = config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE

        out_pipe_field_idx = 28
        for idx in pipe_param_idxs:
            if parameters[idx].value:
                if "Value" in parameters[idx].value:
                    parameters[idx + 1].enabled = parameters[idx + 2].enabled = False
                    parameters[idx + 3].enabled = True

                elif "Features" in parameters[idx].value:
                    parameters[idx + 1].enabled = parameters[idx + 2].enabled = True
                    parameters[idx + 3].enabled = False
                    if parameters[idx + 1].value:
                        parameters[idx + 2].parameterDependencies = [parameters[idx + 1].name]
                else:
                    parameters[idx + 1].enabled = parameters[idx + 3].enabled = False
                    parameters[idx + 2].enabled = True
                    if parameters[0].value and arcpy.Exists(parameters[0].value):
                        parameters[idx + 2].parameterDependencies = [parameters[0].name]

        if "Value" in parameters[4].value:  # outside diameter
            parameters[32].enabled = True
        else:
            parameters[32].enabled = False

        if "Value" in parameters[8].value:  # smys
            parameters[33].enabled = True
        else:
            parameters[33].enabled = False

        if "Value" in parameters[12].value: # maop
            parameters[34].enabled = True
        else:
            parameters[34].enabled = False

        if "Value" in parameters[16].value: # design factor
            parameters[35].enabled = True
        else:
            parameters[35].enabled = False

        return

    def updateMessages(self, parameters):

        pipe_param_idxs = [4, 8, 12, 16]
        for idx in pipe_param_idxs:
            if parameters[idx].value:
                if "Value" in parameters[idx].value:
                    if not parameters[idx + 3].value:
                        parameters[idx + 3].setErrorMessage("Value can not be empty, you must supply a value for the parameter.")
                elif "Features" in parameters[idx].value:
                    if not parameters[idx + 1].value:
                        parameters[idx + 1].setErrorMessage("Features can not be empty, you must supply a value for the parameter.")
                    if not parameters[idx + 2].value:
                        parameters[idx + 2].setErrorMessage("Field can not be empty, you must supply a value for the parameter.")

                elif  "Field" in parameters[idx].value:
                    if parameters[0].value and not parameters[idx + 2].value:
                        parameters[idx + 2].setErrorMessage("Field can not be empty, you must supply a value for the parameter.")
        return

    def enable_params(self, parameters, from_idx, to_idx, in_bool):
        try:
            for i in range(from_idx, to_idx):
                parameters[i].enabled = in_bool

        except Exception as e:
           raise

    def param_changed(self, param):
        changed = param.value and not param.hasBeenValidated

        return changed

    def update_field_names(self, parameters, idx, idx2, field_names):
        try:
            idx1 = idx + 1
            if parameters[idx].value:
                for i in range(idx1, idx2):
                    if not parameters[i].value:
                        parameters[i].value = field_names[i - idx1]
            else:
                for i in range(idx1, idx2):
                    parameters[i].value = None

        except Exception as e:
            raise

    def get_fields(self, in_layer):
        try:
            flds = []
            fc = in_layer
            if fc:
                fls = []
                fls += [f.name.upper() for f in arcpy.ListFields(fc)]
                flds = []
                for f in fls:
                    x = f.split('.')
                    if len(x) > 1:
                        x1 = x[1]
                        flds.append(x1)
                    else:
                        flds.append(f)
            return flds

        except Exception as e:
            raise

    def execute(self, parameters, messages):
        pimsilitool.AddMessage("Start Logging.")
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting ILI Pressure Calculator process...")

        try:          
            ili_inputpoint_fc = parameters[0].value
            if arcpy.Exists(ili_inputpoint_fc):
                ilicount = int(arcpy.GetCount_management(ili_inputpoint_fc).getOutput(0))
                pimsilitool.AddMessage("Record count for ILI Pressure Calculator {}".format(ilicount))
                spatial_joins = []
                pipe_param_idxs = [4, 8, 12, 16]
                for idx in pipe_param_idxs:
                    if parameters[idx].value:
                        if "Features" in parameters[idx].value:
                            spatial_joins.append(idx)

                if ilicount > 0:
                    if len(spatial_joins) > 0:
                        self.build_spatialjoin_table(parameters, spatial_joins)

                    # else:
                    #     # ht_result_flag = False
                    calculateilipressures = CalculateILIPressures()
                    calculateilipressures.fieldsCaliculation(parameters)

                    ili_flds = [f.name.upper() for f in arcpy.ListFields(ili_inputpoint_fc)]
                    delete_fields = [config.PRESSURE_CALCULATOR_OUTPUT_SYMS_FIELDNAME,
                                     config.PRESSURE_CALCULATOR_UTPUT_MAOP_FIELDNAME,
                                     config.PRESSURE_CALCULATOR_OUTPUT_DIAMETER_FIELDNAME,
                                     config.PRESSURE_CALCULATOR_OUTPUT_DESIGN_FACTOR_FIELDNAME]
                    for fld in delete_fields:
                        if fld in ili_flds:
                            arcpy.management.DeleteField(ili_inputpoint_fc, fld)
                else:
                    pimsilitool.AddWarning("There is no records to perform Pressure Calculation.")
            else:
                    pimsilitool.AddWarning("There is no feature class for Pressure Calculation.")
            pimsilitool.AddMessage("Finished ILI Pressure Calculator process.")
            return

        except Exception as e:
            tb = sys.exc_info()[2]
            arcpy.AddError("An error occurred on line %i" % tb.tb_lineno)
            arcpy.AddError(str(e))
            raise

    def populate_add_field(self, flds, parameters, idx, addfield):
        pimsilitool.AddMessage("Processing field {} ".format(addfield))
        if not addfield in flds:
                   # datatype="Field"
                   flds_1 = []
                   flds_1 = flds
                   flds_1.append(addfield)
                   parameters[idx].filter.list = flds_1

        else:
                    parameters[idx].filter.list = flds

        parameters[idx].value = addfield
   
    # ''' Check Intermediate gdb existing or not if not create '''
    def createtempgdb(self, output_dir, output_gdb):
        try:
            # Check for folder, if not create the folder
            if (not os.path.exists(output_dir)):
                os.makedirs(output_dir)
            gdbpath = os.path.join(output_dir, output_gdb)
            pimsilitool.AddMessage("Creating Intermediate GDB")
            if (not os.path.exists(gdbpath)):
                arcpy.management.CreateFileGDB(output_dir, output_gdb, "CURRENT")
            else:
                arcpy.management.Delete(gdbpath, None)
                arcpy.management.CreateFileGDB(output_dir, output_gdb, "CURRENT")
        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Issue in intermediate output folder creation, Please check and try again.\n{}".format(arcpy.GetMessages(2)))
            raise

    def build_spatialjoin_table(self,parameters, spatial_joins):

        try:
            ili_layer = parameters[0].value
            ili_layer_name =  arcpy.Describe(ili_layer).baseName
            ili_flds = []
            ili_flds += [f.name.upper() for f in arcpy.ListFields(ili_layer)]
            delete_fields = [config.PRESSURE_CALCULATOR_OUTPUT_SYMS_FIELDNAME,
                             config.PRESSURE_CALCULATOR_UTPUT_MAOP_FIELDNAME,
                             config.PRESSURE_CALCULATOR_OUTPUT_DIAMETER_FIELDNAME,
                             config.PRESSURE_CALCULATOR_OUTPUT_DESIGN_FACTOR_FIELDNAME]
            for fld in delete_fields:
                if fld in ili_flds:
                    arcpy.management.DeleteField(ili_layer, fld)
            # add temp fields
            arcpy.management.AddFields(ili_layer, config.PRESSURE_CALCULATOR_OUTPUT_TEMP_FIELDS)
            objidField = arcpy.Describe(ili_layer).OIDFieldName

            self.ILI_TEMP_FOLDER = config.PRESSURE_CALCULATOR_TEMP_FOLDER
            self.ILI_TEMP_GDB = config.PRESSURE_CALCULATOR_TEMP_GDB

            # pipesegment_layer=parameters[10].valueAsText
            # maop_layer = parameters[12].valueAsText
            #
            # syms_field = parameters[11].valueAsText
            # maop_field = parameters[13].valueAsText

            tempoutput_workspace = arcpy.env.scratchFolder # if arcpy.Exists(arcpy.env.scratchFolder) and arcpy.env.scratchFolder is not None else self.output_dir
            tempoutput_dir = os.path.join(tempoutput_workspace, self.ILI_TEMP_FOLDER )
            tempoutput_gdb = self.ILI_TEMP_GDB 
            self.tempoutputgdb_path = os.path.join(tempoutput_dir, tempoutput_gdb)
                   
            # Create temp gbd for intermediate process
            self.createtempgdb(tempoutput_dir, tempoutput_gdb)
            pimsilitool.AddMessage("Temp gdb is created and the path is {}".format(self.tempoutputgdb_path))

            # Diameter join
            if 4 in spatial_joins:
                # perform diameeter spatical join
                # bdiam = True
                pimsilitool.AddMessage("Diameter features spatial join...")
                diam_layer = parameters[5].value
                diam_field = parameters[6].valueAsText
                diam_spatialjoin_name = "Diameter_Join"
                diam_spatialjoin = os.path.join(self.tempoutputgdb_path, "Diameter_Join")
                self.process_spatial_join(ili_layer, ili_layer_name, objidField, diam_layer, diam_field,
                                          diam_spatialjoin_name, diam_spatialjoin, config.PRESSURE_CALCULATOR_OUTPUT_DIAMETER_FIELDNAME)
                pimsilitool.AddMessage("Done Diameter features spatial join...")

            # smys join
            if 8 in spatial_joins:
                # perform smys spatical join
                pimsilitool.AddMessage("SMYS features spatial join...")
                smys_layer = parameters[9].value
                smys_field = parameters[10].valueAsText
                smys_spatialjoin_name = "SMYS_Join"
                smys_spatialjoin = os.path.join(self.tempoutputgdb_path, "SMYS_Join")
                self.process_spatial_join(ili_layer, ili_layer_name, objidField, smys_layer, smys_field,
                                          smys_spatialjoin_name, smys_spatialjoin, config.PRESSURE_CALCULATOR_OUTPUT_SYMS_FIELDNAME)

                pimsilitool.AddMessage("Done SMYS features spatial join.")

            # maop join
            if 12 in spatial_joins:
                # perform maop spatical join
                pimsilitool.AddMessage("MAOP features spatial join...")
                maop_layer = parameters[13].value
                maop_field = parameters[14].valueAsText
                maop_spatialjoin_name = "MAOP_Join"
                maop_spatialjoin = os.path.join(self.tempoutputgdb_path, "MAOP_Join")
                self.process_spatial_join(ili_layer, ili_layer_name, objidField, maop_layer, maop_field,
                                          maop_spatialjoin_name,  maop_spatialjoin, config.PRESSURE_CALCULATOR_UTPUT_MAOP_FIELDNAME)
                pimsilitool.AddMessage("Done MAOP features spatial join.")

            # design factor join
            if 16 in spatial_joins:
                # perform design spatical join
                pimsilitool.AddMessage("Design Factor features spatial join...")
                df_layer = parameters[17].value
                df_field = parameters[18].valueAsText
                df_spatialjoin_name = "DesignFactor_SJ"
                df_spatialjoin = os.path.join(self.tempoutputgdb_path, df_spatialjoin_name)

                self.process_spatial_join(ili_layer, ili_layer_name, objidField, df_layer, df_field, df_spatialjoin_name,
                                          df_spatialjoin, config.PRESSURE_CALCULATOR_OUTPUT_DESIGN_FACTOR_FIELDNAME)
                pimsilitool.AddMessage("Done Design Factor features spatial join.")

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Issue in build spatial join creation, Please check and try again.\n{}".format(arcpy.GetMessages(2)))
            raise

    def process_spatial_join(self, ili_layer, ili_layer_name, objidField, sj_layer, sj_field, spatial_join_name, spatial_join_path, out_field):
        try:
            if arcpy.Exists(spatial_join_path):
                arcpy.Delete_management(spatial_join_path)

            arcpy.SpatialJoin_analysis(ili_layer, sj_layer, spatial_join_path, "JOIN_ONE_TO_ONE", "KEEP_ALL",  match_option="INTERSECT", search_radius="0.33 Feet")

            arcpy.AddJoin_management(ili_layer, objidField, spatial_join_path, "TARGET_FID", "KEEP_ALL")
            arcpy.management.CalculateField(ili_layer, ili_layer_name + "." + out_field,   '!' + spatial_join_name + '.' + sj_field + '!', "PYTHON3")

            arcpy.management.RemoveJoin(ili_layer, spatial_join_name)
            arcpy.Delete_management(spatial_join_path)

        except Exception as e:
            raise


class CalculateILIPressures(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        #self.label = "ILI Pressure Calculator Tool"
    
    '''Add The output fields if not exist'''
    def addMissingField(self, fc, outFields):
        if(fc):
            flds = []
            flds += [f.name.upper() for f in arcpy.ListFields (fc)]
            # f1=[]
            # for f in flds:
            #     x=f.split('.')
            #     if len(x)>1:
            #         x1=x[1]
            #         f1.append(x1)
            #     else:
            #         f1.append(f)
           
            for outField in outFields:
                field_list = arcpy.ListFields(fc, outField)

                if len(field_list) == 1:
                    # check field type and update type to DOUBLE
                    # fields = arcpy.ListFields(fc, outField)
                    field_type = field_list[0].type.upper()
                    if field_type != "DOUBLE":
                        arcpy.DeleteField_management(fc, outField)
                        arcpy.AddField_management(fc, outField, "DOUBLE", field_precision=15, field_scale=7,
                                                  field_length=None, field_alias=outField, field_is_nullable="NULLABLE")
                else:
                    # Execute AddField for new fields
                    # As suggested by Tracy, updated field type to DOUBLE,  08-16-21
                    arcpy.AddField_management(fc, outField, "DOUBLE", field_precision=15, field_scale=7,
                                              field_length=None,
                                              field_alias=outField, field_is_nullable="NULLABLE")
                    pimsilitool.AddMessage("{} field added".format(outField))



    def check_int_value(self, in_val):
        try:
            value = int(in_val)
            return True
        except:
            return False

    def fieldsCaliculation(self,parameters):
        try:
            fields=[]
            inFeatures = parameters[0].value
            anom_length_field = parameters[1].valueAsText
            anom_depth_pct_field = parameters[2].valueAsText
            anom_wall_thickness_field = parameters[3].valueAsText

            diam_source = parameters[4].valueAsText
            diam_features = parameters[5].value
            diam_field = parameters[6].valueAsText
            diam_value = parameters[7].valueAsText

            smys_source = parameters[8].valueAsText
            smys_features = parameters[9].value
            smys_field = parameters[10].valueAsText
            smys_value = parameters[11].valueAsText

            maop_source = parameters[12].valueAsText
            maop_features = parameters[13].value
            maop_field = parameters[14].valueAsText
            maop_value = parameters[15].valueAsText

            design_factor_source = parameters[16].valueAsText
            design_factor_features = parameters[17].value
            design_factor_field = parameters[18].valueAsText
            design_factor_value = parameters[19].valueAsText

            fPipeBurstPressure = parameters[20].valueAsText
            fCalculatedPressure = parameters[21].valueAsText
            fSafetyFactor = parameters[22].valueAsText
            fPressureReferencedRatio = parameters[23].valueAsText
            fEstimatedRepairFactor = parameters[24].valueAsText
            fRupturePressureRatio = parameters[25].valueAsText
            fModPipeBurstPressure = parameters[26].valueAsText
            fModCalculatedPressure = parameters[27].valueAsText
            fModSafetyFactor = parameters[28].valueAsText
            fModPressureReferencedRatio = parameters[29].valueAsText
            fModEstimatedRepairFactor = parameters[30].valueAsText
            fModRupturePressureRatio = parameters[31].valueAsText
            fOutsideDiameter = parameters[32].valueAsText
            fMaterialSmys = parameters[33].valueAsText
            fReferencePressure = parameters[34].valueAsText
            fDesignFactor = parameters[35].valueAsText

            # get OID field name
            objidField = arcpy.Describe(inFeatures).OIDFieldName

            # add temporary field
            temp_field = "TEMP_FLD"
            field_list = arcpy.ListFields(inFeatures, temp_field)

            if len(field_list) == 1:
                arcpy.DeleteField_management(inFeatures, temp_field)
                arcpy.AddField_management(inFeatures, temp_field, "DOUBLE", field_precision=15, field_scale=7,
                                          field_length=None, field_alias=temp_field, field_is_nullable="NULLABLE")
            else:
                arcpy.AddField_management(inFeatures, temp_field, "DOUBLE", field_precision=15, field_scale=7,
                                          field_length=None, field_alias=temp_field, field_is_nullable="NULLABLE")


            if diam_source == config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[2]:
                diam_field = config.PRESSURE_CALCULATOR_OUTPUT_DIAMETER_FIELDNAME
            elif diam_source == config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[1]:
                diam_field = temp_field  # place holder field

            if smys_source == config.PRESSURE_CALCULATOR_SMYS_SOURCE[2]:
                smys_field = config.PRESSURE_CALCULATOR_OUTPUT_SYMS_FIELDNAME
            elif smys_source == config.PRESSURE_CALCULATOR_SMYS_SOURCE[1]:
                smys_field = temp_field    # place holder field

            if maop_source == config.PRESSURE_CALCULATOR_MAOP_SOURCE[2]:
                maop_field = config.PRESSURE_CALCULATOR_UTPUT_MAOP_FIELDNAME
            elif maop_source == config.PRESSURE_CALCULATOR_MAOP_SOURCE[1]:
                maop_field = temp_field   # place holder field

            if design_factor_source == config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[2]:
                design_factor_field = config.PRESSURE_CALCULATOR_OUTPUT_DESIGN_FACTOR_FIELDNAME
            elif design_factor_source == config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[1]:
                design_factor_field = temp_field    # place holder field

            infields = [anom_length_field, anom_depth_pct_field, anom_wall_thickness_field, diam_field,  smys_field, maop_field, design_factor_field, objidField]

            if diam_source != config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[1]:
                fOutsideDiameter = temp_field    # place holder field
            if smys_source != config.PRESSURE_CALCULATOR_SMYS_SOURCE[1]:
                fMaterialSmys = temp_field    # place holder field
            if maop_source != config.PRESSURE_CALCULATOR_MAOP_SOURCE[1]:
                fReferencePressure = temp_field  # place holder field
            if design_factor_source != config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[1]:
                fDesignFactor = temp_field  # place holder field

            outputfields = [fPipeBurstPressure, fCalculatedPressure, fSafetyFactor,
                            fPressureReferencedRatio, fEstimatedRepairFactor, fRupturePressureRatio,
                            fModPipeBurstPressure, fModCalculatedPressure, fModSafetyFactor,
                            fModPressureReferencedRatio, fModEstimatedRepairFactor, fModRupturePressureRatio,
                            fOutsideDiameter, fMaterialSmys, fReferencePressure, fDesignFactor]
            # Input fields indexes
            anom_length_fieldIdx = 0
            anom_depth_pct_fieldIdx= 1
            anom_wall_thickness_fieldIdx = 2
            maxDiameterIdx = 3
            pipeSmysIdx = 4
            pipeMAOPFieldIdx = 5
            pipDesignFactorIdx = 6

            fields = infields + outputfields

            # *** Check output fields are existing or not if not add fields
            self.addMissingField(inFeatures, outputfields)

            warningCounter = 0

            where = "{} Is NOT NULL AND {} IS NOT NULL AND {} IS NOT NULL".format(anom_length_field, anom_depth_pct_field, anom_wall_thickness_field)
            if diam_source == config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[0]:
                where += " AND {} IS NOT NULL".format(diam_field)
            if smys_source == config.PRESSURE_CALCULATOR_SMYS_SOURCE[0]:
                where += " AND {} IS NOT NULL".format(smys_field)
            if maop_source == config.PRESSURE_CALCULATOR_MAOP_SOURCE[0]:
                where += " AND {} IS NOT NULL".format(maop_field)
            if design_factor_source == config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[0]:
                where += " AND {} IS NOT NULL".format(design_factor_field)


            # Create update cursor for feature class
            with arcpy.da.UpdateCursor(inFeatures, fields, where) as cursor:
                # Update the fields based on the values
                for row in cursor:
                    reventid = row[7]
                    length_of_anomaly = row[0]
                    depth_of_anomaly_pct = row[1]
                    wall_thickness = row[2]

                    if diam_source == config.PRESSURE_CALCULATOR_DIAMETER_SOURCE[1]:
                        pipe_diameter = float(diam_value)
                        row[20] = float(diam_value)
                    else:
                        pipe_diameter = row[3]

                    if smys_source == config.PRESSURE_CALCULATOR_SMYS_SOURCE[1]:
                        smys = float(smys_value)
                        row[21] = float(smys_value)
                    else:
                        smys = row[4]

                    if maop_source == config.PRESSURE_CALCULATOR_MAOP_SOURCE[1]:
                        maop = float(maop_value)
                        row[22] = float(maop_value)
                    else:
                        maop = row[5]

                    if design_factor_source == config.PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE[1]:
                        design_factor = float(design_factor_value)
                        row[23] = float(design_factor_value)
                    else:
                        design_factor = row[6]

                    # check values
                    emptyfields = []
                    if not self.check_int_value(length_of_anomaly):
                        emptyfields.append(infields[anom_length_fieldIdx])
                    if not self.check_int_value(depth_of_anomaly_pct):
                        emptyfields.append(infields[anom_depth_pct_fieldIdx])
                    if not self.check_int_value(wall_thickness):
                        emptyfields.append(infields[anom_wall_thickness_fieldIdx])

                    if not self.check_int_value(pipe_diameter):
                        emptyfields.append(infields[maxDiameterIdx])
                    if not self.check_int_value(smys):
                        emptyfields.append(infields[pipeSmysIdx])
                    if not self.check_int_value(maop):
                        emptyfields.append(infields[pipeMAOPFieldIdx])
                    if not self.check_int_value(design_factor) or design_factor == 0:
                        emptyfields.append(infields[pipDesignFactorIdx])

                    if len(emptyfields) > 0:
                        warningCounter += 1
                        pimsilitool.AddMessage("{}: {} has invalid value(s) for field(s): {}".format(objidField, reventid, str(emptyfields)))
                        continue

                    # # Design factor
                    # row[8] = design_factor

                    # calculate depth value from depth percent
                    depth_of_anomaly = (depth_of_anomaly_pct * wall_thickness) / 100

                    # calculate Flow Stress and mod Flow Stress
                    flow_stress = (1.1) * smys

                    # calculate foliasFactor
                    # foliasFactor = 0
                    # TODO  if length_of_anomaly < (20 * pipe_diameter * wall_thickness) ** 0.5:
                    l2_by_dt = (length_of_anomaly ** 2) / (pipe_diameter * wall_thickness)
                    folias_factor = math.sqrt(1 + (0.8 * l2_by_dt))

                    # calculate Area Of Metal Loss and Mod Area Of Metal Loss
                    area_of_metal_loss = (2 / 3) * depth_of_anomaly * length_of_anomaly
                    a0 = wall_thickness * length_of_anomaly

                    # calculate pipe Burst Pressure
                    a_by_a0 = 1 - (area_of_metal_loss / a0)
                    a_by_a0M = 1 - (area_of_metal_loss / (a0 * folias_factor))
                    t_by_D = (2 * wall_thickness) / pipe_diameter

                    pipe_burst_pressure = flow_stress * (a_by_a0 / a_by_a0M) * t_by_D

                    row[8] = round(pipe_burst_pressure, 2)

                    # calculate  mod area of metal loss
                    mod_area_of_metal_loss = 0.85 * depth_of_anomaly * length_of_anomaly

                    # calculate mod Flow Stress
                    mod_flow_stress = smys + 10000

                    # calculate  mod Folias Factor
                    mod_l2_by_dt = (length_of_anomaly ** 2) / (pipe_diameter * wall_thickness)

                    if ((length_of_anomaly ** 2) / (pipe_diameter * wall_thickness)) <= 50:
                        mod_folias_factor = math.sqrt(1 + (0.6275 * mod_l2_by_dt) - (0.003375 * (mod_l2_by_dt ** 2)))

                    else:
                        mod_folias_factor = (0.032 * mod_l2_by_dt) + 3.3

                    # calculate Mod Pipe Burst Pressure

                    mod_a0 = wall_thickness * length_of_anomaly
                    mod_a_by_a0 = 1 - (mod_area_of_metal_loss / mod_a0)
                    mod_a_by_a0M = 1 - (mod_area_of_metal_loss / (mod_a0 * mod_folias_factor))
                    mod_t_by_D = (2 * wall_thickness) / pipe_diameter

                    mod_pipe_burst_pressure = mod_flow_stress * (mod_a_by_a0 / mod_a_by_a0M) * mod_t_by_D

                    # mod_pipe_burst_pressure = mod_flow_stress * ((1 - (mod_area_of_metal_loss / a0)) / (1 - (mod_area_of_metal_loss / (a0 * mod_folias_factor)))) * ( (2 * wall_thickness) / pipe_diameter)

                    row[14] = round(mod_pipe_burst_pressure, 2)

                    # Rupture Pressure Ratio
                    pipe_smys = (2 * wall_thickness * smys) / pipe_diameter

                    # Rupture Pressure Ratio
                    rupturePressureRatio = pipe_burst_pressure / pipe_smys
                    row[13] = round(rupturePressureRatio, 4)

                    # Modified Rupture Pressure Ratio
                    modRupturePressureRatio = mod_pipe_burst_pressure / pipe_smys
                    row[19] = round(modRupturePressureRatio, 4)

                    # check MAOP value
                    if not self.check_int_value(maop):
                        warningCounter += 1
                        pimsilitool.AddMessage("{}: {} has invalid MAOP value. Safety Factor, Pressure Referenced "
                            "Ratio and Estimated Repair Factor values can not be calculated".format(objidField, reventid))
                        continue

                    # Reference Pressure
                    referencePressure = maop
                    # row[9] = maop

                    # calculated Safety Pressure
                    # calculatedPressure = (pipe_burst_pressure * maop) / pipe_smys
                    calculatedPressure = pipe_burst_pressure * design_factor
                    row[9] = round(calculatedPressure, 2)

                    # Modified calculated Safety Pressure
                    modCalculatedPressure = mod_pipe_burst_pressure * design_factor
                    row[15] = round(modCalculatedPressure, 2)

                    # Safety Factor
                    safetyFactor = pipe_burst_pressure / maop
                    row[10] = round(safetyFactor, 4)

                    # Modified Safety Factor
                    modSafetyFactor = mod_pipe_burst_pressure / maop
                    row[16] = round(modSafetyFactor, 4)

                    # Pressure Referenced Ratio
                    pressureReferencedRatio = calculatedPressure / referencePressure
                    row[11] = round(pressureReferencedRatio, 4)

                    # Modified Pressure Referenced Ratio
                    modPpressureReferencedRatio = modCalculatedPressure / referencePressure
                    row[17] = round(modPpressureReferencedRatio, 4)

                    # Estimated Repair Factor
                    estimatedRepairFactor = maop / calculatedPressure
                    row[12] = round(estimatedRepairFactor, 4)

                    # Modified Estimated Repair Factor
                    modEestimatedRepairFactor = maop / modCalculatedPressure
                    row[18] = round(modEestimatedRepairFactor, 4)

                    cursor.updateRow(row)

            # delete temporary field
            field_list = arcpy.ListFields(inFeatures, temp_field)
            if len(field_list) == 1:
                arcpy.DeleteField_management(inFeatures, temp_field)

            if warningCounter > 0:
                pimsilitool.AddWarning("Total number of warning(s): {}, due to values are null or empty, "
                                            "Please check the log file for details".format(warningCounter))

        except Exception as e:
            # If an error occurred, print line number and error message
            tb = sys.exc_info()[2]
            arcpy.AddError("An error occurred on line %i" % tb.tb_lineno)
            if("lock" in str(e)):
                arcpy.AddError("Please close all Pressure Calculator tool associated input data tables and try again!")            

            arcpy.AddError(str(e))
            raise

   