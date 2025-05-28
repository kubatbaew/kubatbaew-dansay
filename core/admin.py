from django.contrib import admin

from django.contrib.auth.models import User, Group


admin.site.unregister(Group)

admin.site.site_title = "Дансай Администативная панель"


custom_admin = admin
