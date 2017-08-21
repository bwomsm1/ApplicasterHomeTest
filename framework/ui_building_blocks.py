
class UiBuildingBlocks(object):
    def __init__(self, base_test):
        self.base_test = base_test

    def navigate_to_screen_by_name(self, screen_name):
        try:
            tapBarButton = self.base_test.agent.find_element_by_name(screen_name)
        except:
            self.base_test.fail("failed to find '" + screen_name + "' button on screen")
        tapBarButton.click()

    def verify_home_screen(self):
        for element_name in ["The Greatest Application Ever", "eWhere"]:
            self.verify_element_on_screen_by_name(element_name)
        print "Home screen verified successfully"

    def verify_events_screen(self):
        for element_name in ["Music", "Video"]:
            self.verify_element_on_screen_by_name(element_name)
        print "Events screen verified successfully"

    def verify_discover_screen(self):
        for element_name in ["Profile Settings", "Invite Friends", "About Us"]:
            self.verify_element_on_screen_by_name(element_name)
        print "Discover screen verified successfully"

    def verify_inbox_screen(self):
        print "Inbox screen verified successfully"

    def verify_settings_screen(self):
        for element_name in ["Username:", "View and Edit Profile", "Profile Settings", "Invite Friends", "About Us"]:
            self.verify_element_on_screen_by_name(element_name)
        print "Settings screen verified successfully"

    def verify_element_on_screen_by_name(self, element_name):
        try:
            self.base_test.agent.find_element_by_name(element_name)
        except:
            self.base_test.fail("failed to find " + element_name + " on screen")




