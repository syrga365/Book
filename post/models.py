from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", null=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name="category")


class Review(models.Model):
    post = models.ForeignKey(
        'post.Book',
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


