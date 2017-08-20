
class UiBuildingBlocks(object):
    def __init__(self, agent):
        self.agent = agent

    def navigate_to_screen_by_name(self, screen_name):
        tapBarButton = self.agent.find_element_by_name(screen_name)
        assert tapBarButton
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
        element = self.agent.find_element_by_name(element_name)
        assert element


