from django.contrib.admin import site, ModelAdmin, register
from .models import Book, LibraryBook, Author, User

# site.register(Book)
# site.register(Author)
# site.register(LibraryBook)
site.register(User)


@register(Author)
class AuthorAdmin(ModelAdmin):
    pass


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'publish_date', 'author')


@register(LibraryBook)
class LibraryBookAdmin(ModelAdmin):
    list_display = ('book', 'user', 'checkout_date', 'due_date')
    list_filter = ('user', 'checkout_date')
