from .Inventory import inventory
from .Order import order
from .Item import item
from .Ingredient import ingredient

class OrderSystem(object):
    def __init__(self, inventory):
        self._orders = []
        self._inventory = inventory
    
    def view_inventory(self):
        print(self._inventory)

    def refill_ingredient_stock(self, ingredient_name, quantity):
        self._inventory.increment_stock(ingredient_name, quantity)
    
    def place_order(self, items, price):
        #need to check items and price is valid

        print('Payment authorised.')
        new_order = order(items, len(self._orders), False, price)
        self._orders.append(new_order)

        for item in new_order.items:
            for ingredient in item.ingredients:
                self._inventory.decrement_stock(ingredient.name, item.quantity(ingredient.name), item.serving_size(ingredient.name))

        return new_order
 
    
    def complete_order(self, order_id):
        #exception
        for ord in self._orders:
            if (ord.order_id == order_id):
                ord.update_status()
                return None
        
          
    
    def make_item(self, ingredients, item_type, price, serving_size, quantities):
        # check item_type and price
        return item(ingredients, item_type, price, serving_size, quantities)

    @property
    def orders(self):
        return self._orders
    
    @property
    def inventory(self):
        return self._inventory
    
    def get_order(self, order_id):
        for order in self._orders:
            if (order.order_id == order_id):
                return order
        return None
    
    def get_current_orders(self):
        current_orders = []
        for order in self._orders:
            if (order.update_status == False):
                current_orders.append(order)
        return current_orders
        

    
