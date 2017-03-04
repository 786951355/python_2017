from django.contrib import admin

# Register your models here.

from .models import Article, Author, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_date')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)