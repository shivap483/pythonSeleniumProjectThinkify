from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def initiate_drive(param):
    driver = None
    if param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if param == "edge":
        driver = webdriver.Chrome(EdgeChromiumDriverManager().install())
    if param == "firefox":
        driver = webdriver.Chrome(GeckoDriverManager().install())
    return driver
