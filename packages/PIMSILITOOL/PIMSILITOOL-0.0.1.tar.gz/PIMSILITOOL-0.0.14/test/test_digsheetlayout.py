import arcpy
import os
import inlineinspection
from inlineinspection.digsheetlayout.load_digsheet_data import load_digsheet_data
from inlineinspection import config

# esn = r"C:\workspace\inlineinspection\tbPODS7_fgdb.gdb\Features\ENGINEERING_STA_NETWORK"
# routeid = '{F2BA7E69-C17E-4327-8905-EA1620DE7160}'
# where = "{} = '{}'".format("UNIQUE_ID", routeid)
# pl_from_meas = 26923.370179
# pl_end_meas = 27041.5699458
# shape = None
#
# point = arcpy.Point(-91.219727545528, 30.189097579568, 0, 26923.370179)
# ptGeometry = arcpy.PointGeometry(point)
#
# point1 = arcpy.Point(-91.219806254528, 30.189415389567, 0, 27041.5699458)
# ptGeometry1 = arcpy.PointGeometry(point)
#
# with arcpy.da.SearchCursor(esn,
#                            ["FROM_MEASURE", "TO_MEASURE", "SHAPE@"],
#                            where_clause=where) as cursor:
#         for row in cursor:
#                 esn_from_measure = row[0]
#                 esn_to_measure = row[1]
#                 esn_shape = row[2]
#                 inlineinspection.AddWarning("weld from meaasure: {}".format(pl_from_meas))
#                 inlineinspection.AddWarning("weld to meaasure: {}".format(pl_end_meas))
#
#                 start_measure = float(pl_from_meas - esn_from_measure) / float(esn_to_measure - esn_from_measure)
#                 end_measure = float(pl_end_meas - esn_from_measure) / float(esn_to_measure - esn_from_measure)
#
#                 shape = esn_shape.segmentAlongLine(start_measure, end_measure, True)
#                 # shape = esn_shape.segmentAlongLine(pl_from_meas, pl_end_meas)
#                 query = esn_shape.queryPointAndDistance (point)
#                 query1 = esn_shape.queryPointAndDistance(point1)
#
#                 line_seg = esn_shape.segmentAlongLine(query[1], query1[1])
#
#
#                 inlineinspection.AddWarning(str(shape))
#                 break





ws = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\DigSheetLayout\PODS7_NEW.gdb"

in_ili_features = os.path.join(ws, "ANOMALY_ILI_TEST")
in_weld_features =  os.path.join(ws, "GIRTH_WELD")
in_row_features =  os.path.join(ws, "RIGHT_OF_WAY")
in_digsheet_features = os.path.join(ws, "PIPE_EXCAVATION_TEST")
in_esn_features = os.path.join(ws, "ENGINEERING_STA_NETWORK")

hydrology =  os.path.join(ws, "CROSSING_HYDROLOGY")
pipeline =  os.path.join(ws, "CROSSING_PIPELINE")
transport =  os.path.join(ws, "CROSSING_TRANSPORTATION")
utility =  os.path.join(ws, "CROSSING_UTILITY")
in_interrupt_features = '"' + hydrology + ';' + pipeline + ';' + transport + ';' + utility + '"'
# in_interrupt_features = None



target_anomaly_features = None


try:

        lo = load_digsheet_data()

        lo.in_anomaly_features = in_ili_features
        lo.in_anomaly_routeid_fld  = "NETWORK_ROUTE_ID"
        lo.in_anomaly_id_fld =  "UNIQUE_ID"
        lo.in_anomaly_measure_fld =  "MEASURE"
        lo.in_anomaly_digid_fld = "DIG_SHEET_ID"
        lo.in_anomaly_dig_target_fld = "IS_DIG_TARGET_FEATURE"
        lo.in_anomaly_priority_fld = "ANOMALY_PRIORITY"
        lo.in_anomaly_priority_values = "5;6"

        lo.in_weld_features = in_weld_features
        lo.in_weldid_fld = "UNIQUE_ID"
        lo.in_weld_routeid_fld = "NETWORK_ROUTE_ID"
        lo.in_weld_measure_fld = "MEASURE"

        lo.in_row_features = in_row_features
        lo.in_row_begin_routeid_fld = "FROM_NETWORK_ROUTE_ID"
        lo.in_row_begin_measure_fld = "FROM_MEASURE"
        lo.in_row_end_routeid_fld = "TO_NETWORK_ROUTE_ID"
        lo.in_row_end_measure_fld = "TO_MEASURE"
        lo.in_row_owner_fld =  "LAND_OWNER"

        lo.in_dig_features = in_digsheet_features

        lo.in_digsheet_begin_routeid_field = "FROM_NETWORK_ROUTE_ID"
        lo.in_digsheet_begin_measure_field = "FROM_MEASURE"
        lo.in_digsheet_end_routeid_field = "TO_NETWORK_ROUTE_ID"
        lo.in_digsheet_end_measure_field = "TO_MEASURE"



        lo.in_dig_routeid_fld = "NETWORK_ROUTE_ID"
        lo.in_dig_measure_fld = "MEASURE"
        lo.in_dig_id_fld ="UNIQUE_ID"
        lo.in_dig_begin_weldid_fld = "BEGIN_WELD_ID"
        lo.in_dig_begin_weld_measure_fld = "BEGIN_WELD_MEASURE"
        lo.in_dig_end_weldid_fld =  "END_WELD_ID"
        lo.in_dig_end_weld_measure_fld =  "END_WELD_MEASURE"
        lo.in_dig_row_owner_fld = "LAND_OWNER"
        lo.in_dig_reason_fld = "DIG_REASON"
        lo.in_dig_reason_value = "ILI Verification Dig"
        lo.in_dig_status_fld = "DIG_STATUS"
        lo.in_dig_status_value = "Initialized"
        lo.in_dig_priority_fld = "DIG_PRIORITY"
        lo.in_dig_priority_value = "Immediate"
        lo.in_dig_project_fld = "DIG_SHEET_PROJECT_NUMBER"
        lo.in_dig_project_value = "ABC123"
        lo.in_dig_revision_fld = "REVISION_NUMBER"
        lo.in_dig_revision_value = "1"

        lo.in_digsheet_begin_exc_long_field = "BEG_EXCV_LATITUDE"
        lo.in_digsheet_begin_exc_lat_field=   "BEG_EXCV_LONGITUDE"
        lo.in_digsheet_end_exc_long_field= "END_EXCV_LATITUDE"
        lo.in_digsheet_end_exc_lat_field="END_EXCV_LONGITUDE"

        lo.in_eng_sta_network_features = in_esn_features
        lo.in_eng_sta_network_unique_id = "UNIQUE_ID"
        lo.in_eng_sta_network_from_measure = "FROM_MEASURE"
        lo.in_eng_sta_network_to_measure = "TO_MEASURE"

        lo.in_interrupt_features = in_interrupt_features
        lo.in_interrupt_routeid_fld = "NETWORK_ROUTE_ID"
        lo.in_interrupt_id_fld = "UNIQUE_ID"
        lo.in_interrupt_measure_fld = "MEASURE"

        lo.in_interrupt_crossing_width_source = config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[1]
        lo.in_interrupt_crossing_width_field = "ROAD_WIDTH"
        lo.in_interrupt_crossing_width_value = "30 Feet"


        # default values
        lo.in_min_dig_length = "60 Feet"


        lo.in_target_anomaly_features = None
        lo.in_target_anomaly_routeid_fld = None
        lo.in_target_anomalyid_fld = None
        lo.in_target_anomaly_digid_fld = None


        lo.run()

        inlineinspection.AddError("Test Error")
except Exception as e:
    raise





