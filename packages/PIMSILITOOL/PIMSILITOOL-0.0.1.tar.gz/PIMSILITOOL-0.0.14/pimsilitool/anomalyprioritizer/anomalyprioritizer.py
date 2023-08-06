
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
import numpy
from pimsilitool.license.validate_license.license_operation import LicenseOperation


class AnomalyPrioritizer(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ILI Anomaly Prioritizer"
        self.description = "This Tool Calculates ILI Anomaly Priorities"
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):

        parameters = []

        #   ******************************************
        #   ILI Metal Loss Anomaly Parameters
        #   ******************************************

        # Parameter [0]
        in_ili_features = arcpy.Parameter(category = config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                            displayName="Input ILI Metal Loss Anomaly Features (6:00 Centered)",
                                            name="in_ili_features",
                                            datatype=["GPFeatureLayer","GPTableView"],
                                            parameterType="Required",
                                            direction="Input")
        # Parameter [1]
        in_ili_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                          displayName="Input ILI Metal Loss Anomaly Features  (12:00 Centered)",
                                          name="in_ili_features_12",
                                          datatype=["GPFeatureLayer", "GPTableView"],
                                          parameterType="Optional",
                                          direction="Input")

        # Parameter [2]
        in_pipe_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                                 displayName="Metal Loss Anomaly Network Route ID Field",
                                                 name="in_pipe_routeid_field",
                                                 datatype="Field", parameterType="Required", direction="Input")
        in_pipe_routeid_field.parameterDependencies = [in_ili_features.name]
        #
        #
        # # Parameter [3]
        # in_pipe_measure_field = arcpy.Parameter(category="ILI Metal Loss Anomaly Parameters",
        #                                         displayName="Metal Loss Anomaly Measure Field", name="in_pipe_measure_field",
        #                                         datatype="Field", parameterType="Required", direction="Input")
        # in_pipe_measure_field.parameterDependencies = [in_ili_features.name]
        # in_pipe_measure_field.filter.list = ['int', 'long', 'double']


        # Parameter [2]
        in_pipe_depth_pct_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                                       displayName="Metal Loss Anomaly Depth Percent Field",
                                                       name="in_pipe_depth_pct_field",
                                                       datatype="Field", parameterType="Required", direction="Input")
        in_pipe_depth_pct_field.parameterDependencies = [in_ili_features.name]
        in_pipe_depth_pct_field.filter.list = ['int', 'long', 'double']

        # Parameter [3]
        in_pipe_clockpos_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                                 displayName="Metal Loss Anomaly Clock Position Field",
                                                 name="in_pipe_clockpos_field",
                                                 datatype="Field", parameterType="Required", direction="Input")
        in_pipe_clockpos_field.parameterDependencies = [in_ili_features.name]
        in_pipe_clockpos_field.filter.list = ['Text']

        # Parameter [4]
        in_pipe_maop_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                             displayName="Metal Loss Anomaly MAOP Field", name="in_pipe_maop_field",
                                             datatype="Field", parameterType="Required", direction="Input")
        in_pipe_maop_field.parameterDependencies = [in_ili_features.name]
        in_pipe_maop_field.filter.list = ['int', 'long', 'double']

        # Parameter [5]
        in_pipe_burstpressure_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                                        displayName="Metal Loss Anomaly Pipe Burst Pressure Field",
                                                        name="in_pipe_burstpressure_field",
                                                        datatype="Field", parameterType="Required",
                                                        direction="Input")
        in_pipe_burstpressure_field.filter.list = ['int', 'long', 'double']
        in_pipe_burstpressure_field.parameterDependencies = [in_ili_features.name]

        # Parameter [6]
        in_pipe_safepressure_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                                      displayName="Metal Loss Anomaly Calculated Safe Pressure Field",
                                                      name="in_pipe_safepressure_field",
                                                      datatype="Field", parameterType="Required",
                                                      direction="Input")
        in_pipe_safepressure_field.filter.list = ['int', 'long', 'double']
        in_pipe_safepressure_field.parameterDependencies = [in_ili_features.name]

        # Parameter [7]
        in_pipe_erf_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_ANOMALY,
                                        displayName="Metal Loss Anomaly Estimated Repair Factor Field", name="in_pipe_erf_field",
                                        datatype="Field", parameterType="Required", direction="Input")
        in_pipe_erf_field.parameterDependencies = [in_ili_features.name]
        in_pipe_erf_field.filter.list = ['int', 'long', 'double']

        parameters += [in_ili_features,  in_ili_features_12, in_pipe_routeid_field, in_pipe_depth_pct_field,  in_pipe_clockpos_field,
                        in_pipe_maop_field, in_pipe_burstpressure_field,  in_pipe_safepressure_field, in_pipe_erf_field]

        #   ******************************************
        #   ILI Crack or Crack like Parameters
        #   ******************************************

        # Parameter [8]
        in_crack_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_LIKE,
                                                  displayName="Input Crack or Crack-like Features (6:00 Centered)",
                                                  name="in_crack_features",
                                                  datatype=["GPFeatureLayer", "GPTableView"],
                                                  parameterType="Optional", direction="Input")
        # Parameter [9]
        in_crack_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_LIKE,
                                            displayName="Input Crack or Crack-like Features (12:00 Centered)",
                                            name="in_crack_features_12",
                                            datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")

        # # Parameter [12]
        in_crack_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_LIKE,
                                                       displayName="Crack or Crack-like Network Route ID Field",
                                                       name="in_crack_routeid_field",
                                                       datatype="Field", parameterType="Optional", direction="Input")
        in_crack_routeid_field.parameterDependencies = [in_crack_features.name]
        #
        # # Parameter [13]
        # in_crack_measure_field = arcpy.Parameter(category="ILI Crack or Crack-like Parameters",
        #                                                displayName="Crack Measure Field",
        #                                                name="in_crack_measure_field",
        #                                                datatype="Field", parameterType="Optional", direction="Input")
        # in_crack_measure_field.parameterDependencies = [in_crack_features.name]
        # in_crack_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_crack_features, in_crack_features_12, in_crack_routeid_field]

        #   ******************************************
        #   ILI Stress Riser Parameters
        #   ******************************************

        # Parameter [10]
        in_crack_field_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_FIELD,
                                                  displayName="Input Crack Field Features (6:00 Centered)",
                                                  name="in_crack_field_features",
                                                  datatype=["GPFeatureLayer", "GPTableView"],
                                                  parameterType="Optional", direction="Input")
        # Parameter [11]
        in_crack_field_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_FIELD,
                                                     displayName="Input Crack Field Features (12:00 Centered)",
                                                     name="in_crack_field_features_12",
                                                     datatype=["GPFeatureLayer", "GPTableView"],
                                                     parameterType="Optional", direction="Input")

        # # Parameter [16]
        in_crack_field_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_CRACK_FIELD,
                                                       displayName="Crack Field Network Route ID Field",
                                                       name="in_crack_field_routeid_field",
                                                       datatype="Field", parameterType="Optional", direction="Input")
        in_crack_field_routeid_field.parameterDependencies = [in_crack_field_features.name]
        #
        # # Parameter [17]
        # in_crack_field_measure_field = arcpy.Parameter(category="ILI Crack Field Parameters",
        #                                                displayName="Crack Field Measure Field",
        #                                                name="in_crack_field_measure_field",
        #                                                datatype="Field", parameterType="Optional", direction="Input")
        # in_crack_field_measure_field.parameterDependencies = [in_crack_field_features.name]
        # in_crack_field_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_crack_field_features, in_crack_field_features_12, in_crack_field_routeid_field]


        #   ******************************************
        #   ILI Dent Parameters
        #   ******************************************

        # Parameter [12]
        in_dent_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DENT,
                                           displayName="Input Dent Features (6:00 Centered)",
                                           name="in_dent_features",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")
        # Parameter [13]
        in_dent_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DENT,
                                           displayName="Input Dent Features (12:00 Centered)",
                                           name="in_dent_features_12",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")

        # # Parameter [20]
        in_dent_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DENT,
                                                displayName="Dent Network Route ID Field",
                                                name="in_dent_routeid_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_dent_routeid_field.parameterDependencies = [in_dent_features.name]
        #
        # # Parameter [21]
        # in_dent_measure_field = arcpy.Parameter(category="ILI Dent Parameters",
        #                                         displayName="Dent Measure Field", name="in_dent_measure_field",
        #                                         datatype="Field", parameterType="Optional", direction="Input")
        # in_dent_measure_field.parameterDependencies = [in_dent_features.name]
        # in_dent_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [14]
        in_dent_depth_pct_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DENT,
                                                  displayName="Dent Diameter Percent Reduction Field",
                                                  name="in_dent_depth_pct_field",
                                                  datatype="Field", parameterType="Optional", direction="Input")
        in_dent_depth_pct_field.parameterDependencies = [in_dent_features.name]
        in_dent_depth_pct_field.filter.list = ['int', 'long', 'double']

        # Parameter [15]
        in_dent_clockpos_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DENT,
                                                 displayName="Dent Clock Position Field",
                                                 name="in_dent_clockpos_field",
                                                 datatype="Field", parameterType="Optional", direction="Input")
        in_dent_clockpos_field.parameterDependencies = [in_dent_features.name]
        in_dent_clockpos_field.filter.list = ['Text']

        parameters += [ in_dent_features, in_dent_features_12, in_dent_routeid_field, in_dent_depth_pct_field, in_dent_clockpos_field]

        #   ******************************************
        #   ILI Gouge Parameters
        #   ******************************************

        # Parameter [16]
        in_gouge_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_GOUGE,
                                            displayName="Input Gouge Features (6:00 Centered)",
                                            name="in_gouge_features",
                                            datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")
        # Parameter [17]
        in_gouge_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_GOUGE,
                                            displayName="Input Gouge Features (12:00 Centered)",
                                            name="in_gouge_features_12",
                                            datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")
        # # Parameter [26]
        in_gouge_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_GOUGE,
                                                 displayName="Gouge Network Route ID Field",
                                                 name="in_gouge_routeid_field",
                                                 datatype="Field", parameterType="Optional", direction="Input")
        in_gouge_routeid_field.parameterDependencies = [in_gouge_features.name]
        #
        # # Parameter [27]
        # in_gouge_measure_field = arcpy.Parameter(category="ILI Gouge Parameters",
        #                                          displayName="Gouge Measure Field",
        #                                          name="in_gouge_measure_field",
        #                                          datatype="Field", parameterType="Optional", direction="Input")
        # in_gouge_measure_field.parameterDependencies = [in_gouge_features.name]
        # in_gouge_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [ in_gouge_features, in_gouge_features_12, in_gouge_routeid_field]

        #   ******************************************
        #   ILI Weld Parameters
        #   ******************************************

        # Parameter [18]
        in_weld_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_WELD,
                                           displayName="Input Weld Features (6:00 Centered)",
                                           name="in_weld_features",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")
        # Parameter [19]
        in_weld_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_WELD,
                                           displayName="Input Weld Features (12:00 Centered)",
                                           name="in_weld_features_12",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")

        # # Parameter [30]
        in_weld_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_WELD,
                                                displayName="Weld Network Route ID Field",
                                                name="in_weld_routeid_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_weld_routeid_field.parameterDependencies = [in_weld_features.name]
        #
        # # Parameter [31]
        # in_weld_measure_field = arcpy.Parameter(category="ILI Weld Parameters",
        #                                         displayName="Weld Measure Field", name="in_weld_measure_field",
        #                                         datatype="Field", parameterType="Optional", direction="Input")
        # in_weld_measure_field.parameterDependencies = [in_weld_features.name]
        # in_weld_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_weld_features, in_weld_features_12, in_weld_routeid_field]

        #   ******************************************
        #   ILI Seam Parameters
        #   ******************************************

        # Parameter [20]
        in_seam_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_SEAM,
                                           displayName="Input Seam Features (6:00 Centered)",
                                           name="in_seam_features",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")
        # Parameter [21]
        in_seam_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_SEAM,
                                           displayName="Input Seam Features (12:00 Centered)",
                                           name="in_seam_features_12",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")

        # # Parameter [34]
        in_seam_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_SEAM,
                                                displayName="Seam Network Route ID Field",
                                                name="in_seam_routeid_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_seam_routeid_field.parameterDependencies = [in_seam_features.name]
        #
        # # Parameter [35]
        # in_seam_begin_measure_field = arcpy.Parameter(category="ILI Seam Parameters",
        #                                               displayName="Seam Begin Measure Field",
        #                                               name="in_seam_begin_measure_field",
        #                                               datatype="Field", parameterType="Optional", direction="Input")
        # in_seam_begin_measure_field.parameterDependencies = [in_seam_features.name]
        # in_seam_begin_measure_field.filter.list = ['int', 'long', 'double']
        #
        # # Parameter [36]
        # in_seam_end_measure_field = arcpy.Parameter(category="ILI Seam Parameters",
        #                                             displayName="Seam End Measure Field",
        #                                             name="in_seam_end_measure_field",
        #                                             datatype="Field", parameterType="Optional", direction="Input")
        # in_seam_end_measure_field.parameterDependencies = [in_seam_features.name]
        # in_seam_end_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [ in_seam_features, in_seam_features_12, in_seam_routeid_field]

        #   ******************************************
        #   ILI Bend Parameters
        #   ******************************************

        # Parameter [22]
        in_bend_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_BEND,
                                           displayName="Input Bend Features (6:00 Centered)",
                                           name="in_bend_features",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")
        # Parameter [23]
        in_bend_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_BEND,
                                           displayName="Input Bend Features (12:00 Centered)",
                                           name="in_bend_features_12",
                                           datatype=["GPFeatureLayer", "GPTableView"],
                                           parameterType="Optional",
                                           direction="Input")

        # # Parameter [39]
        in_bend_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_BEND,
                                                displayName="Bend Network Route ID Field",
                                                name="in_bend_routeid_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_bend_routeid_field.parameterDependencies = [in_bend_features.name]

        # # Parameter [40]
        # in_bend_measure_field = arcpy.Parameter(category="ILI Bend Parameters",
        #                                         displayName="Bend Measure Field", name="in_bend_measure_field",
        #                                         datatype="Field", parameterType="Optional", direction="Input")
        # in_bend_measure_field.parameterDependencies = [in_bend_features.name]
        # in_bend_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [ in_bend_features, in_bend_features_12, in_bend_routeid_field]

        #   ******************************************
        #   Highly Sensitive Areas Parameters
        #   ******************************************

        # Parameter [24]
        in_hsa_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_HCA,
                                           displayName="Input Highly Sensitive Area Features  (6:00 Centered)",
                                           name="in_hsa_features",
                                           datatype="GPFeatureLayer",
                                           parameterType="Optional",
                                           direction="Input")
        # Parameter [25]
        in_hsa_features_12 = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_HCA,
                                          displayName="Input Highly Sensitive Area Features  (12:00 Centered)",
                                          name="in_hsa_features_12",
                                          datatype="GPFeatureLayer",
                                          parameterType="Optional",
                                          direction="Input")
        # # Parameter [43]
        in_hsa_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_HCA,
                                                displayName="Input Highly Sensitive Areas Network Route ID Field",
                                                name="in_hsa_routeid_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_hsa_routeid_field.parameterDependencies = [in_hsa_features.name]


        parameters += [in_hsa_features, in_hsa_features_12, in_hsa_routeid_field]

        #   ******************************************
        #   Default Values
        #   ******************************************

        # Parameter [26]
        in_search_distance = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DEFAULT,
                                            displayName="Search Distance",
                                            name="in_search_distance",
                                            datatype="GPLinearUnit",
                                            parameterType="Optional",
                                            direction="Input")
        in_search_distance.value = '0.33 Feet'
        in_search_distance.filter.list = ['Feet', 'Meters']

        # Parameter [27]
        in_pipe_type = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_DEFAULT,
                                             displayName="Pipeline Type",
                                             name="in_pipe_type",
                                             datatype="GPString",
                                             parameterType="Required",
                                             direction="Input")

        in_pipe_type.filter.list = config.ANOMALY_PRIORITY_DEFAULT_PIPELINE_TYPES
        in_pipe_type.value = config.ANOMALY_PRIORITY_DEFAULT_PIPELINE_TYPES[0]

        parameters += [in_search_distance, in_pipe_type]

        #   ******************************************
        #   Target Anamoly Features Parameters
        #   ******************************************

        # Parameter [28]
        target_anomaly_features = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_TARGET_ANOMALY,
                                              displayName="Target Anamoly Features",
                                              name="target_anomaly_features",
                                              datatype=["GPFeatureLayer", "GPTableView"],
                                              parameterType="Optional",
                                              direction="Input")
        # Parameter [29]
        target_anomaly_routeid_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_TARGET_ANOMALY,
                                                  displayName="Target Anamoly Network Route ID Field",
                                                  name="target_anomaly_routeid_field",
                                                  datatype="Field", parameterType="Optional", direction="Input")
        target_anomaly_routeid_field.parameterDependencies = [target_anomaly_features.name]

        # Parameter [29]
        target_anomaly_id_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_TARGET_ANOMALY,
                                                displayName="Target Anamoly Unique ID Field",
                                                name="target_anomaly_id_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        target_anomaly_id_field.parameterDependencies = [target_anomaly_features.name]
        parameters += [target_anomaly_features, target_anomaly_routeid_field, target_anomaly_id_field]

        #   ******************************************
        #   Output Anamoly Priority Parameters
        #   ******************************************

        # Parameter [30]
        out_anomaly_priority_field = arcpy.Parameter(category=config.ANOMALY_PRIORITY_CATEGORY_OUTPUT,
                                                displayName="Out Anamoly Priority Field", name="out_anomaly_priority_field",
                                                datatype="GPString", parameterType="Optional", direction="Input")
        out_anomaly_priority_field.value = config.ANOMALY_PRIORITY_OUTPUT_ANOMALY_PRIORITY_FIELD_NAME

        parameters += [out_anomaly_priority_field]

        return parameters

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):

        # anomaly
        idx = 0
        idx2 = 9
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_ANOMALY_FIELDS)

        # crack or crack-like
        idx = 9
        idx2 = 12
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_CRACK_LIKE_FIELDS)

        # crack field
        idx = 12
        idx2 = 15
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_CRACK_FIELD_FIELDS)

        # dent
        idx = 15
        idx2 = 20
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_DENT_FIELDS)

        # gouge
        idx = 20
        idx2 = 23
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_GOUGE_FIELDS)

        # weld
        idx = 23
        idx2 = 26
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_WELD_LINES_FIELDS)

        # seam
        idx = 26
        idx2 = 29
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_SEAM_LINES_FIELDS)

        # bend
        idx = 29
        idx2 = 32
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_PIPE_BEND_FIELDS)

        # hsa
        idx = 32
        idx2 = 35
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.ANOMALY_PRIORITY_HSA_FIELDS)

        # target anomaly

        if self.param_changed(parameters[37]):
            if not parameters[38].value:
                parameters[38].value = config.ANOMALY_PRIORITY_TARGET_ANOMALY_FIELDS[0]
            if not parameters[39].value:
                parameters[39].value = config.ANOMALY_PRIORITY_TARGET_ANOMALY_FIELDS[1]

        return

    def updateMessages(self, parameters):

        return

    def param_changed(self, param):
        changed = param.value and not param.hasBeenValidated

        return changed

    def update_field_names(self, parameters, idx, idx2, field_names):
        try:
            idx1 = idx + 2
            if parameters[idx].value:
                for i in range(idx1, idx2):
                    if not parameters[i].value:
                        parameters[i].value = field_names[i - idx1]
            else:
                for i in range(idx1, idx2):
                    parameters[i].value = None

        except Exception as e:
            raise

    def execute(self, parameters, messages):
               
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting Anomaly Growth Calculator process...")
        # TODO remove comment after testing
        self.temp_gdm = arcpy.env.scratchGDB
        # self.temp_gdm = r"C:\Surendra\From_Sean\GDBs\Scratch.gdb"

        pimsilitool.AddMessage(self.temp_gdm)

        try:
            # initialize parameter values
            self.init_parameter_values_idxs(parameters)

            pimsilitool.AddMessage("Adding {} field...".format(self.out_anomaly_priority_field))
            # Check if the output field name exists in the input ILI anomaly features (6:00 centered), if not add field
            ili_flds = []
            ili_flds += [f.name.upper() for f in arcpy.ListFields(self.in_ili_features)]
            if self.out_anomaly_priority_field.upper() not in ili_flds:
                # arcpy.AddField_management(in_ili_features, out_anomaly_priority_field, "TEXT", field_length = 500, field_alias = out_anomaly_priority_field)
                arcpy.AddField_management(self.in_ili_features, self.out_anomaly_priority_field, "LONG")

            # Check if the output field name exists in the input ILI anomaly features (12:00 centered), if not add field
            if self.in_ili_features_12 :
                flds_12 = []
                flds_12 += [f.name.upper() for f in arcpy.ListFields(self.in_ili_features_12 )]
                if self.out_anomaly_priority_field.upper() not in flds_12:
                    # arcpy.AddField_management(in_ili_features_12, out_anomaly_priority_field, "TEXT", field_length = 500, field_alias = out_anomaly_priority_field)
                    arcpy.AddField_management(self.in_ili_features_12 , self.out_anomaly_priority_field, "LONG")

            ################
            # Check if the output field name exists in the input dent features (6:00 centered), if not add field
            if self.in_dent_features:
                flds = []
                flds += [f.name.upper() for f in arcpy.ListFields(self.in_dent_features)]
                if self.out_anomaly_priority_field.upper() not in flds:
                    arcpy.AddField_management(self.in_dent_features, self.out_anomaly_priority_field, "LONG")

            # Check if the output field name exists in the input ILI anomaly features (12:00 centered), if not add field
            if self.in_dent_features_12:
                flds_12 = []
                flds_12 += [f.name.upper() for f in arcpy.ListFields(self.in_dent_features_12)]
                if self.out_anomaly_priority_field.upper() not in flds_12:
                    arcpy.AddField_management(self.in_dent_features_12, self.out_anomaly_priority_field, "LONG")

            #################

            pimsilitool.AddMessage("Creating spatial joins..")
            # create spatial joins
            self.create_spatial_joins(parameters)

            self.convert_spatial_joins_to_numpy_array()

            # process input ILI anomaly features (6:00 centered) to update anomaly priority column
            self.calculate_anomaly_priorities(parameters, self.in_ili_features, self.in_dent_features)

            if self.in_ili_features_12  and self.in_dent_features_12:
                # process input ILI anomaly features (12:00 centered) to update anomaly priority column
                self.calculate_anomaly_priorities(parameters, self.in_ili_features_12 , self.in_dent_features_12)

            # Check if the output field name exists in the target anomaly features
            if self.target_anomaly_features:
                flds = []
                flds += [f.name.upper() for f in arcpy.ListFields(self.target_anomaly_features)]
                if self.out_anomaly_priority_field.upper() not in flds:
                    arcpy.AddField_management(self.target_anomaly_features, self.out_anomaly_priority_field, "LONG")

                self.calculate_target_anomaly_priority(self.in_ili_features, self.target_anomaly_features, self.target_anomaly_id_field, self.out_anomaly_priority_field)

            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def create_spatial_joins(self, parameters):
        try:
            # 6 o clock feature joins
            field_mappings = self.build_field_mappings(parameters)
            if self.in_ili_features:
                # [Metal_Loss_Dent_Sj, Metal_Loss_Bend_SJ, Metal_Loss_HCA_SJ, Metal_Loss_Weld_SJ, Metal_Loss_Seam_SJ]
                j = 0
                for lyr in self.metal_loss_join_layers:
                    spatial_join_features = os.path.join(self.temp_gdm, config.ANOMALY_PRIORITY_SPATIAL_JOINS[j])
                    if arcpy.Exists(spatial_join_features):
                        arcpy.Delete_management(spatial_join_features)
                    if lyr is not None:
                        pimsilitool.AddMessage("Spatial join {}".format(str(config.ANOMALY_PRIORITY_SPATIAL_JOINS[j])))
                        self.create_spatial_join(self.in_ili_features, lyr, spatial_join_features, self.in_search_distance, field_mappings[j])
                    j += 1

            if self.in_dent_features:
                # [Dent_Crack_SJ, Dent_Gouge_SJ, Dent_Weld_SJ, Dent_Seam_SJ_12, Dent_Bend_SJ]
                j = 5
                for lyr in self.dent_join_layers:
                    spatial_join_features = os.path.join(self.temp_gdm,  config.ANOMALY_PRIORITY_SPATIAL_JOINS[j])
                    if arcpy.Exists(spatial_join_features):
                        arcpy.Delete_management(spatial_join_features)
                    if lyr is not None:
                        pimsilitool.AddMessage("Spatial join {}".format(str(config.ANOMALY_PRIORITY_SPATIAL_JOINS[j])))
                        self.create_spatial_join(self.in_dent_features, lyr, spatial_join_features, self.in_search_distance, field_mappings[j])
                    j += 1

            # 12 o clock feature joins
            if self.in_ili_features_12:
                j = 0
                for lyr in self.metal_loss_join_layers_12:
                    spatial_join_features = os.path.join(self.temp_gdm, config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[j])
                    if arcpy.Exists(spatial_join_features):
                        arcpy.Delete_management(spatial_join_features)
                    if lyr is not None:
                        pimsilitool.AddMessage( "Spatial join {}".format(str(config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[j])))
                        self.create_spatial_join(self.in_ili_features_12, lyr, spatial_join_features, self.in_search_distance, field_mappings[j])
                    j += 1

            if self.in_dent_features_12:
                j = 5
                for lyr in self.dent_join_layers_12:
                    spatial_join_features = os.path.join(self.temp_gdm, config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[j])
                    if lyr is not None:
                        if arcpy.Exists(spatial_join_features):
                            arcpy.Delete_management(spatial_join_features)
                        pimsilitool.AddMessage("Spatial join {}".format(str(config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[j])))
                        self.create_spatial_join(self.in_dent_features_12, lyr, spatial_join_features, self.in_search_distance, field_mappings[j])
                    j += 1

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def build_field_mappings(self, parameters):
        try:

            field_mappings = []
            metal_loss_field_mappings = None
            crak_like_field_mappings = None
            crack_field_field_mappings = None
            dent_field_mappings = None
            gouge_field_mappings = None
            weld_field_mappings = None
            seam_field_mappings = None
            bend_field_mappings = None
            hca_field_mappings = None

            fld_desc = arcpy.ListFields(self.in_ili_features, self.in_pipe_routeid_field)[0]
            fld_type = fld_desc.type
            fld_legth = fld_desc.legth
            s = str(fld_legth) + ' ' + fld_type

            if self.in_ili_features:
                desc = arcpy.Describe(self.in_ili_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_pipe_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + oid_fieldname
                sj_pipe_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
                sj_pipe_depth_pct_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_depth_pct_field
                sj_pipe_clockpos_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_clockpos_field
                sj_pipe_maop_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_maop_field
                sj_pipe_burstpressure_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_burstpressure_field
                sj_pipe_safepressure_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_safepressure_field
                sj_pipe_erf_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_erf_field

                # fld_desc = arcpy.ListFields(self.in_ili_features, sj_pipe_routeid_field)[0]
                # fld_type = fld_desc.type
                # fld_legth = fld_desc.legth
                # stype = str(fld_legth) + ' ' + fld_type
                stype = self.get_field_type(self.in_ili_features, sj_pipe_routeid_field)

            metal_loss_field_mappings = sj_pipe_objid_field + ' "' + sj_pipe_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                            sj_pipe_routeid_field + ' "' + sj_pipe_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_pipe_routeid_field + ',-1,-1;' + \
                                            sj_pipe_depth_pct_field + ' "' + sj_pipe_depth_pct_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_pipe_depth_pct_field + ',-1,-1;' + \
                                            sj_pipe_clockpos_field + ' "' + sj_pipe_clockpos_field + '" true true false 20 String 0 0,First,#,' + features_path + ',' + self.in_pipe_clockpos_field + ',-1,-1;' + \
                                            sj_pipe_maop_field + ' "' + sj_pipe_maop_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_pipe_maop_field + ',-1,-1;' + \
                                            sj_pipe_burstpressure_field + ' "' + sj_pipe_burstpressure_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_pipe_burstpressure_field  + ',-1,-1;' + \
                                            sj_pipe_safepressure_field + ' "' + sj_pipe_safepressure_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_pipe_safepressure_field + ',-1,-1;' + \
                                            sj_pipe_erf_field + ' "' + sj_pipe_erf_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_pipe_erf_field  + ',-1,-1;'                                                                                                                                                                                                                                                                \

            if self.in_crack_features:
                desc = arcpy.Describe(self.in_crack_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[1] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[1] + self.in_crack_routeid_field

                stype = self.get_field_type(self.in_crack_features, sj_routeid_field)

                crak_like_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                           sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_crack_routeid_field + ',-1,-1;'


            if self.in_crack_field_features:
                desc = arcpy.Describe(self.in_crack_field_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[2] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[2] + self.in_crack_field_routeid_field

                stype = self.get_field_type(self.in_crack_field_features, sj_routeid_field)

                crack_field_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                             sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_crack_field_routeid_field + ',-1,-1;'

            if self.in_dent_features:
                desc = arcpy.Describe(self.in_dent_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                sj_depth_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_depth_pct_field
                sj_clockpos_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_clockpos_field

                stype = self.get_field_type(self.in_dent_features, sj_routeid_field)

                dent_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                             sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_dent_routeid_field + ',-1,-1;' + \
                                             sj_depth_field + ' "' + sj_depth_field + '" true true false 8 Double 0 0,First,#,' + features_path + ',' + self.in_dent_depth_pct_field + ',-1,-1;' + \
                                             sj_clockpos_field + ' "' + sj_clockpos_field + '" true true false 20 String 0 0,First,#,' + features_path + ',' + self.in_dent_clockpos_field + ',-1,-1;'

            if self.in_gouge_features:
                desc = arcpy.Describe(self.in_gouge_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[4] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[4] + self.in_gouge_routeid_field

                stype = self.get_field_type(self.in_gouge_features, sj_routeid_field)

                gouge_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                       sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_gouge_routeid_field  + ',-1,-1;'

            if self.in_weld_features:
                desc = arcpy.Describe(self.in_weld_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + self.in_weld_routeid_field

                stype = self.get_field_type(self.in_weld_features, sj_routeid_field)

                weld_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                       sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_weld_routeid_field  + ',-1,-1;'

            if self.in_seam_features:
                desc = arcpy.Describe(self.in_seam_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + self.in_seam_routeid_field

                stype = self.get_field_type(self.in_seam_features, sj_routeid_field)

                seam_field_mappings =  sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;' + \
                                       sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_seam_routeid_field   + ',-1,-1;'

            if self.in_bend_features :
                desc = arcpy.Describe(self.in_bend_features )
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[7] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[7] + self.in_bend_routeid_field

                stype = self.get_field_type(self.in_bend_features, sj_routeid_field)

                bend_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;'+ \
                                       sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_bend_routeid_field   + ',-1,-1;'

            if self.in_hsa_features:
                desc = arcpy.Describe(self.in_hsa_features)
                oid_fieldname = desc.OIDFieldName
                features_path = desc.catalogPath

                sj_objid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[8] + oid_fieldname
                sj_routeid_field = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[8] + self.in_hsa_routeid_field

                stype = self.get_field_type(self.in_hsa_features, sj_routeid_field)

                hca_field_mappings = sj_objid_field + ' "' + sj_objid_field + '" true true false 10 Long 0 0,First,#,' + features_path + ',' + oid_fieldname + ',-1,-1;'+ \
                                       sj_routeid_field + ' "' + sj_routeid_field + '" true true false ' + stype + ' 0 0,First,#,' + features_path + ',' + self.in_hsa_routeid_field + ',-1,-1;'

            if self.in_ili_features:
                if self.in_dent_features:
                    field_mappings.append(metal_loss_field_mappings + dent_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_bend_features:
                    field_mappings.append(metal_loss_field_mappings + bend_field_mappings)
                else:
                    field_mappings.append(self.null_arr)

                if self.in_hsa_features:
                    field_mappings.append(metal_loss_field_mappings + hca_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_weld_features:
                    field_mappings.append(metal_loss_field_mappings + weld_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_seam_features:
                    field_mappings.append(metal_loss_field_mappings + seam_field_mappings )
                else:
                    field_mappings.append(self.null_arr)
            else:
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)

            if self.in_dent_features:
                if self.in_crack_features:
                    field_mappings.append(dent_field_mappings + crak_like_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_crack_field_features:
                    field_mappings.append(dent_field_mappings + crack_field_field_mappings)
                else:
                    field_mappings.append(self.null_arr)

                if self.in_gouge_features:
                    field_mappings.append(dent_field_mappings + gouge_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_weld_features:
                    field_mappings.append(dent_field_mappings + weld_field_mappings )
                else:
                    field_mappings.append(self.null_arr)
                if self.in_seam_features:
                    field_mappings.append(dent_field_mappings + seam_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
                if self.in_bend_features:
                    field_mappings.append(dent_field_mappings + bend_field_mappings)
                else:
                    field_mappings.append(self.null_arr)
            else:
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)
                field_mappings.append(self.null_arr)

            return field_mappings

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def create_spatial_join(self, target_features, join_features, out_feature_class, search_radius, field_mappings):
        try:
            if arcpy.Exists(out_feature_class):
                arcpy.Delete_management(out_feature_class)
            arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, "JOIN_ONE_TO_MANY", "KEEP_COMMON",
                                       field_mappings,   match_option="WITHIN_A_DISTANCE", search_radius=search_radius)

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def convert_spatial_joins_to_numpy_array(self):
        try:
            self.sj2_numpy_arrays = []
            self.sj2_numpy_arrays_12 = []

            # 06:00 cenetered
            for i in range(0, 11):
                in_layer = os.path.join(self.temp_gdm, config.ANOMALY_PRIORITY_SPATIAL_JOINS[i])
                if arcpy.Exists(in_layer):
                    pimsilitool.AddMessage("Creating Feature Class To NumPy Array " + config.ANOMALY_PRIORITY_SPATIAL_JOINS[i])
                    arr = arcpy.da.FeatureClassToNumPyArray(in_layer, "*", null_value=-999)
                    if len(arr) > 0:
                        self.sj2_numpy_arrays.append(arr)
                    else:
                        self.sj2_numpy_arrays.append(self.null_arr)
                    arcpy.Delete_management(in_layer)
                else:
                    self.sj2_numpy_arrays.append(self.null_arr)

            # 12:00 cenetered
            for i in range(0, 11):
                in_layer = os.path.join(self.temp_gdm, config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[i])
                if arcpy.Exists(in_layer):
                    pimsilitool.AddMessage("Creating Feature Class To NumPy Array " + config.ANOMALY_PRIORITY_SPATIAL_JOINS_12[i])
                    arr = arcpy.da.FeatureClassToNumPyArray(in_layer, "*", null_value=-999)
                    if len(arr) > 0:
                        self.sj2_numpy_arrays_12.append(arr)
                    else:
                        self.sj2_numpy_arrays_12.append(self.null_arr)
                    arcpy.Delete_management(in_layer)
                else:
                    self.sj2_numpy_arrays_12.append(self.null_arr)

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def calculate_anomaly_priorities(self, parameters, in_ili_features, in_dent_features):
        try:
            pipe_oid_fieldname = arcpy.Describe(in_ili_features).OIDFieldName
            if self.in_dent_features is not None:
                dent_oid_fieldname = arcpy.Describe(self.in_dent_features).OIDFieldName
            else:
                dent_oid_fieldname = None

            pipe_fields = [self.out_anomaly_priority_field, pipe_oid_fieldname,
                           self.in_pipe_depth_pct_field, self.in_pipe_clockpos_field,
                           self.in_pipe_maop_field, self.in_pipe_burstpressure_field,
                           self.in_pipe_safepressure_field, self.in_pipe_erf_field, self.in_pipe_routeid_field]

            where_clause = "{} IS NOT NULL AND {} IS NOT NULL AND {} IS NOT NULL AND {} IS NOT NULL " \
                           "AND {} IS NOT NULL AND {} IS NOT NULL".format(
                            self.in_pipe_depth_pct_field, self.in_pipe_clockpos_field , self.in_pipe_maop_field,
                            self.in_pipe_burstpressure_field, self.in_pipe_safepressure_field, self.in_pipe_erf_field)

            # Step 4 open update cursor input ILI anomaly features
            if self.in_pipe_type == config.ANOMALY_PRIORITY_DEFAULT_PIPELINE_TYPES[0]:
                with arcpy.da.UpdateCursor(in_ili_features, pipe_fields, where_clause) as cursor:

                    pimsilitool.AddMessage("Updating {} field...".format(self.out_anomaly_priority_field))
                    pimsilitool.AddMessage(self.in_pipe_type)
                    for row in cursor:
                        pipe_oid = row[1]
                        pipe_depth_pct = row[2]
                        pipe_maop = row[4]
                        pipe_burstpressure = row[5]
                        pipe_safepressure = row[6]
                        pipe_erf = row[7]
                        route_id = row[8]

                        # Step 4.1, check depth pct value is greater than 70% ie Metal loss greater than 70% of nominal wall regardless of length and width
                        if pipe_depth_pct > 70:
                            # row[0] = "1 - Metal loss greater than 70% of nominal wall regardless of length and width. (Priority 1-D70)"
                            row[0] = 1

                        # Step 4.2, Metal loss anomalies with a predicted burst pressure that is less than
                        # the established maximum operating pressure at the location of the anomaly
                        elif pipe_burstpressure < pipe_maop:
                            # row[0] = "2 - Metal loss anomalies with a predicted burst pressure that is less than " \
                            #          "the established maximum operating pressure at the location of the anomaly (Priority 1–Burst)"
                            row[0] = 2
                        # Step 4.3, A dent located on the top of the pipeline (above the 4 and 8 o'clock positions)
                        # that has any indication of metal loss, cracking or a stress riser
                        elif self.dent_located_on_topof_pipe_stress_riser(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, route_id):
                            row[0] = 3
                            # row[0] = "3 - A dent located on the top of the pipeline (above the 4 and 8 o'clock positions) " \
                            #          "that has any indication of metal loss, cracking or a stress riser (Priority 1–Top Stress Riser)"

                        # Step 4.4, A dent located on the top of the pipeline (above the 4 and 8 o'clock positions)
                        # with a depth greater than 6% of the pipe diameter
                        elif self.dent_located_on_topof_pipe_depth_6pct(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 4
                            # row[0] = "4 - A dent located on the top of the pipeline (above the 4 and 8 o'clock positions) " \
                            #          "with a depth greater than 6% of the pipe diameter (Priority 1-Top Dent>6%)"

                        # Step 4.5, Anomalies and anomaly clusters with an Estimated Repair Factor (ERF) of 0.70 or greater
                        elif pipe_erf > 0.7:
                            row[0] = 5
                            # row[0] = "5 - Anomalies and anomaly clusters with an Estimated Repair Factor (ERF) of 0.70 or greater (Priority 1-ERF)"

                        # Step 4.6, Metal loss and dents in bends
                        elif self.metal_loss_dents_in_bends(pipe_oid_fieldname, pipe_oid, route_id):
                            row[0] = 6
                            # row[0] = "6 - Metal loss and dents in bends (Priority 1-B)"

                        # Step 4.7, Anomalies in Highly Sensitive Areas
                        elif self.anomalies_in_hca(pipe_oid_fieldname, pipe_oid, route_id):
                            row[0] = 7
                            # row[0] = "7 - Anomalies in Highly Sensitive Areas (Priority 1-HSA)"

                        # Step 4.8, A dent with depth greater than 3% of the pipeline diameter or greater than 0.250 inches
                        # in depth for a pipeline diameter less than Nominal Pipe Size (NPS) 12.
                        elif self.dent_with_depth_3pct(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 8
                            # row[0] = "8 - A dent with depth greater than 3% of the pipeline diameter or greater than 0.250 inches " \
                            #          "in depth for a pipeline diameter less than Nominal Pipe Size (NPS) 12. (Priority 2-Dent>3%)"

                        # Step 4.9, Metal loss anomalies with depth greater than 30% near girth welds
                        # (the edge of the metal loss within 4 inches of the girth weld
                        elif self.metal_loss_30pct_near_girth_welds(pipe_oid_fieldname, pipe_oid, self.in_pipe_depth_pct_field, route_id):
                            row[0] = 9
                            # row[0] = "9 - Metal loss anomalies with depth greater than 30% near girth welds " \
                            #          "(the edge of the metal loss within 4 inches of the girth weld (Priority 2–D30 EGW)"

                        # Step 4.10, A dent located on the bottom of the pipeline that has any indication of metal loss,
                        # cracking or a stress riser. riser (Priority 2–Bottom Stress Riser)
                        elif self.dent_located_on_bottomof_pipe_stress_riser(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 10
                            # row[0] = "10 - A dent located on the bottom of the pipeline that has any indication of " \
                            #          "metal loss, cracking or a stress riser. riser (Priority 2–Bottom Stress Riser)"

                        # Step 4.11, A dent with a depth greater than 2% of the pipeline's diameter (0.250 inches
                        # in depth for a pipeline diameter less than NPS 12) near girth welds or near longitudinal seam weld.
                        # (the edge of the anomaly within 4 inches of the girth weld or longitudinal seam
                        elif self.dent_2pct_near_weld_seam(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 11
                            # row[0] = "11 - A dent with a depth greater than 2% of the pipeline's diameter " \
                            #          "(0.250 inches in depth for a pipeline diameter less than NPS 12) near girth welds or " \
                            #          "near longitudinal seam weld. (the edge of the anomaly within 4 inches of the girth weld or longitudinal seam (Priority 3-Dent EGW)"

                        # Step 4.12, A dent located on the top of the pipeline (above 4 and 8 o'clock position) with
                        # a depth greater than 2% of the pipeline's diameter (0.250 inches in depth for a pipeline diameter
                        # less than NPS 12). (Priority 3-Top Dent>2%)
                        elif self.dent_located_on_topof_pipe_depth_2pct(pipe_oid_fieldname, pipe_oid, dent_oid_fieldname, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 12
                            # row[0] = "12 - A dent located on the top of the pipeline (above 4 and 8 o'clock position) " \
                            #          "with a depth greater than 2% of the pipeline's diameter (0.250 inches in depth for " \
                            #          "a pipeline diameter less than NPS 12). (Priority 3-Top Dent>2%)"

                        # Step 4.13, Metal loss anomalies with a predicted safe pressure that is less than the
                        # established maximum operating pressure at the location of the anomaly
                        elif pipe_safepressure < pipe_maop:
                            row[0] = 13
                            # row[0] = "13 - Metal loss anomalies with a predicted safe pressure that is less than " \
                            #          "the established maximum operating pressure at the location of the anomaly (Priority 3–MOP)"

                        # Step 4.14, Metal loss anomalies with a predicted depth greater than 50% of nominal wall.
                        elif pipe_depth_pct > 50:
                            row[0] = 14
                            # row[0] = "14 - Metal loss anomalies with a predicted depth greater than 50% of nominal wall. (Priority 3–D50)"

                        # Step 4.15, Metal loss greater than 30% of nominal wall a long a longitudinal seam weld.
                        elif self.metal_loss_30pct_along_seam(pipe_oid_fieldname, pipe_oid, self.in_pipe_depth_pct_field, route_id):
                            row[0] = 15
                            # row[0] = "15 - Metal loss greater than 30% of nominal wall a long a longitudinal seam weld. (Priority 3–D30 ELW)"

                        # Step 4.16, Anomalies not mentioned above but located nearby a priority anomaly to be examined at the same time
                        else:
                            row[0] = 16
                            # row[0] = "16 - Anomalies not mentioned but located nearby a priority anomaly to be examined at the same time (Priority N-1-XXX)"
                        cursor.updateRow(row)
            else:
                """
                    Gas Pipeline
                    1. pipe burst pressure <= 1.1 * reference pressure                    
                    2. dent -> metal loss
                       dent -> cracking
                       dent -> stress riser                    
                    3. dent -> depth > 6% of pipe diameter + clock position 8 and 4                    
                    4. dent -> depth > 2% of pipe diameter + weld 
                       dent -> depth > 2% of pipe diameter + seam                    
                    5. dent -> depth > 6% of pipe diameter + clock position 4 and 8                    
                    6. dent -> depth > 6% of pipe diameter + clock position 8 and 4 + engineering analyses of the dent demonstrate critical strain levels are not exceeded.
                    7. dent -> depth > 2% of pipe diameter + weld + engineering analyses of the dent and girth demonstrate critical strain levels are not exceeded.
                       dent -> depth > 2% of pipe diameter + seam + engineering analyses of the dent and seam weld demonstrate critical strain levels are not exceeded.
                """
                dent_fields = [self.out_anomaly_priority_field, dent_oid_fieldname,
                               self.in_dent_depth_pct_field, self.in_dent_clockpos_field,
                               self.in_pipe_maop_field, self.in_pipe_burstpressure_field,
                               self.in_dent_routeid_field]

                dent_where_clause = "{} IS NOT NULL AND {} IS NOT NULL".format(self.in_dent_depth_pct_field, self.in_dent_clockpos_field)
                with arcpy.da.UpdateCursor(in_dent_features, dent_fields, dent_where_clause) as cursor:

                    pimsilitool.AddMessage("Updating {} field...".format(self.out_anomaly_priority_field))
                    pimsilitool.AddMessage(self.in_pipe_type)
                    for row in cursor:
                        dent_oid = row[1]
                        dent_depth_pct = row[2]
                        dent_clock_pos = row[3]
                        pipe_maop = row[4]
                        pipe_burstpressure = row[5]
                        route_id = row[6]
                        if pipe_burstpressure is not None and pipe_maop is not None:
                            if pipe_burstpressure <= 1.1 * pipe_maop:
                                row[0] = 1
                        if self.gas_dent_located_on_topof_pipe_stress_riser(dent_oid_fieldname, dent_oid, route_id):
                            row[0] = 2
                        elif self.gas_dent_located_on_topof_pipe_depth_6pct_8_4_clock(dent_oid_fieldname, dent_oid, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 3
                        elif self.gas_dent_2pct_near_weld_seam(dent_oid_fieldname, dent_oid, self.in_dent_depth_pct_field, route_id):
                            row[0] = 4
                        elif self.gas_dent_located_on_topof_pipe_depth_6pct_4_8_clock(dent_oid_fieldname, dent_oid, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 5
                        elif self.gas_dent_located_on_topof_pipe_depth_6pct_8_4_clock_eng(dent_oid_fieldname, dent_oid, self.in_dent_clockpos_field, self.in_dent_depth_pct_field, route_id):
                            row[0] = 6
                        elif self.gas_dent_2pct_near_weld_seam_eng(dent_oid_fieldname, dent_oid, self.in_dent_depth_pct_field, route_id):
                            row[0] = 7
                        else:
                            row[0] = 8

                        cursor.updateRow(row)

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_located_on_topof_pipe_stress_riser(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, route_id):
        # TODO Step 4.3, A dent located on the top of the pipeline
        #  (above the 4 and 8 o'clock positions) that has any indication of metal loss, cracking or a stress riser
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            dent_cracklike_features = self.sj2_numpy_arrays[5]
            dent_crackfield_features = self.sj2_numpy_arrays[6]
            dent_gouge_features = self.sj2_numpy_arrays[7]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])

                    if 4 < clock_hours < 8:
                        dent_oid_value = metal_loss_dent_feature[0][dent_obj_field_name]
                        if dent_cracklike_features[0][0] != self.null_arr[0][0]:
                            crack_like_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[1] + self.in_crack_routeid_field
                            dent_cracklike_feature = dent_cracklike_features[(dent_cracklike_features[dent_obj_field_name] == dent_oid_value) &
                                                                             (dent_cracklike_features[dent_routeid_field_name] ==route_id) &
                                                                             (dent_cracklike_features[crack_like_routeid_field_name] == route_id)]
                            if len(dent_cracklike_feature) > 0:
                                return True
                        elif dent_crackfield_features[0][0] != self.null_arr[0][0]:
                            crack_field_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[2] + self.in_crack_field_routeid_field
                            dent_crackfield_feature = dent_crackfield_features[(dent_crackfield_features[dent_obj_field_name] == dent_oid_value) &
                                                                               (dent_crackfield_features[dent_routeid_field_name] == route_id) &
                                                                               (dent_crackfield_features[crack_field_routeid_field_name] == route_id)]
                            if len(dent_crackfield_feature) > 0:
                                return True
                        elif dent_gouge_features[0][0] != self.null_arr[0][0]:
                            gouge_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[4] + self.in_gouge_routeid_field
                            dent_gouge_feature = dent_gouge_features[(dent_gouge_features[dent_obj_field_name] == dent_oid_value) &
                                                                     (dent_gouge_features[dent_routeid_field_name] == route_id) &
                                                                     (dent_gouge_features[gouge_routeid_field_name] == route_id)]
                            if len(dent_gouge_feature) > 0:
                                return True
                        else:
                            return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_located_on_topof_pipe_depth_6pct(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, dent_depth_pct_field, route_id):
        # TODO Step 4.4, A dent located on the top of the pipeline
        #  (above the 4 and 8 o'clock positions) with a depth greater than 6% of the pipe diameter
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            # dent_cracklike_features = self.sj2_numpy_arrays[5]
            # dent_crackfield_features = self.sj2_numpy_arrays[6]
            # dent_gouge_features = self.sj2_numpy_arrays[7]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 6) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])
                    if 4 < clock_hours < 8:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def metal_loss_dents_in_bends(self, pipe_oid_name, pipe_oid_value, route_id):
        # TODO Step 4.6, Metal loss and dents in bends
        try:

            metal_loss_bend_features = self.sj2_numpy_arrays[1]

            if metal_loss_bend_features[0][0] != self.null_arr[0][0]:
                obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                bend_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[7] + self.in_bend_routeid_field
                metal_loss_bend_feature = metal_loss_bend_features[(metal_loss_bend_features[obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_bend_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_bend_features[bend_routeid_field_name] == route_id)]
                if len(metal_loss_bend_feature) > 0:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def anomalies_in_hca(self, pipe_oid_name, pipe_oid_value, route_id):
        try:

            metal_loss_hca_features = self.sj2_numpy_arrays[2]

            if metal_loss_hca_features[0][0] != self.null_arr[0][0]:
                obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                hsa_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[8] + self.in_hsa_routeid_field
                metal_loss_hca_feature = metal_loss_hca_features[(metal_loss_hca_features[obj_field_name] == pipe_oid_value) &
                                                                 (metal_loss_hca_features[pipe_routeid_field_name] == route_id) &
                                                                 (metal_loss_hca_features[hsa_routeid_field_name] == route_id)]
                if len(metal_loss_hca_feature) > 0:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_with_depth_3pct(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, dent_depth_pct_field, route_id):
        # TODO Step 4.8, A dent with depth greater than 3% of the pipeline diameter or greater than 0.250 inches
        #  in depth for a pipeline diameter less than Nominal Pipe Size (NPS) 12.
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            # dent_cracklike_features = self.sj2_numpy_arrays[5]
            # dent_crackfield_features = self.sj2_numpy_arrays[6]
            # dent_gouge_features = self.sj2_numpy_arrays[7]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[ 3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 3) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def metal_loss_30pct_near_girth_welds(self, pipe_oid_name, pipe_oid_value, pipe_depth_pct_field, route_id):
        try:

            metal_loss_weld_features = self.sj2_numpy_arrays[3]

            if metal_loss_weld_features[0][0] != self.null_arr[0][0]:
                obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[ 0] + self.in_pipe_routeid_field
                depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_depth_pct_field

                weld_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + self.in_weld_routeid_field
                metal_loss_weld_feature = metal_loss_weld_features[(metal_loss_weld_features[obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_weld_features[depth_field_name] > 30) &
                                                                   (metal_loss_weld_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_weld_features[weld_routeid_field_name] == route_id)]
                if len(metal_loss_weld_feature) > 0:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_located_on_bottomof_pipe_stress_riser(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, dent_depth_pct_field, route_id):
        # TODO Step 4.10, A dent located on the bottom of the pipeline that has any indication of
        #  metal loss, cracking or a stress riser. riser (Priority 2–Bottom Stress Riser)
        try:
            if dent_oid_name is None:
                return False
            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            dent_cracklike_features = self.sj2_numpy_arrays[5]
            dent_crackfield_features = self.sj2_numpy_arrays[6]
            dent_gouge_features = self.sj2_numpy_arrays[7]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])

                    if 4 > clock_hours > 8:
                        dent_oid_value = metal_loss_dent_feature[0][dent_obj_field_name]
                        if dent_cracklike_features[0][0] != self.null_arr[0][0]:
                            crack_like_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[1] + self.in_crack_routeid_field

                            dent_cracklike_feature = dent_cracklike_features[(dent_cracklike_features[dent_obj_field_name] == dent_oid_value) &
                                                                             (dent_cracklike_features[dent_routeid_field_name] == route_id) &
                                                                             (dent_cracklike_features[crack_like_routeid_field_name] == route_id)]
                            if len(dent_cracklike_feature) > 0:
                                return True
                        elif dent_crackfield_features[0][0] != self.null_arr[0][0]:
                            crack_field_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[2] + self.in_crack_field_routeid_field
                            dent_crackfield_feature = dent_crackfield_features[(dent_crackfield_features[dent_obj_field_name] == dent_oid_value) &
                                                                               (dent_crackfield_features[dent_routeid_field_name] == route_id) &
                                                                               (dent_crackfield_features[crack_field_routeid_field_name] == route_id)]
                            if len(dent_crackfield_feature) > 0:
                                return True
                        elif dent_gouge_features[0][0] != self.null_arr[0][0]:
                            gouge_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[4] + self.in_gouge_routeid_field
                            dent_gouge_feature = dent_gouge_features[(dent_gouge_features[dent_obj_field_name] == dent_oid_value) &
                                                                     (dent_gouge_features[dent_routeid_field_name] == route_id) &
                                                                     (dent_gouge_features[gouge_routeid_field_name] == route_id)]
                            if len(dent_gouge_feature) > 0:
                                return True
                        else:
                            return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_2pct_near_weld_seam(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, dent_depth_pct_field, route_id):
        # TODO Step 4.11, A dent with a depth greater than 2% of the pipeline's diameter
        #  (0.250 inches in depth for a pipeline diameter less than NPS 12) near girth welds or
        #  near longitudinal seam weld. (the edge of the anomaly within 4 inches of the girth weld or longitudinal seam
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            # dent_cracklike_features = self.sj2_numpy_arrays[5]
            # dent_crackfield_features = self.sj2_numpy_arrays[6]
            # dent_gouge_features = self.sj2_numpy_arrays[7]
            dent_weld_features = self.sj2_numpy_arrays[8]
            dent_seam_features = self.sj2_numpy_arrays[9]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[
                                              0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[
                                              3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field
                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 2) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:

                    dent_oid_value = metal_loss_dent_feature[0][dent_obj_field_name]
                    if dent_weld_features[0][0] != self.null_arr[0][0]:
                        weld_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + self.in_dent_routeid_field
                        dent_wekd_feature = dent_weld_features[(dent_weld_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_weld_features[dent_routeid_field_name] == route_id) &
                                                               (dent_weld_features[weld_routeid_field_name] == route_id)]
                        if len(dent_wekd_feature) > 0:
                            return True
                    elif dent_seam_features[0][0] != self.null_arr[0][0]:
                        seam_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + self.in_dent_routeid_field
                        dent_seam_feature = dent_seam_features[(dent_seam_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_seam_features[dent_routeid_field_name] ==  route_id) &
                                                               (dent_seam_features[seam_routeid_field_name] == route_id)]
                        if len(dent_seam_feature) > 0:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def dent_located_on_topof_pipe_depth_2pct(self, pipe_oid_name, pipe_oid_value, dent_oid_name, dent_clockpos_name, dent_depth_pct_field, route_id):
        # TODO Step 4.12, A dent located on the top of the pipeline (above 4 and 8 o'clock position)
        #  with a depth greater than 2% of the pipeline's diameter (0.250 inches in depth for a pipeline diameter less than NPS 12). (Priority 3-Top Dent>2%)
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            # dent_cracklike_features = self.sj2_numpy_arrays[5]
            # dent_crackfield_features = self.sj2_numpy_arrays[6]
            # dent_gouge_features = self.sj2_numpy_arrays[7]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                pipe_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[pipe_obj_field_name] == pipe_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 2) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])
                    if 4 < clock_hours < 8:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def metal_loss_30pct_along_seam(self, pipe_oid_name, pipe_oid_value, pipe_depth_pct_field, route_id):
        try:

            metal_loss_seam_features = self.sj2_numpy_arrays[4]

            if metal_loss_seam_features[0][0] != self.null_arr[0][0]:
                obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_oid_name
                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
                depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + pipe_depth_pct_field

                seam_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + self.in_dent_routeid_field
                metal_loss_seam_feature = metal_loss_seam_features[(metal_loss_seam_features[obj_field_name] == pipe_oid_value) &
                                                                    (metal_loss_seam_features[depth_field_name] > 30) &
                                                                   (metal_loss_seam_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_seam_features[seam_routeid_field_name] == route_id)]
                if len(metal_loss_seam_feature) > 0:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def calculate_target_anomaly_priority(self, in_ili_features, target_anomaly_features, target_anomaly_id_field, out_anomaly_priority_field):
        try:
            pimsilitool.AddMessage("Calculating Target Anomaly Priority..")
            in_ili_features_basename = arcpy.Describe(in_ili_features).baseName
            target_anomaly_features_basename = arcpy.Describe(target_anomaly_features).baseName

            arcpy.management.AddJoin(target_anomaly_features, target_anomaly_id_field,
                                     in_ili_features, target_anomaly_id_field, "KEEP_ALL", "NO_INDEX_JOIN_FIELDS")
            arcpy.management.CalculateField(target_anomaly_features, target_anomaly_features_basename + "." + out_anomaly_priority_field,
                                            "!" + in_ili_features_basename + "." + out_anomaly_priority_field + "!",
                                            "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
        except Exception as e:
            raise

    def init_parameter_values_idxs(self, parameters):
        try:
            self.in_ili_features = parameters[0].value
            self.in_ili_features_12 = parameters[1].value
            self.in_pipe_routeid_field = parameters[2].valueAsText
            self.in_pipe_depth_pct_field = parameters[3].valueAsText
            self.in_pipe_clockpos_field = parameters[4].valueAsText
            self.in_pipe_maop_field = parameters[5].valueAsText
            self.in_pipe_burstpressure_field = parameters[6].valueAsText
            self.in_pipe_safepressure_field = parameters[7].valueAsText
            self.in_pipe_erf_field = parameters[8].valueAsText
            self.in_crack_features = parameters[9].value
            self.in_crack_features_12 = parameters[10].value
            self.in_crack_routeid_field = parameters[11].valueAsText
            self.in_crack_field_features = parameters[12].value
            self.in_crack_field_features_12 = parameters[13].value
            self.in_crack_field_routeid_field = parameters[14].valueAsText
            self.in_dent_features = parameters[15].value
            self.in_dent_features_12 = parameters[16].value
            self.in_dent_routeid_field = parameters[17].valueAsText
            self.in_dent_depth_pct_field = parameters[18].valueAsText
            self.in_dent_clockpos_field = parameters[19].valueAsText
            self.in_gouge_features = parameters[20].value
            self.in_gouge_features_12 = parameters[21].value
            self.in_gouge_routeid_field = parameters[22].valueAsText
            self.in_weld_features = parameters[23].value
            self.in_weld_features_12 = parameters[24].value
            self.in_weld_routeid_field = parameters[25].valueAsText
            self.in_seam_features = parameters[26].value
            self.in_seam_features_12 = parameters[27].value
            self.in_seam_routeid_field = parameters[28].valueAsText
            self.in_bend_features = parameters[29].value
            self.in_bend_features_12 = parameters[30].value
            self.in_bend_routeid_field = parameters[31].valueAsText
            self.in_hsa_features = parameters[32].value
            self.in_hsa_features_12 = parameters[33].value
            self.in_hsa_routeid_field = parameters[34].valueAsText
            self.in_search_distance = parameters[35].valueAsText
            self.in_pipe_type = parameters[36].valueAsText
            self.target_anomaly_features = parameters[37].value
            self.target_anomaly_routeid_field = parameters[38].valueAsText
            self.target_anomaly_id_field = parameters[39].valueAsText
            self.out_anomaly_priority_field = parameters[40].valueAsText

            # metal anomalies spatial join with dent, bend, hsa, weld, seam features, 06:00 cenetered
            # self.metal_loss_join_layer_idxs = [12, 22, 24, 18, 20]
            self.metal_loss_join_layers = [self.in_dent_features,
                                               self.in_bend_features,
                                               self.in_hsa_features,
                                               self.in_weld_features,
                                               self.in_seam_features]

            # metal anomalies spatial join with dent, bend, hsa, weld, seam features, 12:00 cenetered
            # self.metal_loss_join_layer_idxs_12 = [13, 23, 25, 19, 21]
            self.metal_loss_join_layers_12 = [self.in_dent_features_12,
                                                   self.in_bend_features_12,
                                                   self.in_hsa_features_12,
                                                   self.in_weld_features_12,
                                                   self.in_seam_features_12]

            # dent spatial join with crack-like, crack field, gouge, weld, seam, bend features, 06:00 cenetered
            # self.dent_join_layer_idxs = [8, 10, 16, 18, 20, 22]
            self.dent_join_layers = [self.in_crack_features,
                                         self.in_crack_field_features,
                                         self.in_gouge_features,
                                         self.in_weld_features,
                                         self.in_seam_features,
                                         self.in_bend_features]

            # dent spatial join with crack-like, crack field, gouge, weld, seam, bend features, 12:00 cenetered
            # self.dent_join_layer_idxs_12 = [9, 11, 17, 19, 21, 23]
            self.dent_join_layers_12 =  [self.in_crack_features_12,
                                         self.in_crack_field_features_12,
                                         self.in_gouge_features_12,
                                         self.in_weld_features_12,
                                         self.in_seam_features_12,
                                         self.in_bend_features_12]

            # null array
            self.null_arr = numpy.array([(-9999)], dtype=[('id', '<i4')])


        except Exception as e:
            raise

    def gas_dent_located_on_topof_pipe_stress_riser(self, dent_oid_name, dent_oid_value, route_id):
        try:
            if dent_oid_name is None:
                return False
            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            dent_cracklike_features = self.sj2_numpy_arrays[5]
            dent_crackfield_features = self.sj2_numpy_arrays[6]
            dent_gouge_features = self.sj2_numpy_arrays[7]
            dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
            pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
            dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:
                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    return True

            if dent_cracklike_features[0][0] != self.null_arr[0][0]:
                crack_like_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[1] + self.in_crack_routeid_field
                dent_cracklike_feature = dent_cracklike_features[(dent_cracklike_features[dent_obj_field_name] == dent_oid_value) &
                                                                 (dent_cracklike_features[dent_routeid_field_name] == route_id) &
                                                                 (dent_cracklike_features[crack_like_routeid_field_name] == route_id)]
                if len(dent_cracklike_feature) > 0:
                    return True

            if dent_crackfield_features[0][0] != self.null_arr[0][0]:
                crack_field_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[2] + self.in_crack_field_routeid_field
                dent_crackfield_feature = dent_crackfield_features[(dent_crackfield_features[dent_obj_field_name] == dent_oid_value) &
                                                                   (dent_crackfield_features[dent_routeid_field_name] == route_id) &
                                                                   (dent_crackfield_features[crack_field_routeid_field_name] == route_id)]
                if len(dent_crackfield_feature) > 0:
                    return True

            if dent_gouge_features[0][0] != self.null_arr[0][0]:
                gouge_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[4] + self.in_gouge_routeid_field
                dent_gouge_feature = dent_gouge_features[(dent_gouge_features[dent_obj_field_name] == dent_oid_value) &
                                                         (dent_gouge_features[dent_routeid_field_name] == route_id) &
                                                         (dent_gouge_features[gouge_routeid_field_name] == route_id)]
                if len(dent_gouge_feature) > 0:
                    return True

            return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def gas_dent_located_on_topof_pipe_depth_6pct_8_4_clock(self, dent_oid_name, dent_oid_value, dent_clockpos_name, dent_depth_pct_field, route_id):
        try:
            if dent_oid_name is None:
                return False
            metal_loss_dent_features = self.sj2_numpy_arrays[0]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:

                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 6) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])
                    if 8 < clock_hours < 4:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def gas_dent_2pct_near_weld_seam(self,  dent_oid_name, dent_oid_value, dent_depth_pct_field, route_id):
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            dent_weld_features = self.sj2_numpy_arrays[8]
            dent_seam_features = self.sj2_numpy_arrays[9]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:

                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 2) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    if dent_weld_features[0][0] != self.null_arr[0][0]:
                        weld_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + self.in_dent_routeid_field
                        dent_wekd_feature = dent_weld_features[(dent_weld_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_weld_features[dent_routeid_field_name] == route_id) &
                                                               (dent_weld_features[weld_routeid_field_name] == route_id)]
                        if len(dent_wekd_feature) > 0:
                            return True
                    elif dent_seam_features[0][0] != self.null_arr[0][0]:
                        seam_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + self.in_dent_routeid_field
                        dent_seam_feature = dent_seam_features[(dent_seam_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_seam_features[dent_routeid_field_name] ==  route_id) &
                                                               (dent_seam_features[seam_routeid_field_name] == route_id)]
                        if len(dent_seam_feature) > 0:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def gas_dent_located_on_topof_pipe_depth_6pct_4_8_clock(self, dent_oid_name, dent_oid_value, dent_clockpos_name, dent_depth_pct_field, route_id):
        try:
            if dent_oid_name is None:
                return False
            metal_loss_dent_features = self.sj2_numpy_arrays[0]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:

                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 6) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])
                    if 4 < clock_hours < 8:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def gas_dent_located_on_topof_pipe_depth_6pct_8_4_clock_eng(self, dent_oid_name, dent_oid_value, dent_clockpos_name, dent_depth_pct_field, route_id):
        try:
            if dent_oid_name is None:
                return False
            metal_loss_dent_features = self.sj2_numpy_arrays[0]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:

                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field

                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_clockpos_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_clockpos_name
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 6) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    # check clock postion
                    clock_pos = metal_loss_dent_feature[0][dent_clockpos_field_name]
                    clock_parts = clock_pos.split(':')
                    clock_hours = int(clock_parts[0])
                    if 8 < clock_hours < 4:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def gas_dent_2pct_near_weld_seam_eng(self,  dent_oid_name, dent_oid_value, dent_depth_pct_field, route_id):
        try:
            if dent_oid_name is None:
                return False

            metal_loss_dent_features = self.sj2_numpy_arrays[0]
            dent_weld_features = self.sj2_numpy_arrays[8]
            dent_seam_features = self.sj2_numpy_arrays[9]

            if metal_loss_dent_features[0][0] != self.null_arr[0][0]:

                pipe_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[0] + self.in_pipe_routeid_field
                dent_obj_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_oid_name
                dent_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + self.in_dent_routeid_field
                dent_depth_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[3] + dent_depth_pct_field

                # get metal loss dent spatial join
                metal_loss_dent_feature = metal_loss_dent_features[(metal_loss_dent_features[dent_oid_name] == dent_oid_value) &
                                                                   (metal_loss_dent_features[dent_depth_field_name] > 2) &
                                                                   (metal_loss_dent_features[pipe_routeid_field_name] == route_id) &
                                                                   (metal_loss_dent_features[dent_routeid_field_name] == route_id)]
                if len(metal_loss_dent_feature) > 0:
                    if dent_weld_features[0][0] != self.null_arr[0][0]:
                        weld_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[5] + self.in_dent_routeid_field
                        dent_wekd_feature = dent_weld_features[(dent_weld_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_weld_features[dent_routeid_field_name] == route_id) &
                                                               (dent_weld_features[weld_routeid_field_name] == route_id)]
                        if len(dent_wekd_feature) > 0:
                            return True
                    elif dent_seam_features[0][0] != self.null_arr[0][0]:
                        seam_routeid_field_name = config.ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX[6] + self.in_dent_routeid_field
                        dent_seam_feature = dent_seam_features[(dent_seam_features[dent_obj_field_name] == dent_oid_value) &
                                                               (dent_seam_features[dent_routeid_field_name] ==  route_id) &
                                                               (dent_seam_features[seam_routeid_field_name] == route_id)]
                        if len(dent_seam_feature) > 0:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def get_field_type(self, in_fc, in_fld):
        try:
            fld_desc = arcpy.ListFields(in_fc, in_fld)[0]
            fld_type = fld_desc.type
            fld_legth = fld_desc.legth

            return str(fld_legth) + ' ' + fld_type

        except Exception as e:
            raise

