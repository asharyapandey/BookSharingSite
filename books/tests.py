from django.test import TestCase
from .models import BookDetails, Request
from django.contrib.auth.models import User

class ModelsTestCase(TestCase):

    def setUp(self):
        #creating users
        user1 = User.objects.create(
            username ='testUser',
            password = 'testUser',
            email = 'testUser@test.com'
        )
        user2 = User.objects.create(
            username ='testUser1',
            password = 'testUser1',
            email = 'testUser1@test.com'
        )
        # creating books
        book_1 = BookDetails.objects.create(
            name='test1',
            author='test1',
            description='test1',
            publisher ='test1',
            published_year = 1998,
            pages=200,
            category='E',
            image = 'image.jpg',
            added_by = user1
        )
        book_2 = BookDetails.objects.create(
            name='test2',
            author='test2',
            description='test2',
            publisher ='test2',
            published_year = 1998,
            pages=200,
            category='E',
            image = 'image.jpg',
            added_by = user2
        )

        #creating book requests
        request_1 = Request.objects.create(
            requested_book = book_1,
            requested_trade = book_1,
        )
        request_2 = Request.objects.create(
            requested_book = book_1,
            requested_trade = book_2,
        )

    def test_valid_request(self):
        b1 = BookDetails.objects.get(name = 'test1')
        b2 = BookDetails.objects.get(name = 'test1')
        r = Request.objects.get(requested_book = b1, requested_trade = b1)
        self.assertTrue(r.is_valid_request())

    def test_valid_request_two(self):
        b1 = BookDetails.objects.get(name = 'test1')
        b2 = BookDetails.objects.get(name = 'test2')
        r = Request.objects.get(requested_book = b1, requested_trade = b2)
        self.assertTrue(r.is_valid_request())

