from pimsilitool.pressurecalculator.pressurecalculator import PressureCalculator
from pimsilitool.license.validate_license.license_operation import LicenseOperation
import os
import pimsilitool
from .pimsilitool import pimsilitoolLog
import arcpy
import datetime
# import uuid
from pimsilitool import config
import numpy
import pickle

params = ["FILE"]
_pimsilitool_log = pimsilitoolLog(params=params)


# logging procedures
def AddMessage(message):
    """Adds a string message to the current logging system or systems."""
    _pimsilitool_log.addMessage(message)


def AddWarning(message):
    """Adds a string warning to the current logging system or systems."""
    _pimsilitool_log.addWarning(message)


def AddError(message):
    """Adds a string error to the current logging system or systems."""
    _pimsilitool_log.addError(message)


def GetLogFileLocation():
    """Returns the current file that the logs are being written to."""
    return _pimsilitool_log.getLogFileLocation()


def SetLogFileLocation(fileLocation,delete=True):
    """Sets the log file to a new logging location.  If delete is true (default) the previous log file will be deleted first"""
    if GetLogFileLocation() is not None:
        if(os.path.exists(GetLogFileLocation()) and delete):
            os.remove(GetLogFileLocation())

    _eagleLog = pimsilitoolLog(file=fileLocation,params=["FILE","PRINT"])


def SetLogToARCPY(remove=False):
    """Adds the parameter "ARCPY" to the log object.  This ensures that logs are sent to arcpy.
    If remove is set to true (default is False) all other log types are rmoved, thus only arcpy.AddMessage is used."""
    if(remove):
        _pimsilitool_log.removeParam("FILE")
        _pimsilitool_log.removeParam("PRINT")
        _pimsilitool_log.removeParam("DB")
    _pimsilitool_log.addParam("ARCPY")

#end logging


def list_to_string(inlist):
    lststr = ", ".join(str(x) for x in inlist)
    return lststr


def get_utmfrom_point(inpoint):
    try:
        utmzone = str(int(inpoint.X + 186.0) // 6) + ('S' if (inpoint.Y < 0) else 'N')
        return ("WGS 1984 UTM Zone " + utmzone)

    except Exception as e:
        pimsilitool.AddError("Error getting UTM Zone.")
        raise

def check_int_value(in_val):
    try:
        value = int(in_val)
        return True
    except:
        return False

def get_gdb_name(workspace):
    try:
        dir_name = os.path.dirname(workspace)
        base_name = os.path.basename(workspace)
        base_name_no_gdb = base_name
        index = base_name.rfind(".")
        if index > 0:
            base_name_no_gdb = base_name[0:index]

        base_name_gdb = base_name_no_gdb + ".gdb"
        return  dir_name, base_name_gdb

    except Exception as e:
        pimsilitool.AddError("Failed to run get_gdb_name.")
        raise

def get_field_names(inlayer):
    # get the fields names (uppercase) list
    import arcpy
    try:
        return [f.name.upper() for f in arcpy.ListFields(inlayer)]
    except Exception as e:
        pimsilitool.AddError("Error getting fields names.")
        raise


# def unique_values(inlayer, infield):
#     import arcpy
#     with arcpy.da.SearchCursor(inlayer, [infield]) as cursor:
#         return sorted({int(row[0]) for row in cursor})

def get_unique_values(intable, infield):
    """
        Gets unique values in the table for given field name
        :param intable: input table
        :param infield: input field name
        :return: list of unique values
    """
    import arcpy
    try:
        with arcpy.da.SearchCursor(intable, [infield]) as cursor:
            return sorted({row[0] for row in cursor})

    except Exception as e:
        pimsilitool.AddError("Failed to process {}. \n{} ".format("get_unique_values", arcpy.GetMessages(2)))
        raise

def get_available_tokens():
    try:
        # check available tokens
        license_operation = LicenseOperation()
        available_tokens = int(license_operation.get_available_tokens())

        return available_tokens
    except:
        pimsilitool.AddError("Error: getting available tokens from the license server failed.")
        raise


def unpickle_file(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


def get_appdata_roaming_dir():
    try:
        appdata_dir = os.getenv('APPDATA')
        g2is_dir = os.path.join(appdata_dir, "G2-IS")
        pimsilitool_dir = os.path.join(g2is_dir, "PIMS_ILI_Integration")
        if not os.path.exists(g2is_dir):
            os.makedirs(g2is_dir)
            os.makedirs(pimsilitool_dir)
        else:
            if not os.path.exists(pimsilitool_dir):
                os.makedirs(pimsilitool_dir)
        return pimsilitool_dir

    except:
        raise


def create_license_usage_files():
    try:
        in_dir = get_appdata_roaming_dir()

        run_points_file = os.path.join(in_dir, "pims_ili_run_points.pkl")
        token_usage_file = os.path.join(in_dir, "pims_ili_token_usage.pkl")

        if not os.path.exists(run_points_file):
            open(run_points_file, "x")

        if not os.path.exists(token_usage_file):
            open(token_usage_file, "x")

    except Exception as e:
        raise


def get_license_run_points():
    try:
        in_dir = get_appdata_roaming_dir()

        run_points_file = os.path.join(in_dir, "pims_ili_run_points.pkl")
        run_points = []
        if os.path.exists(run_points_file):
            run_points = list(unpickle_file(run_points_file))
        else:
            open(run_points_file, "x")

        return run_points

    except Exception as e:
        raise


def check_point_run(run_points, orig_route_id, route_id, point_id):
    try:
        if len(run_points) < 1:
            return True
        arr = numpy.array(run_points)
        run_pt = arr[(arr["POINT_ID"] == point_id) &
                            (arr["ROUTE_ID"] == route_id) &
                            (arr["ORIGINAL_ROUTE_ID"] == orig_route_id)]

        if len(run_pt) > 0:
            status = numpy.sort(run_pt["STATUS"])[::-1][0]
            dt = numpy.sort(run_pt["RUN_DATE"])[::-1][0]
            days = (numpy.datetime64(datetime.datetime.now()) - dt).astype('timedelta64[D]')
            if days.astype(int) <= config.TOKEN_USE_TIME_DAYS and status == "Completed":
                return False
            else:
                return True
        return True

    except Exception as e:
        raise


def insert_to_run_points_license_file(run_points, run_id, user_name, orig_route_id, route_id, point_id, status, run_date):
    try:
        run_id = '{' + str(run_id) + '}'
        run_points.append(
                        numpy.array([(str(run_id), user_name, orig_route_id, route_id, point_id, status, run_date)],
                        dtype=[('RUN_ID', 'U40'),  ('USER_NAME', 'U50'), ('ORIGINAL_ROUTE_ID', 'U50'), ('ROUTE_ID', 'i'),
                                ('POINT_ID', 'U27'),  ('STATUS', 'U50'), ('RUN_DATE', 'M8[us]') ]))
        return run_points

    except Exception as e:
        raise


def insert_to_token_usage_license_file(run_id, user_name, orig_route_id, route_id, cnt_points,  used_tokens, rem_tokens, tool_name, run_date):
    try:
        run_id = '{' + str(run_id) + '}'
        token_usage = []
        token_usage.append(
            numpy.array([(str(run_id),  user_name, orig_route_id,  route_id, cnt_points,  used_tokens, rem_tokens, tool_name, run_date)],
                   dtype=[('RUN_ID', 'U50'), ('USER_NAME', 'U50'), ('ORIGINAL_ROUTE_ID', 'U50'), ('ROUTE_ID', 'i'),
                          ('RUN_POINTS', 'i'), ('TOKENS_USED', 'i'),  ('REM_TOKENS', 'i'), ('TOOL_NAME', 'U50'), ('RUN_DATE', 'M8[us]') ]))

        return token_usage

    except Exception as e:
        raise


def write_to_run_points_license_file(run_points):
    try:
        in_dir = get_appdata_roaming_dir()
        run_points_file = os.path.join(in_dir, "pims_ili_run_points.pkl")
        with open(run_points_file, "wb") as f:
            pickle.dump(run_points, f)

    except Exception as e:
        raise


def write_to_token_usage_license_file(token_usage):
    try:
        in_dir = get_appdata_roaming_dir()
        token_usage_file = os.path.join(in_dir, "pims_ili_token_usage.pkl")
        with open(token_usage_file, "ab") as f:
            pickle.dump(token_usage, f)
    except Exception as e:
        raise


def get_point_run_status(run_points, orig_route_id, route_id, point_id):
    try:
        if len(run_points) > 0 and len(run_points[0]) > 0:

            arr = numpy.array(run_points)
            if arr.size > 0:
                run_pt = arr[(arr["POINT_ID"] == point_id) &
                             (arr["ROUTE_ID"] == route_id) &
                             (arr["ORIGINAL_ROUTE_ID"] == orig_route_id)]

                if len(run_pt) > 0:
                    status = numpy.sort(run_pt, order="RUN_DATE")[::-1][0]["STATUS"]
                    run_id = numpy.sort(run_pt, order="RUN_DATE")[::-1][0]["RUN_ID"]
                    run_date = numpy.sort(run_pt, order="RUN_DATE")[::-1][0]["RUN_DATE"]
                    days = (numpy.datetime64(datetime.datetime.now()) - run_date).astype('timedelta64[D]')

                    if days.astype(int) <= config.TOKEN_USE_TIME_DAYS and status == "Completed":
                        return False, run_id, run_date
                    else:
                        return True, run_id, run_date
                else:
                    return True, None, None

        else:
            return True, None, None

    except Exception as e:
        raise


def remove_from_run_points(run_points, runid, orig_route_id, route_id, point_id, check_days):
    try:
        index = -1
        if len(run_points) > 0 and len(run_points[0]) > 0:
            for index, pt in enumerate(run_points[0]):
                if runid is not None:
                    if pt["POINT_ID"] == point_id and pt["ROUTE_ID"] == route_id and pt["ORIGINAL_ROUTE_ID"] == orig_route_id and pt["RUN_ID"] == runid:
                        break
            if index > -1:
                # check if run date is more than 30 days
                if check_days:
                    dt = run_points[0][index][0]["RUN_DATE"]
                    days = (numpy.datetime64(datetime.datetime.now()) - dt).astype('timedelta64[D]')
                    if days.astype(int) > config.TOKEN_USE_TIME_DAYS:
                        run_points[0].pop(index)
                else:
                    run_points[0].pop(index)

        return run_points

    except Exception as e:
        raise


def update_case_status_ospointm(case_name_status, ospointmlayer):
    try:
        arr = numpy.array(case_name_status)
        pimsilitool.AddMessage("Updating OSANALYSIS...")
        whereclause = "1 = 1"

        with arcpy.da.UpdateCursor(in_table=ospointmlayer,
                                   field_names=["POINT_ID", "OSANALYSIS"],
                                   where_clause=whereclause) as cursor:
            for row in cursor:
                osanalysis = arr[arr["case_name"] == row[0]]
                if osanalysis:
                    row[1] = osanalysis["osanalysis"][0]
                    cursor.updateRow(row)

        pimsilitool.AddMessage("Done Updating OSANALYSIS.")

    except Exception as e:
        raise


def update_token_usage_ospointm(case_name_status, points, tool_name):
    try:
        import uuid
        # check available tokens
        available_tokens = pimsilitool.get_available_tokens()

        run_points = pimsilitool.get_license_run_points()

        used_tokens = 0
        checkout_tokens = 0
        prev_route_id = None
        prev_orig_route_id = None
        prev_point_id = None
        orig_route_id = None
        route_id  = None
        point_id = None
        token_usage = []
        run_id_new = uuid.uuid4()
        run_date_new = datetime.datetime.now()
        run_points_new = []
        run_points_removed = []
        user_name = os.getlogin()
        # run_id = None
        status = "Completed"
        # run_date = datetime.datetime,numpy

        license_operation = LicenseOperation()
        for i, case in enumerate(case_name_status):
            case_name = case["case_name"][0]
            case_status = case["osanalysis"][0]

            if case_status == "Finished":

                point = points[points[config.POINT_ID_FIELD] == case_name][0]
                orig_route_id = point[config.ORIGINAL_ROUTE_ID_FIELD]
                route_id = point[config.ROUTE_ID_FIELD]
                point_id = point[config.POINT_ID_FIELD]

                # *****************Token update**********************************************
                use_token, run_id, run_date = pimsilitool.get_point_run_status(run_points, orig_route_id, route_id, point_id)

                if use_token:
                    if run_id is not None:
                        # remove old status record from the run_points and new status record
                        run_points = pimsilitool.remove_from_run_points(run_points, run_id, point[4], point[3],  point[2], False)
                        run_points_removed = pimsilitool.insert_to_run_points_license_file(run_points_removed,
                                            run_id,  user_name, point[4],  point[3], point[2], status, run_date)
                        # add new status record
                        run_points_new = pimsilitool.insert_to_run_points_license_file(run_points_new, run_id,
                                                        user_name, point[4],  point[3], point[2], status, run_date)
                    else:
                        run_id = run_id_new
                        run_date = run_date_new

                        # add new status record
                        run_points_new = pimsilitool.insert_to_run_points_license_file(run_points_new, run_id,
                                                        user_name,  point[4], point[3], point[2], status, run_date)

                    checkout_tokens += 1

                    if prev_route_id is None:
                        prev_point_id = point[2]
                        prev_route_id = point[3]
                        prev_orig_route_id = point[4]
                    elif prev_route_id != point[3]:
                        available_tokens = available_tokens - used_tokens
                        token_usage.append(
                            pimsilitool.insert_to_token_usage_license_file(run_id, user_name, prev_orig_route_id,
                                                                          prev_route_id, used_tokens,
                                                                          used_tokens, available_tokens, tool_name, run_date))
                        prev_route_id = None
                        used_tokens = 0
                    used_tokens += 1

                    if i == len(case_name_status) - 1:
                        available_tokens = available_tokens - used_tokens
                        token_usage.append(
                            pimsilitool.insert_to_token_usage_license_file(run_id, user_name, prev_orig_route_id,
                                                                          prev_route_id, used_tokens, used_tokens,
                                                                          available_tokens, tool_name, run_date))


        # update tokens
        result = license_operation.checkout_token(checkout_tokens)

        if len(run_points) > 0:
            for run_pt in run_points[0]:
                run_points_new.append(run_pt)
        if len(run_points_new) > 0:
            pimsilitool.write_to_run_points_license_file(run_points_new)
        if len(token_usage) > 0:
            pimsilitool.write_to_token_usage_license_file(token_usage)

        # *****************End Token update**********************************************

    except Exception as e:
        raise


def check_available_tokens(in_layer):
    try:
        run_points = pimsilitool.get_license_run_points()
        lo = LicenseOperation()
        available_tokens = int(lo.get_available_tokens())
        required_tokes = 0
        release_points = 0

        if arcpy.Exists(in_layer):
            points = arcpy.da.FeatureClassToNumPyArray(
                in_layer,
                [config.POINT_ID_FIELD, config.ROUTE_ID_FIELD, config.ORIGINAL_ROUTE_ID_FIELD],
                spatial_reference=arcpy.SpatialReference(config.WEB_MERCATOR_WKID))
            points = numpy.sort(points, order=config.ROUTE_ID_FIELD)

            release_points = int(arcpy.GetCount_management(in_layer)[0])
            if int(arcpy.GetCount_management(in_layer)[0]) > 0:
                for i, point in enumerate(points):
                    use_token = pimsilitool.check_point_run(run_points, point[2], point[1], point[0])
                    if use_token:
                        required_tokes += 1

        else:
            pimsilitool.AddError("Input Release Points feature class does not exist.")
            return False

        arcpy.AddMessage("=============================================================")
        arcpy.AddMessage("Total available tokens: {}".format(str(available_tokens)))
        arcpy.AddMessage("Total input release points: {}".format(str(release_points)))
        arcpy.AddMessage("Release points ran in last {} days: {}".format(config.TOKEN_USE_TIME_DAYS,
                                                                         str(release_points - required_tokes)))
        arcpy.AddMessage("Total required tokens to run the input release points: {}".format(str(required_tokes)))
        arcpy.AddMessage("=============================================================")

        if available_tokens < required_tokes:
            return False
        else:
            return True

    except Exception as e:
        raise