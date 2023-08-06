import arcpy
import sys, subprocess
from uuid import UUID
from pimsilitool.license.validate_license.license_info import LMInfo
import os
import re
import pimsilitool

class RegisterLicense(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Register License"
        self.description = "Registers license for PIMS ILI Integration tools"
        self.category = "License"
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""

        # Select project database
        # parameter - 0
        user_display_name = arcpy.Parameter(
            displayName="User Display Name",
            name="user_display_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # parameter - 1
        user_email = arcpy.Parameter(
            displayName="User Email",
            name="user_email",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # parameter - 2
        license_key = arcpy.Parameter(
            displayName="License Key",
            name="license_key",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        params = [user_display_name, user_email, license_key]

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
            arcpy.AddMessage("Registering product, Please wait...")
            if not os.path.exists(LMInfo.ARCGISPRO_PATH):
                pimsilitool.AddError("ArcGIS Pro not found, \nPlease install ArcGIS Pro in C:\Program Files\ArcGIS")
                raise
            else:
                propath = LMInfo.ARCGISPRO_PATH
                propath = propath.replace('\\', '/')
                product_id = UUID(LMInfo.PRODUCT_ID)
                rsa_public_key = LMInfo.RSA_PUBLIC_KEY

                rpk = rsa_public_key.replace('\n', '__').replace('  ', '')

                fileDir = os.path.dirname(os.path.realpath(__file__))
                py3_path = os.path.join(fileDir, "../validate_license/lmpy3.py")
                py3_path = os.path.abspath(os.path.realpath(py3_path))

                cmd = "\"" + propath + "\"  \"" + py3_path + "\" \"" + str(product_id) + "\" \"" + rpk + "\" \"" + parameters[2].valueAsText + "\" \"" + parameters[0].valueAsText + "\" \"" + parameters[1].valueAsText + "\""

                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
                output, error = p.communicate()

                if output:
                    pimsilitool.AddMessage("Registration completed successfuly. Please close ArcGIS Pro and reopen it to use the PIMS ILI Integration tools.")
                else:
                    pimsilitool.AddError("Registration failed")
                    pimsilitool.AddError(error)
                    raise
            return
        except Exception as inst:
            arcpy.AddError(str(inst))
            raise

class RequestLicense(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Request License"
        self.description = "Request license for PIMS ILI Integration tools"
        self.category = "License"
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""

        # Select project database
        # parameter - 0
        user_name = arcpy.Parameter(
            displayName="User Display Name",
            name="user_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # parameter - 1
        license_type = arcpy.Parameter(
            displayName="License Type",
            name="license_type",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        license_type.filter.type = "ValueList"
        license_type.filter.list = ['Perpetual Named User License', 'Subscription Named User License',
                                    'Trial Named User License']
        license_type.value = "Perpetual Named User License"

        # parameter - 2
        email_server = arcpy.Parameter(
            displayName="Email Server",
            name="email_server",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        email_server.filter.type = "ValueList"
        email_server.filter.list = ['Microsoft Outlook', 'Google']
        email_server.value = "Microsoft Outlook"

        # parameter - 3
        user_email = arcpy.Parameter(
            displayName="User Email",
            name="user_email",
            datatype="GPString",
            parameterType="Optional",
            direction="Input")

        # parameter - 4
        # Provide password to login to gmail
        password = arcpy.Parameter(
            displayName="Password",
            name="password",
            datatype="GPStringHidden",
            parameterType="Optional",
            direction="Input")
        password.enabled = False
        params = [user_name, license_type, email_server, user_email, password]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        # check selected email server
        if parameters[2].value:
            if parameters[2].valueAsText == "Microsoft Outlook":
                parameters[4].enabled = False
                parameters[3].enabled = False
            elif parameters[2].valueAsText == "Google":
                parameters[4].enabled = True
                parameters[3].enabled = True
        else:
            parameters[4].enabled = False
            parameters[3].enabled = False

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        if parameters[3].valueAsText is not None:
            if not self.check_email(parameters[3].valueAsText):
                parameters[3].setErrorMessage("Invalid email.")

        if parameters[4].enabled is True and parameters[4] is None:
            parameters[4].setErrorMessage("Invalid password.")

        if parameters[2].value == "Google" and parameters[3] is None:
            parameters[3].setErrorMessage("email required")

        return

    def check_email(self, email_id):
        try:
            # Make a regular expression for validating an Email
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

            if (re.search(regex, email_id)):
                return True
            else:
                return False

        except Exception as e:
            arcpy.AddError("Failed to run check_email.\n{0}".format(arcpy.GetMessages(2)))
            raise

    def execute(self, parameters, messages):
        try:

            import pimsilitool.config as config
            pimsilitool.AddMessage("Requesting license...")

            if not os.path.exists(LMInfo.ARCGISPRO_PATH):
                pimsilitool.AddError("ArcGIS Pro not found, \nPlease install ArcGIS Pro in C:\Program Files\ArcGIS")
                raise

            if parameters[2].valueAsText == "Microsoft Outlook":
                import win32com.client
                outlook = win32com.client.Dispatch("Outlook.Application")
                message = outlook.CreateItem(0)
                message.To = config.LISENCE_TO_EMAIL
                message.Subject = "PIMS ILI Integration Tool license"

                message.Body = "PIMS ILI Integration Tool license request from {0} \nLicense Type: {1}".format(parameters[0].valueAsText, parameters[1].valueAsText)

                message.Send()

                pimsilitool.AddMessage("Done Requesting license.")

            elif parameters[2].valueAsText == "Google":
                import smtplib, ssl, email

                # port = 587
                # smtp_server = "smtp.gmail.com"
                sender_email = parameters[3].valueAsText  # "sfaksfhajsfh@gmail.com"
                receiver_email = config.LISENCE_TO_EMAIL
                password = parameters[4].valueAsText  # "Friend@123"
                subject = "PIMS ILI Integration Tool license"
                body = "PIMS ILI Integration Tool license request from {0}, contact email: {1} \nLicense Type: {2}".format(parameters[0].valueAsText, parameters[3].valueAsText, parameters[1].valueAsText)

                message = '\r\n'.join(['To: %s' % receiver_email,
                                       'From: %s' % sender_email,
                                       'Subject: %s' % subject, '', body])

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                try:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)

                except Exception as e:
                    # import traceback

                    pimsilitool.AddError("Failed to login to Gmail. \n")
                    # Get current system exception
                    ex_type, ex_value, ex_traceback = sys.exc_info()

                    if ex_type.__name__ == "SMTPAuthenticationError":
                        pimsilitool.AddError(
                            "Google blocks sign-in attempts from apps which do not use modern security standards.\n"
                            "Turn on the safety feature by going to the link below: \n"
                            "https://www.google.com/settings/security/lesssecureapps")
                    raise
            return

        except Exception as e:
            pimsilitool.AddError(str(e))
            raise



