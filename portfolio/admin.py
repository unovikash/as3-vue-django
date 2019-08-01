from django.contrib import admin
from .models import Customer, Investment, Stock

class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'email', 'cell_phone')
    list_filter = ('city',)
    search_fields = ('cust_number', 'name', 'email')
    ordering = ['cust_number']


class InvestmentList(admin.ModelAdmin):
    list_display = ('customer', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('customer', 'category')
    ordering = ['customer']


class StockList(admin.ModelAdmin):
    list_display = ('customer','symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('name',)
    search_fields = ('customer','symbol', 'name')
    ordering = ['customer']


admin.site.register(Customer, CustomerList)
admin.site.register(Investment, InvestmentList)
admin.site.register(Stock, StockList)