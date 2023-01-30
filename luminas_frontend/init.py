from backend.OrderSystem import OrderSystem
from backend.Order import order
from backend.Inventory import inventory
from backend.Ingredient import ingredient
from backend.Item import item
import pickle

def bootstrap_system():
    try:
        with open('db.txt', 'rb') as f:
            system = pickle.load(f)
    except:

        system_inventory = inventory()
        # buns
        system_inventory.add_ingredient("charcoal bun", {"regular": 2}, {"regular": 1}, 20, "buns", "bun")
        system_inventory.add_ingredient("wholegrain bun", {"regular": 1}, {"regular": 1}, 20, "buns", "bun")

        system_inventory.add_ingredient("wholegrain wrap", {"regular": 1}, {"regular": 1}, 20, "wraps", "wrap")
        system_inventory.add_ingredient("pita wrap", {"regular": 1}, {"regular": 1}, 20, "wraps", "wrap")

        #paddys
        system_inventory.add_ingredient("beef paddy", {"regular": 2}, {"regular": 1}, 20, "paddys", "paddy")
        system_inventory.add_ingredient("chicken paddy",{"regular": 1}, {"regular": 1}, 20, "paddys", "paddy")

        # sides
        system_inventory.add_ingredient("chips", {"small": 2, "medium": 4}, {"small": 75, "medium": 125}, 1000, "g", "side")
        system_inventory.add_ingredient("nuggets", {"small": 3, "medium": 6}, {"small": 3, "medium": 6}, 200, "nuggets", "side")
        system_inventory.add_ingredient("chocolate sundae", {"small": 2, "medium": 3, "large": 4}, {"small": 1, "medium": 2, "large": 3}, 100, "scoops", "side")
        system_inventory.add_ingredient("vanilla sundae", {"small": 2, "medium":3, "large": 4 } ,{"small": 1, "medium": 2, "large": 3}, 100, "scoops", "side")

        # drinks
        system_inventory.add_ingredient("coke", {"can": 2, "bottle": 3}, {"can": 375, "bottle": 600}, 5000, "mL", "drink")
        system_inventory.add_ingredient("orange juice", {"small": 2, "medium":4 } ,{"small": 250, "medium": 450}, 3000, "mL", "drink")


        # ingredients
        system_inventory.add_ingredient("lettuce", {"regular": 0.50}, {"regular": 3}, 100, "pieces", "ingredient")
        system_inventory.add_ingredient("cucumber", {"regular": 0.50}, {"regular": 3}, 100, "slices", "ingredient")

        system = OrderSystem(system_inventory)
            
        with open('db.txt', 'wb') as f:
            pickle.dump(system, f)
    finally:

        return system