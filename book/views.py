from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.
def home(request):
    return render(request,"book-app/home.html")


def add_book(requset):
    if requset.method == 'POST':
         book = BookStoreForm(requset.POST)
         if(book.is_valid):
             book.save()
             return redirect('all-books')
    else:
        book = BookStoreForm()
    return render(requset,'book-app/add-book.html',{'form':book})


def show_all_books(request):
    books = BookStoreModel.objects.all()
    print(books)
    return render(request,"book-app/all-books.html",{'books':books})


def edit_book(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        book = BookStoreForm(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect('all-books')
    return render(request,'book-app/add-book.html',{'form':form})


def delete_book(request,id):
    book = BookStoreModel.objects.get(pk = id).delete()
    
    return redirect("all-books")