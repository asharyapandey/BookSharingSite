from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View 
from .models import BookDetails, Request
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required


class BookListView(ListView):
    context_object_name = 'books'
    template_name = 'books/books.html'
    paginate_by = 6

    def get_queryset(self):
        try:
            term = self.request.GET['search']
            messages.info(self.request, f'You Searched for {term}')
            return BookDetails.objects.filter(name__icontains = term)
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

@login_required(login_url='/users/login/')
def request(request, id):
    book = BookDetails.objects.get(id = id)
    requested_to = User.objects.filter(id = book.added_by.id)
    requested_trades = BookDetails.objects.filter(added_by = request.user)
    context = {
        'requested_book' : book,
        'requested_trades' : requested_trades,
    }
    if request.method == 'POST':
        requested_by = User.objects.get(username = request.POST['requested_by'])
        rtrade = request.POST['requested_trade']
        requested_trade = BookDetails.objects.get(name = rtrade, added_by = requested_by.id)
        #check to see if the book has already been requested
        try:
            new_request = Request.objects.get(requested_book = book, requested_trade = requested_trade)
            messages.warning(request, f'You have already requested this book')
            return redirect('books-home')
        except Request.DoesNotExist:
            new_request = Request(requested_book = book, requested_trade = requested_trade)
            new_request.save()
            messages.warning(request, f'Requested: {book.name}')
            return redirect('books-home')
    return render(request, 'books/request.html', context)

def request_delete(request, id):
    requested = Request.objects.get(id = id)    
    if request.method == 'POST':
        requested.delete()
        return redirect('profile', username = request.user.username)
    context = {
        'requested' : requested
    }
    return render(request, 'books/request_delete.html', context)

def request_update(request, id):
    current_request = Request.objects.get(id = id)
    book = BookDetails.objects.get(id = current_request.requested_book.id)
    requested_trades = BookDetails.objects.filter(added_by = request.user)
    context = {
        'requested_book' : book,
        'requested_trades' : requested_trades,
        'current_request' : current_request,
    }
    if request.method == 'POST':
        requested_by = User.objects.get(username = request.POST['requested_by'])
        rtrade = request.POST['requested_trade']
        requested_trade = BookDetails.objects.get(name = rtrade, added_by = requested_by.id)
        current_request = Request.objects.get(id = id)
        current_request.requested_trade = requested_trade
        current_request.save()
        return redirect('books-home')
    return render(request, 'books/request_update.html', context)

class BookFilterView(ListView):
    context_object_name = 'books'
    template_name = 'books/books.html'
    paginate_by = 6

    def get_queryset(self):
        return BookDetails.objects.filter(category=self.kwargs['category'])