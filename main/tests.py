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
        self.assertContains(response, 'Goodang Page')
        self.assertContains(response, "Syauqi Armanaya Syaki") 
        self.assertContains(response, 'PBP D')