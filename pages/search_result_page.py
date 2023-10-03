
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import locators.search_resultpage_locators
from pages.base_page import BasePage
from locators  import search_resultpage_locators

class SearchResultsPage(BasePage):
    def select_product(self):
        # Click on the product to view details
        product_link = self.driver.find_element(By.CSS_SELECTOR,locators.search_resultpage_locators.product_link )
        product_link.click()
        time.sleep(3)

        # Switch to the newly opened window (this opens a new tab)
        original_window_handle = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        # Add the product to the cart
        time.sleep(6)
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,locators.search_resultpage_locators.add_to_cart ))
        )
        add_to_cart_button.click()
        time.sleep(5)


        # assertion for testing weather page conatins expected elements or other
        #expected ='locators/elements'
        #current = 'locators/elements'
        #assert expected==current