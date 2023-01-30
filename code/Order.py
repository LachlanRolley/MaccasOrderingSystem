from Inventory import inventory
from errors import IngredientValidationError, check_ingredient_validation_error
from errors import AddIngredientToItemError, check_add_ingredient_to_item_error

class order(object):
    def __init__(self, items, order_id, status=False):
        #status is True if ready else false
        self._items = items
        # list of items so the mains, sides and drinks you want
        self._order_id = order_id
        self._status = status
        self._price = 0
           
    def add_item(self, item):
        self._items.append(item)
        self._price += item.price

    def remove_item(self, item):
        #check is in items
        self._items.remove(item)
        self._price -= item.price
    
    @property
    def items(self):
        return self._items  

    @property
    def order_id(self):
        return self._order_id
    
    @property
    def status(self):
        return self._status
    
    def display_status(self):      
        if self._status == True :
            print("your order is ready for pickup")
        else:
            print("your order is still being prepared")    
        





