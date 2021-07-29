from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *
from product.class_views import SearchListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/update/<int:id>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>', ProductDeleteView.as_view(), name='update_product'),
    path('search', SearchListView.as_view(), name='search'),

]