from django import forms
from post.models import Book, Review, Category


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'photo', 'content', 'author', 'category')
        labels = {
            'title': "Название",
            "photo": "Фото",
            "content": "Описание",
            "author": "Автор",
            "category": "Категория",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        labels = {'content': "Контент", }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        labels = {
            'title': "Категория"
        }
