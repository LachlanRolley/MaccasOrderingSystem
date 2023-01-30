from .Ingredient import ingredient

class inventory(object):
    def __init__(self):
        self._stock = {}

    def __str__(self):
        stock = "List of stock:\n"
        for ingredient in self._stock:
            stock += (f'{ingredient}')
        return stock
    
    def add_ingredient(self, name, prices, serving_sizes, stock_level, measuring_unit, ingredient_type):

        new_ingredient = ingredient(name, prices, serving_sizes, stock_level, measuring_unit, ingredient_type)
        self._stock[name] = new_ingredient
    
    def remove_ingredient(self, ingredient_name):
        del self._stock[ingredient_name]
    
    
    def increment_stock(self, ingredient_name, quantity):
        #need to check ingredient name is legit
        self._stock[ingredient_name].increment_stock(quantity)
    
    def decrement_stock(self, ingredient_name, quantity, serving_size):
        #need to check ingredient name is legit
        self._stock[ingredient_name].decrement_stock(quantity, serving_size)
    
    def get_menu(self):
        #this function is a bit messy and needs to be defnied better
        maxes = {}
        base_ingredient_type = {}
        serving_sizes = {}
        base_ingredient_name = {}
        for ingredient_name, ingredient in self._stock.items():
            for serving_size in ingredient.serving_sizes:
                new_name = serving_size + ' ' + ingredient_name
                maxes[new_name] = ingredient.get_max_stock(serving_size)
                base_ingredient_type[new_name] = ingredient.ingredient_type
                serving_sizes[new_name] = serving_size
                base_ingredient_name[new_name] = ingredient_name
        
        menu = []
        menu.append(maxes)
        menu.append(serving_sizes)
        menu.append(base_ingredient_name)
        menu.append(base_ingredient_type)
        return menu
    
     
                
    
    @property 
    def stock(self):
        return self._stock
    

    def get_ingredient(self, ingredient_name):
        if (ingredient_name in self._stock):
            return self._stock[ingredient_name]
        return None
    
    