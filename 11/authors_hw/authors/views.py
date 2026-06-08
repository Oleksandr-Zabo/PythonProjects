from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book


def home(request):
    return render(request, 'authors/home.html', {'title': 'Головна'})


def writer_list(request):
    writers = Author.objects.all().order_by('name')
    return render(request, 'authors/writer_list.html', {'title': 'Письменники', 'writers': writers})


def writer_detail(request, writer_slug):
    # Task 5: Handle query parameters for books by year
    year = request.GET.get('year')
    if year:
        author = get_object_or_404(Author, slug=writer_slug)
        books_by_year = author.books.filter(year=year).order_by('title')
        if books_by_year.exists():
            return render(request, 'authors/books_by_year.html', {
                'title': f'Книги {author.name} за {year} рік',
                'author': author,
                'year': year,
                'books': books_by_year
            })
        else:
            # Redirect to writer detail page if no books for the year
            return redirect('writer_detail', writer_slug=writer_slug)

    # Task 2: Display writer details
    author = get_object_or_404(Author, slug=writer_slug)
    books = author.books.all().order_by('title')
    return render(request, 'authors/writer_detail.html', {'title': author.name, 'author': author, 'books': books})


def book_list(request):
    books = Book.objects.all().order_by('-rating', 'title')
    return render(request, 'authors/book_list.html', {'title': 'Топ найкращих книг', 'books': books})


def book_detail_by_rating(request, rating):
    # Task 3: Display book details by rating
    try:
        book = Book.objects.get(rating=rating)
    except Book.DoesNotExist:
        return redirect('book_list') # Redirect if book at rating not found
    return render(request, 'authors/book_detail.html', {'title': book.title, 'book': book})


def book_detail_by_writer_and_slug(request, writer_slug, book_slug):
    # Task 4: Display book details by writer and book slug
    author = get_object_or_404(Author, slug=writer_slug)
    try:
        book = author.books.get(slug=book_slug)
    except Book.DoesNotExist:
        return redirect('writer_detail', writer_slug=writer_slug) # Redirect to writer detail if book not found
    return render(request, 'authors/book_detail.html', {'title': book.title, 'book': book})


# Author CRUD Views
class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'slug', 'bio', 'birth_year', 'death_year']
    template_name = 'authors/author_form.html'
    success_url = reverse_lazy('writer_list')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'slug', 'bio', 'birth_year', 'death_year']
    template_name = 'authors/author_form.html'
    success_url = reverse_lazy('writer_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = reverse_lazy('writer_list')


# Book CRUD Views
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'slug', 'author', 'year', 'description', 'rating']
    template_name = 'authors/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'slug', 'author', 'year', 'description', 'rating']
    template_name = 'authors/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'authors/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
