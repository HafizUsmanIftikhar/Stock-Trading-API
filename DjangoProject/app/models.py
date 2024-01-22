from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.username

class StockData(models.Model):
    ticker = models.CharField(max_length=10)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ticker

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='u_id')
    ticker = models.CharField(max_length=10)
    transaction_CHOISES=(
        ('Buy','Buy'),
        ('Sell','Sell'),
    )
    transaction_type = models.CharField(max_length=5, choices=transaction_CHOISES, null=True)
    transaction_volume = models.IntegerField()
    transaction_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.ticker}"
    
