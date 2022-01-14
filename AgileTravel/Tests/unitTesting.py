import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class FormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://travel.agileway.net/login")
        print("Title of the page: ", driver.title)

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        print("Form Automated!")

if __name__ == '__main__':
    unittest.main()


