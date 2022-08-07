from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}




@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title']
    


class ProductImageInLine(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title', 'price', 'available', 'slug']
    list_filter = ['available', 'price', 'category']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ProductImageInLine]