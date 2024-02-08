from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.forms import PostCreateForm, ReviewForm, CategoryForm
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
    form = ReviewForm()
    if request.method == 'GET':
        posts = Book.objects.get(id=post_id)
        return render(request, "post/details.html",
                      context={'posts': posts, 'review_form': form})


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


def post_create_view(request):
    if request.method == "GET":
        context = {'form': PostCreateForm()
                   }
        return render(request, 'post/create.html', context=context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('list')
        context = {'form': form}

        return render(request, 'post/create.html', context=context)


def review_create_view(request, post_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.post_id = post_id
            review.save()

        return redirect('details', post_id=post_id)


def category_create_view(request):
    if request.method == 'GET':
        context = {"form": CategoryForm()}
        return render(request, 'post/category_create.html', context=context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category')
        context = {
            "form": form
        }
        return render(request, 'post/category_create.html', context=context)
