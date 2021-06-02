from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CommonMethods:
    def __init__(self,driver):
        self.driver = driver

    def launch_url(self,url):
        self.driver.get(url)

    def click_element(self,locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()
        # self.driver.find_element_by_id(locator).click()

    def send_text(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def read_text(self,locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text

    def close_browser(self):
        self.driver.quit()