import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_form_valid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
        #work on filter for sorting prices
        time.sleep(2)
        Sorting_Price = Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select'))
        Sorting_Price.select_by_visible_text('Price (low to high)')
        #check item
        driver.find_element(By.ID, 'item_2_img_link').click()
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        driver.find_element(By.ID, 'back-to-products').click()
        Sorting_Price = Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select'))
        Sorting_Price.select_by_visible_text('Price (low to high)')
        time.sleep(2)
        #adding products
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        #Checkout
        driver.find_element(By.ID, 'checkout').click()
        #checkout info
        driver.find_element(By.ID, 'first-name').send_keys("Hola")
        driver.find_element(By.ID, 'last-name').send_keys("bola")
        driver.find_element(By.ID, 'postal-code').send_keys("99999")
        driver.find_element(By.ID, 'continue').click()
        time.sleep(2)
        #finish
        driver.find_element(By.ID, 'finish').click()
        #back to home
        driver.find_element(By.ID, 'back-to-products').click()
        #click logout
        driver.find_element(By.ID, 'react-burger-menu-btn').click()
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        print("Testing done!")



if __name__ == '__main__':
    unittest.main()