#exception to make sure ingredient is a valid ingrdient in inventory
class IngredientValidationError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Ingredient validation error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg) 
        self.errors = errors


def check_ingredient_validation_error(ingredient, ingredients):
    errors = {}
    if (ingredient not in ingredients):
        errors['invalid_ingredient'] = "Please specify a valid ingredient"
    if errors:
        raise IngredientValidationError(errors)

#exception to make sure ingredient is in stock and can be added to that item
class AddIngredientToItemError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Add ingredient to item error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg) 
        self.errors = errors

def check_add_ingredient_to_item_error(item_type, ingredient, stock_level, measuring_quantity, items_for_ingredient):
    errors = {}
    if (item_type not in items_for_ingredient[ingredient]):
        errors['wrong_ingredient'] = "Can't add ingredient to this item"

    if (stock_level[ingredient] < measuring_quantity[ingredient]):
        errors['out_of_stock'] = "Ingredient is out of stock"
    
    if errors:
        raise AddIngredientToItemError(errors)

#exception to add ingredient to inventory (make sure valid ingredient, quantity, price, amount)
class AddIngredientToInventoryError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Add ingredient to inventory error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg) 
        self.errors = errors

def check_add_ingredient_to_inventory_error(quantity, amount, price):
    errors = {}
    if (quantity <= 0):
        errors['quantity'] = "Please specify valid quantity"
    
    if (amount <= 0):
        errors['amount'] = "Please specify valid amount"
    
    if (cost <= 0):
        errors['price'] = "Please specify valid price"
    
    if errors:
        raise AddIngredientToInventoryError(errors)

#exception to update stock(make sure valid stock and quantity)
class UpdateStockError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Update stock error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg) 
        self.errors = errors

def check_update_stock_error(quantity):
    errors = {}
    if (quantity <= 0):
        errors['invalid_quantity'] = "Please specify a valid quantity"

    if errors:
        raise UpdateStockError(errors)



