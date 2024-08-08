from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from Locators.locators import Locators
import csv

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_button_classname = "nav-link"
        self.catalog_sidebar_xpath = '//a[@href="#"]//i[@class="nav-icon fas fa-book"]'
        self.product_sidebar_xpath = "//p[text()=' Products']"
        self.search_category_id = "SearchCategoryId"
        self.search_product_id = "search-products"
        self.pdf_download_button_xpath = '//button[@name="download-catalog-pdf"]'
        self.promotions_sidebar_xpath = '//a[@href="#"]//i[@class="nav-icon fas fa-tags"]'
        self.discounts_sidebar_xpath = "//p[text()=' Discounts']"
        self.startdate_box_id = "SearchStartDate"
        self.enddate_box_id = "SearchEndDate"
        self.discount_dropdown_id = "SearchDiscountTypeId"
        self.search_discount_button_id = "search-discounts"

    def click_logout(self):
        self.driver.find_element(By.CLASS_NAME, self.logout_button_classname).click()

    def download_product_jewelry_as_pdf(self):
        action = ActionChains(self.driver)
        catalog_sidebar = self.driver.find_element(By.XPATH, Locators.catalog_sidebar_xpath)
        action.move_to_element(catalog_sidebar).perform()
        action.click(catalog_sidebar).perform()
        product_sidebar = self.driver.find_element(By.XPATH, Locators.product_sidebar_xpath)
        action.move_to_element(product_sidebar).perform()
        action.click(product_sidebar).perform()
        category_dropdown = self.driver.find_element(By.ID, Locators.search_category_id)
        sel = Select(category_dropdown)
        sel.select_by_visible_text('Jewelry')
        self.driver.find_element(By.ID, Locators.search_product_id).click()
        self.driver.find_element(By.XPATH, Locators.pdf_download_button_xpath).click()

    def go_to_discounts(self):
        action = ActionChains(self.driver)
        promotions_sidebar = self.driver.find_element(By.XPATH, '//a[@href="#"]//i[@class="nav-icon fas fa-tags"]')
        action.move_to_element(promotions_sidebar).perform()
        action.click(promotions_sidebar).perform()
        discounts_sidebar = self.driver.find_element(By.XPATH, "//p[text()=' Discounts']")
        action.move_to_element(discounts_sidebar).perform()
        action.click(discounts_sidebar).perform()
        
    def pick_discounts_startdate(self):
        action = ActionChains(self.driver)
        startdate_box = self.driver.find_element(By.ID, Locators.startdate_box_id)
        action.click(startdate_box).perform()
        action.send_keys_to_element(startdate_box, Keys.NUMPAD1 + Keys.NUMPAD2 + Keys.NUMPAD3 + Keys.NUMPAD1 + Keys.NUMPAD2 + Keys.NUMPAD0 + Keys.NUMPAD0 + Keys.NUMPAD9).perform()
        #action.send_keys_to_element(startdate_box, "12312009").perform()

    def pick_discounts_enddate(self):
        action = ActionChains(self.driver)
        enddate_box = self.driver.find_element(By.ID, Locators.enddate_box_id)
        action.click(enddate_box)
        action.send_keys_to_element(enddate_box, Keys.NUMPAD1 + Keys.NUMPAD2 + Keys.NUMPAD3 + Keys.NUMPAD1 + Keys.NUMPAD2 + Keys.NUMPAD0 + Keys.NUMPAD1 + Keys.NUMPAD9).perform()
        #action.send_keys(enddate_box, "12312019").perform()

    def select_discount_type(self):
        discount_dropdown = self.driver.find_element(By.ID, Locators.discount_dropdown_id)
        sel = Select(discount_dropdown)
        sel.select_by_visible_text('Assigned to order total')

    def click_search_discounts_button(self):
        self.driver.find_element(By.ID, Locators.search_discount_button_id).click()

    def get_discount_table_values(self):
        data = []
        # Define the CSV file path
        csv_file_path = 'discounts_table.csv'

        # Locate the rows in the table body
        discounts_tbody = self.driver.find_element(By.XPATH, '//*[@id="discounts-grid"]/tbody')
        tr = discounts_tbody.find_element(By.XPATH, '//*[@id="discounts-grid"]/tbody/tr')
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
        data.append(row)
    
        # Write the data to the CSV file
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
        return data