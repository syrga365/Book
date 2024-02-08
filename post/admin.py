from django.contrib import admin
from post.models import Book, Category, Review
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    fields = ["id", "title", "photo", "content", 'author', "rate", 'category', "created_at", "updated_at"]
    readonly_fields = ["id", "created_at", "updated_at"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']


admin.site.register(Review)
