#import arcpy

from inlineinspection.pressurecalculator.pressurecalculator import PressureCalculator
from inlineinspection.anomalygrowthcalculator.anomalygrowthcalculator import AnomalyGrowthCalculator
from inlineinspection.anomalyconverter.anomalyconverter import AnomalyConverter
from inlineinspection.anomalycomparer.anomalycomparer import AnomalyComparer
from inlineinspection.anomalyprioritizer.anomalyprioritizer import AnomalyPrioritizer
from inlineinspection.digsheetlayout.digsheetlayout import DigSheetLayout

class Toolbox(object):

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""

        self.label = "PIMS ILI Data Integration Tools"
        self.alias = "inlineinspection"

        # List of tool classes associated with this toolbox
        self.tools = [PressureCalculator, AnomalyConverter, AnomalyComparer,
                      AnomalyGrowthCalculator, AnomalyPrioritizer, DigSheetLayout
                      ]
