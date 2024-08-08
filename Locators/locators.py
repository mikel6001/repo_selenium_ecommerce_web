

class Locators():

    #Login page objects
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    login_button_xpath = '//button[@type="submit"]'
    invalid_username_error_msg_id = 'Email-error'
    #login_error_message_xpath = '//div[@class="message-error validation-summary-errors"]'

    #Home page objects
    logout_button_classname = "nav-link"
    catalog_sidebar_xpath = '//a[@href="#"]//i[@class="nav-icon fas fa-book"]'
    product_sidebar_xpath = "//p[text()=' Products']"

    #Catalog>>Products objects
    search_category_id = "SearchCategoryId"
    search_product_id = "search-products"
    pdf_download_button_xpath = '//button[@name="download-catalog-pdf"]'

    #Promotions>>Discounts object
    discounts_sidebar_xpath = "//p[text()=' Discounts']"
    startdate_box_id = "SearchStartDate"
    enddate_box_id = "SearchEndDate"
    discount_dropdown_id = "SearchDiscountTypeId"
    search_discount_button_id = "search-discounts"
