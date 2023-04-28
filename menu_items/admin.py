from django.contrib import admin

from . import models


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'menu')


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
