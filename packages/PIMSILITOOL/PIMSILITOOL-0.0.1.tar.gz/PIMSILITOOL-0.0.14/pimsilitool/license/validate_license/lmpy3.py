"""
This script will be executed in ArcGIS Pro python version 3 to register and validate G2 em license.
"""
import sys
from pimsilitool.license.validate_license import lm
import pimsilitool
import traceback
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            pimsilitool.AddMessage("Parameters not found. Please pass product_id,rsa_public_key as parameters")

        elif len(sys.argv) == 3:
            # public_key = str(test).replace('__','\\n\\\r\t\t\t')
            public_key = str(sys.argv[2]).replace('__', '\n                        ')
            status, error = lm.validate_product(sys.argv[1],public_key)
            if status:
                pimsilitool.AddMessage("True")
            else:
                pimsilitool.AddMessage("False," + str(error))

        elif len(sys.argv) == 6:
            public_key = str(sys.argv[2]).replace('__', '\n                        ')

            status, error = lm.register_product(sys.argv[1], public_key, sys.argv[3], sys.argv[4], sys.argv[5])
            if status:
                pimsilitool.AddMessage("True")
            else:

                pimsilitool.AddMessage("False," + str(error))

    except Exception as e:
        raise