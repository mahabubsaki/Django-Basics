from django.urls import path
from book.views import home,add_book,show_all_books,edit_book,delete_book
# from . import views

urlpatterns = [
    path('',home,name="book-home"),
    #shortcut
    # path('',views.HomeClassView.as_view(template_name='book-app/home.html')),
    path('all-books/',show_all_books,name="all-books"),
    path('add-book/',add_book,name="add-book"),
    path('edit-book/<int:id>',edit_book,name="edit-book"),
    path('delete-book/<int:id>',delete_book,name="delete-book")
]