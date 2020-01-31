from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View 
from .models import BookDetails
from django.utils.datastructures import MultiValueDictKeyError


def books(request):
    return render(request, 'books/index.html')

class BookListView(ListView):
    context_object_name = 'books'
    template_name = 'books/books.html'

    def get_queryset(self):
        try:
            term = self.request.GET['search']
            messages.info(self.request, f'You Searched for {term}')
            return BookDetails.objects.filter(name__contains = term)
        except MultiValueDictKeyError:
            return BookDetails.objects.all() 



class BookDetailView(DetailView):
    model = BookDetails
    context_object_name = 'book'
    template_name = 'books/books_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = BookDetails
    fields= ['name', 'author', 'publisher', 'pages', 'published_year', 'isbn', 'category', 'description', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookDetails
    fields= ['name', 'author', 'publisher', 'pages', 'published_year', 'isbn', 'category', 'description', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BookDetails
    context_object_name = 'book'
    success_url = reverse_lazy('books-home')

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False

class BookSearchView(View):

    def post(self, request):
        queryset = BookDetails.objects.filter(name = request.POST['search'])
        context_object_name = 'books'
        template_name = 'books/books.html'
