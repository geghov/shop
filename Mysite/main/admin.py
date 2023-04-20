from django.contrib import admin
from .models import Carusel, CategoryL0, CategoryL1, Product, Contact

# Register your models here.
admin.site.register(Carusel)
admin.site.register(CategoryL0)

@admin.register(CategoryL1)
class CategoryL1Admin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'category']
    list_display_links = ['name', 'category']
    search_fields = ['name', 'category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'head', 'price', 'cotegory', 'availability', 'condition']
    list_display_links = ['head', 'price']
    search_fields = ['head', 'price', 'cotegory', 'availability', 'condition']

@admin.register(Contact)
class CategoryL1Admin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'email', 'subject']
    list_display_links = ['name', 'email', 'subject']
    search_fields = ['name', 'email', 'subject', 'message']