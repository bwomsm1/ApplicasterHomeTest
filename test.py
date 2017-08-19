__author__ = 'Boaz Warshawsky'

import unittest
from framework.base_test import BaseTest


class eWhereAppTests(BaseTest):

    def test_navigate_to_all_screens(self):
        self.ui_building_blocks.navigate_to_screen_by_name("Events")
        self.ui_building_blocks.verify_events_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Discover")
        e = self.agent.find_element_by_class_name("UIImageView")
        self.ui_building_blocks.verify_discover_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Inbox")
        self.ui_building_blocks.verify_inbox_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Settings")
        self.ui_building_blocks.verify_settings_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Home")
        self.ui_building_blocks.verify_home_screen()


    def shortDescription(self):
        return "This test perform basic navigation between all screens of the application"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(eWhereAppTests)
    unittest.TextTestRunner().run(suite)
