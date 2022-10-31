from django.contrib import admin

from .models import Category,Product

admin.site.register(Category)
#admin.site.register(Product)
#dmin.site.register(Brand)  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['name', 'price']
    #list_display_links = ['name',]
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['category']