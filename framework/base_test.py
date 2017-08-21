

import unittest
from appium import webdriver


from framework.common_defines import *
from framework.test_config import TestConfiguration
from appium_webdriver_wrapper import AppiumWebDriverWrapper
from ui_building_blocks import UiBuildingBlocks


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.configuration = TestConfiguration()

    def setUp(self):
        super(BaseTest, self).setUp()
        self.setupWebDriver()
        self.ui_building_blocks = UiBuildingBlocks(self)

    def tearDown(self):
        super(BaseTest, self).tearDown()

        self.appiumWrapper.close()
        print self.id(), "finished running."
        print self.shortDescription()

    def setupWebDriver(self):
        self.appiumWrapper = AppiumWebDriverWrapper(self.configuration)
        self.agent = self.appiumWrapper.driver


