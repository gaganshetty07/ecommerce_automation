import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators.checkoutpage_locators
from locators.checkoutpage_locators import *
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def checkout(self, username, password):
        # Locate the username input field and enter the username
        username_input = self.driver.find_element(By.ID, locators.checkoutpage_locators.username_input)
        username_input.send_keys(username)
        continue_button = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.username_continue)
        continue_button.click()
        time.sleep(5)
        # Locate the password input field and enter the password
        password_input = self.driver.find_element(By.ID, locators.checkoutpage_locators.passwaor_input)
        password_input.send_keys(password)
        sign_in = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.sign_in)
        sign_in.click()
        time.sleep(5)

        #  shipping and payment information

        add_new_address = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.add_address)
        add_new_address.click()
        time.sleep(4)

        full_name = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.name_input)
        full_name.send_keys('Test')
        time.sleep(2)

        mobile = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.mobile_number)
        mobile.send_keys('9990008881')
        time.sleep(2)

        pincode = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.pin_code)
        pincode.send_keys('560079')
        time.sleep(2)

        address = self.driver.find_element(By.XPATH, locators.checkoutpage_locators.address_input)
        address.send_keys('no 31 4th cross vinayakanagar')
        time.sleep(2)

        use_address = self.driver.find_element(By.CSS_SELECTOR,locators.checkoutpage_locators.use_address)

        use_address.click()
        time.sleep(5)

        # for now done only for COD option, others can be implemented here
        cod_select = self.driver.find_element(By.CSS_SELECTOR,locators.checkoutpage_locators.cod_select)

        cod_select.click()
        time.sleep(2)

        use_payment = self.driver.find_element(By.CSS_SELECTOR, locators.checkoutpage_locators.use_payment)
        use_payment.click()

        place_order = self.driver.find_element(By.CSS_SELECTOR, locators.checkoutpage_locators.place_order_button)
        place_order.click()
        time.sleep(5)

        # Verify that the purchase is successful
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,locators.checkoutpage_locators.success_message ))
        )
        assert "Thank you for your purchase!" in confirmation_message.text

