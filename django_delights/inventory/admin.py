from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)
admin.site.register(Purchase)
