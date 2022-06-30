from django.contrib import admin
from .models import Customer
# Register your models here.

#classe para regisrar e exibir objetos no DB
@admin.register(Customer)
class CustumerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email"]