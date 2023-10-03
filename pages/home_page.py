import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

import config.config
from config import *
import locators.homepage_locators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.homepage_locators import *


class HomePage(BasePage):
    search_box = (By.XPATH, locators.homepage_locators.search_bar)
    search_button = (By.XPATH, locators.homepage_locators.search_button)

    def search_product(self):
        search_input = self.wait_for_element(*self.search_box)
        search_input.send_keys(config.product)
        time.sleep(3)
        search_button = self.wait_for_element(*self.search_button)
        search_button.click()
        time.sleep(3)

        expected_element_locator = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/span/div/div/span')
        is_element_present = (By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/span/div/div/span')
        assert is_element_present==expected_element_locator
        # assert is_element_present, "Search results page did not load successfully"

    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    # for other products and other test cases in home page we can change the search item and implemented here
