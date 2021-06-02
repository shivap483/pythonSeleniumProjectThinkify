from Configs.TestData import TestData
from Pages.HomePage import HomePage
from Tests import test_conf


class HomeTest:
    def __init__(self, driver):
        self.homePage = HomePage(test_conf.initiate_drive(driver))

    def launch_application_and_find_distance(self):
        self.homePage.launch_application(TestData.URL)
        self.homePage.click_directions_button()
        self.homePage.enter_source_location(TestData.SOURCE)
        self.homePage.enter_destination_location(TestData.DESTINATION)
        # self.homePage.click_search_button()
        distance = self.homePage.read_distance()
        self.homePage.print_output(TestData.SOURCE, TestData.DESTINATION, distance)
        self.homePage.close()


test = HomeTest(TestData.BROWSER)
test.launch_application_and_find_distance()
