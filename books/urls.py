from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView

from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='books-home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
    path('add/', BookCreateView.as_view(), name='books-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='books-update'),
]


