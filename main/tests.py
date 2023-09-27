from django.test import TestCase, Client
from django.urls import reverse
from main.models import Item
from django.contrib.auth.models import User 
from datetime import datetime

# Get the current datetime and format it as a string
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_html_details(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='your_username',
            password='your_password'
        )
        self.client.login(username='your_username', password='your_password')
        self.client.cookies['last_login'] = current_datetime
        response = self.client.get('')
        self.assertContains(response, 'Goodang Page')
        self.assertContains(response, 'PBP D')

    def setUp(self):
        # Membuat pengguna untuk pengujian
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Membuat beberapa item
        self.item1 = Item.objects.create(
            user=self.user,
            owner='Owner 1',
            item_name='Item 1',
            category='Category 1',
            amount=5,
            price=10,
            description='Description 1'
        )

        self.item2 = Item.objects.create(
            user=self.user,
            owner='Owner 2',
            item_name='Item 2',
            category='Category 2',
            amount=3,
            price=15,
            description='Description 2'
        )

    def test_show_main_view(self):
        # Menggunakan self.client untuk mengakses URL
        user01 = Item.objects.get(owner="Owner 1")
        user02 = Item.objects.get(owner="Owner 2")
        self.assertEqual(user01.user, self.user)
        self.assertEqual(user02.user, self.user)
        self.assertEqual(user01.item_name, "Item 1")
        self.assertEqual(user02.item_name, "Item 2")
        self.assertEqual(user01.category, "Category 1")
        self.assertEqual(user02.category, "Category 2")
        self.assertEqual(user01.amount, 5)
        self.assertEqual(user02.amount, 3)
        self.assertEqual(user01.price, 10)
        self.assertEqual(user02.price, 15)
        self.assertEqual(user01.description, "Description 1")
        self.assertEqual(user02.description, "Description 2")