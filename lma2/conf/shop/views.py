from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

class HomeListView(ListView):
    model = Home
    template_name = 'shop/index.html'
    context_object_name = 'gallerys'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    slug_field = 'slug'