__author__ = 'Boaz Warshawsky'

import unittest
from framework.base_test import BaseTest
from time import sleep


class eWhereAppTestNavigation(BaseTest):

    def test_navigate_to_all_screens(self):
        self.ui_building_blocks.navigate_to_screen_by_name("Events")
        self.ui_building_blocks.verify_events_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Discover")
        self.ui_building_blocks.verify_discover_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Inbox")
        self.ui_building_blocks.verify_inbox_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Settings")
        self.ui_building_blocks.verify_settings_screen()

        self.ui_building_blocks.navigate_to_screen_by_name("Home")
        self.ui_building_blocks.verify_home_screen()

    def shortDescription(self):
        return "This test perform basic navigation between all screens of the application"


class eWhereAppTestStress(BaseTest):

    def test_stress_test_launch_application(self):
        for i in range(5):
            self.agent.close_app()
            self.agent.launch_app()
            sleep(1)
            self.ui_building_blocks.verify_home_screen()

    def shortDescription(self):
        return "This test perform stress test for by launching the application 5 times in a row"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(eWhereAppTestNavigation)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(eWhereAppTestStress)
    unittest.TextTestRunner().run(suite)


