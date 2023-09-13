from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_item_details(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Kaos hitam polos')
        self.assertContains(response, 20) 
        self.assertContains(response, 'Kaos polos pria berbahan Cotton Combed 30s round neck reguler fit') 
        self.assertContains(response, 50000) 
        self.assertContains(response, 'fashion pria')