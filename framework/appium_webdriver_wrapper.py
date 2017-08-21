
from appium import webdriver
from framework.common_defines import *


class AppiumWebDriverWrapper(object):
    def __init__(self, configuration):
        self.configuration = configuration
        self.setup()

    def setup(self):
        desired_caps = {
            PLATFORM_NAME: 'iOS',
            PLATFORM_VERSION: self.configuration.platform_version,
            DEVICE_NAME: self.configuration.device_name,
            SHOW_IOS_LOGS: 'true',
            BUNDLE_ID: self.configuration.bundle_id,
            DEVICE_ORIENTATION: "portrait",
        }

        self.driver = webdriver.Remote('http://'+self.configuration.appium_server_host+'/wd/hub', desired_caps)

    def close(self):
        self.driver.quit()
