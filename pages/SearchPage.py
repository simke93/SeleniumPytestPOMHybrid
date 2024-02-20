from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_hp_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text", self.valid_hp_product_link_text)
    
        # return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()
    

    def retrive_no_product_message(self):
        return self.retrive_element_text("no_product_message_xpath", self.no_product_message_xpath)
    
        # return self.driver.find_element(By.XPATH, self.no_product_message_xpath).text



