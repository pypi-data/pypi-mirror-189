import arcpy,os

ws = r"C:\Surendra\From_Sean\GDBs\CreatedData_2022_6oclock_v2.gdb"
infc = os.path.join(ws, "Anomaly_Ellipse_6_Oclock_2022")
# maxid = max([cur[0] for cur in arcpy.da.SearchCursor(infc, "OBJECTID")])
f = "CL_NAME"
field = arcpy.ListFields(infc,f)[0]
print (field.type)
print (field.length)
sj_pipe_routeid_field = "route_id"
in_pipe_routeid_field =  "route_id"
s = str(field.length) + ' ' + field.type


a = sj_pipe_routeid_field + ' "' + sj_pipe_routeid_field + '" true true false 38 Guid 0 0,First,#,' + infc + ',' + in_pipe_routeid_field + ',-1,-1;'

b = sj_pipe_routeid_field + ' "' + sj_pipe_routeid_field + '" true true false ' + s + ' 0 0,First,#,' + infc + ',' + in_pipe_routeid_field + ',-1,-1;'

import numpy
import sqlite3
import os
import math




from inlineinspection.license.validate_license.license_operation import LicenseOperation
# l = LicenseOperation()
# a = l.validate_license()
lic = LicenseOperation.is_licensed


lst = [2,3,4]
arr = tuple(lst)

try:


    arcpy.env.workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\PIMS ILI Demo_473068\p20\scratch.gdb"
    arcpy.env.overwriteOutput = True
    target_features = "AnomalyEllipse6OClock2012"
    weld_features = "WeldLines6OClock2012"
    seam_features = "SeamLines6OClock2012"
    anom_weld_spatial_join = "Anomaly_Weld_join"
    anom_seam_spatial_join = "Anomaly_Seam_join"
    target_routeid_field = "EventID"
    target_measure_field = "Measure"
    target_depth_field = "MaxDepthPCT"
    target_clockpos_field = "ClockPosition"
    target_maop_field = "B31GMAOP"
    target_burstpressure_field = "B31GERF"
    target_erf_field = "MaxDepthMeasured"
    weld_routeid_field = "Route_ID"
    weld_measure_field = "Outer_Nomi"
    seam_routeid_field = "EventID"
    seam_beginmeasure_field = "Measure"
    seam_endmeasure_field = "Station"

    target_routeid_field_sj = "Anom_" +  target_routeid_field
    target_measure_field_sj = "Anom_" + target_measure_field
    target_depth_field_sj = "Anom_" + target_depth_field
    target_clockpos_field_sj = "Anom_" + target_clockpos_field
    target_maop_field_sj = "Anom_" + target_maop_field
    target_burstpressure_field_sj = "Anom_" + target_burstpressure_field
    target_erf_field_sj = "Anom_" + target_erf_field

    weld_routeid_field_sj = "Weld_" + weld_routeid_field
    weld_measure_field_sj = "Weld_" + weld_measure_field
    seam_routeid_field_sj = "Seam_" + seam_routeid_field
    seam_beginmeasure_field_sj = "Seam_" + seam_beginmeasure_field
    seam_endmeasure_field_sj = "Seam_" + seam_endmeasure_field


    #
    #
    # anom_weld_spatial_join_field_mapping = "'" +   target_routeid_field_sj +  "\"" + target_routeid_field_sj + "\" true true false 38 String 0 0,First,#,\""  + target_features + "\"," + target_routeid_field + ",-1,-1,\"" + target_features + "\"," + target_routeid_field + ",-1,-1;" +
    #                                          target_measure_field_sj +  "\"" + target_measure_field_sj + "\" true true false 8 Double 0 0,First,#,\"" + target_features + "\"," + target_measure_field + ",-1,-1,\"" + target_features + "\"," + target_measure_field + ",-1,-1;" +
    #                                          target_depth_field_sj   +  "\"" + target_depth_field_sj   + "\" true true false 4 Double 0 0,First,#,\"" + target_features + "\"," + target_depth_field   + ",-1,-1,\"" + target_features + "\"," + target_depth_field + ",-1,-1;" +
    #                                         weld_routeid_field_sj +  "\"" + weld_routeid_field_sj + "\" true true false 38 String 0 0,First,#,\"" + weld_features + "\"," + weld_routeid_field + ",-1,-1,\"" + weld_features + "\"," + weld_routeid_field + ",-1,-1;" +
    #                                         weld_measure_field_sj +  "\"" + weld_measure_field_sj + "\" true true false 8 Double 0 0,First,#,\""  + weld_features + "\"," + weld_measure_field + ",-1,-1,\"" + weld_features + "\"," + weld_measure_field + ",-1,-1;" + "'"
    #



    fieldmappings_weld = arcpy.FieldMappings()
    fieldmappings_weld.addTable(target_features)
    fieldmappings_weld.addTable(weld_features)



    weld_routeid_field_idx = fieldmappings_weld.findFieldMapIndex(weld_routeid_field)
    fieldmap_weld_route_id = fieldmappings_weld.getFieldMap(weld_routeid_field_idx)

    # Get the output field's properties as a field object
    field_weld_route_id = fieldmap_weld_route_id.outputField

    # Rename the field and pass the updated field object back into the field map
    field_weld_route_id.name = "ANOM_WELD_JOIN_ROUTE_ID"
    field_weld_route_id.aliasName = "ANOM_WELD_JOIN_ROUTE_ID"
    field_weld_route_id.outputField = field_weld_route_id

    ###############################

    weld_measure_field_idx = fieldmappings_weld.findFieldMapIndex(weld_measure_field)
    fieldmap_weld_measure = fieldmappings_weld.getFieldMap(weld_measure_field_idx)

    # Get the output field's properties as a field object
    field_weld_measure = fieldmap_weld_measure.outputField

    # Rename the field and pass the updated field object back into the field map
    field_weld_measure.name = "ANOM_WELD_JOIN_MEASURE"
    field_weld_measure.aliasName = "ANOM_WELD_JOIN_MEASURE"
    field_weld_measure.outputField = field_weld_measure


    fieldmappings_weld.replaceFieldMap(weld_routeid_field_idx, fieldmap_weld_route_id)
    fieldmappings_weld.replaceFieldMap(weld_measure_field_idx, fieldmap_weld_measure)

    # arcpy.SpatialJoin_analysis(target_features, weld_features, anom_weld_spatial_join, "#", "#",fieldmappings_weld)
    # "e - 2012, 6 o\'clock\",EventID,-1,-1;Anom_Measure \"Anom_Measure\" true true false 8" +
    # arcpy.analysis.SpatialJoin(target_features, weld_features, anom_weld_spatial_join, "JOIN_ONE_TO_ONE", "KEEP_ALL",
    #                             target_routeid_field_sj +  ' "' + target_routeid_field_sj + '" true true false 38 String 0 0,First,#,' + target_features + ',' + target_routeid_field + ',-1,-1;' +
    #                                 target_measure_field_sj + ' "'  + target_measure_field_sj + '" true true false 8 Double 0 0,First,#,'  + target_features + ',' + target_measure_field + ',-1,-1;' +
    #                                 target_depth_field_sj + ' "'    + target_depth_field_sj   + '" true true false 8 Double 0 0,First,#,'  + target_features + ',' + target_depth_field + ',-1,-1;' +
    #                                 weld_routeid_field_sj + ' "'    + weld_routeid_field_sj   + '" true true false 38 String 0 0,First,#,' + weld_features + ',' + weld_routeid_field + ',-1,-1;' +
    #                                 weld_measure_field_sj + ' "'    + weld_measure_field_sj   + '" true true false 8 Double 0 0,First,#,'  + weld_features + ',' + weld_measure_field + ',-1,-1;' ,
    #                             "INTERSECT", "0.33 Feet", '')

    # arcpy.analysis.SpatialJoin(target_features, weld_features, anom_weld_spatial_join, "JOIN_ONE_TO_ONE", "KEEP_ALL",
    #                            "'" + target_routeid_field_sj + "\"" + target_routeid_field_sj + "\" true true false 38 String 0 0,First,#,\"" + target_features + "\"," + target_routeid_field + ",-1,-1,\"" + target_features + "\"," + target_routeid_field + ",-1,-1;" +
    #                            target_measure_field_sj + "\"" + target_measure_field_sj + "\" true true false 8 Double 0 0,First,#,\"" + target_features + "\"," + target_measure_field + ",-1,-1,\"" + target_features + "\"," + target_measure_field + ",-1,-1;" +
    #                            target_depth_field_sj + "\"" + target_depth_field_sj + "\" true true false 4 Double 0 0,First,#,\"" + target_features + "\"," + target_depth_field + ",-1,-1,\"" + target_features + "\"," + target_depth_field + ",-1,-1;" +
    #                            weld_routeid_field_sj + "\"" + weld_routeid_field_sj + "\" true true false 38 String 0 0,First,#,\"" + weld_features + "\"," + weld_routeid_field + ",-1,-1,\"" + weld_features + "\"," + weld_routeid_field + ",-1,-1;" +
    #                            weld_measure_field_sj + "\"" + weld_measure_field_sj + "\" true true false 8 Double 0 0,First,#,\"" + weld_features + "\"," + weld_measure_field + ",-1,-1,\"" + weld_features + "\"," + weld_measure_field + ",-1,-1;" + "'",
    #                            "INTERSECT", "0.33 Feet", '')


    metal_loss_field_mappings =  target_routeid_field_sj +  ' "' + target_routeid_field_sj + '" true true false 38 String 0 0,First,#,' + target_features + ',' + target_routeid_field + ',-1,-1;' + \
                                    target_measure_field_sj + ' "'  + target_measure_field_sj + '" true true false 8 Double 0 0,First,#,'  + target_features + ',' + target_measure_field + ',-1,-1;' + \
                                    target_depth_field_sj + ' "'    + target_depth_field_sj   + '" true true false 8 Double 0 0,First,#,'  + target_features + ',' + target_depth_field + ',-1,-1;'

    weld_field_mappings =  weld_routeid_field_sj + ' "' + weld_routeid_field_sj + '" true true false 38 String 0 0,First,#,' + weld_features + ',' + weld_routeid_field + ',-1,-1;' + \
                                  weld_measure_field_sj + ' "' + weld_measure_field_sj + '" true true false 8 Double 0 0,First,#,' + weld_features + ',' + weld_measure_field + ',-1,-1;'

    field_mappings = metal_loss_field_mappings + weld_field_mappings
    arcpy.analysis.SpatialJoin(target_features, weld_features, anom_weld_spatial_join, "JOIN_ONE_TO_ONE", "KEEP_COMMON",  field_mappings, "WITHIN_A_DISTANCE", "0.33 Feet", '')

    anom_weld_spatial_join_nparr = arcpy.da.FeatureClassToNumPyArray(anom_weld_spatial_join, "*", null_value=-9999)

    # arcpy.SpatialJoin_analysis(target_features, weld_features, anom_weld_spatial_join, "JOIN_ONE_TO_ONE", "KEEP_ALL",
    #                            r'' + config.OUTPUT_SYMS_FIELDNAME + ' "' + config.OUTPUT_SYMS_FIELDNAME + '"  true true false 50 Long 0 0,First,#,' + pipesegment_layer + ',' + syms_field + ',0,50',
    #                            "INTERSECT", None, '')

    # arcpy.analysis.SpatialJoin(
    #     r"Anomalies, 6 o'clock-centered\2012 Anomalies, 6 o'clock\Anomaly Ellipse - 2012, 6 o'clock",
    #     r"Anomalies, 6 o'clock-centered\2017 Anomalies, 6 o'clock\Weld Lines - 2017, 6 o'clock",
    #     r"C:\Surendra\From_Tracy\scratch.gdb\aaa", "JOIN_ONE_TO_ONE", "KEEP_ALL",
    #     "Anom_EventID \"Anom_EventID\" true true false 38 Guid 0 0,First,#,\"Anomalies, 6 o\'c" +
    #     "lock-centered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",Event" +
    #     "ID,-1,-1,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellips" +
    #     "e - 2012, 6 o\'clock\",EventID,-1,-1;Anom_Measure \"Anom_Measure\" true true false 8" +
    #     " Double 0 0,First,#,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clock\\Ano" +
    #     "maly Ellipse - 2012, 6 o\'clock\",Measure,-1,-1,\"Anomalies, 6 o\'clock-centered\\201" +
    #     "2 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",Measure,-1,-1;Anom_B31" +
    #     "GMAOP \"Anom_B31GMAOP\" true true false 4 Long 0 0,First,#,\"Anomalies, 6 o\'clock-c" +
    #     "entered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",B31GMAOP,-1" +
    #     ",-1,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2" +
    #     "012, 6 o\'clock\",B31GMAOP,-1,-1;_Anom_MaxDepthPCT \"_Anom_MaxDepthPCT\" true true f" +
    #     "alse 8 Double 0 0,First,#,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clo" +
    #     "ck\\Anomaly Ellipse - 2012, 6 o\'clock\",MaxDepthPCT,-1,-1,\"Anomalies, 6 o\'clock-ce" +
    #     "ntered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",MaxDepthPCT," +
    #     "-1,-1;Anom_MeasuredWallThickness \"Anom_MeasuredWallThickness\" true true false 8 " +
    #     "Double 0 0,First,#,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clock\\Anom" +
    #     "aly Ellipse - 2012, 6 o\'clock\",MeasuredWallThickness,-1,-1,\"Anomalies, 6 o\'clock" +
    #     "-centered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",MeasuredW" +
    #     "allThickness,-1,-1;Weld_EventID \"Weld_EventID\" true true false 38 Guid 0 0,First" +
    #     ",#,\"Anomalies, 6 o\'clock-centered\\2017 Anomalies, 6 o\'clock\\Weld Lines - 2017, 6" +
    #     " o\'clock\",EventID,-1,-1,\"Anomalies, 6 o\'clock-centered\\2012 Anomalies, 6 o\'clock" +
    #     "\\Anomaly Ellipse - 2012, 6 o\'clock\",EventID,-1,-1;Wels_Measure \"Wels_Measure\" tr" +
    #     "ue true false 8 Double 0 0,First,#,\"Anomalies, 6 o\'clock-centered\\2017 Anomalies" +
    #     ", 6 o\'clock\\Weld Lines - 2017, 6 o\'clock\",Measure,-1,-1,\"Anomalies, 6 o\'clock-ce" +
    #     "ntered\\2012 Anomalies, 6 o\'clock\\Anomaly Ellipse - 2012, 6 o\'clock\",Measure,-1,-" +
    #     "1", "INTERSECT", "0.33 Feet", '')






    in_rows = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\United Brine Data Loading 20201026_e05205\p20\scratch.gdb\WeldLines__clock_12"
    weld2np = arcpy.da.FeatureClassToNumPyArray(in_rows, ("WeldXMinCoord"))

    weld2np = numpy.sort(weld2np, order="WeldXMinCoord")

    weld2np_rec = weld2np[(weld2np["WeldXMinCoord"] <= 144719.13)]
    if len(weld2np_rec) < 1:
        weld2np_rec = weld2np[(weld2np["WeldXMinCoord"] < 144719.13)]
    if len(weld2np_rec) > 0:
        meas = weld2np_rec[len(weld2np_rec) - 1]

    in_rows =   r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\United Brine Data Loading 20201026_e05205\p20\scratch.gdb\AnomalyComparer"
    join_tab1 = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\United Brine Data Loading 20201026_e05205\p20\scratch.gdb\AnomalyEllipse_2012_clock_6"
    join_tab2 = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\United Brine Data Loading 20201026_e05205\p20\scratch.gdb\AnomalyEllipse_2017_clock_6"
    p_fld = r"PARENT_EventID"
    c_fld = "CHILD_EventID"
    join_fld = r"EventID"
    fieldList = ["Measure", "MaxDepthPCT"]
    arcpy.JoinField_management(in_rows, p_fld, join_tab1, join_fld,  fieldList)
    arcpy.AlterField_management(in_rows, "Measure", "PARENT_Measure", "PARENT_Measure")
    arcpy.AlterField_management(in_rows, "MaxDepthPCT", "PARENT_MaxDepthPCT", "PARENT_MaxDepthPCT")
    arcpy.JoinField_management(in_rows, c_fld, join_tab2, join_fld, fieldList)
    arcpy.AlterField_management(in_rows, "Measure", "CHILD_Measure", "CHILD_Measure")
    arcpy.AlterField_management(in_rows, "MaxDepthPCT", "CHILD_MaxDepthPCT", "CHILD_MaxDepthPCT")


    # calc_anomaly_y_coord(! % Input ILI Pipe Tally Clock Position Field %!,
    # % Input Pipeline Diameter Value %,
    # % Input False  Northing Value %,
    # % Input Clock Position Offset %,
    # % Input Y - Axis Clock Orientation %)r
    #

    def calc_anomaly_y_coord(clock_pos, pipe_od, false_northing, clock_offset, y_axis_clock):
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
        if y_axis_clock == "6:00 Centered":
            if clock_hours == 12:
                y_coord = ((clock_minutes / 60 / 12) * (pipe_od / 12 * math.pi)) + false_northing
            else:
                y_coord = (((clock_hours / 12) + (clock_minutes / 60 / 12)) * (pipe_od / 12 * math.pi)) + false_northing
        else:  # y_axis_clock = "12:00 Centered"
            if clock_hours == 12:
                y_coord = (-1) * (((clock_minutes / 60 / 12) * (pipe_od / 12 * math.pi)) + false_northing)
            elif 1 <= clock_hours < 6:
                y_coord = (-1) * ((((clock_hours / 12) + (clock_minutes / 60 / 12)) * (
                            pipe_od / 12 * math.pi)) + false_northing)
            else:  # 6 <= clock_hours <= 11
                y_coord = ((1 - ((clock_hours / 12) + (clock_minutes / 60 / 12))) * (
                            pipe_od / 12 * math.pi)) + false_northing
        return y_coord


    sqlite_db = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\PIMS2.sqlite"
    if  arcpy.Exists(sqlite_db):
        arcpy.Delete_management(sqlite_db)
    arcpy.CreateSQLiteDatabase_management(sqlite_db, 'ST_GEOMETRY')

    arcpy.env.workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\scratch.gdb"
    arcpy.env.overwriteOutput = True
    outtable =  "test_neartable_prior2recent_06"
    outtable_12 = "test_neartable_prior2recent_12"
    outtable_join = "test_neartable_prior2recent_06_join"
    pre_data = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\scratch.gdb\AnomalyEllipse_old_6"
    cur_data = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\scratch.gdb\AnomalyEllipse_new_6"

    pre_data_12 = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\scratch.gdb\AnomalyEllipse_old_12"
    cur_data_12 = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\PIMS\scratch.gdb\AnomalyEllipse_new_12"

    old_6 = os.path.join(arcpy.env.workspace, "old_6")
    new_6 = os.path.join(arcpy.env.workspace, "new_6")

    old_12 = os.path.join(arcpy.env.workspace, "old_12")
    new_12 = os.path.join(arcpy.env.workspace, "new_12")

    for fc in [old_6, new_6, old_12, new_12]:
        if arcpy.Exists(fc):
            arcpy.Delete_management(fc)



    arcpy.FeatureClassToFeatureClass_conversion(pre_data, arcpy.env.workspace, "old_6")
    arcpy.FeatureClassToFeatureClass_conversion(cur_data, arcpy.env.workspace, "new_6")
    arcpy.FeatureClassToFeatureClass_conversion(pre_data_12, arcpy.env.workspace, "old_12")
    arcpy.FeatureClassToFeatureClass_conversion(cur_data_12, arcpy.env.workspace, "new_12")


    arcpy.AddField_management(old_6, "ORIGINAL_OBJECTID", "LONG")
    arcpy.AddField_management(new_6, "ORIGINAL_OBJECTID", "LONG")
    arcpy.AddField_management(old_12, "ORIGINAL_OBJECTID", "LONG")
    arcpy.AddField_management(new_12, "ORIGINAL_OBJECTID", "LONG")

    arcpy.CalculateField_management(old_6, "ORIGINAL_OBJECTID", '!OBJECTID!', "PYTHON3")
    arcpy.CalculateField_management(new_6, "ORIGINAL_OBJECTID", '!OBJECTID!', "PYTHON3")
    arcpy.CalculateField_management(old_12, "ORIGINAL_OBJECTID", '!OBJECTID!', "PYTHON3")
    arcpy.CalculateField_management(new_12, "ORIGINAL_OBJECTID", '!OBJECTID!', "PYTHON3")





    arcpy.FeatureClassToGeodatabase_conversion([old_6, new_6, old_12, new_12],  sqlite_db)

    arcpy.analysis.GenerateNearTable(old_6, new_6, outtable, "1 Feet", "LOCATION", "NO_ANGLE", "ALL", 1000, "PLANAR")

    arcpy.analysis.GenerateNearTable(old_12, new_12, outtable_12, "1 Feet", "LOCATION", "NO_ANGLE", "ALL", 1000,  "PLANAR")

    arcpy.TableToGeodatabase_conversion([outtable, outtable_12], sqlite_db)

    # view_6 = "CREATE VIEW view_6 AS SELECT * from main.test_neartable_prior2recent_06 p6 " \
    #          "left outer join main.AnomalyEllipse_old_6  on p6.IN_FID =  main.AnomalyEllipse_old_6.OBJECTID " \
    #          "left outer join main.AnomalyEllipse_new_6  on p6.NEAR_FID =  main.AnomalyEllipse_new_6.OBJECTID; "

    # view_12 = "CREATE VIEW view_12 AS SELECT * from main.test_neartable_prior2recent_12 p12 " \
    #          "left outer join main.AnomalyEllipse_old_12  on p12.IN_FID =  main.AnomalyEllipse_old_12.OBJECTID " \
    #          "left outer join main.AnomalyEllipse_new_12  on p12.NEAR_FID =  main.AnomalyEllipse_new_12.OBJECTID; "

    conn = sqlite3.connect(sqlite_db)
    cur = conn.cursor()
    # cur.executescript(view_6)
    # cur.executescript(view_12)
    # arr1 = arcpy.da.TableToNumPyArray(os.path.join(sqlite_db, 'main.view_6'), "*", null_value=-9999)
    # arr2 = arcpy.da.TableToNumPyArray(os.path.join(sqlite_db, 'main.view_12'), "*", null_value=-9999)

    cur.execute("SELECT * from main.test_neartable_prior2recent_06")
    result0 = cur.fetchall()
    #
    # # Fetching 1st row from the table
    # result = cur.fetchone()
    # print(result)

    # Fetching 1st row from the table
    # result = cur.fetchall();
    # arcpy.management.SelectLayerByAttribute("NearTable_old2new_6", "NEW_SELECTION",
    #                                         "AnomalyEllipse_old_6.EventID = AnomalyEllipse_new_6.EventID", None)

    cur.execute("SELECT p6.IN_FID, p6.NEAR_FID, main.old_6.ORIGINAL_OBJECTID, "
                "main.old_6.EventID, main.new_6.ORIGINAL_OBJECTID, "
                "main.new_6.EventID "
                "from main.test_neartable_prior2recent_06 p6 " \
                "left outer join main.old_6  on p6.IN_FID =  main.old_6.ORIGINAL_OBJECTID " 
                "left outer join main.new_6  on p6.NEAR_FID =  main.new_6.ORIGINAL_OBJECTID;")


    result1 = cur.fetchall()

    cur.execute("SELECT p6.IN_FID, p6.NEAR_FID, main.old_6.ORIGINAL_OBJECTID, main.old_6.EventID, main.new_6.ORIGINAL_OBJECTID, main.new_6.EventID "
        "from main.test_neartable_prior2recent_06 p6 " \
        "left outer join main.old_6  on p6.IN_FID =  main.old_6.ORIGINAL_OBJECTID " \
        "left outer join main.new_6  on p6.NEAR_FID =  main.new_6.ORIGINAL_OBJECTID "
        "where main.old_6.EventID =  main.new_6.EventID;")

    result2 = cur.fetchall()
    # cur.execute(
    #     "SELECT main.AnomalyEllipse_old_6.OBJECTID, main.AnomalyEllipse_old_6.EventID from main.test_neartable_prior2recent_06 p6 " \
    #     "left outer join main.AnomalyEllipse_old_6  on p6.IN_FID =  main.AnomalyEllipse_old_6.OBJECTID " \
    #     "left outer join main.AnomalyEllipse_new_6  on p6.NEAR_FID =  main.AnomalyEllipse_new_6.OBJECTID "
    #     "where main.AnomalyEllipse_old_6.EventID =  main.AnomalyEllipse_new_6.EventID;")
    #
    # result3 = cur.fetchall()

    conn.close()

    # arr = arcpy.da.TableToNumPyArray(outtable, "*", null_value=-9999)
    #
    # arcpy.management.AddJoin(outtable, "IN_FID", pre_data, "OBJECTID",  "KEEP_ALL")
    # arr1 = arcpy.da.TableToNumPyArray(outtable, "*", null_value=-9999)
    # # arcpy.management.AddJoin(outtable, "NEAR_FID",  cur_data, "OBJECTID", "KEEP_ALL")
    #
    # arcpy.management.JoinField(outtable, "IN_FID", pre_data, "OBJECTID", None)
    # arr2 = arcpy.da.TableToNumPyArray(outtable, "*", null_value=-9999)
    #
    # arcpy.management.JoinField(outtable, "NEAR_FID", cur_data, "OBJECTID", None)
    # arr3 = arcpy.da.TableToNumPyArray(outtable, "*", null_value=-9999)

    arcpy.AddMessage("Completed...")

except Exception as e:
    arcpy.AddMessage(e)