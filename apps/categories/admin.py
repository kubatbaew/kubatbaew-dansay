from django.contrib import admin

from apps.categories.models import Category
 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    exclude = ['slug']
