from OrderSystem import OrderSystem
from Order import order
from Inventory import inventory
from Item import item
import pytest

class test_place_order: 

    def test_order_add_item(self):
        inv = inventory
        sys = OrderSystem(inv)
        order1 = order(1, [])
        
        order1.add_item(5, ["paddy", "bun", "cheese"], "Main")
        
        assert order1.items == 1
        assert order1.id == 1
        assert order1.status == False
        assert order1.price == 5

    def test_order_remove_item(self):
        inv = inventory
        sys = OrderSystem(inv)
        order1 = order(1, [])
        
        order1.add_item(5, ["paddy", "bun", "cheese"], "Main")
        
        assert order1.items == 1
        assert order1.id == 1
        assert order1.status == False
        assert order1.price == 5

    def test_successful_place_order(self):
        
        # create order with burger
        burger = item(setup_method.sys.inventory, "burger", "burger", 0, 1, True)
        paddy = item(setup_method.sys.inventory, "paddy", "paddy", 5, 1, True)        
        burger.add_component(paddy)              
        setup_method.order.add_item(burger)

        # place order to OrderSystem
        setup_method.sys.place_order(setup_method.order)

        # check order has been placed
        assert (setup_method.sys.orders[0] != None)

# need to:
#   test_place_order
#   order.test_add_item
#   order.test_remove_item
#   order.calc_price
#   item.add_ingredient
#   item.remove ingredient
test = test_place_order
test.test_order_add_item
