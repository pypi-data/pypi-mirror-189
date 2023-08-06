class LMInfo:
    # from inlineinspection import config
    import winreg, os

    reg_path = r"SOFTWARE\ESRI\ArcGISPro"
    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ)
    condaroot, regtype = winreg.QueryValueEx(registry_key, "PythonCondaRoot")
    condaenv, regtype1 = winreg.QueryValueEx(registry_key, "PythonCondaEnv")
    ARCGISPRO_PATH = os.path.join(condaroot, "envs", condaenv, "python.exe")
    winreg.CloseKey(registry_key)

    # ARCGISPRO_PATH = 'C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python.exe'
    # ARCGISPRO_PATH = config.ARCGIS_PRO_PYTHON_PATH

    LISENCE_TO_EMAIL = 'licensing@g2-is.com'

    # production kyes
    # PRODUCT_ID = '9145E227-422B-434E-89A2-4EEB7AF106D4'

    # RSA_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n\
    #                         MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxVeHxDKgjjfiEKYRGbQ4\n\
    #                         xf6+JkRFjHi16Bc6jRs2Y8IWfp5KEuaMCqRF7w1tfjbUrfjpY0u2HTeDnJwETAmX\n\
    #                         vE3qzhnjaVlUKua60BgzKRNLOKx8DE55NX21U9N7jsnmRpe3gt/dJkMWiyANjPi5\n\
    #                         NdYR3NC3+tXHbO5gQiqobtns3+omGKxi4kfB8BEXGMQPnUui3M9VZMTi0lLLevUo\n\
    #                         v/jIUQ+x78jqUx5dFn38Nz1ErK7O/xsYdwSoQmDKjdlAhkzzHkgViR6JpJI9Yj5/\n\
    #                         NPxLh3fLiSx6UzAaa3MUNBO6CO/hMTePhWQsyY71D1uye+m7UsTG5xs1MQGnUJwQ\n\
    #                         oQIDAQAB\n\
    #                         -----END PUBLIC KEY-----"

    PRODUCT_ID = 'B7F7241C-82FB-48D4-B362-6780EDE5F56D'

    RSA_PUBLIC_KEY =  "-----BEGIN PUBLIC KEY-----\n\
                        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4nGOwmknRGir2v4jeAHq\n\
                        rpDTXJ6s04rOA1HL+zcdq147VLfF+HAZyPVZrSoQ5pxUMyXx3HPhKORo/HCMVB49\n\
                        uC7wb93km5A9XVBmbHN6X3aGvVg3X27VJDKAGRlMqviDC5ny/OUAtmwOi5WbzXNX\n\
                        mF5cYu801pjF92dP4RA8Fzo6twRoX2jEXQ2RagRtUmujQh/id+sDdnnc7/E+Gdqm\n\
                        dP3pHqaY61GXP06YNBdeqcof+SqnGxJ1BnTIBrmCOpNkCivX446VIDtdPmpPSDGa\n\
                        KE7JbASXRhXPHYCMeCBXbG98YSgLMtVZ6SpebbLvr+PJdDNXA0vw57eL6F5ZhrYo\n\
                        twIDAQAB\n\
                        -----END PUBLIC KEY-----"

    # staging keys
    # PRODUCT_ID = 'BCD67C3E-9765-48CE-8053-BE03491C906D'
    #
    # RSA_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n\
    #                 MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA08DpbcOEhWr8fdMuwyzE\n\
    #                 snLqBtO25sgBLW6RNWEWuv62vDmxLCZwiCA6rN/dYmDLa6MobxgQH9jbMSQluuSM\n\
    #                 PmpqEczBy+N6v9sVwZ7lvSj5AOejfSbqu6BB0Vivx144DP/uGK3M5LBQcIuq63IR\n\
    #                 dUHJDgjwqZCDWhILTeJt1QHZ+6bQHxyNbaeAQwZns56CNEvQHhc+lQb3FUH0pQN9\n\
    #                 XWURW7Mtiz8vJNMT35vZCY2XgAx94fy0MOXaKsytrvpE+JxCQyGyuuGJqdnJIBHv\n\
    #                 +zvcR010vf3wl6FZm85zrSDJDbCVSjzx8ywUwEwlgjmBe6I6ytEqsu+uMQ5hd3gj\n\
    #                 KwIDAQAB\n\
    #                 -----END PUBLIC KEY-----"
