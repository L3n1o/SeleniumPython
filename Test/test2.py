from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class FirstTestWithInstance(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Chrome("Driver\\chromedriver.exe")
            self.driver.get("http://book.theautomatedtester.co.uk/")
            self.driver.fullscreen_window()
        except FileNotFoundError:
            print("Driver for Chrome not found!")

    def mainProcedure(self):
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
            self.driver.find_element_by_id("html5div").send_keys("Example name")

            self.driver.find_element_by_id("secondajaxbutton").click()

            text = self.driver.find_element_by_id("html5div").text
            print(text)
            self.driver.implicitly_wait(7)
            self.driver.save_screenshot("Screenshots\\Chapter1PageScreenshot.png")

            self.driver.find_element_by_link_text('Home Page')
            self.driver.implicitly_wait(5)
            self.driver.save_screenshot("Screenshots\\HomePageScreenshot.png")
        except NoSuchElementException:
            print("Something went wrong")

    def tearDown(self):
        try:
            self.driver.close()
            print("Success!")
        except Exception:
            print("Something went wrong")


test = FirstTestWithInstance()
test.setUp()
test.mainProcedure()
test.tearDown()

