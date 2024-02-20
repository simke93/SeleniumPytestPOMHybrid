from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name,locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value )
        return element.is_displayed()
    

    
    def retrive_element_text(self, locator_name,locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text
    

    def get_element(self, locator_name, locator_value):
          element = None
          if locator_name.endswith("_id"):
              element = self.driver.find_element(By.ID, locator_value)
          elif locator_name.endswith("_name"):
              element = self.driver.find_element(By.NAME, locator_value)
          elif locator_name.endswith("_class_name"):
              element = self.driver.find_element(By.CLASS_NAME, locator_value)
          elif locator_name.endswith("_link_text"):
              element = self.driver.find_element(By.LINK_TEXT, locator_value)
          elif locator_name.endswith("_xpath"):
              element = self.driver.find_element(By.XPATH, locator_value)
          elif locator_name.endswith("_css"):
              element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
          return element
    
    # def get_element(self, locator_name, locator_value):
    #     """
    #     Attempts to find an element on the web page based on a locator type and value.
    #     The locator type is determined by the suffix of the locator_name argument.
        
    #     Parameters:
    #     - locator_name: A string indicating the type of locator and its strategy,
    #                     e.g., "search_button_cssselector" for CSS selector.
    #     - locator_value: The actual locator value, e.g., "#search > span > button" for CSS selector.
        
    #     Returns:
    #     - WebElement if found
    #     - None if element is not found or if an exception occurs
    #     """
    #     element = None
    #     try:
    #         locator_strategy = self._get_locator_strategy(locator_name)
    #         # Wait up to 10 seconds for the element to be present
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((locator_strategy, locator_value))
    #         )
    #     except (NoSuchElementException, TimeoutException) as e:
    #         print(f"An error occurred while trying to find the element: {e}")
    #     return element

    # def _get_locator_strategy(self, locator_name):
    #     """
    #     Determines the Selenium By strategy based on the suffix of the locator_name.
        
    #     Parameters:
    #     - locator_name: The name of the locator which includes a suffix indicating the strategy
        
    #     Returns:
    #     - A Selenium By strategy, e.g., By.ID, By.CSS_SELECTOR, etc.
        
    #     Raises:
    #     - ValueError if the suffix does not match any known strategy
    #     """
    #     if locator_name.endswith("_id"):
    #         return By.ID
    #     elif locator_name.endswith("_name"):
    #         return By.NAME
    #     elif locator_name.endswith("_class_name"):
    #         return By.CLASS_NAME
    #     elif locator_name.endswith("_link_text"):
    #         return By.LINK_TEXT
    #     elif locator_name.endswith("_xpath"):
    #         return By.XPATH
    #     elif locator_name.endswith("_css"):
    #         return By.CSS_SELECTOR
    #     else:
    #         raise ValueError(f"Unsupported locator strategy: {locator_name}")
