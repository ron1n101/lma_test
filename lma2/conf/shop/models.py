from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Home(models.Model):
    title = models.CharField(max_length=64, db_index=True, blank=True)
    image_main = models.ImageField(upload_to='shop/images/home_gallery', null=True)
    image_second = models.ImageField(upload_to='shop/images/home_gallery', null=True)
    image_third = models.ImageField(upload_to='shop/images/home_gallery', null=True)
    pass


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    title = models.CharField(max_length=128, db_index=True, blank=True)
    desc = models.TextField(blank=True)
    stock = models.IntegerField(null=True)
    size = models.ManyToManyField('ProductSize', related_name='product_size')
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    slug = models.SlugField(unique=True)
    poster = models.ImageField(upload_to='shop/images/poster')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class ProductSize(models.Model):
    # SIZES = [
    #     ('SMALL', 'SMALL'),
    #     ('MEDIUM', 'MEDIUM'),
    #     ('LARGE', 'LARGE'),
    # ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(null=True)
    size = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    is_available = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class ProductImage(models.Model):
    name = models.CharField('Заголовок', max_length=128, blank=False)
    product = models.ForeignKey(Product, related_name='image_product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/images/prod_detail_img')

    class Meta:
        verbose_name = 'Фото Товара'
        verbose_name_plural = 'Фото Товаров'

    def __str__(self):
        return self.name
