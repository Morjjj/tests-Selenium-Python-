import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#Тест1 - провера работоспособности поиска(textbox,SearchButton) Yandex.ru
options = Options()
options.page_load_strategy = 'normal'

class PythonSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\HomePC\Python\chromedriver', options=options)

    def test_search(self):
        driver = self.driver
        driver.get("http://www.yandex.ru")
        self.assertIn("Яндекс", driver.title)
        try:
            elem = driver.find_element_by_name("text")
            elem.send_keys("Selenium+py")
            driver.find_element_by_css_selector('.button_theme_websearch').click()
            driver.back()
        except:
            print("ButtonSearh not found")

        assert "No results found." not in driver.page_source

def tearDown(self):
    time.sleep(5)
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
