from django.db import models

# 1. INGREDIENTI
# Questo modello rappresenta il magazzino degli ingredienti disponibili per la preparazione dei piatti.
# Esempio : "Uova", quantità 100, prezzo unitario : 0.50
class Ingredient(models.Model):
    name = models.CharField(max_lenghth=200)
    quantity = models.FloatField(default=0)  # Quantità disponibile in magazzino
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
# 2 MENU
# Questo modello rappresenta il menu del ristorante, con i piatti disponibili.
# Esempio : "Spaghetti alla Carbonara", prezzo: 12.00
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    def __str__(sefl):
        return self.title
    
# 3 RICETTA (collegamento tra MenuItem e Ingredient)
# Questo dice: "Per fare una carbonara (MenuItem), ho bisogno di 100g di pasta (Ingredient), 50g di guanciale (Ingredient), 1 uovo (Ingredient), 30g di pecorino (Ingredient)")    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)        
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0) # Quantità necessaria per preparare il piatto

    def __str__(self):
        return f"Order: {self.menu.title}"
    
