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
    list_display = ['category','title', 'price', 'slug']
    list_filter = ['price', 'category']
    list_editable = ['price']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ProductImageInLine]

# @admin.register(ProductSize)
# class ProductSizesAdmin(admin.ModelAdmin):
#     model = ProductSize
#

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'size', 'is_available']
    list_filter = ['product', 'size', 'count', 'is_available']
    list_editable = ['count', 'is_available']