from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException


class TibiaTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        try:
            cls.driver = webdriver.Chrome("Driver\\chromedriver.exe")
        except FileNotFoundError:
            print("Driver for google not found!")

    def testRegistrationFormTibia(self):
        try:
            self.driver.get("https://www.tibia.com/mmorpg/free-multiplayer-online-role-playing-game.php")
            self.driver.find_element_by_id("email").send_keys("pnad@elvisor.org")
            self.driver.find_element_by_id("password1").send_keys("klenio12")
            self.driver.find_element_by_id("charactername").clear()
            self.driver.find_element_by_id("charactername").send_keys("MichealJordanII")
            self.driver.find_element_by_id("sex_female").click()
            self.driver.find_element_by_id("ButtonPlayNow").click()
            time.sleep(10)
        except NoSuchElementException:
            print("Something went wrong")

    @classmethod
    def tearDown(cls):
        try:
            cls.driver.close()
        except Exception:
            print("Something went wrong")


if __name__ == '__main__':
    unittest.main()
