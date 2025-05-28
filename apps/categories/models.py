from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            # Проверка на уникальность слага
            while Category.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
