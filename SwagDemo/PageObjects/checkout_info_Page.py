from selenium.webdriver.common.by import By


class CheckoutInfo():

    def __init__(self, driver):
        self.driver = driver
        self.firstName_textarea_ID = 'first-name'
        self.lastName_textarea_ID = 'last-name'
        self.postalCode_textarea_ID = 'postal-code'
        self.continue_button_ID = 'continue'

    def enter_FirstName(self, FirstName):
        self. driver.find_element(By.ID, self.firstName_textarea_ID).send_keys(FirstName)

    def enter_LastName(self, LastName):
        self. driver.find_element(By.ID, self.lastName_textarea_ID).send_keys(LastName)

    def enter_Postal_code(self, Postal_code):
        self. driver.find_element(By.ID, self.postalCode_textarea_ID).send_keys(Postal_code)

    def click_Continue(self):
        self.driver.find_element(By.ID, self.continue_button_ID).click()


