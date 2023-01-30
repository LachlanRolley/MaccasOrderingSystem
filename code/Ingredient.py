# cant have inventory passed into it

class ingredient:
    def __init__(self, name, price, item_types, ingredient_type, measuring_quantity, stock_level):
        self._name = name
        self._price = price
        self._item_types = item_type
        self._ingredient_type = ingredient_type
        self._measuring_quantity = measuring_quantity       # quantity in 1 of this ingredient 
        self._stock_level = (stock_level * measuring_quantity)

    def __str__(self):
        return f"{self._name} at stock level {self._stock_level}"
    
    def update_stock(self, quantity):
        self._stock_level += (quantity * self._measuring_quantity)
    
    def is_available(self):
        return (self._stock_level >= self._measuring_quantity)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def item_types(self):
        return self._item_type

    @property
    def ingredient_type(self):
        return self._ingredient_type
    
    @property
    def measuring_quantity(self):
        return self._measuring_quantity

    @property
    def stock_level(self):
        return self._stock_level

    
