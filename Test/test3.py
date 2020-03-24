from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class FirstTestSelfRunning(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome("Driver\\chromedriver.exe")
            cls.driver.get("http://book.theautomatedtester.co.uk/")
            cls.driver.fullscreen_window()
        except FileNotFoundError:
            print("Driver for Chrome not found!")

    def test_first_test(self):
        try:

            self.driver.find_element_by_id("q").send_keys("Test 1 perform")
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("//a[@href='/chapter1']").click()
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "html5div"))
                )
            except NoSuchElementException:
                self.driver.quit()
            self.driver.find_element_by_id("radiobutton").click()

            select = Select(self.driver.find_element_by_id("selecttype"))
            select.select_by_visible_text("Selenium Grid")

            self.driver.find_element_by_name("selected(1234)").click()

            self.driver.find_element_by_id("html5div").clear()
            self.driver.find_element_by_id("html5div").send_keys("Example name xD")

            self.driver.find_element_by_id("secondajaxbutton").click()

            text = self.driver.find_element_by_id("html5div").text
            print(text)
            self.driver.implicitly_wait(7)

            self.driver.find_element_by_link_text('Home Page')
            self.driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Something went wrong")

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.close()
            print("Success!")
        except Exception:
            print("Something went wrong")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='Report'))
