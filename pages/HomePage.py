from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage

from pages.SearchPage import SearchPage



class HomePage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_cssselector_css = "#search > span > button"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    registration_option_link_text = "Register"

    def enter_product_into_search_box_field(self,product_name):
        self.type_into_element(product_name, "search_box_field_name", self.search_box_field_name)

        # self.driver.find_element(By.NAME, self.search_box_field_name).click()
        # self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        # self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.element_click("search_button_cssselector_css", self.search_button_cssselector_css)
        # self.driver.find_element(By.CSS_SELECTOR, self.search_button_cssselector_css).click()
        return SearchPage(self.driver)
    
    def click_on_my_account_drop_menu(self):

        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

        # self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_on_login_option(self):
        self.element_click("login_option_link_text", self.login_option_link_text)

        # self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)
    
    #method to combine two actions 
    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_login_option()
    
    def click_on_register_option(self):
        self.element_click("registration_option_link_text", self.registration_option_link_text)
        # self.driver.find_element(By.LINK_TEXT, self.registration_option_link_text).click()
        return RegisterPage(self.driver)
    
    #method to navigate to register page 
    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_register_option()

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()
        #return SearchPage(self.driver)
    
