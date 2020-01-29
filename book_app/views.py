from django.shortcuts import render,redirect
from .models import Book,Author
def index(request):
    context={
        "library":Book.objects.all()
    }
    return render(request,"index.html",context)

def create_book(request):
    new_title= request.POST["title"]
    new_desc= request.POST["description"]
    Book.objects.create(title=new_title,description=new_desc)
    return redirect('/')

def show_books(request,book_id):
    book=Book.objects.get(id=book_id)
    all_authors = Author.objects.all()
    context={
        "book":book,
        "all_authors": all_authors
    }
    return render (request,"books.html",context)

def add_author(request,book_id):
    book=Book.objects.get(id=book_id)
    author=Author.objects.get(id = request.POST['author_id'])
    book.authors.add(author)
    return redirect('/')

def author(request):
    context={
        "authors":Author.objects.all()
    }
    return render(request, "author.html",context)

def create_author(request):
  new_name= request.POST["firstname"] 
  new_shim= request.POST["last_name"] 
  new_notes= request.POST["notes"] 
  Author.objects.create(first_name =new_name, last_name=new_shim,notes=new_notes) 
  return redirect('/')
  
def show_authors(request,author_id):
    author=Author.objects.get(id=author_id)
    all_books= Book.objects.all()
    context={
      "author" :author,
      "all_books":all_books 
    }
    return render(request,"authors.html",context)

def add_book(request,author_id):
    author=Author.objects.get(id=author_id)
    book=Book.objects.get(id=request.POST[book_id])
    author.books.add(books)
    return redirect('/')