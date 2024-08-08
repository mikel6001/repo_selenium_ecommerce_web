from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        service = Service(executable_path="C:/Users/michaeljohn.roguel/Desktop/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        login = LoginPage(driver)
        login.enter_email("admin@yourstore.com")
        login.enter_password("admin")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_logout()
        # self.driver.find_element(By.ID, "Email").clear()
        # self.driver.find_element(By.ID, "Password").clear()
        # self.driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
        # self.driver.find_element(By.ID, "Password").send_keys("admin")
        # self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        # self.driver.find_element(By.CLASS_NAME, "nav-link").click()
        time.sleep(3)
    # def test_01_login_valid(self):
    #     self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    #     email = self.driver.find_element(By.ID, "Email")
    #     email.clear()
    #     email.send_keys("admin@yourstore.com")
    #     password = self.driver.find_element(By.ID, "Password")
    #     password.clear()
    #     password.send_keys("admin")
    #     login = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     login.click()
    #     logout = self.driver.find_element(By.CLASS_NAME, "nav-link")
    #     logout.click()
    #     time.sleep(3)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Process Completed")


if __name__ == '__main__':
    unittest.main()