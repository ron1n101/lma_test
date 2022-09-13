from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='products_list'),
    # path('<slug:slug>/', views.ProductDetailView.as_view(), name = 'prod_detail'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact', views.feedback, name='feedback')
]
