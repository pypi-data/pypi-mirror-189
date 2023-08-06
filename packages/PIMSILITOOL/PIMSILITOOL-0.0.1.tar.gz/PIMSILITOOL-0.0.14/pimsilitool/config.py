"""
A collection of default settings that are used throughout the PIMS system.
These can be overridden by using a
config file.
"""

# ************ Convert ILI Anomalies to Point, Envelope and Ellipse features *************

CONVERT_ILI_CATEGORY_METAL_LOSS_ANOMALY = "ILI Metal Loss Anomaly Parameters"
CONVERT_ILI_CATEGORY_DEFAULT_VALUES = "Default Values"
CONVERT_ILI_CATEGORY_GRID_LINES = "Grid Lines Parameters"
CONVERT_ILI_CATEGORY_CRACK_LIKE = "Crack or Crack-like Features"
CONVERT_ILI_CATEGORY_CRACK_FIELD = "ILI Crack Field Parameters"
CONVERT_ILI_CATEGORY_DENT = "ILI Dent Parameters"
CONVERT_ILI_CATEGORY_GOUGE = "ILI Gouge Parameters"
CONVERT_ILI_CATEGORY_WELD_LINES = "Generate Weld Lines"
CONVERT_ILI_CATEGORY_SEAM_LINES = "Generate Seam Lines"
CONVERT_ILI_CATEGORY_BEND = "ILI Bend Parameters"
CONVERT_ILI_CATEGORY_HSA = "ILI High Consequence Areas Parameters"
CONVERT_ILI_CATEGORY_OUTPUT = "Output"

CONVERT_ILI_ANOM_CLOCK_POSITION = ["ILI Anomaly Matching Layers (6:00 Centered Versions)",
                           "ILI Anomaly Matching Layers (12:00 Centered Versions)"]
CONVERT_ILI_OUTPUT_NAME_SUFFIX_6_CLOCK = "_6_Oclock"
CONVERT_ILI_OUTPUT_NAME_SUFFIX_12_CLOCK = "_12_Oclock"

CONVERT_ILI_ANOMALY_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "WIDTH_INCH",
                                  "LENGTH_INCH",
                                  "CLOCK_POSITION"
                                  ]

CONVERT_ILI_CRACK_LIKE_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "WIDTH_INCH",
                                  "LENGTH_INCH",
                                  "CLOCK_POSITION"
                                  ]

CONVERT_ILI_CRACK_FIELD_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "WIDTH_INCH",
                                  "LENGTH_INCH",
                                  "CLOCK_POSITION"
                                  ]


CONVERT_ILI_DENT_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "WIDTH_INCH",
                                  "LENGTH_INCH",
                                  "CLOCK_POSITION"
                                  ]

CONVERT_ILI_GOUGE_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "WIDTH_INCH",
                                  "LENGTH_INCH",
                                  "CLOCK_POSITION"
                                  ]

CONVERT_ILI_WELD_LINES_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE"
                                  ]

CONVERT_ILI_SEAM_LINES_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "CLOCK_POSITION"
                                  ]

CONVERT_ILI_PIPE_BEND_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "MEASURE",
                                  "FROM_MEASURE",
                                  "TO_MEASURE"
                                  ]

CONVERT_ILI_HSA_FIELDS = [#"NETWORK_ROUTE_ID",
                                  "FROM_MEASURE",
                                  "TO_MEASURE"
                                  ]

CONVERT_ILI_OUTPUT_ANOMALY_NAMES = ["Anomaly_Point",
                                    "Anomaly_Ellipse",
                                    "Anomaly_Envelop"
                                    ]
CONVERT_ILI_OUTPUT_GRID_NAMES = ["Grid_Lines"]

CONVERT_ILI_OUTPUT_CRACK_LIKE_NAMES = ["Crack_like_Point",
                                       "Crack_like_Ellipse",
                                       "Crack_like_Envelop"
                                       ]
CONVERT_ILI_OUTPUT_CRACK_FIELD_NAMES = ["Crack_Field_Point",
                                        "Crack_Field_Ellipse",
                                        "Crack_Field_Envelop"
                                        ]
CONVERT_ILI_OUTPUT_DENT_NAMES = ["Dent_Point",
                                 "Dent_Ellipse",
                                 "Dent_Envelop"
                                 ]
CONVERT_ILI_OUTPUT_GOUGE_NAMES = ["Gouge_Point",
                                  "Gouge_Ellipse",
                                  "Gouge_Envelop"
                                  ]
CONVERT_ILI_OUTPUT_WELD_NAMES = ["Weld_Lines"]
CONVERT_ILI_OUTPUT_SEAM_NAMES = ["Seam_Lines"]
CONVERT_ILI_OUTPUT_BEND_NAMES = ["Bends"]
CONVERT_ILI_OUTPUT_HCA_NAMES = ["HCA"]

CONVERT_ILI_PIPETALLY_VIEW_FIELDS = [ ["AnomalyXCoord", "DOUBLE", "AnomalyXCoord", None],
                                      ["AnomalyYCoord", "DOUBLE", "AnomalyYCoord", None],
                                      ["AnomalyMajorAxisFt", "DOUBLE", "AnomalyMajorAxisFt", None],
                                      ["AnomalyMinorAxisFt", "DOUBLE", "AnomalyMinorAxisFt", None],
                                      ["Azimuth", "DOUBLE", "Azimuth", None]
                                      ]

# ************ ILI Anomaly Pressure Calculator *************

PRESSURE_CALCULATOR_TOOL_LABEL ='ILI Anomaly Pressure Calculator'
PRESSURE_CALCULATOR_TOOL_DESC = 'Performs Pressure Calculations for ILI'

PRESSURE_CALCULATOR_CATEGORY_ANOMALY = "Input ILI Anomaly Data Parameters"
PRESSURE_CALCULATOR_CATEGORY_PIPE_DATA = "Input Pipe Data Fields"
PRESSURE_CALCULATOR_CATEGORY_OUTPUT_FIELDS = "Output Calculated ILI Fields"

PRESSURE_CALCULATOR_ANOMALY_FIELDS = ["LENGTH_INCH",
                                    "METAL_LOSS_DEPTH_PERCENT",
                                    "WALL_THICKNESS_INCH"
                                    ]

PRESSURE_CALCULATOR_DIAMETER_SOURCE = ["Diameter Field",
                                        "Diameter Value",
                                        "Diameter Features"
                                        ]
PRESSURE_CALCULATOR_SMYS_SOURCE = ["SMYS Field",
                                    "SMYS Value",
                                    "SMYS Features"
                                    ]

PRESSURE_CALCULATOR_MAOP_SOURCE = ["MAOP or MOP Field",
                                    "MAOP or MOP Value",
                                    "MAOP or MOP Features"
                                    ]

PRESSURE_CALCULATOR_DESIGN_FACTOR_SOURCE = ["Design Factor Field",
                                             "Design Factor Value",
                                             "Design Factor Features"
                                             ]


PRESSURE_CALCULATOR_ADDING_FIELDS = ['PIPE_BURST_PRESSURE',
                                     'CALCULATED_SAFE_PRESSURE',
                                     'SAFETY_FACTOR',
                                     'PRESSURE_REFERENCE_RATIO',
                                     'ESTIMATED_REPAIR_FACTOR',
                                     'RUPTURE_PRESSURE_RATIO',
                                     'MOD_PIPEBURST_PRESSURE',
                                     'MOD_CALCULATED_SAFE_PRESSURE',
                                     'MOD_SAFETY_FACTOR',
                                     'MOD_PRESSURE_REFERENCE_RATIO',
                                     'MOD_ESTIMATED_REPAIR_FACTOR',
                                     'MOD_RUPTURE_PRESSURE_RATIO',
                                     "OUTSIDE_DIAMETER",
                                     'MATERIAL_SMYS',
                                     'REFERENCE_PRESSURE',
                                     "DESIGN_FACTOR"
                                    ]

PRESSURE_CALCULATOR_OUTPUT_DIAMETER_FIELDNAME = "DIAM_SJ"
PRESSURE_CALCULATOR_OUTPUT_SYMS_FIELDNAME = "SMYS_SJ"
PRESSURE_CALCULATOR_UTPUT_MAOP_FIELDNAME ="MAOP_SJ"
PRESSURE_CALCULATOR_OUTPUT_DESIGN_FACTOR_FIELDNAME ="DF_SJ"

PRESSURE_CALCULATOR_OUTPUT_TEMP_FIELDS = [["DIAM_SJ", "DOUBLE", "DIAM_SJ", None],
                                            ["SMYS_SJ", "DOUBLE", "SMYS_SJ", None],
                                            ["MAOP_SJ", "DOUBLE", "MAOP_SJ", None],
                                            ["DF_SJ", "DOUBLE", "DF_SJ", None ]
                                          ]
PRESSURE_CALCULATOR_TEMP_FOLDER = "ILI_TEMP"
PRESSURE_CALCULATOR_TEMP_GDB = "ILI_TEMP_GDB.gdb"


# ************ ILI Anomaly Matching/comparer *************

ANOMALY_MATCHING_CLOCK_POSITION = ["ILI Anomaly Matching Layers (6:00 Centered Versions)",
                                   "ILI Anomaly Matching Layers (12:00 Centered Versions)"
                                   ]

ANOMALY_MATCHING_ANOMALY_FIELDS = ["UNIQUE_ID"
                                  ]

ANOMALY_MATCHING_OUTPUT_TABLE_NAME = "ANOMALY_MATCHES"

ANOMALY_MATCHING_SQLITE_DB_NAME = "AnamolyCompare.sqlite"

ANOMALY_MATCHING_NEAR_TABLE_NAMES = ["NearTable_Prev_to_Curr_clock_12",
                                    "NearTable_Prev_to_Curr_clock_6"
                                    ]
# ANOMALY_MATCHING_JOIN_TABLE_NAMES = ["JoinTable_Prev_to_Curr_clock_12",
#                                     "JoinTable_Prev_to_Curr_clock_6"
#                                     ]
# ANOMALY_MATCHING_DUPLICATE_ROWS = "DuplicateRows_Prev_to_Curr"


# ************ ILI Anomaly Growth calculator *************

ANOMALY_GROWTH_CATEGORY_ANOMALY_MATCHES = "Anomaly Matches Parameters"
ANOMALY_GROWTH_CATEGORY_PARENT_FEATURES = "ILI Anomaly Parent Features Parameters"
ANOMALY_GROWTH_CATEGORY_CHILD_FEATURES = "ILI Anomaly Child Features Parameters"
ANOMALY_GROWTH_CATEGORY_DEFAULT = "Default Parameters"
ANOMALY_GROWTH_CATEGORY_OUTPUT = "Output"



ANOMALY_GROWTH_ANOMALY_FIELDS = ["UNIQUE_ID",
                                 "METAL_LOSS_DEPTH_PERCENT"
                                  ]

ANOMALY_GROWTH_CALC_DIRECTION = ["Calculate statistics for child anomalies",
                                "Calculate statistics for parent anomalies"
                                ]

ANOMALY_GROWTH_OUTPUT_TABLE_NAME = "ANOMALY_GROWTH"
ANOMALY_GROWTH_OUTPUT_UNMATCHED_TABLE_NAME = "UNMATCHED_CHILD_ANOMALY_GROWTH"


# ************ Anomaly Prioritizer *************

ANOMALY_PRIORITY_CATEGORY_ANOMALY = "ILI Metal Loss Anomaly Parameters"
ANOMALY_PRIORITY_CATEGORY_CRACK_LIKE = "ILI Crack or Crack-like Parameters"
ANOMALY_PRIORITY_CATEGORY_CRACK_FIELD = "ILI Crack Field Parameters"
ANOMALY_PRIORITY_CATEGORY_DENT = "ILI Dent Parameters"
ANOMALY_PRIORITY_CATEGORY_GOUGE = "ILI Gouge Parameters"
ANOMALY_PRIORITY_CATEGORY_WELD = "ILI Weld Parameters"
ANOMALY_PRIORITY_CATEGORY_SEAM = "ILI Seam Parameters"
ANOMALY_PRIORITY_CATEGORY_BEND = "ILI Bend Parameters"
ANOMALY_PRIORITY_CATEGORY_HCA = "Highly Sensitive Areas Parameters"
ANOMALY_PRIORITY_CATEGORY_DEFAULT = "Default Values"
ANOMALY_PRIORITY_CATEGORY_TARGET_ANOMALY = "Target Anamoly Features Parameters"
ANOMALY_PRIORITY_CATEGORY_OUTPUT = "Output Anamoly Priority Parameters"


ANOMALY_PRIORITY_ANOMALY_FIELDS = ["NETWORK_ROUTE_ID",
                                    "METAL_LOSS_DEPTH_PERCENT",
                                    "CLOCK_POSITION",
                                    "REFERENCE_PRESSURE",
                                    "PIPE_BURST_PRESSURE",
                                    "CALCULATED_SAFE_PRESSURE",
                                    "ESTIMATED_REPAIR_FACTOR"
                                  ]

ANOMALY_PRIORITY_CRACK_LIKE_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_CRACK_FIELD_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]


ANOMALY_PRIORITY_DENT_FIELDS = ["NETWORK_ROUTE_ID",
                                  "DENT_DEPTH_PERCENT",
                                  "CLOCK_POSITION"
                                  ]

ANOMALY_PRIORITY_GOUGE_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_WELD_LINES_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_SEAM_LINES_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_PIPE_BEND_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_HSA_FIELDS = ["NETWORK_ROUTE_ID"
                                  ]

ANOMALY_PRIORITY_TARGET_ANOMALY_FIELDS = ["NETWORK_ROUTE_ID",
                                          "UNIQUE_ID"
                                  ]

ANOMALY_PRIORITY_DEFAULT_PIPELINE_TYPES = ['Liquid Pipeline',
                                           'Gas Pipeline'
                                           ]

ANOMALY_PRIORITY_OUTPUT_ANOMALY_PRIORITY_FIELD_NAME = "ANOMALY_PRIORITY"

ANOMALY_PRIORITY_SPATIAL_JOINS = ["Metal_Loss_Dent_SJ",
                                      "Metal_Loss_Bend_SJ",
                                      "Metal_Loss_HCA_SJ",
                                      "Metal_Loss_Weld_SJ",
                                      "Metal_Loss_Seam_SJ",
                                      "Dent_Crack_SJ",
                                      "Dent_Crack_Field_SJ",
                                      "Dent_Gouge_SJ",
                                      "Dent_Weld_SJ",
                                      "Dent_Seam_SJ",
                                      "Dent_Bend_SJ"
                                      ]

ANOMALY_PRIORITY_SPATIAL_JOINS_12 = ["Metal_Loss_Dent_SJ_12",
                                     "Metal_Loss_Bend_SJ_12",
                                     "Metal_Loss_HCA_SJ_12",
                                     "Metal_Loss_Weld_SJ_12",
                                     "Metal_Loss_Seam_SJ_12",
                                      "Dent_Crack_SJ_12",
                                     "Dent_Crack_Field_SJ_12",
                                     "Dent_Gouge_SJ_12",
                                     "Dent_Weld_SJ_12",
                                     "Dent_Seam_SJ_12",
                                     "Dent_Bend_SJ_12" ]

ANOMALY_PRIORITY_SPATIAL_JOIN_FIELD_MAP_PREFIX = ["MetalLoss_",
                                                  "CrackLike_",
                                                  "CrackField_",
                                                  "Dent_",
                                                  "Gouge_",
                                                  "Weld_",
                                                  "Seam_",
                                                  "Bend_",
                                                  "HSA_"]

# ************ Dig Sheet Layout *************

DIGSHEET_LAYOUT_DEFAULT_MIN_DIG_LENGTH = 65

DIGSHEET_LAYOUT_CATEGORY_ILI_METAL_LOSS_ANOMALY = "ILI Metal Loss Anomaly Parameters"
DIGSHEET_LAYOUT_CATEGORY_WELD_LINES = "Weld Lines Parameters"
DIGSHEET_LAYOUT_CATEGORY_RIGHT_OF_WAY = "Right of Way Layer Parameters"
DIGSHEET_LAYOUT_CATEGORY_OWNER_OPERATOR = "Owner Operator Layer Parameters"
DIGSHEET_LAYOUT_CATEGORY_DIG_SHEET_LAYOUT = "Dig Sheet Layout Parameters"
DIGSHEET_LAYOUT_CATEGORY_TARGET_ANOMALY = "Target Anomaly Layer Parameters"
DIGSHEET_LAYOUT_CATEGORY_INTERRUPT_FEATURES = "Dig Sheet Interruption Features Parameters"
DIGSHEET_LAYOUT_CATEGORY_ENG_STA_NETWORK_FEATURES = "Engineering Station Network Parameters"
DIGSHEET_LAYOUT_CATEGORY_DEFAULT_VALUES = "Default Values"

DIGSHEET_LAYOUT_REASON_VALUES = ["ILI Verification Dig",
                                 "Leak Report",
                                 "Unknown"
                                 ]
DIGSHEET_LAYOUT_STATUS_VALUES = ["Initialized",
                                 "Unknown"
                                 ]
DIGSHEET_LAYOUT_PRIORITY_VALUES = ["Immediate",
                                   "Monitored",
                                   "Scheduled",
                                   "Closed",
                                   "Unknown"
                                   ]
DIGSHEET_LAYOUT_PROJECT_NUMBER_VALUES = ["ABC123"]
DIGSHEET_LAYOUT_REVISION_NUMBER_VALUES = [1]

DIGSHEET_LAYOUT_ANOMALY_PRIORITY_TARGET_VALUE = "target"
DIGSHEET_LAYOUT_ANOMALY_PRIORITY_INFO_VALUE = "info"

DIGSHEET_LAYOUT_ANOMALY_FIELDS = ["NETWORK_ROUTE_ID",
                                  "UNIQUE_ID",
                                  "MEASURE",
                                  "DIG_SHEET_ID",
                                  "IS_DIG_TARGET_FEATURE",
                                  "ANOMALY_PRIORITY"
                                  ]
DIGSHEET_LAYOUT_GIRTH_WELD_FIELDS = ["NETWORK_ROUTE_ID",
                                      "UNIQUE_ID",
                                      "MEASURE"
                                      ]

DIGSHEET_LAYOUT_RIGHT_OF_WAY_FIELDS = ["FROM_NETWORK_ROUTE_ID",
                                      "FROM_MEASURE",
                                      "TO_NETWORK_ROUTE_ID",
                                      "TO_MEASURE",
                                      "LAND_OWNER"
                                      ]

DIGSHEET_LAYOUT_DIG_SHEET_FIELDS = ["FROM_NETWORK_ROUTE_ID",
                                    "FROM_MEASURE",
                                    "TO_NETWORK_ROUTE_ID",
                                    "TO_MEASURE",
                                    "UNIQUE_ID",
                                    "BEGIN_WELD_ID",
                                    "BEGIN_WELD_MEASURE",
                                    "END_WELD_ID",
                                    "END_WELD_MEASURE",
                                    "LAND_OWNER",
                                    "DIG_REASON",
                                    "DIG_STATUS",
                                    "DIG_PRIORITY",
                                    "DIG_SHEET_PROJECT_NUMBER",
                                    # "REVISION_NUMBER",
                                    "BEG_EXCV_LATITUDE",
                                    "BEG_EXCV_LONGITUDE",
                                    "END_EXCV_LATITUDE",
                                    "END_EXCV_LONGITUDE"
                                  ]

DIGSHEET_LAYOUT_DIG_INTERRUPT_FIELDS = ["NETWORK_ROUTE_ID",
                                        "UNIQUE_ID",
                                        "MEASURE",
                                        "ROAD_WIDTH"
                                        ]


DIGSHEET_LAYOUT_TARGET_ANOMALY_FIELDS = ["NETWORK_ROUTE_ID",
                                          "UNIQUE_ID",
                                          "DIG_SHEET_ID"
                                          ]

DIGSHEET_LAYOUT_ENG_STA_NETWORK_FIELDS = ["UNIQUE_ID",
                                           "FROM_MEASURE",
                                            "TO_MEASURE"
                                          ]
DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE = ["Crossing Width Field",
                                         "Crossing Width Value"
                                         ]

# ************ License *************

TOKEN_USE_TIME_DAYS = 365
LISENCE_TO_EMAIL = "licensing@g2-is.com"
ARCGIS_PRO_PYTHON_PATH = r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
