from django.contrib import admin
from .models import Product, Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_available', 'brand')
    list_filter = ('is_available', 'brand')
    search_fields = ('title', 'brand__title')
    ordering = ('brand__title',)


class BrandAdmin(admin.ModelAdmin):
    list_filter = ('nationality',)
    search_fields = ('title',)
    ordering = ('title',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
