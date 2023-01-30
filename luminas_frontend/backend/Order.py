from .Item import item
from .Ingredient import ingredient

class order(object):
    def __init__(self, items, order_id, status, price):
        #status is True if ready else false
        self._items = items
        # list of items so the mains, sides and drinks you want
        self._order_id = order_id
        self._status = status
        self._price = price
    
    @property
    def items(self):
        return self._items  

    @property
    def order_id(self):
        return self._order_id
    
    @property
    def status(self):
        return self._status


    @property
    def price(self):
        return self._price
    
    def update_status(self):
        self._status = True
    
    def __str__(self):      
        output = "Order id is " + str(self._order_id) + "\n"

        if self._status == True :
            output += ("Order is ready for pickup\n")
        else:
            output += ("Oder is still being prepared\n")

        output += ("Order contains the following items\n\n")

        for item in self._items:
            output += (f'{item} \n')
        return output    
        





