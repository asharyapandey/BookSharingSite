from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BookDetails


def books(request):
    return render(request, 'books/index.html')

class BookListView(ListView):
    model = BookDetails
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = BookDetails
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = BookDetails
    fields= ['name', 'author', 'publisher', 'pages', 'published_year', 'isbn', 'category', 'description', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = BookDetails
    fields= ['name', 'author', 'publisher', 'pages', 'published_year', 'isbn', 'category', 'description', 'image']

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)