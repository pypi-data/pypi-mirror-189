import arcpy
from pimsilitool.license.validate_license.license_operation import LicenseOperation
import os
import pimsilitool
from pimsilitool import config
import numpy


class CheckAvailableTokens(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Check Token Availability"
        self.description = "Checks available tokens for PIMS ILI Integration Tool"
        self.category = "License"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        in_ospointm_features = arcpy.Parameter(
            displayName="Input Release Point Features", name="in_ospointm_features",
            datatype="GPFeatureLayer", parameterType="Required",
            direction="Input")
        in_ospointm_features.filter.list = ['Point']

        tool_status = arcpy.Parameter(
            displayName="Tool Status",
            name="tool_status",
            datatype="GPBoolean",
            parameterType="Derived",
            direction="Output")

        params = [in_ospointm_features,  tool_status ]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        return

    def execute(self, parameters, messages):
        try:
            # gdb_path = os.path.join(os.getenv('LOCALAPPDATA') + "\\License.gdb")
            # pdb = ProjectDatabase.create_db(gdb_path)
            arcpy.AddMessage("Checking required tokens...")

            ospointm_feature_class = parameters[0].value

            # check if user has required tokens to run the tool
            lo = LicenseOperation()
            available_tokens = int(lo.get_available_tokens())
            run_points = pimsilitool.get_license_run_points()
            required_tokes = 0
            release_points = 0

            points = arcpy.da.FeatureClassToNumPyArray(
                parameters[0].value,
                ["SHAPE@X", "SHAPE@Y", config.POINT_ID_FIELD, config.ROUTE_ID_FIELD, config.ORIGINAL_ROUTE_ID_FIELD],
                spatial_reference=arcpy.SpatialReference(config.WEB_MERCATOR_WKID))
            points = numpy.sort(points, order=config.ROUTE_ID_FIELD)

            if arcpy.Exists(ospointm_feature_class):
                release_points = int(arcpy.GetCount_management(parameters[0].value)[0])
                if int(arcpy.GetCount_management(parameters[0].value)[0]) > 0:
                    for i, point in enumerate(points):
                        use_token = pimsilitool.check_point_run(run_points, point[4], point[3], point[2])
                        if use_token:
                            required_tokes += 1

            else:
                pimsilitool.AddError("Input Release Points feature class does not exist.")
                return


            arcpy.AddMessage("=============================================================")
            arcpy.AddMessage("Total available tokens: {}".format(str(available_tokens)))
            arcpy.AddMessage("Total release points: {}".format(str(release_points)))
            arcpy.AddMessage("Release points ran in last {} days: {}".format(config.TOKEN_USE_TIME_DAYS, str(release_points - required_tokes)))
            arcpy.AddMessage("Total required tokens to run the input release points: {}".format(str(required_tokes)))
            arcpy.AddMessage("=============================================================")

            if available_tokens < required_tokes:
                parameters[1].value = False
            else:
                parameters[1].value = True

            return

        except Exception as inst:
            raise




