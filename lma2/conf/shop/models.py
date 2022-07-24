from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
    

class Home(models.Model):
    title = models.CharField(max_length=64, blank=False)
    image = models.ImageField(upload_to='shop/image/home_gallery')

    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    title = models.CharField(max_length=128, db_index=True, blank=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    available = models. BooleanField(default=True)
    slug = models.SlugField(unique=True)
    poster = models.ImageField(upload_to='shop/images/poster')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title





class ProductImage(models.Model):
    name = models.CharField('Заголовок', max_length=128)
    product = models.ForeignKey(Product, related_name='image_product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/images/prod_detail_img')

    class Meta:
        verbose_name = 'Фото Товара'
        verbose_name_plural = 'Фото Товаров'

    def __str__(self):
        return self.name

