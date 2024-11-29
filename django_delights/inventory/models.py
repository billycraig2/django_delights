from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

    def __str__(self):
        return f'{self.unit_price} for {self.quantity} {self.unit} of {self.name}'
    
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f'{self.price} for {self.title}'
    
    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.quantity} {self.ingredient.unit} of {self.ingredient.name} needed to make {self.menu_item.title}'
    
    class Meta:
        verbose_name = 'Recipe Requirement'
        verbose_name_plural = 'Recipe Requirements'

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.menu_item.title} ordered at {self.timestamp}'
    
    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
