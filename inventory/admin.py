from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# Diciamo a Django Admin di mostrare questi modelli nell'interfaccia di amministrazione
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)


# Register your models here.
