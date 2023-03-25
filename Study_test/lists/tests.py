from django.test import TestCase
from django.urls import resolve
from .views import home_page

from django.http import HttpRequest

class HomeTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_currect(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))

    def test_uses_home_template(self):
        """Проверка что на нужной странице"""
        response = self.client.get('/')
        self.assertTemplateUsed(response,'lists/home.html')
    
    def test_can_save_a_POST(self):
        """Проверка можно ли сохранить пост запрос"""
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response,'lists/home.html')