from selenium.webdriver.common.by import By


class Checkout_CompletePage():

    def __init__(self, driver):
        self.driver = driver
        self.finish_button_ID = 'finish'
        self.backHome_button_ID = 'back-to-products'

    def click_Finish(self):
        self.driver.find_element(By.ID, self.finish_button_ID).click()

    def click_BackHome(self):
        self.driver.find_element(By.ID, self.backHome_button_ID ).click()




