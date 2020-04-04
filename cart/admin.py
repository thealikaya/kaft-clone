from django.contrib import admin
from .models import ShoppingCartItem, ShoppingCart

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)