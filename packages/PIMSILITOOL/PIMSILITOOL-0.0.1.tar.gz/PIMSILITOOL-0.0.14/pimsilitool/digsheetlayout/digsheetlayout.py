
""" Headline: Anomaly Processing Inline Inspection Anomaly Growth Calculation tool
    Calls:  inlineinspection, inlineinspection.config
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
import uuid
from pimsilitool.digsheetlayout.load_digsheet_data import load_digsheet_data
from pimsilitool.license.validate_license.license_operation import LicenseOperation

class DigSheet(object):

    def __init__(self, shapex, shapey, shapem, routeid, measure,  sheetno, reason, status,
                 beginweldid, beginweldmeasure, endweldid, endweldmeasure, landowner, client):
        self.shapex = shapex
        self.shapey = shapey
        self.shapem = shapem
        self.routeid = routeid
        self.measure = measure
        self.sheetno = sheetno
        self.reason = reason
        self.status = status
        self.beginweldid = beginweldid
        self.beginweldmeasure = beginweldmeasure
        self.endweldid = endweldid
        self.endweldmeasure = endweldmeasure
        self.landowner = landowner
        self.client = client

    def __getitem__(self, item):
        return getattr(self, item)



class DigSheetLayout(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Dig Sheet Layout"
        self.description = "This Tool Calculates Dig Sheet Layout Revision Number"
        self.canRunInBackground = False
        #self.category = config.ILI_PC_TOOL_CATAGORY  
               
    def getParameterInfo(self):

        parameters = []

        #   ******************************************
        #   ILI Metal Loss Anomaly Parameters
        #   ******************************************

        # Parameter [0]
        in_ili_features = arcpy.Parameter(category = config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                            displayName="Input ILI Metal Loss Anomaly Features",
                                            name="in_ili_features", datatype=["GPFeatureLayer","GPTableView"],
                                            parameterType="Required",
                                            direction="Input")
        # Parameter [1]
        in_ili_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                               displayName="ILI Anomaly Network Route ID Field",
                                               name="in_ili_routeid_field",
                                               datatype="Field", parameterType="Required", direction="Input")
        in_ili_routeid_field.parameterDependencies = [in_ili_features.name]
        # in_ili_routename_field.filter.list = ['int', 'long', 'double']

        # Parameter [2]
        in_ili_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                               displayName="ILI Anomaly Unique ID Field",
                                               name="in_ili_id_field",
                                               datatype="Field", parameterType="Required", direction="Input")
        in_ili_id_field.parameterDependencies = [in_ili_features.name]

        # Parameter [3]
        in_ili_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                             displayName="ILI Anomaly Measure Field",
                                             name="in_ili_measure_field",
                                             datatype="Field", parameterType="Required", direction="Input")
        in_ili_measure_field.parameterDependencies = [in_ili_features.name]
        in_ili_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [4]
        in_ili_dig_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                                displayName="Target ILI Anomaly Dig Sheet ID Field",
                                                name="in_ili_dig_id_field",
                                                datatype="Field", parameterType="Required",
                                                direction="Input")
        in_ili_dig_id_field.parameterDependencies = [in_ili_features.name]

        # Parameter [5]
        in_ili_dig_target_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                            displayName="Target ILI Anomaly Is Dig Target Field",
                                            name="in_ili_dig_target_field",
                                            datatype="Field",
                                            parameterType="Required",
                                            direction="Input")
        in_ili_dig_target_field.parameterDependencies = [in_ili_features.name]
        in_ili_dig_target_field.filter.list = ['Text']

        # Parameter [6]
        in_ili_priority_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                                displayName="ILI Anomaly Priority Field",
                                                name="in_ili_priority_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_ili_priority_field.parameterDependencies = [in_ili_features.name]
        in_ili_priority_field.filter.list = ['int', 'long', 'double']

        # Parameter [7]
        in_ili_priority_values = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY,
                                                 displayName="ILI Anomaly Priority Values",
                                                 name="in_ili_priority_values", multiValue=True,
                                                 datatype="GPDouble", parameterType="Required", direction="Input")
        in_ili_priority_values.filter.type = "ValueList"
        in_ili_priority_values.filter.list = []

        parameters += [in_ili_features,  in_ili_routeid_field, in_ili_id_field,   in_ili_measure_field,
                       in_ili_dig_id_field, in_ili_dig_target_field,
                       in_ili_priority_field, in_ili_priority_values]

        #   ******************************************
        #   ILI Weld Parameters
        #   ******************************************

        # Parameter [7]
        in_weld_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_WELD_LINES,
                                               displayName="Input Weld Features",
                                               name="in_weld_features", datatype=["GPFeatureLayer", "GPTableView"],
                                               parameterType="Required",
                                               direction="Input")

        # Parameter [9]
        in_weld_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_WELD_LINES,
                                                displayName="Weld Network Route ID Field",
                                                name="in_weld_routeid_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_weld_routeid_field.parameterDependencies = [in_weld_features.name]

        # Parameter [8]
        in_weld_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_WELD_LINES,
                                                displayName="Weld Unique ID Field",
                                                name="in_weld_id_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_weld_id_field.parameterDependencies = [in_weld_features.name]

        # Parameter [10]
        in_weld_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_WELD_LINES,
                                                displayName="Weld Measure Field", name="in_weld_measure_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_weld_measure_field.parameterDependencies = [in_weld_features.name]
        in_weld_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [in_weld_features, in_weld_routeid_field, in_weld_id_field,  in_weld_measure_field]

        #   ******************************************
        #   Right of Way Layer Parameters
        #   ******************************************

        # Parameter [11]
        in_row_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                          displayName="Input Right of Way Features",
                                          name="in_row_features",
                                          datatype=["GPFeatureLayer", "GPTableView"],
                                          parameterType="Required", direction="Input")

        # Parameter [13]
        in_row_begin_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                                displayName="Right of Way Begin Network Route ID Field",
                                                name="in_row_begin_routeid_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_row_begin_routeid_field.parameterDependencies = [in_row_features.name]

        # Parameter [14]
        in_row_begin_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                                displayName="Right of Way Begin Measure Field", name="in_row_begin_measure_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_row_begin_measure_field.parameterDependencies = [in_row_features.name]
        in_row_begin_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [15]
        in_row_end_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                                     displayName="Right of Way End Network Route ID Field",
                                                     name="in_row_end_routeid_field",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_row_end_routeid_field.parameterDependencies = [in_row_features.name]

        # Parameter [16]
        in_row_end_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                                     displayName="Right of Way End Measure Field",
                                                     name="in_row_end_measure_field",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_row_end_measure_field.parameterDependencies = [in_row_features.name]
        in_row_end_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [12]
        in_row_ownerid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY,
                                               displayName="Right of Way Land Owner Field",
                                               name="in_row_ownerid_field",
                                               datatype="Field", parameterType="Required", direction="Input")
        in_row_ownerid_field.parameterDependencies = [in_row_features.name]

        parameters += [in_row_features, in_row_begin_routeid_field, in_row_begin_measure_field,
                       in_row_end_routeid_field, in_row_end_measure_field, in_row_ownerid_field]

        # #   ******************************************
        # #   Owner Operator Layer Parameters
        # #   ******************************************
        #
        # # Parameter [17]
        # in_client_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                      displayName="Input Owner Operator Features",
        #                                      name="in_client_features",
        #                                      datatype=["GPFeatureLayer", "GPTableView"],
        #                                      parameterType="Required", direction="Input")
        # # Parameter [18]
        # in_client_name_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                        displayName="Owner Operator ID Field",
        #                                        name="in_client_name_field",
        #                                        datatype="Field", parameterType="Required", direction="Input")
        # in_client_name_field.parameterDependencies = [in_client_features.name]
        #
        # # Parameter [19]
        # in_client_begin_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                              displayName="Owner Operator Begin Network Route ID Field",
        #                                              name="in_client_begin_routeid_field",
        #                                              datatype="Field", parameterType="Required", direction="Input")
        # in_client_begin_routeid_field.parameterDependencies = [in_client_features.name]
        #
        # # Parameter [20]
        # in_client_begin_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                              displayName="Owner Operator Begin Measure Field",
        #                                              name="in_client_begin_measure_field",
        #                                              datatype="Field", parameterType="Required", direction="Input")
        # in_client_begin_measure_field.parameterDependencies = [in_client_features.name]
        # in_client_begin_measure_field.filter.list = ['int', 'long', 'double']
        #
        # # Parameter [21]
        # in_client_end_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                            displayName="Owner Operator End Network Route ID Field",
        #                                            name="in_client_end_routeid_field",
        #                                            datatype="Field", parameterType="Required", direction="Input")
        # in_client_end_routeid_field.parameterDependencies = [in_client_features.name]
        #
        # # Parameter [22]
        # in_client_end_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR,
        #                                            displayName="Owner Operator End Measure Field",
        #                                            name="in_client_end_measure_field",
        #                                            datatype="Field", parameterType="Required", direction="Input")
        # in_client_end_measure_field.parameterDependencies = [in_client_features.name]
        # in_client_end_measure_field.filter.list = ['int', 'long', 'double']
        #
        # parameters += [in_client_features, in_client_name_field, in_client_begin_routeid_field, in_client_begin_measure_field,
        #                in_client_end_routeid_field, in_client_end_measure_field]

        #   ******************************************
        #   ILI Dig Sheet Parameters
        #   ******************************************

        # Parameter [24]
        in_digsheet_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                               displayName="Target Dig Sheet Features",
                                               name="in_digsheet_features",
                                               datatype=["GPFeatureLayer", "GPTableView"],
                                               parameterType="Required", direction="Input")
        # Parameter [24]
        in_digsheet_begin_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                displayName="Target Dig Sheet Begin Network Route ID Field",
                                                name="in_digsheet_begin_routeid_field",
                                                datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_begin_routeid_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [25]
        in_digsheet_begin_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Dig Sheet Begin Measure Field",
                                                    name="in_digsheet_begin_measure_field",
                                                    datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_begin_measure_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_begin_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [24]
        in_digsheet_end_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                          displayName="Target Dig Sheet End Network Route ID Field",
                                                          name="in_digsheet_end_routeid_field",
                                                          datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_end_routeid_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [25]
        in_digsheet_end_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                         displayName="Target Dig Sheet End Measure Field",
                                                         name="in_digsheet_end_measure_field",
                                                         datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_end_measure_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_end_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [26]
        in_digsheet_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                               displayName="Target Dig Sheet Unique ID Field",
                                               name="in_digsheet_id_field",
                                               datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_id_field.parameterDependencies = [in_digsheet_features.name]
        # in_digsheet_id_field.filter.list = ['int', 'long', 'double']

        # Parameter [31]
        in_digsheet_begin_weld_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                       displayName="Target Begin Weld ID Field",
                                                       name="in_digsheet_begin_weld_id_field",
                                                       datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_begin_weld_id_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [32]
        in_digsheet_begin_weld_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Begin Weld Measure Field",
                                                    name="in_digsheet_begin_weld_measure_field",
                                                    datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_begin_weld_measure_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_begin_weld_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [33
        in_digsheet_end_weld_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                     displayName="Target End Weld ID Field",
                                                     name="in_digsheet_end_weld_id_field",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_end_weld_id_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [34]
        in_digsheet_end_weld_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                      displayName="Target End Weld Measure Field",
                                                      name="in_digsheet_end_weld_measure_field",
                                                      datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_end_weld_measure_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_end_weld_measure_field.filter.list = ['int', 'long', 'double']

        # Parameter [35]
        in_digsheet_owner_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                     displayName="Target Right of Way Land Owner Name Field",
                                                     name="in_digsheet_owner_field",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_owner_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [27]
        in_digsheet_reason_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                   displayName="Target Dig Sheet Reason Field",
                                                   name="in_digsheet_reason_field",
                                                   datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_reason_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [28]
        in_digsheet_reason_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                   displayName="Target Dig Sheet Reason Value",
                                                   name="in_digsheet_reason_value", datatype="GPString",
                                                   parameterType="Required", direction="Input")
        in_digsheet_reason_value.filter.type = "ValueList"
        # in_digsheet_reason_value.filter.list = config.DIGSHEET_LAYOUT_REASON_VALUES
        # in_digsheet_reason_value.value = config.DIGSHEET_LAYOUT_REASON_VALUES[0]

        # Parameter [29]
        in_digsheet_status_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                   displayName="Target Dig Sheet Status Field",
                                                   name="in_digsheet_status_field",
                                                   datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_status_field.parameterDependencies = [in_digsheet_features.name]
        # in_digsheet_reason_field.filter.list = ['int', 'long', 'double']

        # Parameter [20]
        in_digsheet_status_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                   displayName="Target Dig Sheet Status Value",
                                                   name="in_digsheet_status_value", datatype="GPString",
                                                   parameterType="Required", direction="Input")
        in_digsheet_status_value.filter.type = "ValueList"
        # in_digsheet_status_value.filter.list = config.DIGSHEET_LAYOUT_STATUS_VALUES
        # in_digsheet_status_value.value = config.DIGSHEET_LAYOUT_STATUS_VALUES[0]

        # Parameter [35]
        in_digsheet_priority_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Priority Ranking Field",
                                                    name="in_digsheet_priority_field",
                                                    datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_priority_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [20]
        in_digsheet_priority_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Dig Sheet Priority Ranking Value",
                                                    name="in_digsheet_priority_value", datatype="GPString",
                                                    parameterType="Required", direction="Input")
        in_digsheet_priority_value.filter.type = "ValueList"
        # in_digsheet_priority_value.filter.list = config.DIGSHEET_LAYOUT_PRIORITY_VALUES
        # in_digsheet_priority_value.value = config.DIGSHEET_LAYOUT_PRIORITY_VALUES[0]

        # Parameter [35]
        in_digsheet_project_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Project Number Field",
                                                    name="in_digsheet_project_field",
                                                    datatype="Field", parameterType="Required", direction="Input")
        in_digsheet_project_field.parameterDependencies = [in_digsheet_features.name]

        # Parameter [20]
        in_digsheet_project_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                    displayName="Target Dig Sheet Project Number Value",
                                                    name="in_digsheet_project_value", datatype="GPString",
                                                    parameterType="Required", direction="Input")
        in_digsheet_project_value.filter.type = "ValueList"
        # in_digsheet_project_value.filter.list = config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES
        # in_digsheet_project_value.value = config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES[0]

        # # Parameter [35]
        # in_digsheet_revision_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
        #                                              displayName="Target Revision Number Field",
        #                                              name="in_digsheet_revision_field",
        #                                              datatype="Field", parameterType="Required", direction="Input")
        # in_digsheet_revision_field.parameterDependencies = [in_digsheet_features.name]
        #
        # # Parameter [20]
        # in_digsheet_revision_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
        #                                              displayName="Target Dig Sheet Revision Number Value",
        #                                              name="in_digsheet_revision_value", datatype="GPLong",
        #                                              parameterType="Required", direction="Input")
        # in_digsheet_revision_value.filter.type = "ValueList"
        # in_digsheet_revision_value.filter.list = config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES
        # in_digsheet_revision_value.value = config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES[0]

        in_digsheet_begin_exc_lat_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                     displayName="Input Excavation Begin Latitude Field",
                                                     name="in_digsheet_begin_exc_lat_field",
                                                     datatype="Field", parameterType="Optional", direction="Input")
        in_digsheet_begin_exc_lat_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_begin_exc_lat_field.filter.list = ['int', 'long', 'double']

        in_digsheet_begin_exc_long_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                          displayName="Input Excavation Begin Longitude Field",
                                                          name="in_digsheet_begin_exc_long_field",
                                                          datatype="Field", parameterType="Optional", direction="Input")
        in_digsheet_begin_exc_long_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_begin_exc_long_field.filter.list = ['int', 'long', 'double']

        in_digsheet_end_exc_lat_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                          displayName="Input Excavation End Latitude Field",
                                                          name="in_digsheet_end_exc_lat_field",
                                                          datatype="Field", parameterType="Optional", direction="Input")
        in_digsheet_end_exc_lat_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_end_exc_lat_field.filter.list = ['int', 'long', 'double']

        in_digsheet_end_exc_long_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT,
                                                           displayName="Input Excavation End Longitude Field",
                                                           name="in_digsheet_end_exc_long_field",
                                                           datatype="Field", parameterType="Optional",
                                                           direction="Input")
        in_digsheet_end_exc_long_field.parameterDependencies = [in_digsheet_features.name]
        in_digsheet_end_exc_long_field.filter.list = ['int', 'long', 'double']

        parameters += [in_digsheet_features,
                       in_digsheet_begin_routeid_field, in_digsheet_begin_measure_field,
                       in_digsheet_end_routeid_field, in_digsheet_end_measure_field,
                       in_digsheet_id_field,
                       in_digsheet_begin_weld_id_field, in_digsheet_begin_weld_measure_field,
                       in_digsheet_end_weld_id_field, in_digsheet_end_weld_measure_field, in_digsheet_owner_field,
                       in_digsheet_reason_field, in_digsheet_reason_value,
                       in_digsheet_status_field, in_digsheet_status_value,
                       in_digsheet_priority_field, in_digsheet_priority_value,
                       in_digsheet_project_field, in_digsheet_project_value,
                       in_digsheet_begin_exc_lat_field, in_digsheet_begin_exc_long_field,
                       in_digsheet_end_exc_lat_field, in_digsheet_end_exc_long_field
                       ]

        #   ******************************************
        #   Engineering Station Network Parameters
        #   ******************************************

        # Parameter [11]
        in_eng_sta_network_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ENG_STA_NETWORK_FEATURES,
                                          displayName="Input Engineering Station Network Features",
                                          name="in_eng_sta_network_features",
                                          datatype=["GPFeatureLayer", "GPTableView"],
                                          parameterType="Required", direction="Input")

        # Parameter [13]
        in_eng_sta_network_unique_id = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ENG_STA_NETWORK_FEATURES,
                                                     displayName="Engineering Station Network Unique ID Field",
                                                     name="in_eng_sta_network_unique_id",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_eng_sta_network_unique_id.parameterDependencies = [in_eng_sta_network_features.name]

        # Parameter [14]
        in_eng_sta_network_from_measure = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ENG_STA_NETWORK_FEATURES,
                                                     displayName="Engineering Station Network Begin Measure Field",
                                                     name="in_eng_sta_network_from_measure",
                                                     datatype="Field", parameterType="Required", direction="Input")
        in_eng_sta_network_from_measure.parameterDependencies = [in_eng_sta_network_features.name]
        in_eng_sta_network_from_measure.filter.list = ['int', 'long', 'double']

        # Parameter [15]
        in_eng_sta_network_to_measure = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_ENG_STA_NETWORK_FEATURES,
                                                   displayName="Engineering Station Network End Measure Field",
                                                   name="in_eng_sta_network_to_measure",
                                                   datatype="Field", parameterType="Required", direction="Input")
        in_eng_sta_network_to_measure.parameterDependencies = [in_eng_sta_network_features.name]
        in_eng_sta_network_to_measure.filter.list = ['int', 'long', 'double']

        parameters += [in_eng_sta_network_features, in_eng_sta_network_unique_id,
                       in_eng_sta_network_from_measure, in_eng_sta_network_to_measure]

        #   ******************************************
        #  Dig Sheet Interruption Features Parameters
        #   ******************************************

        # Parameter [30]
        in_interrupt_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                displayName="Input Dig Sheet Interruption Features",
                                                name="in_interrupt_features",
                                                datatype=["GPFeatureLayer", "GPTableView"], multiValue=True,
                                                parameterType="Optional", direction="Input")

        # Parameter [38]
        in_interrupt_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                     displayName="Dig Sheet Interruption Network Route ID Field",
                                                     name="in_interrupt_routeid_field",
                                                     datatype="Field", parameterType="Optional", direction="Input")
        in_interrupt_routeid_field.parameterDependencies = [in_interrupt_features.name]

        # Parameter [38]
        in_interrupt_id_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                displayName="Dig Sheet Interruption Unique ID Field",
                                                name="in_interrupt_id_field",
                                                datatype="Field", parameterType="Optional", direction="Input")
        in_interrupt_id_field.parameterDependencies = [in_interrupt_features.name]

        # Parameter [39]
        in_interrupt_measure_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                     displayName="Input Dig Sheet Interruption Measure Field",
                                                     name="in_interrupt_measure_field",
                                                     datatype="Field", parameterType="Optional", direction="Input")
        in_interrupt_measure_field.parameterDependencies = [in_interrupt_features.name]

        # Parameter [16]
        in_interrupt_crossing_width_source = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                    displayName="Input Dig Sheet Interruption Crossing Width Source",
                                                    name="in_interrupt_crossing_width_source",
                                                    datatype="GPString",
                                                    parameterType="optional",
                                                    direction="Input")
        in_interrupt_crossing_width_source.filter.list = config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE
        in_interrupt_crossing_width_source.value = config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[0]  # value

        # Parameter [39]
        in_interrupt_crossing_width_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                                     displayName="Input Dig Sheet Interruption Crossing Width Field",
                                                     name="in_interrupt_crossing_width_field",
                                                     datatype="Field", parameterType="Optional", direction="Input")
        in_interrupt_crossing_width_field.parameterDependencies = [in_interrupt_features.name]


        # Parameter [26]
        in_interrupt_crossing_width_value = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES,
                                             displayName="Input Dig Sheet Interruption Crossing Width Value",
                                             name="in_interrupt_crossing_width_value",
                                             datatype="GPLinearUnit",
                                             parameterType="Optional",
                                             direction="Input")
        in_interrupt_crossing_width_value.value = '30 Feet'
        in_interrupt_crossing_width_value.filter.list = ['Feet']

        parameters += [in_interrupt_features, in_interrupt_routeid_field, in_interrupt_id_field,
                       in_interrupt_measure_field, in_interrupt_crossing_width_source,
                       in_interrupt_crossing_width_field, in_interrupt_crossing_width_value]

        #   ******************************************
        #   Default values
        #   ******************************************

        # Parameter [26]
        in_min_dig_length = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_DEFAULT_VALUES,
                                                            displayName="Input Minimum Dig Length",
                                                            name="in_min_dig_length",
                                                            datatype="GPLinearUnit",
                                                            parameterType="Optional",
                                                            direction="Input")
        in_min_dig_length.value = '60 Feet'
        in_min_dig_length.filter.list = ['Feet']

        parameters += [in_min_dig_length]

        #   ******************************************
        #   Target Anomaly Layer Parameters
        #   ******************************************

        # Parameter [37]
        target_anomaly_features = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY,
                                                       displayName="Target Anomaly Features",
                                                       name="in_target_anomaly_features",
                                                       datatype=["GPFeatureLayer", "GPTableView"],
                                                       parameterType="Optional", direction="Input")

        # Parameter [38]
        target_anomaly_routeid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY,
                                                 displayName="Anomaly Network Route ID Field",
                                                 name="target_anomaly_routeid_field",
                                                 datatype="Field", parameterType="Optional", direction="Input")
        target_anomaly_routeid_field.parameterDependencies = [target_anomaly_features.name]

        # Parameter [38]
        target_anomalyid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY,
                                                        displayName="Anomaly Unique ID Field",
                                                        name="target_anomalyid_field",
                                                        datatype="Field", parameterType="Optional", direction="Input")
        target_anomalyid_field.parameterDependencies = [target_anomaly_features.name]

        # Parameter [39]
        target_digsheetid_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY,
                                                        displayName="Dig Sheet ID Field",
                                                        name="target_digsheetid_field",
                                                        datatype="Field", parameterType="Optional", direction="Input")
        target_digsheetid_field.parameterDependencies = [target_anomaly_features.name]
        # in_digsheet_measure_field.filter.list = ['int', 'long', 'double']

        parameters += [target_anomaly_features, target_anomaly_routeid_field, target_anomalyid_field, target_digsheetid_field]

        # # Parameter [39]
        # test_field = arcpy.Parameter(category=config.DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY,
        #                                           displayName="Test string",
        #                                           name="test_field",
        #                                           datatype="GPString", parameterType="Optional", direction="Input")
        # parameters += [test_field]

        return parameters

    def isLicensed(self):  # optional
        # return True
        return LicenseOperation.is_licensed

    def updateParameters(self, parameters):
        # anomaly
        idx = 0
        idx2 = 7
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_ANOMALY_FIELDS)

        if self.param_changed(parameters[6]):
            uniq_values = list(set(row[0] for row in arcpy.da.SearchCursor(parameters[0].value, parameters[6].valueAsText)))
            parameters[7].value = [i for i in uniq_values if i]

        # girth weld
        idx = 8
        idx2 = 12
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_GIRTH_WELD_FIELDS)

        # right of way
        idx = 12
        idx2 = 18
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_RIGHT_OF_WAY_FIELDS)

        # dig sheet
        idx = 18
        idx2 = 30
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS)

        if parameters[18].value:    # dig sheet layer
            # dig sheet status field
            if not parameters[31].value:
                parameters[31].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[11]

            # dig sheet priority field
            if not parameters[33].value:
                parameters[33].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[12]

            # dig sheet project field
            if not parameters[35].value:
                parameters[35].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[13]

            # # dig sheet revision field
            # if not parameters[37].value:
            #     parameters[37].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[14]

            # dig sheet reason value
            if not parameters[30].value:
                parameters[30].filter.list = config.DIGSHEET_LAYOUT_REASON_VALUES
                parameters[30].value = config.DIGSHEET_LAYOUT_REASON_VALUES[0]
            elif parameters[30].valueAsText not in config.DIGSHEET_LAYOUT_REASON_VALUES:
                lst = self.update_list_items(parameters[30].valueAsText, config.DIGSHEET_LAYOUT_REASON_VALUES)
                parameters[30].filter.list = lst
                parameters[30].value = lst[0]

            # dig sheet status value
            if not parameters[32].value:
                parameters[32].filter.list = config.DIGSHEET_LAYOUT_STATUS_VALUES
                parameters[32].value = config.DIGSHEET_LAYOUT_STATUS_VALUES[0]
            elif parameters[32].valueAsText not in config.DIGSHEET_LAYOUT_STATUS_VALUES:
                lst = self.update_list_items(parameters[32].valueAsText, config.DIGSHEET_LAYOUT_STATUS_VALUES)
                parameters[32].filter.list = lst
                parameters[32].value = lst[0]

            # dig sheet priority value
            if not parameters[34].value:
                parameters[34].filter.list = config.DIGSHEET_LAYOUT_PRIORITY_VALUES
                parameters[34].value = config.DIGSHEET_LAYOUT_PRIORITY_VALUES[0]
            elif parameters[34].valueAsText not in config.DIGSHEET_LAYOUT_PRIORITY_VALUES:
                lst = self.update_list_items(parameters[34].valueAsText, config.DIGSHEET_LAYOUT_PRIORITY_VALUES)
                parameters[34].filter.list = lst
                parameters[34].value = lst[0]

            # dig sheet project value
            if not parameters[36].value:
                parameters[36].filter.list = config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES
                parameters[36].value = config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES[0]
            elif parameters[36].valueAsText not in config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES:
                lst = self.update_list_items(parameters[36].valueAsText, config.DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES)
                parameters[36].filter.list = lst
                parameters[36].value = lst[0]

            # # dig sheet revision value
            # if not parameters[36].value:
            #     parameters[36].filter.list = config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES
            #     parameters[36].value = config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES[0]
            # elif parameters[36].valueAsText not in config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES:
            #     lst = self.update_list_items(parameters[36].valueAsText, config.DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES)
            #     parameters[36].filter.list = lst
            #     parameters[36].value = lst[0]

            # dig sheet excavation from latitude field
            if not parameters[37].value:
                parameters[37].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[14]

            # dig sheet excavation from laongitude field
            if not parameters[38].value:
                parameters[38].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[15]

            # dig sheet excavation to latitude field
            if not parameters[39].value:
                parameters[39].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[16]

            # dig sheet excavation to laongitude field
            if not parameters[40].value:
                parameters[40].value = config.DIGSHEET_LAYOUT_DIG_SHEET_FIELDS[17]

        else:
            parameters[31].value = parameters[33].value = parameters[35].value =  parameters[37].value = \
                parameters[38].value =  parameters[39].value =  parameters[40].value = None

        # engineering station network
        idx = 41
        idx2 = 45
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_ENG_STA_NETWORK_FIELDS)

        # dig interruption features
        idx = 45
        idx2 = 49
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_DIG_INTERRUPT_FIELDS)

        # crossing width
        if parameters[45].value:
            if parameters[49].value == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[0]:
                parameters[50].enabled = True
                if not parameters[50].value:
                    parameters[50].value = config.DIGSHEET_LAYOUT_DIG_INTERRUPT_FIELDS[3]
                parameters[51].enabled = False
            else:
                parameters[50].enabled = False
                parameters[50].value = None
                parameters[51].enabled = True
        else:
            parameters[50].enabled = True
            parameters[49].value = config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[0]
            parameters[51].enabled = False

        # target anomaly
        idx = 53
        idx2 = 57
        if self.param_changed(parameters[idx]):
            self.update_field_names(parameters, idx, idx2, config.DIGSHEET_LAYOUT_TARGET_ANOMALY_FIELDS)

        return

    def updateMessages(self, parameters):

        if parameters[45].value:
            txt = parameters[45].valueAsText
            lst = txt.split(";")
            for layer in lst:
                name = os.path.basename(layer)
                # check field names
                flds = []
                flds += [f.name.upper() for f in arcpy.ListFields(layer)]
                if parameters[46].value and parameters[46].valueAsText not in flds:
                        parameters[46].setErrorMessage("Field does not exists in input {} features.".format(name))
                if parameters[47].value and parameters[47].valueAsText not in flds:
                        parameters[47].setErrorMessage("Field does not exists in input {} features.".format(name))
                if parameters[48].value and parameters[48].valueAsText not in flds:
                        parameters[48].setErrorMessage("Field does not exists in input {} features.".format(name))
                if parameters[49].value == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[0]:
                    if parameters[50].value and parameters[50].valueAsText not in flds:
                        parameters[50].setErrorMessage("Field does not exists in input {} features.".format(name))
        return

    def param_changed(self, param):
        changed = param.value and not param.hasBeenValidated

        return changed

    def update_field_names(self, parameters, idx, idx2, field_names):
        try:
            idx1 = idx + 1
            # if arcpy.Exists(parameters[idx].value):
            if parameters[idx].value:
                for i in range(idx1, idx2):
                    if not parameters[i].value:
                        parameters[i].value = field_names[i - idx1]
            else:
                for i in range(idx1, idx2):
                    parameters[i].value = None

        except Exception as e:
            raise

    def update_list_items(self, txt, in_lst):
        try:
            lst = [txt]
            lst.extend(in_lst)
            return lst
        except Exception as e:
            raise

    def execute(self, parameters, messages):
               
        arcpy.AddMessage("Log file location: " + pimsilitool.GetLogFileLocation())
        pimsilitool.AddMessage("Starting Anomaly Growth Calculator process...")
        pimsilitool.AddMessage(arcpy.env.scratchGDB)

        try:
            ds = load_digsheet_data()

            # Anomaly parameters
            ds.in_anomaly_features = parameters[0].value
            ds.in_anomaly_routeid_fld = parameters[1].valueAsText
            ds.in_anomaly_id_fld = parameters[2].valueAsText
            ds.in_anomaly_measure_fld = parameters[3].valueAsText
            ds.in_anomaly_digid_fld = parameters[4].valueAsText
            ds.in_anomaly_dig_target_fld = parameters[5].valueAsText
            ds.in_anomaly_priority_fld = parameters[6].valueAsText
            ds.in_anomaly_priority_values = parameters[7].valueAsText

            # Weld parameters
            ds.in_weld_features = parameters[8].value
            ds.in_weld_routeid_fld = parameters[9].valueAsText
            ds.in_weldid_fld = parameters[10].valueAsText
            ds.in_weld_measure_fld = parameters[11].valueAsText

            # Right of way parameters
            ds.in_row_features = parameters[12].value
            ds.in_row_begin_routeid_fld = parameters[13].valueAsText
            ds.in_row_begin_measure_fld = parameters[14].valueAsText
            ds.in_row_end_routeid_fld = parameters[15].valueAsText
            ds.in_row_end_measure_fld = parameters[16].valueAsText
            ds.in_row_owner_fld = parameters[17].valueAsText

            # Dig sheet parameters
            ds.in_dig_features = parameters[18].value
            ds.in_digsheet_begin_routeid_field = parameters[19].valueAsText
            ds.in_digsheet_begin_measure_field = parameters[20].valueAsText
            ds.in_digsheet_end_routeid_field = parameters[21].valueAsText
            ds.in_digsheet_end_measure_field = parameters[22].valueAsText
            ds.in_dig_id_fld = parameters[23].valueAsText
            ds.in_dig_begin_weldid_fld = parameters[24].valueAsText
            ds.in_dig_begin_weld_measure_fld = parameters[25].valueAsText
            ds.in_dig_end_weldid_fld = parameters[26].valueAsText
            ds.in_dig_end_weld_measure_fld = parameters[27].valueAsText
            ds.in_dig_row_owner_fld = parameters[28].valueAsText
            ds.in_dig_reason_fld = parameters[29].valueAsText
            ds.in_dig_reason_value = parameters[30].valueAsText
            ds.in_dig_status_fld = parameters[31].valueAsText
            ds.in_dig_status_value = parameters[32].valueAsText
            ds.in_dig_priority_fld = parameters[33].valueAsText
            ds.in_dig_priority_value = parameters[34].valueAsText
            ds.in_dig_project_fld = parameters[35].valueAsText
            ds.in_dig_project_value = parameters[36].valueAsText
            # ds.in_dig_revision_fld = parameters[35].valueAsText
            # ds.in_dig_revision_value = parameters[36].valueAsText
            ds.in_digsheet_begin_exc_lat_field = parameters[37].valueAsText
            ds.in_digsheet_begin_exc_long_field = parameters[38].valueAsText
            ds.in_digsheet_end_exc_lat_field = parameters[39].valueAsText
            ds.in_digsheet_end_exc_long_field = parameters[40].valueAsText

            # engineering station network
            ds.in_eng_sta_network_features = parameters[41].valueAsText
            ds.in_eng_sta_network_unique_id = parameters[42].valueAsText
            ds.in_eng_sta_network_from_measure = parameters[43].valueAsText
            ds.in_eng_sta_network_to_measure = parameters[44].valueAsText

            # dig sheet interrupt features
            ds.in_interrupt_features = parameters[45].valueAsText
            ds.in_interrupt_routeid_fld = parameters[46].valueAsText
            ds.in_interrupt_id_fld = parameters[47].valueAsText
            ds.in_interrupt_measure_fld = parameters[48].valueAsText
            ds.in_interrupt_crossing_width_source = parameters[49].valueAsText
            ds.in_interrupt_crossing_width_field = parameters[50].valueAsText
            ds.in_interrupt_crossing_width_value = parameters[51].valueAsText

            # default values
            ds.in_min_dig_length = parameters[52].valueAsText

            # Target anomaly parameters
            ds.in_target_anomaly_features = parameters[53].value
            ds.in_target_anomaly_routeid_fld = parameters[54].valueAsText
            ds.in_target_anomalyid_fld = parameters[55].valueAsText
            ds.in_target_anomaly_digid_fld = parameters[56].valueAsText

            ds.run()

            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

