from selenium.webdriver.common.by import By
from Locators.locators import Locators

class LoginPage():

    #this is a contructor in python, init=initialize
    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = '//button[@type="submit"]'
        #self.invalid_username_error_msg_id = Locators.invalid_username_error_msg_id
        self.invalid_username_error_msg_xpath = '//*[@id="Email-error"]'

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_username_message(self, expected_message):
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[1]/h1').click()
        # Find the element containing the error message
        error_element = self.driver.find_element(By.XPATH, '//*[@id="Email-error"]')
        # Get the text content of the error message
        actual_message = error_element.text
        # Assert that the actual message matches the expected message
        assert actual_message == expected_message
        # assert actual_message == expected_message, f"Expected error message: '{expected_message}', but got: '{actual_message}'"