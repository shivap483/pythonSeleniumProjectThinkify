from Configs.TestData import TestData
from Tests.test_HomePage import HomeTest

if __name__ == '__main__':
    test = HomeTest(TestData.BROWSER)
    test.launch_application_and_find_distance()