from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book
from .calc_operations import calc_object

# тут описывается, все что будет отобрвжвться на страницах сайта


def index(request):
    ctx = {}
    ctx['a'] = 45
    all_books = Book.objects.all() # select * from app
    ctx['all_books'] = all_books
    for book in all_books:
        print (book.title)
    return render(request, 'index.html', ctx)

def calculator(request):
    ctx = {}
    ctx['operations'] = calc_object.keys()

    if request.method == 'GET':
        print(calc_object.keys())
    elif request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num'))
            operation = request.POST.get('operation')
            second_num = float(request.POST.get('second_num'))
            result = calc_object[operation](first_num, second_num)
            ctx['msg'] = result
        except(ValueError, ZeroDivisionError, ) as e:
            ctx['msg'] = e

    return render(request, 'calculator.html', ctx)