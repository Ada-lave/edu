from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitor(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def check_row_in_list_table(self, row_text):
        '''функция для потдверждения наличия текста в таблице'''
        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_create_and_get_list(self):
        """Создание и получение списка"""

        self.browser.get("http://localhost:8000")

        self.assertIn('To-Do lists', self.browser.title)

        header_text = self.browser.find_element('tag name','h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element('id','id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),\
                         'Enter a to-do item')
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element('id','id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_row_in_list_table('1: Купить павлиньи перья')
        self.check_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')