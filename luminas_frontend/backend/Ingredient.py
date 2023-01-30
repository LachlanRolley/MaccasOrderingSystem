
class ingredient:
    def __init__(self, name, prices, serving_sizes, stock_level, measuring_unit, ingredient_type):
        self._name = name
        self._serving_sizes = serving_sizes #this is either small, medium, large, 
        self._stock_level = stock_level
        self._measuring_unit = measuring_unit
        self._prices = prices
        self._ingredient_type = ingredient_type

    def __str__(self):
        return f"{self._name} has {self._stock_level} {self._measuring_unit} in stock"
    
    def increment_stock(self, quantity):
        #need to cehck quantity is positive
        self._stock_level += int(quantity)
    
    def decrement_stock(self, quantity, serving_size):
        #need to check quantity is positive
        # need to check serving size in self.serving sizes
        self._stock_level -= (int(quantity) * int(self._serving_sizes[serving_size]))


    @property
    def name(self):
        return self._name

    @property
    def prices(self):
        return self._prices

    @property
    def measuring_unit(self):
        return self._measuring_unit

    @property
    def stock_level(self):
        return self._stock_level

    @property
    def ingredient_type(self):
        return self._ingredient_type

    @property
    def serving_sizes(self):
        return self._serving_sizes
    
    def get_max_stock(self, serving_size):
        return min(int(self._stock_level / (self._serving_sizes[serving_size])), 4)

    
