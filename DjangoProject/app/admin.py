from django.contrib import admin

# Register your models here.
from .models import Users,Transactions, StockData

admin.site.register(Users)
admin.site.register(Transactions)
admin.site.register(StockData)