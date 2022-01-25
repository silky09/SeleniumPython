from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textarea_ID = 'user-name'
        self.password_textarea_ID = 'password'
        self.login_button_ID = 'login-button'

    def enter_Username(self, Username):
        self.driver.find_element(By.ID, self.username_textarea_ID).send_keys(Username)

    def enter_Password(self, Password):
        self.driver.find_element(By.ID, self.password_textarea_ID).send_keys(Password)

    def click_Login(self):
        self.driver.find_element(By.ID, self.login_button_ID).click()