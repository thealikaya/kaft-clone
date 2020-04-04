from django.urls import path

from product.views import category_show

urlpatterns = [
    path('<slug:category_slug>/', category_show, name='category_show'),
]
