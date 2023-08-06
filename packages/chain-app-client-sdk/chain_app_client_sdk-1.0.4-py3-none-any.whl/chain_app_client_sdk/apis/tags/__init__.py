# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chain_app_client_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTH = "auth"
    MAIN = "main"
    MAIN_POOL = "main_pool"
    MASS_CLAIMING = "mass_claiming"
    USER_INFO = "user_info"
