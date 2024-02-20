from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)



    account_creation_message_xpath = "//div[@id='content']/h1"


    def retrive_account_creation_msg(self):
        return self.retrive_element_text("account_creation_message_xpath", self.account_creation_message_xpath)
    

        # return self.driver.find_element(By.XPATH, self.account_creation_message_xpath).text