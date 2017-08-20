
from appium import webdriver
from framework.common_defines import *


class AppiumWebDriverWrapper(object):
    def __init__(self, configuration):
        self.configuration = configuration
        self.setup()

    def setup(self):
        desired_caps = {
            PLATFORM_NAME: 'iOS',
            PLATFORM_VERSION: '10.3',
            DEVICE_NAME: 'iPhone 6',
            SHOW_IOS_LOGS: 'true',
            BUNDLE_ID: "SMWarren.e-Where",
            DEVICE_ORIENTATION: "portrait",
            BROWSER_NAME: ""
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def close(self):
        self.driver.quit()
