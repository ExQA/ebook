from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book


def index(request):
    ctx = {}
    ctx['a'] = 45
    all_books = Book.objects.all() # select * from app
    ctx['all_books'] = all_books
    for book in all_books:
        print (book.title)
    return render(request, 'index.html', ctx)

def calc(request):
    return HttpResponse('Calclcl ldkgodpfgk ')