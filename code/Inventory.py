from errors import IngredientValidationError,check_ingredient_validation_error
from errors import AddIngredientToInventoryError
from errors import check_add_ingredient_to_inventory_error
from errors import UpdateStockError, check_update_stock_error
from Ingredient import ingredient

class inventory(object):
    def __init__(self):
        self._stock = {}

    def __str__(self):
        stock = "List of stock:\n"
        for ingredient in self._stock:
            stock.append(f'{ingredient.name} has {ingredient._stock_level} in stock')
        return stock
    
    def add_ingredient(self, ingredient_name, price, item_type, ingredient_type, quantity, stock_level):
        
        '''
        try:
            check_ingredient_validation_error(ingredient, self._ingredients)
        except IngredientValidationError as ive:
            return None, ive.errors
        
        try:
            check_add_ingredient_to_inventory_error(quantity, amount, price)
        except AddIngredientToInventoryError as aitie:
            return None, aitie.errors
        '''

        ingredient = ingredient(ingredient_name, price, item_type, ingredient_type, quantity, stock_level)
        self._stock[ingredient_name] = ingredient
    
    def remove_ingredient(self, ingredient):
        '''
        try:
            check_ingredient_validation_error(ingredient, self._ingredients)
        except IngredientValidationError as ive:
            return None, ive.errors
        '''
        del self._stock[ingredient.name]

    def update_stock(self, ingredient, quantity):
        '''
        try:
            check_ingredient_validation_error(ingredient, self._ingredients)
        except IngredientValidationError as ive:
            return None, ive.errors

        try:
            check_update_stock_error(quantity)
        except UpdateStockError as use:
            return None, use.errors
        '''
        self._stock[ingredient.name].stock_level += quantity

    
    def is_available(self, ingredient):
        '''
        try:
            check_ingredient_validation_error(ingredient, self._ingredients)
        except IngredientValidationError as ive:
            return None, ive.errors
        '''
        return self._stock.has_key(ingredient.name)
    
    @property 
    def stock(self):
        return self._stock