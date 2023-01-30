#this is the test for placing an order
from backend.Inventory import inventory
from bakcend.Order import order
from backend.Item import item
from backend.Ingredient import ingredient
from backend.OrderSystem import OrderSystem
import pytest

@pytest.fixture
def sys():
    system_inventory = inventory()
    # buns
    system_inventory.add_ingredient("charcoal bun", {"regular": 2}, {"regular": 1}, 20, "buns", "bun")
    system_inventory.add_ingredient("wholegrain bun", {"regular": 1}, {"regular": 1}, 20, "buns", "bun")

    #paddys
    system_inventory.add_ingredient("beef paddy", {"regular": 2}, {"regular": 1}, 20, "paddys", "paddy")
    system_inventory.add_ingredient("chicken paddy",{"regular": 1}, {"regular": 1}, 20, "paddys", "paddy")

    # sides
    system_inventory.add_ingredient("chips", {"small": 2, "medium": 4}, {"small": 75, "medium": 125}, 1000, "g", "side")
    system_inventory.add_ingredient("nuggets", {"small": 3, "medium": 6}, {"small": 3, "medium": 6}, 200, "nuggets", "side")
    

    # drinks
    system_inventory.add_ingredient("coke", {"can": 2, "bottle": 3}, {"can": 375, "bottle": 600}, 5000, "mL", "drink")
    system_inventory.add_ingredient("orange juice", {"small": 2, "medium":4 } ,{"small": 250, "medium": 450}, 3000, "mL", "drink")

    # ingredients
    system_inventory.add_ingredient("lettuce", {"regular": 0.50}, {"regular": 3}, 100, "pieces", "ingredient")
    system_inventory.add_ingredient("cucumber", {"regular": 0.50}, {"regular": 3}, 100, "slices", "ingredient")

    system = OrderSystem(system_inventory)

    return system

## so your acceptance criteria need to be met here
## so when placing an order you need to 
## 1) test_make_item_with_valid_ingredients
## 2) test_make_item_with_invalid_ingredients
## 3) tes_make_order_with_valid_ingredients
## 4) test_make_order_with_invalid_ingredients
## 5) test_can_place_valid_order
## 6) test_cant_place_out_of_stock_order
class TestMakeItem():
    def test_can_make_valid_item(self, sys):
        

    def test_cant_make_invalid_item(self, sys):
    
class TestMakeOrder():
    def test_can_make_valid_order(self, sys):
        

    def test_cant_make_invalid_order(self, sys):

class TestPlaceOrder():
    def test_can_place_valid_order(self, sys):
        

    def test_cant_place_invalid_order(self, sys):