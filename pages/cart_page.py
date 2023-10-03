import time
from selenium.webdriver.common.by import By

import locators.cartpage_locators
from locators.cartpage_locators import *
from pages.base_page import BasePage

class CartPage(BasePage):


    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, locators.cartpage_locators.proceed_button)
        checkout_button.click()
        time.sleep(6)

        # assertion for testing
        # expected_checkout_page='locaotrs'
        # checkout_page='locators'
        # assert expected_checkout_page==checkout_page
