from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.CommonUtils import CommonMethods


class HomePage(CommonMethods):
    button_directions = (By.ID, 'searchbox-directions')
    text_box_source = (By.XPATH, "//input[contains(@placeholder,'Choose starting point')]")
    text_box_destination = (By.XPATH, "//input[contains(@placeholder,'Choose destination')]")
    button_search = (By.XPATH, "//button[@data-tooltip='Search']")
    read_only_distace = (By.XPATH, "(//div[contains(text(),'km')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def launch_application(self, url):
        self.launch_url(url)

    def click_directions_button(self):
        self.click_element(self.button_directions)

    def enter_source_location(self, source):
        self.send_text(self.text_box_source, source)

    def enter_destination_location(self, destination):
        self.send_text(self.text_box_destination, destination + Keys.RETURN)

    def click_search_button(self):
        self.click_element(self.button_search)

    def read_distance(self):
        distance = self.read_text(self.read_only_distace)
        return distance

    def close(self):
        self.close_browser()

    def print_output(self, SOURCE, DESTINATION, distance):
        print("Distance between {} and {} is {}".format(SOURCE, DESTINATION, distance))
