from selenium.webdriver.common.by import By


class CartCheckoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button_ID = 'checkout'

    def click_Checkout(self):
        self.driver.find_element(By.ID, self.checkout_button_ID).click()

