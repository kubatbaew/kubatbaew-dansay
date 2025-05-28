from django.db import models

from apps.categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="products_cats",
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображения"
    )
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание",
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Цена"
    )
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
