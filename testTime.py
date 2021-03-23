import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Тест3 - Проверка обновления секции часов(минуты).
options = Options()
options.page_load_strategy = 'normal'

class PythonTestTimeMinute(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\HomePC\Python\chromedriver',options=options)

    def test_Minute(self):

        driver = self.driver
        driver.get("http://www.yandex.ru")
        self.assertIn("Яндекс", driver.title)
        TimeMin = driver.find_element_by_class_name("datetime__min")
        TimeMin1 = TimeMin.get_attribute("textContent")
        i = 0
        while time.sleep(i) == time.sleep(i):
            if TimeMin.get_attribute("textContent") == TimeMin1:
                i = i + 1
                print(i)
            else:
                print('Current time: '+TimeMin.get_attribute("textContent"),'Past time: '+TimeMin1, "OK")
                break
            if i > 60:
                print("Clock is broken")
                break

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()