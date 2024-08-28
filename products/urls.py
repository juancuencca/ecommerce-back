from django.urls import path
from .views import ProductDetailView, ProductListView, CategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
]