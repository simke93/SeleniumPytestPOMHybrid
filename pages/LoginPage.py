from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_selector_css = "#content > div > div:nth-child(2) > div > form > input"
    warning_message_selector_css = "#account-login > div.alert.alert-danger.alert-dismissible" 

    def enter_email_address(self, email_address_text):
        self.type_into_element(email_address_text, "email_address_field_id", self.email_address_field_id)

        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address_text)

    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_id", self.password_field_id)

        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_login_btn(self):
        self.element_click("login_button_selector_css", self.login_button_selector_css)

        # self.driver.find_element(By.CSS_SELECTOR, self.login_button_selector_css).click()
        return AccountPage(self.driver)
    
    ##Login method input credentials and click on login button
    def login_to_app(self, email_address_text, password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_login_btn()


    def retrive_warning_message(self):
        return self.retrive_element_text("warning_message_selector_css", self.warning_message_selector_css)
    
        # return self.driver.find_element(By.CSS_SELECTOR, self.warning_message_selector_css).text


    
        