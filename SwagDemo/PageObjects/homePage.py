from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.sortingPrice_low_dropdown_XPATH = '//*[@id="header_container"]/div[2]/div[2]/span/select'
        self.checkItem_link_ID = 'item_2_img_link'
        self.addToCart_button_ID = 'add-to-cart-sauce-labs-onesie'
        self.backToProduct_button_ID = 'back-to-products'
        #adding products
        self.addToCart_tshirt_button_ID = 'add-to-cart-sauce-labs-bolt-t-shirt'
        self.addToCart_backpack_button_ID = 'add-to-cart-sauce-labs-backpack'
        #click cart
        self.shopping_cart_link_XPATH = '//*[@id="shopping_cart_container"]/a'

        #logout
        self.burger_menu_button_ID = 'react-burger-menu-btn'
        self.logout_link_XPATH = '//*[@id="logout_sidebar_link"]'


    def select_Sortingprice(self, SortPrice):
        Select(self.driver.find_element(By.XPATH, self.sortingPrice_low_dropdown_XPATH)).select_by_visible_text(SortPrice)

    def click_image(self):
        self.driver.find_element(By.ID, self.checkItem_link_ID).click()

    def click_AddToCart(self):
        self.driver.find_element(By.ID, self.addToCart_button_ID).click()

    def click_BackToProducts(self):
        self.driver.find_element(By.ID, self.backToProduct_button_ID).click()

    def select_SauceLabsBolt_Tshirt(self):
        self.driver.find_element(By.ID, self.addToCart_tshirt_button_ID).click()

    def select_SauceLabs_Backpack(self):
        self.driver.find_element(By.ID, self.addToCart_backpack_button_ID).click()

    def click_Shopping_Cart(self):
        self.driver.find_element(By.XPATH, self.shopping_cart_link_XPATH ).click()

    def click_Burger_menu(self):
        self.driver.find_element(By.ID, self.burger_menu_button_ID).click()

    def click_Logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_XPATH).click()



