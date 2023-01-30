from .Ingredient import ingredient


class item(object):
    
    def __init__(self, ingredients, item_type, price, serving_sizes, quantities):
        ''' item is only main side or drink '''
        self._ingredients = ingredients
        self._item_type = item_type
        self._price = price
        if (self._item_type == 'main'):
            self._price += 5
        self._serving_sizes = serving_sizes
        self._quantities = quantities
    
    def add_ingredient(self, ingredient, serving_size, quantity):
        #test valid serving size and quantity
        self._ingredients.append(ingredient)
        self._price += ingredient.prices[serving_size]
        self._serving_sizes[ingredient.name] = serving_size
        self._quantities[ingredient.name] = quantity
    
    @property
    def ingredients(self):
        return self._ingredients
    
    @property
    def price(self):
        return self._price
    
    @property
    def item_type(self):
        return self._item_type
    
    
    def serving_size(self, ingredient_name):
        return self._serving_sizes[ingredient_name]
    
    def quantity(self, ingredient_name):
        return self._quantities[ingredient_name]
    

    
    def __str__(self):
        string = f"{self._item_type} contains:\n"
        for ingredient in self._ingredients:
            string += (f"{self._quantities[ingredient.name]}  {self._serving_sizes[ingredient.name]} {ingredient.name}\n")
        return string

    

    
