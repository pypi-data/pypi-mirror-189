
""" Headline: Anomaly Processing Inline Inspection Anomaly Growth Calculation tool
    Calls:  pimsilitool, pimsilitool.config
    inputs: ILI Feature class(Which is calibrated and imported)
    Description: This tool calculates Anomaly Growth.  
    Output: The output of this tool.
   """

from logging import exception
import arcpy
import pimsilitool
import os
import datetime as dt
import math
from pimsilitool import config
import traceback
import sys
from arcpy import env
import numpy
from pimsilitool.license.validate_license.license_operation import LicenseOperation

class AnomalyConverter(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Convert ILI Anomalies to Point, Envelope and Ellipse Features"
        self.description = "This Tool Convert ILI Anomalies to Point, Envelopes and Eclipese Features"
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):

        parameters = []

        #   ******************************************
        #   ILI Metal Loss Anomaly Parameters
        #   ******************************************
               
        # Input ILI point featuere - Parameter [0]       
        in_ili_features = arcpy.Parameter(displayName="Input ILI Anomaly Features", name="in_ili_features",
                                        category = config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype=["GPFeatureLayer","GPTableView"], parameterType="Required", direction="Input")
        #  Parameter[1]
        in_ili_odometer_field = arcpy.Parameter(displayName="ILI Anomaly Measure Field", name="in_ili_odometer_field",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="Field", parameterType="Required", direction="Input")
        in_ili_odometer_field.parameterDependencies = [in_ili_features.name]       
        in_ili_odometer_field.filter.list = ['int', 'long', 'double']

        #  Parameter[2]
        in_ili_width_field = arcpy.Parameter(displayName="ILI Anomaly Width Field", name="in_ili_width_field",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="Field", parameterType="Required", direction="Input")
        in_ili_width_field.parameterDependencies = [in_ili_features.name]
        in_ili_width_field.filter.list = ['int', 'long', 'double']

        #  Parameter[3]
        in_ili_length_field = arcpy.Parameter(displayName="ILI Anomaly Length Field", name="in_ili_length_field",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="Field", parameterType="Required", direction="Input")
        in_ili_length_field.parameterDependencies = [in_ili_features.name]       
        in_ili_length_field.filter.list = ['int', 'long', 'double']

        #  Parameter[4]
        in_ili_clockposition_field = arcpy.Parameter(displayName="ILI Anomaly Clock Position Field", name="in_ili_clockposition_field",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="Field", parameterType="Required", direction="Input")
        in_ili_clockposition_field.parameterDependencies = [in_ili_features.name]
        in_ili_clockposition_field.filter.list = ['Text']

        #  Parameter[5]
        in_ili_pipediameter_value = arcpy.Parameter(displayName="ILI Pipe Diameter Value", name="in_ili_pipediameter_value",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="GPLong", parameterType="Required", direction="Input")

        #  Parameter[6]
        in_ili_yaxisorientation_value = arcpy.Parameter(displayName="Input Y-Axis Clock Orientation", name="in_ili_yaxisorientation_value",
                                        category=config.CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY,
                                        datatype="GPString", parameterType="Required", direction="Input")
        in_ili_yaxisorientation_value.filter.list = config.CONVERT_ILI_ANOM_CLOCK_POSITION
        in_ili_yaxisorientation_value.value = config.CONVERT_ILI_ANOM_CLOCK_POSITION[0]

        parameters += [in_ili_features, in_ili_odometer_field, in_ili_width_field, in_ili_length_field,
                       in_ili_clockposition_field, in_ili_pipediameter_value, in_ili_yaxisorientation_value]

        #   ******************************************
        #   Default Values Parameters
        #   ******************************************

        #  Parameter[7]
        in_ili_clockpostion_offset_value = arcpy.Parameter(displayName="Input Clock Position Offset", name="in_ili_clockpostion_offset_value",
                                        category=config.CONVERT_ILI_CATEGORY_DEFAULT_VALUES,
                                        datatype="GPString", parameterType="Required", direction="Input")
        in_ili_clockpostion_offset_value.value="0:00"

        #  Parameter[8]
        in_ili_sr = arcpy.Parameter(displayName="Spatial Refference for Output Features", name="in_ili_sr",
                                        category=config.CONVERT_ILI_CATEGORY_DEFAULT_VALUES,
                                        datatype="GPSpatialReference",parameterType="Required", direction="Input")
        in_ili_sr.value = "PROJCS['NAD_1983_UTM_Zone_16N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Foot_US',0.3048006096012192]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

        #  Parameter[9]
        in_ili_falsenorthing_value = arcpy.Parameter(displayName="Input False Northing Value", name="in_ili_falsenorthing_value",
                                        category=config.CONVERT_ILI_CATEGORY_DEFAULT_VALUES,
                                        datatype="GPDouble", parameterType="Required", direction="Input")
        in_ili_falsenorthing_value.value=0

        #  Parameter[10]
        in_ili_falseeasting_value = arcpy.Parameter(displayName="Input False Easting Value", name="in_ili_falseeasting_value",
                                        category=config.CONVERT_ILI_CATEGORY_DEFAULT_VALUES,
                                        datatype="GPDouble", parameterType="Required", direction="Input")
        in_ili_falseeasting_value.value=0

        parameters += [in_ili_clockpostion_offset_value, in_ili_sr, in_ili_falsenorthing_value, in_ili_falseeasting_value]

        #   ******************************************
        #   Generate Grid Lines Parameters
        #   ******************************************
         
        # Generate Grid Lines
        #  Parameter[11]
        in_is_grid_line = arcpy.Parameter(displayName="Generate Grid Lines", name="in_is_grid_line",
                                            category=config.CONVERT_ILI_CATEGORY_GRID_LINES,
                                            datatype="GPBoolean",  parameterType="Optional", direction="Input")
        in_is_grid_line.value = True

        parameters += [in_is_grid_line]

        #   ******************************************
        #   ILI Crack or Crack-like Parameters
        #   ******************************************

        # Parameter [12]
        in_crack_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_LIKE,
                                            displayName="Input Crack or Crack-like Features", name="in_crack_features",
                                            datatype=["GPFeatureLayer", "GPTableView"], parameterType="Optional", direction="Input")
        # Parameter [13]
        in_crack_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_LIKE,
                                             displayName="Crack or Crack-like Measure Field", name="in_crack_measure_field",
                                             datatype="Field", parameterType="Optional", direction="Input")
        in_crack_measure_field.parameterDependencies = [in_crack_features.name]
        in_crack_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[14]
        in_crack_width_field = arcpy.Parameter(displayName="Crack or Crack-like Width Field", name="in_crack_width_field",
                                            category=config.CONVERT_ILI_CATEGORY_CRACK_LIKE,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_width_field.parameterDependencies = [in_crack_features.name]
        in_crack_width_field.filter.list = ['int', 'long', 'double']

        #  Parameter[15]
        in_crack_length_field = arcpy.Parameter(displayName="Crack or Crack-like Length Field", name="in_crack_length_field",
                                            category=config.CONVERT_ILI_CATEGORY_CRACK_LIKE,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_length_field.parameterDependencies = [in_crack_features.name]
        in_crack_length_field.filter.list = ['int', 'long', 'double']

        #  Parameter[16]
        in_crack_clockposition_field = arcpy.Parameter(displayName="Crack or Crack-like Clock Position Field", name="in_crack_clockposition_field",
                                            category=config.CONVERT_ILI_CATEGORY_CRACK_LIKE,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_clockposition_field.parameterDependencies = [in_crack_features.name]
        in_crack_clockposition_field.filter.list = ['Text']

        parameters += [in_crack_features, in_crack_measure_field, in_crack_width_field, in_crack_length_field, in_crack_clockposition_field]

        #   ******************************************
        #   ILI Crack Field Parameters
        #   ******************************************

        # Parameter [17]
        in_crack_field_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_FIELD, displayName="Input Crack Field Features",
                                            name="in_crack_field_features", datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")
        # Parameter [18]
        in_crack_field_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_FIELD,
                                            displayName="Crack Field Measure Field", name="in_crack_field_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_field_measure_field.parameterDependencies = [in_crack_field_features.name]
        in_crack_field_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[19]
        in_crack_field_width_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_FIELD,
                                            displayName="Crack Field Width Field", name="in_crack_field_width_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_field_width_field.parameterDependencies = [in_crack_field_features.name]
        in_crack_field_width_field.filter.list = ['int', 'long', 'double']

        #  Parameter[20]
        in_crack_field_length_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_FIELD,
                                            displayName="Crack Field Length Field", name="in_crack_field_length_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_field_length_field.parameterDependencies = [in_crack_field_features.name]
        in_crack_field_length_field.filter.list = ['int', 'long', 'double']

        #  Parameter[21]
        in_crack_field_clockposition_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_CRACK_FIELD,
                                            displayName="Crack Field Clock Position Field", name="in_crack_field_clockposition_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_crack_field_clockposition_field.parameterDependencies = [in_crack_field_features.name]
        in_crack_field_clockposition_field.filter.list = ['Text']

        parameters += [in_crack_field_features, in_crack_field_measure_field, in_crack_field_width_field,
                       in_crack_field_length_field, in_crack_field_clockposition_field]

        #   ******************************************
        #   ILI Dent Parameters
        #   ******************************************

        # Parameter [22]
        in_dent_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_DENT, displayName="Input Dent Features",
                                            name="in_dent_features", datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")

        # Parameter [23]
        in_dent_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_DENT, displayName="Dent Measure Field",
                                            name="in_dent_measure_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_dent_measure_field.parameterDependencies = [in_dent_features.name]
        in_dent_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[24]
        in_dent_width_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_DENT, displayName="Dent Width Field",
                                            name="in_dent_width_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_dent_width_field.parameterDependencies = [in_dent_features.name]
        in_dent_width_field.filter.list = ['int', 'long', 'double']

        #  Parameter[25]
        in_dent_length_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_DENT, displayName="Dent Length Field",
                                            name="in_dent_length_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_dent_length_field.parameterDependencies = [in_dent_features.name]
        in_dent_length_field.filter.list = ['int', 'long', 'double']

        #  Parameter[26]
        in_dent_clockpos_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_DENT,  displayName="Dent Clock Position Field",
                                            name="in_dent_clockpos_field",  datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_dent_clockpos_field.parameterDependencies = [in_dent_features.name]
        in_dent_clockpos_field.filter.list = ['Text']

        parameters += [in_dent_features, in_dent_measure_field, in_dent_width_field,
                       in_dent_length_field, in_dent_clockpos_field]

        #   ******************************************
        #   ILI Gouge Parameters
        #   ******************************************

        # Parameter [27]
        in_gouge_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_GOUGE, displayName="Input Gouge Features",
                                            name="in_gouge_features", datatype=["GPFeatureLayer", "GPTableView"],
                                            parameterType="Optional", direction="Input")

        # Parameter [28]
        in_gouge_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_GOUGE, displayName="Gouge Measure Field",
                                            name="in_gouge_measure_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_gouge_measure_field.parameterDependencies = [in_gouge_features.name]
        in_gouge_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[29]
        in_gouge_width_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_GOUGE, displayName="Gouge Width Field",
                                            name="in_gouge_width_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_gouge_width_field.parameterDependencies = [in_gouge_features.name]
        in_gouge_width_field.filter.list = ['int', 'long', 'double']

        #  Parameter[30]
        in_gouge_length_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_GOUGE, displayName="Gouge Length Field",
                                            name="in_gouge_length_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_gouge_length_field.parameterDependencies = [in_gouge_features.name]
        in_gouge_length_field.filter.list = ['int', 'long', 'double']

        #  Parameter[31]
        in_gouge_clockposition_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_GOUGE, displayName="Gouge Clock Position Field",
                                            name="in_gouge_clockposition_field", datatype="Field",
                                            parameterType="Optional", direction="Input")
        in_gouge_clockposition_field.parameterDependencies = [in_gouge_features.name]
        in_gouge_clockposition_field.filter.list = ['Text']

        parameters += [in_gouge_features, in_gouge_measure_field, in_gouge_width_field,
                       in_gouge_length_field, in_gouge_clockposition_field]

        #   ******************************************
        #   ILI Weld Lines Parameters
        #   ******************************************
        #  Parameter[32]
        in_is_weld_line = arcpy.Parameter(displayName="Generate Weld Lines", name="in_is_weld_line",
                                            category=config.CONVERT_ILI_CATEGORY_WELD_LINES,
                                            datatype="GPBoolean",  parameterType="Optional", direction="Input")
        in_is_weld_line.value = True

        #  Parameter[33]
        in_ili_weld_features = arcpy.Parameter( displayName="Input ILI Weld Features", name="in_ili_weld_features",
                                            category=config.CONVERT_ILI_CATEGORY_WELD_LINES,
                                            datatype=["GPFeatureLayer","GPTableView"], parameterType="Optional", direction="Input")

        #  Parameter[34]
        in_ili_weld_odometer_field = arcpy.Parameter(displayName="ILI Weld Measure Field", name="in_ili_weld_odometer_field",
                                            category=config.CONVERT_ILI_CATEGORY_WELD_LINES,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_ili_weld_odometer_field.parameterDependencies = [in_ili_weld_features.name]       
        in_ili_weld_odometer_field.filter.list = ['int', 'long', 'double']

        # #  Parameter[35]
        # in_ili_weld_diameter_value = arcpy.Parameter( displayName="ILI Weld Diameter Value", name="in_ili_weld_diameter_value",
        #                                     category="Weld Lines Parameters",
        #                                     datatype="GPLong", parameterType="Optional", direction="Input")

        parameters += [in_is_weld_line, in_ili_weld_features, in_ili_weld_odometer_field]

        #   ******************************************
        #   ILI Seam Parameters
        #   ******************************************

        #  Parameter[35]
        in_is_seam_line = arcpy.Parameter(displayName="Generate Seam Lines", name="in_is_seam_line",
                                            category=config.CONVERT_ILI_CATEGORY_SEAM_LINES, datatype="GPBoolean",
                                            parameterType="Optional", direction="Input")
        in_is_seam_line.value = True

        #  Parameter[36]
        in_ili_seam_features = arcpy.Parameter( displayName="Input ILI Seam Features", name="in_ili_seam_features",
                                            category=config.CONVERT_ILI_CATEGORY_SEAM_LINES,
                                            datatype=["GPFeatureLayer", "GPTableView"], parameterType="Optional", direction="Input")

        #  Parameter[37]
        in_ili_seam_odometer_field = arcpy.Parameter( displayName="ILI Seam Measure Field", name="in_ili_seam_odometer_field",
                                            category=config.CONVERT_ILI_CATEGORY_SEAM_LINES,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_ili_seam_odometer_field.parameterDependencies = [in_ili_seam_features.name]
        in_ili_seam_odometer_field.filter.list = ['int', 'long', 'double']

        #  Parameter[38]
        in_ili_seam_clockpos_field = arcpy.Parameter(displayName="ILI Seam Clock Position Field", name="in_ili_seam_clockpos_field",
                                            category=config.CONVERT_ILI_CATEGORY_SEAM_LINES,
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_ili_seam_clockpos_field.parameterDependencies = [in_ili_seam_features.name]
        in_ili_seam_clockpos_field.filter.list = ['Text']

        parameters += [in_is_seam_line, in_ili_seam_features, in_ili_seam_odometer_field, in_ili_seam_clockpos_field]

        #   ******************************************
        #   ILI Bend Parameters
        #   ******************************************

        # Parameter [39]
        in_bend_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_BEND, displayName="Input Bend Features",
                                            name="in_bend_features",
                                            datatype=["GPFeatureLayer", "GPTableView", "DETable"], parameterType="Optional", direction="Input")

        # Parameter [40]
        in_bend_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_BEND, displayName="Bend Measure Field",
                                            name="in_bend_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_bend_measure_field.parameterDependencies = [in_bend_features.name]
        in_bend_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[41]
        in_bend_from_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_BEND, displayName="Bend From Measure Field",
                                            name="in_bend_from_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_bend_from_measure_field.parameterDependencies = [in_bend_features.name]
        in_bend_from_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[42]
        in_bend_to_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_BEND, displayName="Bend To Measure Field",
                                            name="in_bend_to_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_bend_to_measure_field.parameterDependencies = [in_bend_features.name]
        in_bend_to_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_bend_features, in_bend_measure_field, in_bend_from_measure_field,  in_bend_to_measure_field]

        #   ******************************************
        #   ILI HCA Parameters
        #   ******************************************

        # Parameter [43]
        in_hsa_features = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_HSA, displayName="Input High Consequence Areas Features",
                                            name="in_hsa_features",
                                            datatype=["GPFeatureLayer", "GPTableView", "DETable"], parameterType="Optional", direction="Input")

        #  Parameter[44]
        in_hsa_from_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_HSA, displayName="HSA From Measure Field",
                                            name="in_hsa_from_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_hsa_from_measure_field.parameterDependencies = [in_hsa_features.name]
        in_hsa_from_measure_field.filter.list = ['int', 'long', 'double']

        #  Parameter[45]
        in_hsa_to_measure_field = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_HSA, displayName="HSA To Measure Field",
                                            name="in_hsa_to_measure_field",
                                            datatype="Field", parameterType="Optional", direction="Input")
        in_hsa_to_measure_field.parameterDependencies = [in_hsa_features.name]
        in_hsa_to_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_hsa_features, in_hsa_from_measure_field, in_hsa_to_measure_field]

        #   ******************************************
        #   ILI Output Parameters
        #   ******************************************

        # Parameter[46]
        in_workspace = arcpy.Parameter(category=config.CONVERT_ILI_CATEGORY_OUTPUT, displayName="Target GeoDatabase", name="in_workspace",
                                            datatype="DEWorkspace", parameterType="Required", direction="Input")
        in_workspace.value = arcpy.env.workspace

        #  Parameter[47]
        out_ili_point_features = arcpy.Parameter(displayName="Output Anomaly Point Features", name="out_ili_point_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Required",
                                            direction="Output")

        #  Parameter[48]
        out_ili_ellipse_features = arcpy.Parameter(displayName="Output Anomaly Ellipse Features", name="out_ili_ellipse_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Required",
                                            direction="Output")

        #  Parameter[49]
        out_ili_envelop_features = arcpy.Parameter(displayName="Output Anomaly Envelop Features", name="out_ili_envelop_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Required",
                                            direction="Output")

        #  Parameter[50]
        out_grid_features = arcpy.Parameter(displayName="Output Grid Line Features", name="out_grid_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")

        # Parameter[51]
        out_crack_point_features = arcpy.Parameter(displayName="Output Crack or Crack-like Point Features", name="out_crack_point_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        #  Parameter[52]
        out_crack_ellipse_features = arcpy.Parameter(displayName="Output Crack or Crack-like Ellipse Features", name="out_crack_ellipse_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")

        #  Parameter[53]
        out_crack_envelop_features = arcpy.Parameter(displayName="Output Crack or Crack-like Envelop Features", name="out_crack_envelop_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")

        # Parameter[54]
        out_crack_field_point_features = arcpy.Parameter(displayName="Output Crack Field Point Features", name="out_crack_field_point_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")
        #  Parameter[55]
        out_crack_field_ellipse_features = arcpy.Parameter(displayName="Output Crack Field Ellipse Features", name="out_crack_field_ellipse_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")

        #  Parameter[56]
        out_crack_field_envelop_features = arcpy.Parameter(displayName="Output Crack Field Envelop Features", name="out_crack_field_envelop_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        # Parameter[57]
        out_dent_point_features = arcpy.Parameter(displayName="Output Dent Point Features", name="out_dent_point_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")
        #  Parameter[58]
        out_dent_ellipse_features = arcpy.Parameter(displayName="Output Dent Ellipse Features", name="out_dent_ellipse_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        #  Parameter[59]
        out_dent_envelop_features = arcpy.Parameter(displayName="Output Dent Envelop Features", name="out_dent_envelop_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        # Parameter[60]
        out_gouge_point_features = arcpy.Parameter(displayName="Output Gouge Point Features", name="out_gouge_point_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        #  Parameter[61]
        out_gouge_ellipse_features = arcpy.Parameter(displayName="Output Gouge Ellipse Features", name="out_gouge_ellipse_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")

        #  Parameter[62]
        out_gouge_envelop_features = arcpy.Parameter(displayName="Output Gouge Envelop Features", name="out_gouge_envelop_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        #  Parameter[63]
        out_weld_features = arcpy.Parameter(displayName="Output Weld Line Features", name="out_weld_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")

        #  Parameter[64]
        out_seam_features = arcpy.Parameter(displayName="Output Seam Line Features", name="out_seam_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer", parameterType="Optional",
                                            direction="Output")
        #  Parameter[65]
        out_bend_features = arcpy.Parameter(displayName="Output Bend Features", name="out_bend_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")
        #  Parameter[66]
        out_hsa_features = arcpy.Parameter(displayName="Output High Consequence Areas Features", name="out_hsa_features",
                                            category=config.CONVERT_ILI_CATEGORY_OUTPUT, datatype="GPFeatureLayer",  parameterType="Optional",
                                            direction="Output")

        parameters += [in_workspace, out_ili_point_features, out_ili_ellipse_features, out_ili_envelop_features, out_grid_features,
                       out_crack_point_features, out_crack_ellipse_features, out_crack_envelop_features,
                       out_crack_field_point_features, out_crack_field_ellipse_features, out_crack_field_envelop_features,
                       out_dent_point_features, out_dent_ellipse_features, out_dent_envelop_features,
                       out_gouge_point_features, out_gouge_ellipse_features, out_gouge_envelop_features,
                       out_weld_features,  out_seam_features, out_bend_features, out_hsa_features]

        return parameters

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):

        # metal loss anomaly
        idx = 0
        idx2 = 5
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_ANOMALY_FIELDS)

        # crack or crack like
        idx = 12
        idx2 = 17
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_CRACK_LIKE_FIELDS)

        # crack field
        idx = 17
        idx2 = 22
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_CRACK_FIELD_FIELDS)

        # dent
        idx = 22
        idx2 = 27
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_DENT_FIELDS)

        # gouge
        idx = 27
        idx2 = 32
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_GOUGE_FIELDS)

        # weld lines
        idx = 33
        idx2 = 35
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_WELD_LINES_FIELDS)

        # Weld parameters  based on the check box selection
        if parameters[32].value:
            parameters[33].enabled = parameters[34].enabled = parameters[63].enabled = True
        else:
            parameters[33].enabled = parameters[34].enabled = parameters[63].enabled = False

        # seam lines
        idx = 36
        idx2 = 39
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_SEAM_LINES_FIELDS)

        # Seam parameters  based on the check box selection
        if parameters[35].value:
            parameters[36].enabled = parameters[37].enabled = parameters[38].enabled = parameters[64].enabled = True
        else:
            parameters[36].enabled = parameters[37].enabled = parameters[38].enabled = parameters[64].enabled = False

        # bend
        idx = 39
        idx2 = 43
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_PIPE_BEND_FIELDS)

        # hsa
        idx = 43
        idx2 = 46
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.CONVERT_ILI_HSA_FIELDS)

        if parameters[6].value == config.CONVERT_ILI_ANOM_CLOCK_POSITION[0]:# and "6:00 Centered" in parameters[6].valueAsText:
            sufx = config.CONVERT_ILI_OUTPUT_NAME_SUFFIX_6_CLOCK
        else:
            sufx = config.CONVERT_ILI_OUTPUT_NAME_SUFFIX_12_CLOCK
        if self.param_changed(parameters[6]):
            yaxis_changed = True
        else:
            yaxis_changed = False

        if not parameters[46].value:
            parameters[46].value = arcpy.env.workspace

        # metal loss anomalies
        in_layer_idx = 0
        out_layer_idxs = [47, 48, 49]
        field_idx = [1, 2, 3, 4]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_ANOMALY_NAMES, sufx, yaxis_changed)

        # grid
        in_layer_idx = 11
        out_layer_idxs = [50]
        field_idx = []
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_GRID_NAMES, sufx, yaxis_changed)

        # crack like
        in_layer_idx = 12
        out_layer_idxs = [51, 52, 53]
        field_idx = [13, 14, 15, 16]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs,field_idx, config.CONVERT_ILI_OUTPUT_CRACK_LIKE_NAMES, sufx, yaxis_changed)

        # crack field
        in_layer_idx = 17
        out_layer_idxs = [54, 55, 56]
        field_idx = [18, 19, 20, 21]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_CRACK_FIELD_NAMES, sufx, yaxis_changed)

        # dent
        in_layer_idx = 22
        out_layer_idxs = [57, 58, 59]
        field_idx = [57, 58, 59]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_DENT_NAMES, sufx, yaxis_changed)

        # gouge
        in_layer_idx = 27
        out_layer_idxs = [60, 61, 62]
        field_idx = [28, 29, 30, 31]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_GOUGE_NAMES, sufx, yaxis_changed)

        # weld
        in_layer_idx = 33
        out_layer_idxs = [63]
        field_idx = [34]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_WELD_NAMES, sufx, yaxis_changed)

        # seam
        in_layer_idx = 36
        out_layer_idxs = [64]
        field_idx = [37, 38]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_SEAM_NAMES, sufx, yaxis_changed)

        # bend features
        in_layer_idx = 39
        out_layer_idxs = [65]
        field_idx = [40,41,42]

        if parameters[39].value:
            parameters[65].enabled = True
            is_point = False
            desc = arcpy.Describe(parameters[39].value)
            if desc.datatype == 'FeatureClass' or desc.datatype == 'FeatureLayer':
                if desc.shapeType == 'Point':
                    is_point = True
            if is_point:
                parameters[40].enabled = True
                if parameters[40].value is None:
                    parameters[40].value = config.CONVERT_ILI_PIPE_BEND_FIELDS[0]
                parameters[41].enabled = parameters[42].enabled = False
                parameters[41].value = parameters[42].value = None
            else:
                parameters[41].enabled = parameters[42].enabled = True
                if parameters[41].value is None:
                    parameters[41].value = config.CONVERT_ILI_PIPE_BEND_FIELDS[1]
                if parameters[42].value is None:
                    parameters[42].value = config.CONVERT_ILI_PIPE_BEND_FIELDS[2]
                parameters[40].enabled = False
                parameters[40].value = None
        else:
            parameters[40].enabled = parameters[41].enabled = parameters[42].enabled = parameters[65].enabled = False
            parameters[40].value = parameters[41].value = parameters[42].value = parameters[65].value = None
        if parameters[46].value is not None:
            workspace = parameters[46].valueAsText
            if parameters[65].enabled:
                if parameters[65].value is None:
                    parameters[65].value =  os.path.join(workspace, config.CONVERT_ILI_OUTPUT_BEND_NAMES[0] + sufx)
                else:
                    fc_name = os.path.basename(parameters[65].valueAsText)
                    parameters[65].value = os.path.join(workspace, fc_name)
        # hsa
        in_layer_idx = 43
        out_layer_idxs = [66]
        field_idx = [44, 45]
        self.set_default_layers(parameters, in_layer_idx, out_layer_idxs, field_idx, config.CONVERT_ILI_OUTPUT_HCA_NAMES, sufx, yaxis_changed)

        return

    def updateMessages(self, parameters):  
        if parameters[0].value:
            if parameters[32].value:    # weld features
                if not parameters[33].value:
                    parameters[33].setErrorMessage("Please select input Weld Features/Table,\n As Generate Weld Lines Option is selected.")
                if not parameters[34].value:
                    parameters[34].setErrorMessage("Please select the field,\n As Generate Weld Lines Option is selected.")

            if parameters[35].value:    # seam features
                if not parameters[36].value:
                    parameters[36].setErrorMessage("Please select input Seam Features/Table,\n As Generate Seam Lines Option is selected.")
                if not parameters[37].value:
                    parameters[37].setErrorMessage("Please select the field,\n As Generate Seam Lines Option is selected.")
                if not parameters[38].value:
                    parameters[38].setErrorMessage("Please provide the value,\n As Generate Seam Lines Option is selected.")
            if parameters[35].value and not parameters[32].value:
                parameters[32].setErrorMessage("Please select input Weld Features,\n As Generate Seam Lines Option is selected.")

        return

    def check_field_exists(self, param):
        try:
            if not param.value:
                param.setErrorMessage("Parameter can not be empty.")

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

    def set_default_layers(self, parameters, idx, layer_ids, fld_idxs, descs, sufx, yaxis_changed):
        try:
            workspace = parameters[46].valueAsText
            if parameters[idx].value:
                for i in range(0, len(layer_ids)):
                    parameters[layer_ids[i]].enabled = True
                    if (not parameters[layer_ids[i]].value) or yaxis_changed:
                        # parameters[layer_ids[i]].value = os.path.join(arcpy.env.scratchGDB, descs[i] + sufx)
                        parameters[layer_ids[i]].value = os.path.join(workspace, descs[i] + sufx)
                    else:
                        # update the gdb
                        fc_name  = os.path.basename(parameters[layer_ids[i]].valueAsText)
                        parameters[layer_ids[i]].value = os.path.join(workspace, fc_name)
            else:
                for i in range(0, len(layer_ids)):
                    parameters[layer_ids[i]].enabled = False
                    parameters[layer_ids[i]].value = None
                if len(fld_idxs) > 0:
                    for i in range(0, len(fld_idxs)):
                        # parameters[layer_ids[i]].enabled = False
                        parameters[fld_idxs[i]].value = None

        except Exception as e:
                raise

    def execute(self, parameters, messages):
               
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting Convert ILI Anomalies process...")

        try:
            if arcpy.GetInstallInfo()['LicenseLevel'] != 'Advanced':
                pimsilitool.AddWarning("ArcGIS Pro Advanced License is required to run this tool. Please update ArcGIS Pro License and try again! ")
                return
            ili_inputpoint_fc = parameters[0].value # Anomaly features

            ili_anomaly_param_idxs = [0,1,2,3,4,47,48,49]
            crack_like_param_idxs = [12,13,14,15,16,51,52,53]
            crack_field_param_idsx = [17,18,19,20,21,54,55,56]
            dent_param_idxs = [22,23,24,25,26,57,58,59]
            gouge_param_idxs = [27,28,29,30,31,60,61,62]

            in_crack_like_fc = parameters[12].value  # crack-like features
            in_crack_field_fc = parameters[17].value  # crack field features
            in_dent_fc = parameters[22].value  # dent features
            in_gouge_fc = parameters[27].value  # gouge features
            in_bend_fc = parameters[39].value  # bend features
            in_hca_fc = parameters[43].value  # hca features

            is_grid_line = parameters[11].value
            is_weld_line = parameters[32].value
            is_seam_line = parameters[35].value
            
            if arcpy.Exists(ili_inputpoint_fc):
                # check if field names exist in the input feature class
                for i in range(1, 5):
                    if not arcpy.ListFields(ili_inputpoint_fc, parameters[i].valueAsText):
                        pimsilitool.AddError("Field name {} does not exist.".format(parameters[i].valueAsText))
                        return

                ilicount = int(arcpy.GetCount_management(ili_inputpoint_fc).getOutput(0))  

                if ilicount > 0:
                    # Generate Output point,llipse, Envelop for the Anamalies
                    self.ILIAnomaly2Geography(parameters, ili_anomaly_param_idxs, "ILI Anomaly")

                    # Generate Output point,llipse, Envelop for crack-like features
                    if in_crack_like_fc:
                        self.ILIAnomaly2Geography(parameters, crack_like_param_idxs, "Crack or Crack-like")

                    # Generate Output point,llipse, Envelop for crack field features
                    if in_crack_field_fc:
                        self.ILIAnomaly2Geography(parameters, crack_field_param_idsx, "Crack Field")

                    # Generate Output point,llipse, Envelop for dent features
                    if in_dent_fc:
                        self.ILIAnomaly2Geography(parameters, dent_param_idxs, "Dent")

                    # Generate Output point,llipse, Envelop for gougle features
                    if in_gouge_fc:
                        self.ILIAnomaly2Geography(parameters, gouge_param_idxs, "Gouge")

                    # Genrate Grid lines only if the option is selected
                    if is_grid_line:
                        self.iliGrid2Geography(parameters)
                    
                    # Genrate Weld lines only if the option is selected
                    if is_weld_line:
                        self.iliWeld2Geography(parameters)

                    # Genrate Seam lines only if the option is selected
                    if is_seam_line:
                        self.iliSeam2Geography(parameters)

                    if in_bend_fc:
                        self.iliBend2Geography(parameters)

                    if in_hca_fc:
                        self.iliHCA2Geography(parameters)
                else:
                    pimsilitool.AddWarning("There are no records to perform Anomaly Conversion.")
            else:
                pimsilitool.AddWarning("There is no feature class for Anomaly Conversion.")
                return

            pimsilitool.AddMessage("Completed Convert ILI Anomalies process.")

            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def ILIAnomaly2Geography(self,parameters, param_idxs, feat_desc):
        try:

            Input_ILI_Pipe_Tally_Table = parameters[param_idxs[0]].value
            Input_ILI_Pipe_Tally_Odometer_Field = parameters[param_idxs[1]].valueAsText
            Input_ILI_Pipe_Tally_Anomaly_Width_Field = parameters[param_idxs[2]].valueAsText
            Input_ILI_Pipe_Tally_Anomaly_Length_Field = parameters[param_idxs[3]].valueAsText
            Input_ILI_Pipe_Tally_Clock_Position_Field = parameters[param_idxs[4]].valueAsText

            Output_Anomaly_Point_Features = parameters[param_idxs[5]].valueAsText
            Output_Anomaly_Ellipse_Features = parameters[param_idxs[6]].valueAsText
            Output_Anomaly_Envelope_Features = parameters[param_idxs[7]].valueAsText

            Input_Pipeline_Diameter_Value = parameters[5].value
            Input_Y_Axis_Clock_Orientation = parameters[6].valueAsText

            Input_Clock_Position_Offset = parameters[7].valueAsText
            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].value
            Input_False_Easting_Value = parameters[10].value
            out_gdb = parameters[46].valueAsText

            # Convert ILI Anomalies to Point, Envelope and Ellipse Features
            # To allow overwriting outputs change overwriteOutput option to True.
            arcpy.env.overwriteOutput = True

            # Select all the features which have clock position value
            clockpos_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Pipe_Tally_Table, Input_ILI_Pipe_Tally_Clock_Position_Field)
            meas_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Pipe_Tally_Table, Input_ILI_Pipe_Tally_Odometer_Field)
            width_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Pipe_Tally_Table,  Input_ILI_Pipe_Tally_Anomaly_Width_Field)
            length_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Pipe_Tally_Table, Input_ILI_Pipe_Tally_Anomaly_Length_Field)
            # expr = """{0} IS NOT NULL AND {0} <> '' """.format(fieldName)
            expr = "{0} IS NOT NULL AND {0} <> '' AND {1} IS NOT NULL  AND {2} IS NOT NULL  AND {3} IS NOT NULL".format(clockpos_fieldName,
                                                        meas_fieldName, width_fieldName, length_fieldName)

            # Select all the features which have clock position value
            arcpy.management.SelectLayerByAttribute(Input_ILI_Pipe_Tally_Table, "NEW_SELECTION",  expr)


            # Process: Copy Rows (Copy Rows) (management)
            pimsilitool.AddMessage("Copying {} features...".format(feat_desc))
            Pipe_Tally_Table = os.path.join(out_gdb, "PipeTally")
            arcpy.CopyFeatures_management(Input_ILI_Pipe_Tally_Table, Pipe_Tally_Table)
            pimsilitool.AddMessage("Done copying features.")

            arcpy.SelectLayerByAttribute_management(Input_ILI_Pipe_Tally_Table, 'CLEAR_SELECTION')

            # Process: Make Table View (Make Table View) (management)
            pimsilitool.AddMessage("Make Table View {}...".format(feat_desc))
            Pipe_Tally_Table_View = "PipeTally_View"
            arcpy.management.MakeTableView(in_table=Pipe_Tally_Table, out_view=Pipe_Tally_Table_View, where_clause="", workspace="", field_info="")
            # pimsilitool.AddMessage("Make Table View is done: {}".format(feat_desc))

            pimsilitool.AddMessage("Adding fields to table view {}...".format(feat_desc))
            arcpy.AddFields_management(Pipe_Tally_Table_View, config.CONVERT_ILI_PIPETALLY_VIEW_FIELDS)
            # pimsilitool.AddMessage("Done adding fields to table view.")

            pimsilitool.AddMessage("Calculating X,Y field values {}...".format(feat_desc))

            with arcpy.da.UpdateCursor(Pipe_Tally_Table_View,
                                       field_names=[Input_ILI_Pipe_Tally_Odometer_Field,
                                                    Input_ILI_Pipe_Tally_Anomaly_Width_Field,
                                                    Input_ILI_Pipe_Tally_Anomaly_Length_Field,
                                                    Input_ILI_Pipe_Tally_Clock_Position_Field,
                                                    "AnomalyXCoord",
                                                    "AnomalyYCoord",
                                                    "AnomalyMajorAxisFt",
                                                    "AnomalyMinorAxisFt",
                                                    "Azimuth"]) as cursor:
                for row in cursor:
                    odometer = row[0]
                    width = row[1]
                    length = row[2]
                    clock_pos = row[3]
                    row[4] = odometer - Input_False_Easting_Value
                    row[5] = self.calc_anomaly_y_coord(clock_pos, Input_Pipeline_Diameter_Value,
                                Input_False_Northing_Value, Input_Clock_Position_Offset, Input_Y_Axis_Clock_Orientation)
                    row[6] = width / 12
                    row[7] = length / 12
                    row[8] = 0.1
                    cursor.updateRow(row)


            # Process: Make XY Event Layer (Make XY Event Layer) (management)
            pimsilitool.AddMessage("Making XY event layer {}...".format(feat_desc))
            Anomaly_Point_Events = "AnomalyEvents_Layer"
            arcpy.management.MakeXYEventLayer(table = Pipe_Tally_Table_View, in_x_field = "AnomalyXCoord",
                                              in_y_field = "AnomalyYCoord", out_layer = Anomaly_Point_Events,
                                              spatial_reference = Spatial_Reference_for_Output_Features, in_z_field = "")

            # Process: Copy Features (Copy Features) (management)
            pimsilitool.AddMessage("Copying events features {}...".format(feat_desc))
            arcpy.management.CopyFeatures(in_features = Anomaly_Point_Events,
                                          out_feature_class = Output_Anomaly_Point_Features,
                                          config_keyword = "",
                                          spatial_grid_1 = 0, spatial_grid_2 = 0, spatial_grid_3 = 0)
            pimsilitool.AddMessage("Done copying events features.")

            # Process: Table To Ellipse (Table To Ellipse) (management)
            pimsilitool.AddMessage("Processing TableToEllipse {}...".format(feat_desc))
            Anomaly_Ellipse_Polylines = "AnomalyEllipsePolyline"

            arcpy.management.TableToEllipse(Output_Anomaly_Point_Features, Anomaly_Ellipse_Polylines,
                                        "AnomalyXCoord", "AnomalyYCoord", "AnomalyMajorAxisFt", "AnomalyMinorAxisFt",
                                        "FEET", "Azimuth", "DEGREES", None, Spatial_Reference_for_Output_Features,
                                        "ATTRIBUTES")
            pimsilitool.AddMessage("Done processing TableToEllipse.")

            fieldList = [f.name.upper() for f in arcpy.ListFields (Anomaly_Ellipse_Polylines)]
            if 'SHAPE' in fieldList: fieldList.remove('SHAPE')
            if 'SHAPE_LENGTH' in fieldList: fieldList.remove('SHAPE_LENGTH')

            pimsilitool.AddMessage("Processing ellipse features to polygon {}...".format(feat_desc))

            arcpy.management.CreateFeatureclass(os.path.dirname(Output_Anomaly_Ellipse_Features),
                                                os.path.basename(Output_Anomaly_Ellipse_Features),
                                                geometry_type = "POLYGON",
                                                spatial_reference = Spatial_Reference_for_Output_Features)

            arcpy.AddField_management(Output_Anomaly_Ellipse_Features, "ORIG_ELLIPSE_OID", "LONG")
            oid_fieldname = arcpy.Describe(Anomaly_Ellipse_Polylines).OIDFieldName
            for row in arcpy.da.SearchCursor(Anomaly_Ellipse_Polylines, [oid_fieldname, "SHAPE@"]):
                vertexArray = arcpy.Array()
                oid = row[0]

                for part in row[1]:
                    for pnt in part:
                        vertexArray.add(pnt)
                with arcpy.da.InsertCursor(Output_Anomaly_Ellipse_Features, ("SHAPE@","ORIG_ELLIPSE_OID")) as cursor:
                    feature = arcpy.Polygon(vertexArray, Spatial_Reference_for_Output_Features)
                    cursor.insertRow((feature,oid))

            arcpy.JoinField_management(Output_Anomaly_Ellipse_Features, "ORIG_ELLIPSE_OID", Anomaly_Ellipse_Polylines, oid_fieldname, fieldList)
            pimsilitool.AddMessage("Done processing ellipse features to polygon.")
            
            # Process: Feature Envelope To Polygon (Feature Envelope To Polygon) (management)
            pimsilitool.AddMessage("Processing FeatureEnvelopeToPolygon {}...".format(feat_desc))
            arcpy.management.FeatureEnvelopeToPolygon(in_features=Output_Anomaly_Ellipse_Features,
                                                      out_feature_class=Output_Anomaly_Envelope_Features,
                                                      single_envelope="SINGLEPART")
            pimsilitool.AddMessage("Done processing FeatureEnvelopeToPolygon.")
            
        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Issue in ILI Anomaly 2 Geography.\n{}".format(arcpy.GetMessages(2)))
            # return False
            raise

    def iliWeld2Geography(self,parameters):
        try:
            Input_ILI_Weld_Diameter_value = parameters[5].value
            Input_Y_Axis_Clock_Orientation = "\"" + parameters[6].valueAsText + "\""
            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].valueAsText
            Input_ILI_Weld_Table = parameters[33].value
            Input_ILI_Weld_Odometer_Field = parameters[34].valueAsText

            Output_Weld_Features = parameters[63].valueAsText
            out_gdb = parameters[46].valueAsText

            arcpy.env.overwriteOutput = True
            
            # Process: Copy Rows (Copy Rows) (management)
            pimsilitool.AddMessage("Copying weld features...")
            Pipe_WeldTally_Table = os.path.join(out_gdb, "PipeWeldTally")
            arcpy.management.CopyRows(in_rows=Input_ILI_Weld_Table, out_table=Pipe_WeldTally_Table, config_keyword="")
            pimsilitool.AddMessage("Done copying weld features.")

            pimsilitool.AddMessage("Adding Weld X,Y coordinate fields...")
            arcpy.management.AddFields(Pipe_WeldTally_Table, "WeldXMinCoord DOUBLE # # # #;"
                                                             "WeldYMinCoord DOUBLE # # # #;"
                                                             "WeldXMaxCoord DOUBLE # # # #;"
                                                             "WeldYMaxCoord DOUBLE # # # #")
            pimsilitool.AddMessage("Done adding Weld X,Y coordinate fields.")

            pimsilitool.AddMessage("Calculating Weld X,Y coordinate fields...")
            if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:

                    arcpy.management.CalculateFields(Pipe_WeldTally_Table, "PYTHON3",
                                                    "WeldXMinCoord !" + Input_ILI_Weld_Odometer_Field + "!;"
                                                    "WeldYMinCoord  \'(((0 / 12) + (0 / 60 / 12)) * (" + str(Input_ILI_Weld_Diameter_value) + "/ 12 * math.pi)) +float(" + str(Input_False_Northing_Value) + ")\';"
                                                    "WeldXMaxCoord !" +  Input_ILI_Weld_Odometer_Field + "!;"
                                                    "WeldYMaxCoord \'(((12 / 12) + (0 / 60 / 12)) * (" +  str(Input_ILI_Weld_Diameter_value) + "/ 12) * math.pi) + float(" + str(Input_False_Northing_Value)+")\'", '')
            else:

                    arcpy.management.CalculateFields(Pipe_WeldTally_Table, "PYTHON3",
                                                    "WeldXMinCoord !" + Input_ILI_Weld_Odometer_Field + "!;"
                                                    "WeldYMinCoord \'(-1)*((((6 / 12) + (0 / 60 / 12)) * (" + str(Input_ILI_Weld_Diameter_value) + "/ 12 * math.pi)) + float(" + str(Input_False_Northing_Value) +" ))\';"
                                                    "WeldXMaxCoord !" + Input_ILI_Weld_Odometer_Field + "!;"
                                                    "WeldYMaxCoord \'(0.5 * (" +  str(Input_ILI_Weld_Diameter_value) + "/12 * math.pi)) + float(" + str(Input_False_Northing_Value)+")\'", '')

            pimsilitool.AddMessage("Done calculating Weld X,Y coordinate fields...")
            pimsilitool.AddMessage("Creating Weld line features (XYToLine)...")
            arcpy.management.XYToLine(Pipe_WeldTally_Table, Output_Weld_Features, "WeldXMinCoord", "WeldYMinCoord", "WeldXMaxCoord",
                                      "WeldYMaxCoord", "GEODESIC", spatial_reference = Spatial_Reference_for_Output_Features, attributes= "ATTRIBUTES")
            pimsilitool.AddMessage("Done creating Weld line features (XYToLine).")

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Error in Weld Line Features Creation")

    def iliGrid2Geography(self, parameters):
        try:
            pimsilitool.AddMessage("Generting Grid line features...")
            Input_ILI_Pipe_Tally_Table = parameters[0].value
            Input_ILI_Pipe_Tally_Odometer_Field = parameters[1].valueAsText
            Input_Pipeline_Diameter_Value = parameters[5].value
            Input_Y_Axis_Clock_Orientation = "\"" + parameters[6].valueAsText + "\""

            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].valueAsText

            Input_is_weld_value = parameters[32].value
            Input_ILI_Weld_Table = parameters[33].valueAsText
            Input_ILI_Weld_Odometer_Field = parameters[34].valueAsText

            Output_Grid_Features = parameters[50].valueAsText
            out_gdb = parameters[46].valueAsText

            # To allow overwriting outputs change overwriteOutput option to True.
            arcpy.env.overwriteOutput = True

            field_to_find_x_max = Input_ILI_Pipe_Tally_Odometer_Field

            x_max_AnamalyValue = arcpy.da.SearchCursor(Input_ILI_Pipe_Tally_Table, field_to_find_x_max, "{} IS NOT NULL".format(field_to_find_x_max),
                                                       sql_clause = (None, "ORDER BY {} DESC".format(field_to_find_x_max))).next()[0]
            y_max_AnamalyValue = Input_Pipeline_Diameter_Value

            x_max_WeldValue = 0.0
            y_max_WeldValue = 0.0

            # check max x, y values from weld lines
            if Input_is_weld_value:
                x_max_WeldValue = arcpy.da.SearchCursor(Input_ILI_Weld_Table, Input_ILI_Weld_Odometer_Field, "{} IS NOT NULL".format(Input_ILI_Weld_Odometer_Field),
                                                        sql_clause = (None, "ORDER BY {} DESC".format(Input_ILI_Weld_Odometer_Field))).next()[0]
                y_max_WeldValue = Input_Pipeline_Diameter_Value

            x_max_value = x_max_WeldValue if x_max_AnamalyValue < x_max_WeldValue else x_max_AnamalyValue
            y_max_value = y_max_WeldValue if y_max_AnamalyValue < y_max_WeldValue else y_max_AnamalyValue

            if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:
                ymin_coord = (((0 / 12) + (0 / 60 / 12)) * (y_max_value / 12 * math.pi)) + float(Input_False_Northing_Value)
                ymax_coord = (((12 / 12) + (0 / 60 / 12)) * (y_max_value / 12 * math.pi)) + float(Input_False_Northing_Value)
               
            else:                
                ymin_coord = (-1) * ((((6 / 12) + (0 / 60 / 12)) * (y_max_value / 12 * math.pi)) + float(Input_False_Northing_Value))
                ymax_coord = ((1 - ((6 / 12) + (0 / 60 / 12))) * (y_max_value / 12 * math.pi)) + float(Input_False_Northing_Value)

            x_min_value = 0
            split_interval = 5
            grid_interval = round((ymax_coord-ymin_coord)/(split_interval-1),6)

            pimsilitool.AddMessage(" ymin_coord {} ,ymax_coord {}, grid_interval {} ".format(ymin_coord,ymax_coord,grid_interval))
            
            grid_id = ["6:00","3:00","12:00","9:00","6:00"]
            if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:
                grid_id = ["12:00","3:00","6:00","9:00","12:00"]
                                            
            fc_name = os.path.basename(Output_Grid_Features)
            wspace = os.path.dirname(Output_Grid_Features)
           
            GridLable_Column="ClockPosition"
            Output_Grid_FeatureClass = arcpy.management.CreateFeatureclass(wspace, fc_name, "POLYLINE", None, "DISABLED", "DISABLED", Spatial_Reference_for_Output_Features)
            arcpy.management.AddFields(Output_Grid_FeatureClass,
                                                                GridLable_Column+" TEXT # 255 # #;"
                                                                "GridXMinCoord DOUBLE # # # #;"
                                                                "GridYMinCoord DOUBLE # # # #;"
                                                                "GridXMaxCoord DOUBLE # # # #;"
                                                                "GridYMaxCoord DOUBLE # # # #")

            # Inserting into polyline logic           
            point = arcpy.Point()
            array = arcpy.Array()

            featureList = []
            cursor = arcpy.InsertCursor(Output_Grid_FeatureClass,["SHAPE@", GridLable_Column])
            feat = cursor.newRow()

            for interval in range(0, split_interval):
                # Set X and Y for start and end points
                point.X = x_min_value
                point.Y = ymin_coord+(interval*grid_interval)
                array.add(point)
                point.X = x_max_value
                point.Y = ymin_coord+(interval*grid_interval)
                array.add(point)   
                # Create a Polyline object based on the array of points
                polyline = arcpy.Polyline(array)
                # Clear the array for future use
                array.removeAll()
                # Append to the list of Polyline objects
                featureList.append(polyline)
                # Insert the feature
                feat.shape = polyline
                feat.setValue(GridLable_Column, grid_id[interval])
                feat.setValue("GridXMinCoord", x_min_value)
                feat.setValue("GridYMinCoord", ymin_coord + (interval*grid_interval))
                feat.setValue("GridXMaxCoord", x_max_value)
                feat.setValue("GridYMaxCoord", ymin_coord + (interval*grid_interval))
                cursor.insertRow(feat)
            del feat
            del cursor

            pimsilitool.AddMessage("Done generting Grid line features.")

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Error in Grid Line Features creation")
            raise

    def calc_anomaly_y_coord(self, clock_pos, pipe_od, false_northing, clock_offset, y_axis_clock):
        try:

            clock_parts = clock_pos.split(':')
            clock_hours = float(clock_parts[0])
            clock_minutes = float(clock_parts[1])
            pipe_od = float(pipe_od)
            offset_parts = clock_offset.split(':')
            offset_hours = float(offset_parts[0])
            offset_minutes = float(offset_parts[1])

            # Correct clock minutes for the clock minutes offset
            if offset_hours < 0:
                offset_minutes = offset_minutes * (-1)
            clock_minutes = clock_minutes + offset_minutes
            if clock_minutes > 59:
                clock_minutes = clock_minutes - 60
                clock_hours = clock_hours + 1
            elif clock_minutes < 0:
                clock_minutes = clock_minutes + 60
                clock_hours = clock_hours - 1

            # Correct clock hours for the clock hours offset
            clock_hours = clock_hours + offset_hours
            if clock_hours > 12:
                clock_hours = clock_hours - 12
            elif clock_hours < 0:
                clock_hours = clock_hours + 12

            # Calculate y-coordinate
            if y_axis_clock == config.CONVERT_ILI_ANOM_CLOCK_POSITION[0]:   #"6:00 Centered":
                if clock_hours == 12:
                    y_coord = ((clock_minutes / 60 / 12) * (pipe_od / 12 * math.pi)) + false_northing
                else:
                    y_coord = (((clock_hours / 12) + (clock_minutes / 60 / 12)) * (pipe_od / 12 * math.pi)) + false_northing
            else:  # y_axis_clock = "12:00 Centered"
                if clock_hours == 12:
                    y_coord = (-1) * (((clock_minutes / 60 / 12) * (pipe_od / 12 * math.pi)) + false_northing)
                elif 1 <= clock_hours < 6:
                    y_coord = (-1) * ((((clock_hours / 12) + (clock_minutes / 60 / 12)) * (pipe_od / 12 * math.pi)) + false_northing)
                else:  # 6 <= clock_hours <= 11
                    y_coord = ((1 - ((clock_hours / 12) + (clock_minutes / 60 / 12))) * (pipe_od / 12 * math.pi)) + false_northing
            return y_coord

        except Exception as e:
            raise

    def iliSeam2Geography(self, parameters):
        try:
            Input_ILI_Pipe_Tally_Table = parameters[0].valueAsText

            Input_ILI_Pipe_Tally_Odometer_Field = parameters[1].valueAsText
            Input_Pipeline_Diameter_Value = parameters[5].value

            # Input_Y_Axis_Clock_Orientation = "\"" + parameters[6].valueAsText + "\""
            Input_Y_Axis_Clock_Orientation = parameters[6].valueAsText

            Input_Clock_Position_Offset = parameters[7].valueAsText
            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].value
            Input_False_Easting_Value = parameters[10].value

            Input_ILI_Seam_Table = parameters[36].value
            Input_ILI_Seam_Odometer_Field = parameters[37].valueAsText
            Input_Seam_Clock_Position_Field = parameters[38].valueAsText

            Output_Weld_Features = parameters[63].valueAsText
            Output_Seam_Features = parameters[64].valueAsText
            out_gdb = parameters[46].valueAsText

            weld2np = arcpy.da.FeatureClassToNumPyArray(Output_Weld_Features, ("WeldXMinCoord"))

            weld2np = numpy.sort(weld2np, order="WeldXMinCoord")

            # fieldName = arcpy.AddFieldDelimiters(Input_ILI_Seam_Table, Input_Seam_Clock_Position_Field)
            # # expr = """{0} IS NOT NULL""".format(fieldName)
            # expr = "{0} IS NOT NULL AND {0} <> '' ".format(fieldName)

            # Select all the features which have clock position value
            clockpos_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Seam_Table, Input_Seam_Clock_Position_Field)
            meas_fieldName = arcpy.AddFieldDelimiters(Input_ILI_Seam_Table, Input_ILI_Seam_Odometer_Field)

            expr = "{0} IS NOT NULL AND {0} <> '' AND {1} IS NOT NULL".format(clockpos_fieldName, meas_fieldName)


            arcpy.SelectLayerByAttribute_management(Input_ILI_Seam_Table, 'NEW_SELECTION', expr)

            # Process: Copy Rows (Copy Rows) (management)
            pimsilitool.AddMessage("Copying Seam features...")
            # Process: Copy Rows (Copy Rows) (management)
            Pipe_SeamTally_Table = os.path.join(out_gdb, "PipeSeamTally")
            arcpy.management.CopyRows(in_rows=Input_ILI_Seam_Table, out_table=Pipe_SeamTally_Table, config_keyword="")
            pimsilitool.AddMessage("Done copying Seam features.")

            # clear selection
            arcpy.SelectLayerByAttribute_management(Input_ILI_Seam_Table, 'CLEAR_SELECTION')

            pimsilitool.AddMessage("Adding Seam X,Y coordinate fields...")
            arcpy.management.AddFields(Pipe_SeamTally_Table, "SeamXMinCoord DOUBLE # # # #;"
                                                            "SeamYMinCoord DOUBLE # # # #;"
                                                            "SeamXMaxCoord DOUBLE # # # #;"
                                                            "SeamYMaxCoord DOUBLE # # # #")
            pimsilitool.AddMessage("Done adding Seam X,Y coordinate fields.")

            fields = [Input_ILI_Seam_Odometer_Field, Input_Seam_Clock_Position_Field,"SeamXMinCoord","SeamYMinCoord", "SeamXMaxCoord","SeamYMaxCoord"]

            pimsilitool.AddMessage("Calculating Seam X,Y coordinate fields...")
            with arcpy.da.UpdateCursor(Pipe_SeamTally_Table, fields) as cursor:
                for row in cursor:
                    odometer = row[0]
                    clock_pos = row[1]

                    # get x min value from weld feature
                    weld2np_recs = weld2np[(weld2np["WeldXMinCoord"] <= (odometer - Input_False_Easting_Value))]
                    xmin_rec = weld2np_recs[len(weld2np_recs) - 1]
                    if len(xmin_rec) > 0:
                        row[2] = xmin_rec[0]
                    else:
                        row[2] = odometer

                    row[3] = self.calc_anomaly_y_coord(clock_pos,
                                                       Input_Pipeline_Diameter_Value,
                                                       Input_False_Northing_Value,
                                                       Input_Clock_Position_Offset,
                                                       Input_Y_Axis_Clock_Orientation)
                    # get x max value from weld feature
                    xmax_rec = weld2np[weld2np["WeldXMinCoord"] > odometer]

                    if len(xmax_rec) > 0:
                        row[4] = xmax_rec[0][0]
                    else:
                        row[4] = odometer
                    row[5] = row[3]
                    cursor.updateRow(row)
            pimsilitool.AddMessage("Done calculating Seam X,Y coordinate fields.")

            # oidFieldName = arcpy.Describe(Input_ILI_Weld_Table).oidFieldName
            pimsilitool.AddMessage("Creating Seam line features (XYToLine)...")
            arcpy.management.XYToLine(Pipe_SeamTally_Table, Output_Seam_Features, "SeamXMinCoord", "SeamYMinCoord",
                                      "SeamXMaxCoord", "SeamYMaxCoord", "GEODESIC", spatial_reference=Spatial_Reference_for_Output_Features, attributes="ATTRIBUTES")
            pimsilitool.AddMessage("Done creating Seam line features (XYToLine)...")

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            pimsilitool.AddError("Error in Seam Line Features creation")
            raise

    def iliBend2Geography(self, parameters):
        try:
            Input_ILI_Bend_Diameter_value = parameters[5].value
            Input_Y_Axis_Clock_Orientation = "\"" + parameters[6].valueAsText + "\""
            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].value
            Input_False_Easting_Value = parameters[10].value
            Input_ILI_Bend_Table = parameters[39].value
            # Input_ILI_Bend_Measure_Field = parameters[40].valueAsText
            # Input_ILI_Bend_From_Measure_Field = parameters[41].valueAsText
            # Input_ILI_Bend_To_Measure_Field = parameters[42].valueAsText
            Output_Bend_Features = parameters[65].valueAsText
            is_measure_enabled = parameters[40].enabled
            out_gdb = parameters[46].valueAsText

            arcpy.env.overwriteOutput = True

            # Process: Copy Rows (Copy Rows) (management)
            pimsilitool.AddMessage("Copying Bend features...")
            Pipe_BendTally_Table = os.path.join(out_gdb, "PipeBendTally")
            arcpy.management.CopyRows(in_rows=Input_ILI_Bend_Table, out_table=Pipe_BendTally_Table, config_keyword="")
            pimsilitool.AddMessage("Done copying Bend features.")

            pimsilitool.AddMessage("Adding Bend X,Y coordinate fields...")
            arcpy.management.AddFields(Pipe_BendTally_Table, "BendXMinCoord DOUBLE # # # #;"
                                                             "BendYMinCoord DOUBLE # # # #;"
                                                             "BendXMaxCoord DOUBLE # # # #;"
                                                             "BendYMaxCoord DOUBLE # # # #")
            pimsilitool.AddMessage("Done adding Bend X,Y coordinate fields.")

            pimsilitool.AddMessage("Calculating Bend X,Y coordinate fields...")

            # **************
            if is_measure_enabled:
                Input_ILI_Bend_Measure_Field = parameters[40].valueAsText
                flds = [Input_ILI_Bend_Measure_Field, "BendXMinCoord",  "BendYMinCoord", "BendXMaxCoord", "BendYMaxCoord"]
            else:
                Input_ILI_Bend_From_Measure_Field = parameters[41].valueAsText
                Input_ILI_Bend_To_Measure_Field = parameters[42].valueAsText
                flds = [Input_ILI_Bend_From_Measure_Field,  Input_ILI_Bend_To_Measure_Field, "BendXMinCoord", "BendYMinCoord", "BendXMaxCoord", "BendYMaxCoord"]

            with arcpy.da.UpdateCursor(Pipe_BendTally_Table, field_names = flds) as cursor:
                for row in cursor:
                    if is_measure_enabled:
                        row[1] = row[0] - Input_False_Easting_Value - 1   # x min
                        row[3] = row[0] - Input_False_Easting_Value + 1  # x max
                        if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:
                            row[2] = (((0 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value    # y min
                            row[4] = (((12 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12) * math.pi + Input_False_Northing_Value   # y max
                        else:
                            row[2] = (-1) * (((6 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value  # y min
                            row[4] = (0.5 * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value  # y max
                        # row[2] = float(ymin)
                        # row[4] = float(ymax)
                    else:
                        row[2] = row[0] - Input_False_Easting_Value       # x min
                        row[4] = row[1] - Input_False_Easting_Value  # x max
                        if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:
                            row[3] = (((0 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value    # y min
                            row[5] = (((12 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12) * math.pi + Input_False_Northing_Value   # y max

                        else:
                            row[3] = (-1) * (((6 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value # y min
                            row[5] = (0.5 * Input_ILI_Bend_Diameter_value /12 * math.pi) + Input_False_Northing_Value  # y max
                        # row[3] = float(ymin)
                        # row[5] = float(ymax)

                    cursor.updateRow(row)

            pimsilitool.AddMessage("Done calculating Bend X,Y coordinate fields...")

            pimsilitool.AddMessage("Creating Bend features...")
            Bend_xy2line_Table = os.path.join(out_gdb, "Bend_xy2line")

            arcpy.management.XYToLine(Pipe_BendTally_Table, Bend_xy2line_Table,
                                      "BendXMinCoord",
                                      "BendYMinCoord",
                                      "BendXMaxCoord",
                                      "BendYMaxCoord", "GEODESIC",
                                      spatial_reference=Spatial_Reference_for_Output_Features, attributes="ATTRIBUTES")

            arcpy.management.FeatureEnvelopeToPolygon(Bend_xy2line_Table, Output_Bend_Features, "SINGLEPART")
            pimsilitool.AddMessage("Done creating Bend features).")

        except Exception as e:
            raise

    def iliHCA2Geography(self, parameters):
        try:
            Input_ILI_Bend_Diameter_value = parameters[5].value
            Input_Y_Axis_Clock_Orientation = "\"" + parameters[6].valueAsText + "\""
            Spatial_Reference_for_Output_Features = parameters[8].valueAsText
            Input_False_Northing_Value = parameters[9].value
            Input_False_Easting_Value = parameters[10].value
            Input_ILI_HCA_Table = parameters[43].value
            Input_ILI_HCA_From_Measure_Field = parameters[44].valueAsText
            Input_ILI_HCA_To_Measure_Field = parameters[45].valueAsText
            Output_HCA_Features = parameters[66].valueAsText
            out_gdb = parameters[46].valueAsText

            arcpy.env.overwriteOutput = True

            # Process: Copy Rows (Copy Rows) (management)
            pimsilitool.AddMessage("Copying HCA features...")
            Pipe_HCATally_Table = os.path.join(out_gdb, "PipeHCATally")
            arcpy.management.CopyRows(in_rows=Input_ILI_HCA_Table, out_table=Pipe_HCATally_Table, config_keyword="")
            pimsilitool.AddMessage("Done copying HCA features.")

            pimsilitool.AddMessage("Adding HCA X,Y coordinate fields...")
            arcpy.management.AddFields(Pipe_HCATally_Table,  "HCAXMinCoord DOUBLE # # # #;"
                                                             "HCAYMinCoord DOUBLE # # # #;"
                                                             "HCAXMaxCoord DOUBLE # # # #;"
                                                             "HCAYMaxCoord DOUBLE # # # #")
            pimsilitool.AddMessage("Done adding HCA X,Y coordinate fields.")

            pimsilitool.AddMessage("Calculating HCA X,Y coordinate fields...")

            # **************

            flds = [Input_ILI_HCA_From_Measure_Field, Input_ILI_HCA_To_Measure_Field, "HCAXMinCoord",
                        "HCAYMinCoord", "HCAXMaxCoord", "HCAYMaxCoord"]

            with arcpy.da.UpdateCursor(Pipe_HCATally_Table, field_names=flds) as cursor:
                for row in cursor:
                    row[2] = row[0] - Input_False_Easting_Value  # x min
                    row[4] = row[1] - Input_False_Easting_Value  # x max
                    if "6:00 Centered" in Input_Y_Axis_Clock_Orientation:
                        row[3] = (((0 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value  # y min
                        row[5] = (((12 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12) * math.pi + Input_False_Northing_Value  # y max

                    else:
                        row[3] = (-1) * (((6 / 12) + (0 / 60 / 12)) * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value  # y min
                        row[5] = (0.5 * Input_ILI_Bend_Diameter_value / 12 * math.pi) + Input_False_Northing_Value  # y max
                    # row[3] = float(ymin)
                    # row[5] = float(ymax)

                    cursor.updateRow(row)

            pimsilitool.AddMessage("Done calculating HCA X,Y coordinate fields...")

            pimsilitool.AddMessage("Creating HCA features...")
            HCA_xy2line_Table = os.path.join(out_gdb, "HCA_xy2line")
            arcpy.management.XYToLine(Pipe_HCATally_Table, HCA_xy2line_Table,
                                      "HCAXMinCoord",
                                      "HCAYMinCoord",
                                      "HCAXMaxCoord",
                                      "HCAYMaxCoord", "GEODESIC",
                                      spatial_reference=Spatial_Reference_for_Output_Features, attributes="ATTRIBUTES")

            arcpy.management.FeatureEnvelopeToPolygon(HCA_xy2line_Table, Output_HCA_Features, "SINGLEPART")

            pimsilitool.AddMessage("Done creating HCA features).")

        except Exception as e:
            raise