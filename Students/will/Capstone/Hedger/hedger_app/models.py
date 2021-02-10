from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class API(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    api_key = models.CharField(max_length=50)
    secret_api = models.CharField(max_length=50)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.api_key

class Balances(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    PAX_balance = models.CharField(max_length=60)
    BTC_balance = models.CharField(max_length=60)
    PAX_price = models.CharField(max_length=60, default=0)
    PAX_value = models.CharField(max_length=60, default=0)
    Account_value = models.CharField(max_length=60, default=0)
    date_time = models.CharField(max_length=60, default=0)

    def __str__(self):
        return self.date_time

class APIgets(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    balances = models.CharField(max_length=200)
    ticker = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.date_time

