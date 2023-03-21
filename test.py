from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_create_and_get_list(self):
        """Создание и получение списка"""

        self.browser.get("http://localhost:8000")

        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')