from Inventory import inventory
from Ingredient import ingredient
from errors import IngredientValidationError, check_ingredient_validation_error
from errors import AddIngredientToItemError, check_add_ingredient_to_item_error

class item(object):
    
    def __init__(self, ingredients, item_type):
        ''' item is only main side or drink '''
        self._ingredients = ingredients
        self._item_type = item_type
        self._price = 0

             
    def add_ingredient(self, ingredient, inventory):
        #need to somehow implement a check that the ingredient is the right type
        # so you cant add a drink to a burger type item
        # check valid ingredient (is in inventory)
        #check that ingredient is of right type
        if not inventory.has_key(ingredient_name):
            return None

        ingredient = inventory.stock[ingredient_name]    
        
        self._ingredients.append(ingredient)
        self._price += ingredient.price
        inventory.update_stock(ingredient, -1)

    
    def remove_ingredient(self, ingredient_name):
         if not inventory.has_key(ingredient_name):
            return None

        ingredient = inventory.stock[ingredient_name]
        
        self._ingredients.remove(ingredient)
        self.price -= ingredient.price
        inventory.update_stock(ingredient, +1)        
    
    @property
    def ingredients(self):
        return self._ingredients
    
    @property
    def price(self):
        return self._price
    
    @property
    def item_type(self):
        return self._item_type
    
    def __str__(self):
        string = f"{self._item_type} contains:\n"
        for ingredient in self._ingredients:
            string.append(f"{ingredient.quantity} : {ingredient.name}\n")
        return string

    

    
