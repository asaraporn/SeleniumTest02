from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_success(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()
        self.driver.save_screenshot('testResult/capture01.png')

    def test_search_failed(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        # NG-case
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Project/Selenium_Project02/reports/'))
    # print("To do ")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/'))




