"""
This script will be executed in ArcGIS Pro python version 3 to register and validate G2 em license.
"""
import pimsilitool.license.validate_license.lm as lm
import sys
import subprocess
from pimsilitool.license.validate_license.license_info import LMInfo
import pimsilitool
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            pimsilitool.AddMessage("Parameters not found. Please pass input as parameters")

        else:

            if sys.argv[3] == "Microsoft Outlook":
                # Install pywin32 module
                # subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])

                import win32com.client
                outlook = win32com.client.Dispatch("Outlook.Application")
                message = outlook.CreateItem(0)
                message.To = LMInfo.LISENCE_TO_EMAIL
                message.Subject = "PIMS ILI Integration Tool license"

                message.Body = "PIMS ILI Integration Tool license request from {0} \nLicense Type: {1}".format(
                    sys.argv[1], sys.argv[2])

                message.Send()

                pimsilitool.AddMessage("True")

            elif sys.argv[3] == "Google":
                import smtplib, ssl, email

                # port = 587
                # smtp_server = "smtp.gmail.com"
                sender_email = sys.argv[4] #"sfaksfhajsfh@gmail.com"
                receiver_email = LMInfo.LISENCE_TO_EMAIL
                password = sys.argv[5]    #"Friend@123"
                subject = "PIMS ILI Integration Tool license"
                body = "PIMS ILI Integration Tool license request from {0}, contact email: {1} \nLicense Type: {2}".format(sys.argv[1], sys.argv[4], sys.argv[2])

                message = '\r\n'.join(['To: %s' % receiver_email,
                                    'From: %s' % sender_email,
                                    'Subject: %s' % subject, '', body])

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                try:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                    pimsilitool.AddMessage("True")
                except Exception as e:
                    # import traceback

                    pimsilitool.AddMessage("Failed to login to Gmail. \n")
                    # Get current system exception
                    ex_type, ex_value, ex_traceback = sys.exc_info()

                    if ex_type.__name__ == "SMTPAuthenticationError":
                        pimsilitool.AddMessage("Google blocks sign-in attempts from apps which do not use modern security standards.\n"
                                            "Turn on the safety feature by going to the link below: \n"
                                            "https://www.google.com/settings/security/lesssecureapps")
                    raise


    except Exception as e:
        pimsilitool.AddMessage("False")
        raise