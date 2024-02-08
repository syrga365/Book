from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from post.models import Book, Category

# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, It's my project")


def current_date_view(request):
    if request.method == 'GET':
        current_datetime = datetime.now()
        return HttpResponse(current_datetime)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Good bye, user!!!")


def post_list_view(request):
    if request.method == 'GET':
        print(request.user)
        posts = Book.objects.all()
        return render(request, "post/list.html",
                      context={'posts': posts})


def post_details_view(request, post_id):
    if request.method == 'GET':
        posts = Book.objects.get(id=post_id)
        return render(request, "post/details.html",
                      context={'posts': posts})


def category_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, "post/category.html",
                      context={'categories': category})


def category_details_view(request, category_id):
    if request.method == 'GET':
        categories = Category.objects.filter(id=category_id)
        posts = Book.objects.filter(category__in=categories)
        return render(request, "post/category_details.html",
                      context={'categories': categories, "posts": posts})

