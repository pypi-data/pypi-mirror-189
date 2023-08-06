#import arcpy

from pimsilitool.pressurecalculator.pressurecalculator import PressureCalculator
from pimsilitool.anomalygrowthcalculator.anomalygrowthcalculator import AnomalyGrowthCalculator
from pimsilitool.anomalyconverter.anomalyconverter import AnomalyConverter
from pimsilitool.anomalycomparer.anomalycomparer import AnomalyComparer
from pimsilitool.anomalyprioritizer.anomalyprioritizer import AnomalyPrioritizer
from pimsilitool.digsheetlayout.digsheetlayout import DigSheetLayout

from pimsilitool.license.toolbox.license_manager import RequestLicense, RegisterLicense
# from pimsilitool.license.toolbox.check_tokens import CheckAvailableTokens
from pimsilitool.license.validate_license.license_operation import LicenseOperation


class Toolbox(object):

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        lm = LicenseOperation()
        lm.validate_license()

        self.label = "PIMS ILI Data Integration Tools"
        self.alias = "pimsilitool"

        # List of tool classes associated with this toolbox
        self.tools = [PressureCalculator,
                      AnomalyConverter,
                      AnomalyComparer,
                      AnomalyGrowthCalculator,
                      AnomalyPrioritizer,
                      DigSheetLayout,
                      RequestLicense,
                      RegisterLicense
                      ]
