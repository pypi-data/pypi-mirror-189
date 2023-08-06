import arcpy
import os

try:
    # in_workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\PIMS ILI Demo_473068\p20\scratch.gdb"
    in_workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\DigSheetLayout\DigSheetLayout.gdb"
    in_ili_features = arcpy.Parameter()
    in_ili_features.value = os.path.join(in_workspace, "Anomaly_Ellipse_6_Oclock")

    in_ili_features_12 = arcpy.Parameter()
    in_ili_features_12.value = None

    in_pipe_routeid_field = arcpy.Parameter()
    in_pipe_routeid_field.value = "NETWORK_ROUTE_ID"

    in_pipe_depth_pct_field = arcpy.Parameter()
    in_pipe_depth_pct_field.value = 'METAL_LOSS_DEPTH_PERCENT'

    # in_pipe_measure_field = arcpy.Parameter()
    # in_pipe_measure_field.value = 'Measure'

    in_pipe_clockpos_field = arcpy.Parameter()
    in_pipe_clockpos_field.value = 'CLOCK_POSITION'

    in_pipe_maop_field = arcpy.Parameter()
    in_pipe_maop_field.value = 'ReferencePressure'

    in_pipe_burstpressure_field = arcpy.Parameter()
    in_pipe_burstpressure_field.value = 'PipeBurstPressure'

    in_pipe_safepressure_field = arcpy.Parameter()
    in_pipe_safepressure_field.value = 'CalculatedSafePressure'

    in_pipe_erf_field = arcpy.Parameter()
    in_pipe_erf_field.value = 'EstimatedRepairFactor'

    in_crack_features = arcpy.Parameter()
    in_crack_features.value = os.path.join(in_workspace, 'Crack_like_Ellipse_6_Oclock')

    in_crack_features_12 = arcpy.Parameter()
    in_crack_features_12.value = None

    in_crack_routeid_field = arcpy.Parameter()
    in_crack_routeid_field.value = 'NETWORK_ROUTE_ID'

    # in_crack_measure_field = arcpy.Parameter()
    # in_crack_measure_field.value = 'Measure'

    in_crack_field_features = arcpy.Parameter()
    in_crack_field_features.value = os.path.join(in_workspace, 'Crack_like_Envelop_6_Oclock')

    in_crack_field_features_12 = arcpy.Parameter()
    in_crack_field_features_12.value = None

    in_crack_field_routeid_field = arcpy.Parameter()
    in_crack_field_routeid_field.value = 'NETWORK_ROUTE_ID'

    # in_crack_field_measure_field = arcpy.Parameter()
    # in_crack_field_measure_field.value = 'Measure'

    in_dent_features = arcpy.Parameter()
    in_dent_features.value = os.path.join(in_workspace, 'Dent_Ellipse_6_Oclock')

    in_dent_features_12 = arcpy.Parameter()
    in_dent_features_12.value = None

    in_dent_routeid_field = arcpy.Parameter()
    in_dent_routeid_field.value = 'NETWORK_ROUTE_ID'

    # in_dent_measure_field = arcpy.Parameter()
    # in_dent_measure_field.value = 'Measure'

    in_dent_depth_pct_field = arcpy.Parameter()
    in_dent_depth_pct_field.value = 'DENT_DEPTH_PERCENT'

    in_dent_clockpos_field = arcpy.Parameter()
    in_dent_clockpos_field.value = 'CLOCK_POSITION'

    in_gouge_features = arcpy.Parameter()
    in_gouge_features.value = os.path.join(in_workspace, "Gouge_Ellipse_6_Oclock")

    in_gouge_features_12 = arcpy.Parameter()
    in_gouge_features_12.value = None

    in_gouge_routeid_field = arcpy.Parameter()
    in_gouge_routeid_field .value= "NETWORK_ROUTE_ID"

    # in_gouge_measure_field = arcpy.Parameter()
    # in_gouge_measure_field.value = None

    in_weld_features = arcpy.Parameter()
    in_weld_features.value = os.path.join(in_workspace, 'Weld_6_Oclock')

    in_weld_features_12 = arcpy.Parameter()
    in_weld_features_12.value = None

    in_weld_routeid_field = arcpy.Parameter()
    in_weld_routeid_field.value = 'NETWORK_ROUTE_ID'

    # in_weld_measure_field = arcpy.Parameter()
    # in_weld_measure_field.value = 'PODSMeasure'

    in_seam_features = arcpy.Parameter()
    in_seam_features.value = os.path.join(in_workspace, 'Seam_6_Oclock')

    in_seam_features_12 = arcpy.Parameter()
    in_seam_features_12.value = None

    in_seam_routeid_field = arcpy.Parameter()
    in_seam_routeid_field.value = 'NETWORK_ROUTE_ID'

    # in_seam_begin_measure_field = arcpy.Parameter()
    # in_seam_begin_measure_field.value = 'PODSMeasure'
    #
    # in_seam_end_measure_field = arcpy.Parameter()
    # in_seam_end_measure_field.value = 'PODSMeasure'

    in_bend_features = arcpy.Parameter()
    in_bend_features.value = os.path.join(in_workspace,"Bend_6_Oclock")

    in_bend_features_12 = arcpy.Parameter()
    in_bend_features_12.value = None

    in_bend_routeid_field = arcpy.Parameter()
    in_bend_routeid_field.value = "NETWORK_ROUTE_ID"

    # in_bend_measure_field = arcpy.Parameter()
    # in_bend_measure_field.value = None

    in_hsa_features = arcpy.Parameter()
    in_hsa_features.value = None

    in_hsa_features_12 = arcpy.Parameter()
    in_hsa_features_12.value = None

    in_hsa_routeid_field = arcpy.Parameter()
    in_hsa_routeid_field.value = None

    in_search_distance = arcpy.Parameter()
    in_search_distance.value = '0.33 Feet'

    in_pipe_type = arcpy.Parameter()
    in_pipe_type.value = 'Liquid Pipeline'

    target_anomaly_features = arcpy.Parameter()
    target_anomaly_features.value = os.path.join(in_workspace,"Anomaly_Ellipse_12_Oclock")

    target_anomaly_routeid_field = arcpy.Parameter()
    target_anomaly_routeid_field.value = "NETWORK_ROUTE_ID"

    target_anomaly_id_field = arcpy.Parameter()
    target_anomaly_id_field.value = "UNIQUE_ID"

    out_anomaly_priority_field = arcpy.Parameter()
    out_anomaly_priority_field.value = 'ANOMALY_PRIORITY'

    parameters = []

    parameters += [in_ili_features, in_ili_features_12, in_pipe_routeid_field, in_pipe_depth_pct_field, in_pipe_clockpos_field,
                   in_pipe_maop_field, in_pipe_burstpressure_field, in_pipe_safepressure_field, in_pipe_erf_field]
    parameters += [in_crack_features, in_crack_features_12, in_crack_routeid_field]
    parameters += [in_crack_field_features, in_crack_field_features_12, in_crack_field_routeid_field]
    parameters += [in_dent_features, in_dent_features_12, in_dent_routeid_field, in_dent_depth_pct_field, in_dent_clockpos_field]
    parameters += [in_gouge_features, in_gouge_features_12, in_gouge_routeid_field]
    parameters += [in_weld_features, in_weld_features_12, in_weld_routeid_field]
    parameters += [in_seam_features, in_seam_features_12, in_seam_routeid_field]
    parameters += [in_bend_features, in_bend_features_12, in_bend_routeid_field]
    parameters += [in_hsa_features, in_hsa_features_12, in_hsa_routeid_field]
    parameters += [in_search_distance, in_pipe_type]
    parameters += [target_anomaly_features, target_anomaly_routeid_field, target_anomaly_id_field]
    parameters += [out_anomaly_priority_field]

    from inlineinspection.anomalyprioritizer.anomalyprioritizer import AnomalyPrioritizer

    ap = AnomalyPrioritizer()
    ap.execute(parameters, None)


except Exception as e:
    arcpy.AddMessage(e)