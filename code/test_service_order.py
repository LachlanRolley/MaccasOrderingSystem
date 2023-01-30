from Inventory import inventory
from Item import item
from Order import order
from OrderSystem import OrderSystem
import random
import pytest

@pytest.fixture
def sys():
    inventory = inventory()
    for ingredient in ["charcoal bun", "wholegrain bun", "wholegrain wrap", "beef paddy", "pork paddy", "lettuce", "tomato", "chips", "nuggets", "coke", "water"]:
        inventory.add_ingredient(ingredient, 1, 10, 5)
    system = OrderSystem()
    return system

# test complete correct order
# test complete incorrect order
class TestServiceValidOrder:

    def test_succesful_service_all(self, sys):
        # loop through ingredients
        # throw together some items
        # throw together some orders
        # throw in to order
        # loop through and service
        items = []
        items.append(item(["charcoal bun", "beef paddy", "lettuce", "tomato"], burger))
        items.append(item(["wholegrain bun", "pork paddy", "tomato"], burger))
        items.appenditem(["chips"], side)
        items.append(item(["nuggets"], side))
        items.append(item(["coke"], drink))
        items.append(item(["water"], drink))
        items.append(item(["charcoal bun", "pork paddy", "lettuce", "tomato"], burger))
        items.append(item(["wholegrain bun", "beef paddy", "lettuce", "tomato"], burger))
        items.append(item(["wholegrain wrap", "lettuce", "tomato"], wrap))

        for i in range(0,10):
            r1 = random.randint(0,len(items))
            r2 = random.randint(0, len(items))
            r3 = random.randint(0, len(items))
            order_items = []
            order_items.append(items[r1])
            order_items.append(items[r2])
            order_items.append(items[r3])
            sys.place_order(order_items)
        
        for i in range(0,10):
            len1 = len(sys.orders)
            sys.complete_order(i)
            assert(len(sys.orders) == (len1 -1))


        assert(len(sys.orders) == 0)
        

#class TestServiceInvalidOrder():
