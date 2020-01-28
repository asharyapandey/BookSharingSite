from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='books-home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
    path('add/', BookCreateView.as_view(), name='books-add'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='books-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='books-delete'),
]


