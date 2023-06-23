from django.contrib import admin

from blog.models import Category, Post

# Register your models here.
admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}