import arcpy
import os

try:
    # in_workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Packages\PIMS ILI Demo_473068\p20\scratch.gdb"
    in_workspace = r"C:\Users\surendra.pinjala\Documents\ArcGIS\Projects\DigSheetLayout\PODS7_NEW.gdb"

    in_ili_features = arcpy.Parameter()
    in_ili_features.value = os.path.join(in_workspace, "ANOMALY_ILI")

    in_pc_length_field = arcpy.Parameter()
    in_pc_length_field.value = "LENGTH_INCH"

    in_pc_MaxDepthMeasured_field = arcpy.Parameter()
    in_pc_MaxDepthMeasured_field.value = "METAL_LOSS_DEPTH_PERCENT"

    in_pc_MeasuredWallThickness_field = arcpy.Parameter()
    in_pc_MeasuredWallThickness_field.value = 'WALL_THICKNESS_INCH'

    in_diameter_source = arcpy.Parameter()
    in_diameter_source.value = "Diameter Value"
    in_diameter_features = arcpy.Parameter()
    in_diameter_features.value = None
    in_diameter_field = arcpy.Parameter()
    in_diameter_field.value = None
    in_diameter_value = arcpy.Parameter()
    in_diameter_value.value = 12.75

    in_smys_source = arcpy.Parameter()
    in_smys_source.value = "SMYS Value"
    in_smys_features = arcpy.Parameter()
    in_smys_features.value = None
    in_smys_field = arcpy.Parameter()
    in_smys_field.value = "SMYS_PSI"
    in_smys_value = arcpy.Parameter()
    in_smys_value.value = 52000

    in_maop_source = arcpy.Parameter()
    in_maop_source.value = "MAOP or MOP Value"
    in_maop_features = arcpy.Parameter()
    in_maop_features.value = None
    in_maop_field = arcpy.Parameter()
    in_maop_field.value = None
    in_maop_value = arcpy.Parameter()
    in_maop_value.value = 1250

    in_design_factor_source = arcpy.Parameter()
    in_design_factor_source.value = "Design Factor Value"
    in_design_factor_features = arcpy.Parameter()
    in_design_factor_features.value = None
    in_design_factor_field = arcpy.Parameter()
    in_design_factor_field.value = "DESIGN_FACTOR"
    in_design_factor_value = arcpy.Parameter()
    in_design_factor_value.value = 0.72


    in_pc_pipeBurstPressure_field = arcpy.Parameter()
    in_pc_pipeBurstPressure_field.value = 'PIPE_BURST_PRESSURE'
    in_pc_calculatePressure_field = arcpy.Parameter()
    in_pc_calculatePressure_field.value = "CALCULATED_SAFE_PRESSURE"
    in_pc_safetyFactor_field = arcpy.Parameter()
    in_pc_safetyFactor_field.value = "SAFETY_FACTOR"
    in_pc_pressureReferencedRatio_field = arcpy.Parameter()
    in_pc_pressureReferencedRatio_field.value = 'PRESSURE_REFERENCE_RATIO'
    in_pc_estimatedRepairFactor_field = arcpy.Parameter()
    in_pc_estimatedRepairFactor_field.value = "ESTIMATED_REPAIR_FACTOR"
    in_pc_rupturePressureRatio_field = arcpy.Parameter()
    in_pc_rupturePressureRatio_field.value = "RUPTURE_PRESSURE_RATIO"
    in_pc_modPipeBurstPressure_field = arcpy.Parameter()
    in_pc_modPipeBurstPressure_field.value = 'MOD_PIPEBURST_PRESSURE'
    in_pc_modCalculatePressure_field = arcpy.Parameter()
    in_pc_modCalculatePressure_field.value = "MOD_CALCULATED_SAFE_PRESSURE"
    in_pc_modSafetyFactor_field = arcpy.Parameter()
    in_pc_modSafetyFactor_field.value = "MOD_SAFETY_FACTOR"
    in_pc_modPressureReferencedRatio_field = arcpy.Parameter()
    in_pc_modPressureReferencedRatio_field.value = 'MOD_PRESSURE_REFERENCE_RATIO'
    in_pc_modEstimatedRepairFactor_field = arcpy.Parameter()
    in_pc_modEstimatedRepairFactor_field.value = "MOD_ESTIMATED_REPAIR_FACTOR"
    in_pc_modRupturePressureRatio_field = arcpy.Parameter()
    in_pc_modRupturePressureRatio_field.value = 'MOD_RUPTURE_PRESSURE_RATIO'

    in_pc_outside_diameter_field = arcpy.Parameter()
    in_pc_outside_diameter_field.value = "OUTSIDE_DIAMETER"
    in_pc_smys_field = arcpy.Parameter()
    in_pc_smys_field.value = "MATERIAL_SMYS"

    in_pc_referencePressure_field = arcpy.Parameter()
    in_pc_referencePressure_field.value = "REFERENCE_PRESSURE"
    in_pc_designFactor_field = arcpy.Parameter()
    in_pc_designFactor_field.value = "DESIGN_FACTOR"



    parameters = []

    parameters += [in_ili_features, in_pc_length_field, in_pc_MaxDepthMeasured_field, in_pc_MeasuredWallThickness_field]
    parameters += [in_diameter_source, in_diameter_features, in_diameter_field, in_diameter_value]
    parameters += [in_smys_source, in_smys_features, in_smys_field, in_smys_value]
    parameters += [in_maop_source, in_maop_features, in_maop_field, in_maop_value]
    parameters += [in_design_factor_source, in_design_factor_features, in_design_factor_field, in_design_factor_value]
    parameters += [in_pc_pipeBurstPressure_field, in_pc_calculatePressure_field]
    parameters += [in_pc_safetyFactor_field, in_pc_pressureReferencedRatio_field, in_pc_estimatedRepairFactor_field, in_pc_rupturePressureRatio_field]
    parameters += [in_pc_modPipeBurstPressure_field, in_pc_modCalculatePressure_field, in_pc_modSafetyFactor_field, in_pc_modPressureReferencedRatio_field]
    parameters += [in_pc_modEstimatedRepairFactor_field, in_pc_modRupturePressureRatio_field]
    parameters += [in_pc_outside_diameter_field, in_pc_smys_field, in_pc_referencePressure_field,  in_pc_designFactor_field]


    from inlineinspection.pressurecalculator.pressurecalculator import PressureCalculator

    pc = PressureCalculator()
    pc.execute(parameters, None)


except Exception as e:
    arcpy.AddMessage(e)