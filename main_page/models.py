from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name



#Таблица продуктов
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_specification = models.TextField()
    product_image = models.ImageField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

#Таблица корзины пользователя
class UserCart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField()



