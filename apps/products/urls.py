from django.urls import path

from apps.products.views import homepage, list_products, search_logics

urlpatterns = [
    path('', homepage, name="homepage"),
    path('products/<int:pk>', list_products, name="list_products"),
    path('search/', search_logics, name="search_logics"),
]
