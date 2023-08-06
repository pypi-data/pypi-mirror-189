"""
This script will be executed in ArcGIS Pro python version 3 to checkout G2 elm license.
"""
from pimsilitool.license.validate_license import lm
import sys
import pimsilitool
if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            pimsilitool.AddMessage("Parameters not found. Please pass product_id,rsa_public_key as parameters")

        elif len(sys.argv) == 3:
            # public_key = str(test).replace('__','\\n\\\r\t\t\t')
            public_key = str(sys.argv[2]).replace('__', '\n                        ')
            manager = lm.get_controlmanager(sys.argv[1],public_key)
            components = manager.SessionManager.GetComponentsStatus()

            total_tokens = int(components.ComponentEntitlements[0].CurrencyUsage.currency_entitled)
            used_tokens = int(components.ComponentEntitlements[0].CurrencyUsage.currency_used)
            available_tokens = total_tokens - used_tokens
            pimsilitool.AddMessage(str(available_tokens))

        elif len(sys.argv) == 4:
            public_key = str(sys.argv[2]).replace('__', '\n                        ')
            manager = lm.get_controlmanager(sys.argv[1], public_key)
            no_of_tokens = int(sys.argv[3])
            components = manager.SessionManager.GetComponentsStatus()

            comp_checkout_result = manager.CheckOutConsumableComponent("PIMSILITool", no_of_tokens)

            if comp_checkout_result.Success:
                pimsilitool.AddMessage("True")
            else:
                pimsilitool.AddMessage("False," + str(comp_checkout_result.FailureReason.name))

    except Exception as e:
        raise