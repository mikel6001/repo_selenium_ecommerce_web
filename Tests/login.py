# to RUN >> "cd .." to the parents folder/directory >> then in the terminal "python -m Tests.login"
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"."))

import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        service = Service(executable_path="C:/Users/michaeljohn.roguel/Desktop/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_check_title(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        web_title = self.driver.title
        assert web_title == "Your store. Login"
        time.sleep(3)

    def test_02_login_valid(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        loginpage = LoginPage(driver)
        loginpage.enter_email("admin@yourstore.com")
        loginpage.enter_password("admin")
        loginpage.click_login()
        homepage = HomePage(driver)
        homepage.click_logout()
        time.sleep(3)

    def test_03_login_invalid_email(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        
        loginpage = LoginPage(driver)
        loginpage.enter_email('adminn')
        loginpage.enter_password('admin')
        loginpage.click_login()
        self.driver.implicitly_wait(5)
        loginpage.check_invalid_username_message("Please enter a valid email address.")
        time.sleep(3)

    def test_04_download_pdf_jewelry(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        loginpage = LoginPage(driver)
        loginpage.enter_email("admin@yourstore.com")
        loginpage.enter_password("admin")
        loginpage.click_login()
        homepage = HomePage(driver)
        homepage.download_product_jewelry_as_pdf()
        homepage.click_logout()
        time.sleep(3)

    def test_05_get_discount_table_values_by_row(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

        loginpage = LoginPage(driver)
        loginpage.enter_email("admin@yourstore.com")
        self.driver.implicitly_wait(3)
        loginpage.enter_password("admin")
        self.driver.implicitly_wait(3)
        loginpage.click_login()
        self.driver.implicitly_wait(5)
        homepage = HomePage(driver)
        self.driver.implicitly_wait(10)
        homepage.go_to_discounts()
        homepage.pick_discounts_startdate()
        self.driver.implicitly_wait(5)
        homepage.pick_discounts_enddate()
        self.driver.implicitly_wait(5)
        homepage.select_discount_type()
        self.driver.implicitly_wait(2)
        homepage.click_search_discounts_button()
        self.driver.implicitly_wait(10)
        homepage.get_discount_table_values()
        self.driver.implicitly_wait(5)
        homepage.click_logout()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Process Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/michaeljohn.roguel/Desktop/selenium_PracticeProject_commerce/Reports"))