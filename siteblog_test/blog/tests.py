from django.test import TestCase
from .models import Tag
from django.test import Client


class TestTag(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(title='city')


    def tearDown(self):
        print('я выполняюсь после')


    def test_str(self):
        self.tag = Tag(title='city')
        self.assertEqual(str(self.tag), 'city')


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(title='city')


    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        text = response.content.decode(encoding='utf-8')
        self.assertTrue('Home' in text)



        print(response.context)
        self.assertTrue('object_list' in response.context)
        self.assertTrue('title' in response.context)
        self.assertEqual(response.context['title'], 'Classic Blog Design')