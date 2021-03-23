import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
#Тест2 - Тест на вход в почтовый ящик yandex.ru
options = Options()
options.page_load_strategy = 'normal'

class PythonTestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\HomePC\Python\chromedriver',options=options)

    def test_Login(self):

        driver = self.driver
        driver.get("http://www.yandex.ru")
        self.assertIn("Яндекс", driver.title)

        wait = WebDriverWait(driver, 10)
        original_window = driver.current_window_handle
        assert len(driver.window_handles) == 1
        driver.find_element_by_class_name('desk-notif-card__card').click()
        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        wait.until(EC.title_is("Авторизация"))
        driver.find_element_by_name("login").send_keys('Name'+ Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("passp-field-passwd").send_keys('password' + Keys.ENTER)
        try:
            assert driver.find_element_by_class_name("passp-form-field__error")
        except NoSuchElementException:
            print("OK")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()