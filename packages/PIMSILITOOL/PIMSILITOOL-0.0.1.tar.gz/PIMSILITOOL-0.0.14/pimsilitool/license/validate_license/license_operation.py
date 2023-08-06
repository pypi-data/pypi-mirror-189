import arcpy
import sys, subprocess
# from uuid import UUID
import os
import pimsilitool
from pimsilitool.license.validate_license.license_info import LMInfo

class LicenseOperation():
    is_licensed = False
    def __init__(self):
        return
    def validate_license(self):
        try:
            if not os.path.exists(LMInfo.ARCGISPRO_PATH):
                arcpy.AddMessage(
                    "ArcGIS Pro not found in the default location, Please update ARCGIS_PRO_PYTHON_PATH varialbe in the "
                    "\<ArcGIS Pro install path>\Lib\site-packages\lpimsilitool\config.py file.")
            else:
                propath = LMInfo.ARCGISPRO_PATH
                propath = propath.replace('\\', '/')
                product_id = LMInfo.PRODUCT_ID
                rsa_public_key = LMInfo.RSA_PUBLIC_KEY

                rpk = rsa_public_key.replace('\n', '__').replace('  ', '')
                fileDir = os.path.dirname(os.path.realpath(__file__))
                py3_path = os.path.join(fileDir, "../validate_license/lmpy3.py")
                py3_path = os.path.abspath(os.path.realpath(py3_path))

                cmd = "\"" + propath + "\"  \"" + py3_path + "\" \"" + str(product_id) + "\" \"" + rpk + "\""

                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,startupinfo=si)
                output, error = p.communicate()

                if "True" in str(output):
                    LicenseOperation.is_licensed = True
                    return True
                else:
                    pimsilitool.AddMessage(str(output))
                    pimsilitool.AddMessage(str(error))
                    LicenseOperation.is_licensed = False
                    arcpy.AddError(error)
                    return False
        except Exception as e:
            pimsilitool.AddMessage(str(e))
            raise

    def get_available_tokens(self):
        try:
            propath = LMInfo.ARCGISPRO_PATH
            propath = propath.replace('\\', '/')
            product_id = LMInfo.PRODUCT_ID
            rsa_public_key = LMInfo.RSA_PUBLIC_KEY

            rpk = rsa_public_key.replace('\n', '__').replace('  ', '')
            fileDir = os.path.dirname(os.path.realpath(__file__))
            py3_path = os.path.join(fileDir, "../validate_license/checkout_token.py")
            py3_path = os.path.abspath(os.path.realpath(py3_path))

            cmd = "\"" + propath + "\"  \"" + py3_path + "\" \"" + str(product_id) + "\" \"" + rpk + "\""

            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,startupinfo=si)
            output, error = p.communicate()
            return output
        except Exception as e:
            pimsilitool.AddMessage(str(e))
            raise

    def checkout_token(self, no_of_tokens):
        try:
            propath = LMInfo.ARCGISPRO_PATH
            propath = propath.replace('\\', '/')
            product_id = LMInfo.PRODUCT_ID
            rsa_public_key = LMInfo.RSA_PUBLIC_KEY

            rpk = rsa_public_key.replace('\n', '__').replace('  ', '')

            fileDir = os.path.dirname(os.path.realpath(__file__))
            py3_path = os.path.join(fileDir, "../validate_license/checkout_token.py")
            py3_path = os.path.abspath(os.path.realpath(py3_path))

            cmd = "\"" + propath + "\"  \"" + py3_path + "\" \"" + str(product_id) + "\" \"" + rpk + "\" \"" + str(no_of_tokens) + "\""

            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
            output, error = p.communicate()
            if "True" in str(output):
                return True
            else:
                arcpy.AddError(error)
                return False
        except Exception as e:
            pimsilitool.AddMessage(str(e))
            raise