import os
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import  config
from pages.home_page import HomePage
from pages.search_result_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestEcommercePurchase(unittest.TestCase):

    def setUp(self):
        ## to initialize driver from relative path but its not working as expected

        # current_directory = os.path.dirname(__file__)
        # relative_chromedriver_path = os.path.join(current_directory, "drivers", "chromedriver.exe")
        # self.driver = webdriver.Chrome(executable_path=relative_chromedriver_path)

        #initializing driver from absolute path
        chromedriver_path = config.driver_path
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.implicitly_wait(1)
        self.base_url = config.url
        # self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

    def test_purchase_product(self):
        home_page = HomePage(self.driver)
        home_page.search_product()

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.select_product()

        cart_page = CartPage(self.driver)
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.checkout(config.username,config.password)

        self.assertTrue(checkout_page, f"Purchase for product failed")



if __name__ == '__main__':
    unittest.main()


