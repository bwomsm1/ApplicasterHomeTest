
import json
from common_defines import APPLICATION_FILE_PATH, CONFIGURATION_FILE


class TestConfiguration(object):

    def __init__(self):
        json_data = open(CONFIGURATION_FILE).read()
        data = json.loads(json_data)

        self.app_path = data[APPLICATION_FILE_PATH]
        self.platform_version = data["platform_version"]
        self.device_name = data["device_name"]
        self.bundle_id = data["bundle_id"]
        self.appium_server_host = data["appium_server_host"]



