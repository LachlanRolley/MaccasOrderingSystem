#this is the test for maintaining inventory
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


class TestMainInInventory():
    def test_view_inventory(self, sys):
        #check all have correct amounts


    def test_successful_update_inventory(self, sys):
    

    def test_invalid_update_inventory(self, sys):
        #check you cant update
        #check you get an error