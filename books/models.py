from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class BookDetails(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 500)
    pages =  models.CharField(max_length = 10)
    published_year = models.CharField(max_length = 4)
    isbn = models.CharField(max_length = 100)
    description = models.TextField()
    CATEGORY_OF_BOOKS =[
        ('E','Educational'),
        ('F','Fiction'),
        ('N','Non-Fiction'),
    ]
    category = models.CharField(max_length = 1, choices = CATEGORY_OF_BOOKS,)
    image = models.ImageField(upload_to='book_images')
    added_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('books-detail', kwargs={'pk' : self.pk})

    class Meta:
        db_table = 'book_details'



class Request(models.Model):
    requested_book = models.ForeignKey(BookDetails, on_delete = models.CASCADE, related_name='requested_book') 
    requested_trade = models.ForeignKey(BookDetails, on_delete = models.CASCADE, related_name='requested_trade')
    is_accepted = models.BooleanField(default = False)

    def __str__(self):
        return  f'requested book is { self.requested_book } trade is { self.requested_trade }'
    
    class Meta:
        db_table = 'request_table'
