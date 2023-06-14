from django.contrib import admin

from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'category', 'show')
    list_editable = ('phone', 'email', 'category', 'show')
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone',)
    list_per_page = 10
    list_max_show_all = 50


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
