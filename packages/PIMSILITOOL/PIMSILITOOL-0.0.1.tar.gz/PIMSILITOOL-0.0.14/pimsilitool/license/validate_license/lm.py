"""
This script will be executed in ArcGIS Pro python version 3 to register and validate G2 em license.
"""

from uuid import UUID
import sys
import os
sys.path.insert(0, os.path.abspath("../"))
from evoleap_licensing.InstanceIdentity import InstanceIdentity, InstanceIdentityValue
from evoleap_licensing.UserIdentity import UserIdentity
from evoleap_licensing.desktop.ControlManager import ControlManager
from evoleap_licensing.webservice.ConnectionSettings import ConnectionSettings
from evoleap_licensing.UserInfo import UserInfo
from evoleap_licensing.enumerations.licensing_enumerations import SessionState
import pimsilitool


from uuid import getnode as get_mac
import pickle
# import getpass


evoleap_server = 'https://elm.evoleap.com/'
version = "3.0.0.0"
# evoleap_server = 'https://elm-staging.evoleap.com/'
# version = "2.6.01"


def get_mac_address():
    """ read system mac address"""
    mac = get_mac()
    h = iter(hex(mac)[2:].zfill(12))
    return ":".join(i + next(h) for i in h)


def get_HDD_SN():
    return os.popen("wmic diskdrive get serialnumber").read().split()[-1]


def register_product(product_id,rsa_public_key,license_key,user_display_name,user_email):
    '''
    This function registers product with G2-Evoleap license portal
    :param product_id: Can get from from G2-Evoleap portal
    :param rsa_public_key: can get from G2-Evoleap portal
    :param license_key: can get from G2-Evoleap portal
    :param user_display_name: can be any name which showup in G2-Evoleap portal
    :param user_email: user email id
    :return:
    '''
    try:
        p_id = UUID(product_id)
        instance_identity_info = {'mac': InstanceIdentityValue(get_mac_address())
                                  ,'hddsn': InstanceIdentityValue(get_HDD_SN())}

        user_identity_info = {'UPN': os.getlogin()}

        user_info = UserInfo(user_display_name, user_email)

        ConnectionSettings.SetHost(evoleap_server)  # staging server

        user_identity = UserIdentity(user_identity_info)
        instance_identity = InstanceIdentity(instance_identity_info)
        manager = ControlManager(p_id, version, rsa_public_key, user_identity, instance_identity)

        registration_result = manager.Register(license_key, user_info)
        if registration_result.Success:
            in_dir = pimsilitool.get_appdata_roaming_dir()
            file = os.path.join(in_dir, product_id + ".pkl")
            with open(file, 'wb') as output:
                pickle.dump(manager.State, output)
            pimsilitool.AddMessage("Registration succeeded")
            pimsilitool.AddMessage("First registered at " + str(manager.State.RegisteredAt))
            return True, None
        else:
            pimsilitool.AddMessage("Registration failed: " + registration_result.ErrorMessage)
            return False, registration_result.ErrorMessage

    except Exception as e:
        raise
        # error_type, error_instance, traceback = sys.exc_info()
        # raise error_type(error_instance).with_traceback(traceback)

def validate_product(product_id,rsa_public_key):
    '''
      This function checks wheather license valid or not from G2-Evoleap license portal
      :param product_id: Can get from from G2-Evoleap portal
      :param rsa_public_key: can get from G2-Evoleap portal
      :param license_key: can get from G2-Evoleap portal
      :return:
      '''
    try:
        p_id = UUID(product_id)

        instance_identity_info = {'mac': InstanceIdentityValue(get_mac_address()),
                                  'hddsn': InstanceIdentityValue(get_HDD_SN())}

        user_identity_info = {'UPN': os.getlogin()}

        ConnectionSettings.SetHost(evoleap_server)  # staging server
        user_identity = UserIdentity(user_identity_info)
        instance_identity = InstanceIdentity(instance_identity_info)
        in_dir = pimsilitool.get_appdata_roaming_dir()

        file = os.path.join(in_dir, product_id + ".pkl")
        if not os.path.exists(file):
            return False, "Product not registered"
        with open(file, 'rb') as input:
            vs = pickle.load(input)
        manager = ControlManager(product_id, version, rsa_public_key, user_identity, instance_identity,saved_state=vs)
        if manager.State.Registered:
            # Start a session
            validation_result = manager.ValidateSession()
            if validation_result.IsValid:
                file = os.path.join(in_dir, product_id + ".pkl")
                with open(file, 'wb') as output:
                    pickle.dump(manager.State, output)
                return True, None
            else:
                return False, validation_result.InvalidReason
    except Exception as e:
        raise
        # error_type, error_instance, traceback = sys.exc_info()
        # raise error_type(error_instance).with_traceback(traceback)

def get_controlmanager(product_id,rsa_public_key):
    '''
      This function returns control manager object to checkout tokens
      :param product_id: Can get from from G2-Evoleap portal
      :param rsa_public_key: can get from G2-Evoleap portal
      :param license_key: can get from G2-Evoleap portal
      :return:
      '''
    try:
        p_id = UUID(product_id)

        instance_identity_info = {'mac': InstanceIdentityValue(get_mac_address()),
                                  'hddsn': InstanceIdentityValue(get_HDD_SN())}
        user_identity_info = {'UPN': os.getlogin()}
        # user_identity_info = {'UPN': 'G2Test2'}
        ConnectionSettings.SetHost(evoleap_server)  # staging server
        # ConnectionSettings.DEFAULT_REQUEST_TIMEOUT = timedelta(seconds=120)
        user_identity = UserIdentity(user_identity_info)
        instance_identity = InstanceIdentity(instance_identity_info)
        in_dir = pimsilitool.get_appdata_roaming_dir()
        # file = os.path.join(os.getenv('LOCALAPPDATA') + "\\"+product_id+".pkl")
        file = os.path.join(in_dir, product_id + ".pkl")
        if not os.path.exists(file):
            return False, "Product not registered"
        with open(file, 'rb') as input:
            vs = pickle.load(input)
        manager = ControlManager(product_id, version, rsa_public_key, user_identity, instance_identity,saved_state=vs)
        if manager.State.Registered:
            # Start a session
            validation_result = manager.ValidateSession()
            if validation_result.IsValid:
                # file = os.path.join(os.getenv('LOCALAPPDATA') + "\\"+product_id+".pkl")
                file = os.path.join(in_dir, product_id + ".pkl")
                with open(file, 'wb') as output:
                    pickle.dump(manager.State, output)

        return manager
    except Exception as e:
        raise
