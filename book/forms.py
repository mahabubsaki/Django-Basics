from django import forms
from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        exclude = ['first_pub','last_pub']
        labels = {
            'id':'Book ID',
            'book_name': 'Book Name',
            'author': 'Book Author',
            'category': 'Book Category',
        }
        widgets= {
            'id':forms.NumberInput(attrs={'class':'input input-bordered w-full'}),
            'book_name':forms.TextInput(attrs={'class':'input input-bordered w-full'}),
            'author':forms.TextInput(attrs={'class':'input input-bordered w-full'}),
            'category':forms.Select(attrs={'class':'select select-bordered w-full'})
        }