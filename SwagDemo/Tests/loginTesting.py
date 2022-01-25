import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from SwagDemo.PageObjects.loginPage import LoginPage
from SwagDemo.PageObjects.homePage import HomePage
from SwagDemo.PageObjects.cart_checkoutPage import CartCheckoutPage
from SwagDemo.PageObjects.checkout_info_Page import CheckoutInfo
from SwagDemo.PageObjects.checkout_complete_Page import Checkout_CompletePage


import unittest
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_form_valid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_Username("standard_user")
        login.enter_Password("secret_sauce")
        login.click_Login()

        time.sleep(2)
        home = HomePage(driver)
        home.select_Sortingprice('Price (low to high)')
        home.click_image()
        home.click_AddToCart()
        time.sleep(2)
        home.click_BackToProducts()
        home.select_Sortingprice('Price (low to high)')

        time.sleep(2)

        #adding products

        products = HomePage(driver)
        products.select_SauceLabsBolt_Tshirt()
        products.select_SauceLabs_Backpack()
        products.click_Shopping_Cart()

        # Checkout

        checkout = CartCheckoutPage(driver)
        checkout.click_Checkout()

        #checkout info

        checkout_info = CheckoutInfo(driver)
        checkout_info.enter_FirstName("SAN")
        checkout_info.enter_LastName("JAN")
        checkout_info.enter_Postal_code("12123")
        time.sleep(1)
        checkout_info.click_Continue()

        #finish
        checkout_complete = Checkout_CompletePage(driver)
        checkout_complete.click_Finish()

        #back to home
        checkout_complete.click_BackHome()

        #click logout
        logout = HomePage(driver)
        logout.click_Burger_menu()
        time.sleep(2)
        logout.click_Logout()



    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        print("Testing done!")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/SeleniumPython/SwagDemo/HTML_reports"))