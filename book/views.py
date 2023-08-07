from django.shortcuts import render
from book.forms import BookStoreForm

# Create your views here.
def home(request):
    return  render(request, 'store_book.html')

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form':book})
