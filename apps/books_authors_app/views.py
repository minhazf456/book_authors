from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
def index(request):
    context={
        "books" : Book.objects.all()
    }
    return render(request, "books_authors_app/index.html", context)

def add_book(request):
    print("*"*100)
    print("processing new book")
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['text'])
    return redirect('/')

def book_info(request, book_id):
    print('*'*100)
    print("this is the book info page")
    context = {
        'books' : Book.objects.get(id = book_id),
        'authors' : Book.objects.get(id = book_id).authors.all(),
        'all_authors' : Author.objects.all(),
    }
    return render(request, "books_authors_app/book_info.html", context)

def author(request):
    context={
        "authors" : Author.objects.all()
    }
    return render(request, "books_authors_app/author.html", context)

def add_author(request) :
    new_author = Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['text'])
    return redirect('/author')

def author_info(request, author_id):
    print('*'*100)
    print("this is the author info page")
    context = {
        'authors' : Author.objects.get(id = author_id),
        'books' : Author.objects.get(id = author_id).books.all(),
        'all_books' : Book.objects.all(),
    }
    return render(request, "books_authors_app/author_info.html", context)
    



