from django.urls import path
from .views import product_page, product_create, lookup_view, product_delete, products_display

app_name = "shop"

urlpatterns = [
    path("", product_page),
    path('create/', product_create),#POST
    path("lookup/<int:my_id>/", lookup_view, name='lookup'),#GET
    path("delete/<int:my_id>/", product_delete, name="delete"),#DELETE
    path("all/", products_display)#GET
]
