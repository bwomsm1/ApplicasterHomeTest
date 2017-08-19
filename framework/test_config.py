
import json
from common_defines import APPLICATION_FILE_PATH, CONFIGURATION_FILE


class TestConfiguration(object):

    def __init__(self):
        json_data = open(CONFIGURATION_FILE).read()
        data = json.loads(json_data)

        self.app_path = data[APPLICATION_FILE_PATH]



