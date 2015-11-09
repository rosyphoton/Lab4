from django.contrib import admin
from books.models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorID', 'Name', 'Age', 'Country')
#    search_fields = ('Name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'Title', 'AuthorID', 'Publisher', 'PublishDate', 'Price')
#    list_filter = ('PublishDate',)
#    date_hierarchy = 'PublishDate'
#    ordering = ('-PublishDate',)
#    filter_horizontal = ('AuthorID',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)