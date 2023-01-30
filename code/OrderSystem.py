from Inventory import inventory
from Order import order
from Item import item
from Ingredient import ingredient

class OrderSystem(object):
    def __init__(self, inventory):
        self._orders = []
        self._inventory = inventory
    
    def view_inventory(self):
        print(self._inventory)

    def update_inventory(self, ingredient, quantity):
        self._inventory.update_stock(ingredient, quantity)
    
    def place_order(self, items):
        answer = input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
             self._orders.append(order(items, len(self._orders), False))
        else:
            print('Payment not authorised.')
    
    def complete_order(self, order_id):
        for ord in self._orders:
            if (ord.order_id == order_id):
                ord.status = True
                self._orders.remove(ord)
                return None
        
        print("Order ID is invalid")   

    @property
    def orders(self):
        return self._orders

        

    
