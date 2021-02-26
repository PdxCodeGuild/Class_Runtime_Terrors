from django.db.models import Model, CharField, DateTimeField, ForeignKey, RESTRICT
from django.utils.timezone import now as t_now, timedelta


class Book(Model):
    title = CharField(max_length=250)
    publish_date = DateTimeField()
    author = ForeignKey('Author', on_delete=RESTRICT)

    def __str__(self):
        return self.title


class Author(Model):
    name = CharField(max_length=250)

    def __str__(self):
        return self.name


class User(Model):
    name = CharField(max_length=250)

    def __str__(self):
        return self.name


class LibraryBook(Model):
    book = ForeignKey('Book', on_delete=RESTRICT)
    user = ForeignKey('User', on_delete=RESTRICT, null=True, blank=True)
    checkout_date = DateTimeField(null=True, blank=True)
    due_date = DateTimeField(help_text="default due date 7 days", null=True, blank=True
                             )

    def __str__(self):
        return f'{self.book} checked out by {self.user}'

    def checkOut(self, user: User, daysCheckedOut=7):
        self.user = user
        self.checkout_date = t_now()
        self.due_date = self.checkout_date + timedelta(daysCheckedOut)

    def checkIn(self):
        self.user = None
        self.checkout_date = None
        self.due_date = None

    def isCheckedOut(self):
        return True if self.checkout_date else False
