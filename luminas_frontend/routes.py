from flask import render_template, request, redirect, url_for, abort
from server import app, system
from backend.OrderSystem import OrderSystem
from backend.Order import order
from backend.Inventory import inventory
from backend.Ingredient import ingredient
from backend.Item import item
import pickle
#import errors?



@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


@app.route('/staff/view_current_orders', methods=["GET", "POST"])
def view_current_orders():
    with open('db.txt', 'rb') as f:
        system = pickle.load(f)

    return render_template('view_orders.html', orders = system.orders)

@app.route('/staff/service_order/<int:order_id>', methods=["GET", "POST"])
def service(order_id):
    with open('db.txt', 'rb') as f:
        system = pickle.load(f)
    if request.method == 'POST':
        form = request.form
        system.complete_order(order_id)
        with open('db.txt', 'wb') as f:
            pickle.dump(system, f)

    return render_template('service_order.html', order = system.get_order(order_id))


@app.route('/staff/maintain_inventory', methods=["GET", "POST"])
def maintain_inventory():
    with open('db.txt', 'rb') as f:
        system = pickle.load(f)

    if request.method == 'POST':
        form = request.form
        for ingredient_name in system.inventory.stock:
            if (form[ingredient_name] == ""): continue
            system.refill_ingredient_stock(ingredient_name, form[ingredient_name])
            with open('db.txt', 'wb') as f:
                pickle.dump(system, f)


    return render_template('maintain_inventory.html', stock = system.inventory.stock)


@app.route('/track_order/<int:order_id>', methods=["GET"])
def track(order_id):
    with open('db.txt', 'rb') as f:
        system = pickle.load(f)
    return render_template('order_confirm.html', order = system.get_order(order_id))




@app.route('/', methods=["GET", "POST"])
def home():
    with open('db.txt', 'rb') as f:
        system = pickle.load(f)
    
    menu = system.inventory.get_menu()
    maxes = menu[0]
    serving_size = menu[1]
    base_ingredient_name= menu[2]
    base_ingredient_type = menu[3]
    price = 0

    if request.method == 'POST':
        form = request.form
        main = system.make_item([], "main", 0, {}, {})
        items = []
        for ingredient_name, ingredient_type in base_ingredient_type.items():
            base_ingredient = system.inventory.get_ingredient(base_ingredient_name[ingredient_name])
            if (ingredient_type == 'side' or ingredient_type == 'drink'):
                if (ingredient_type not in form): continue
                if (form[ingredient_type] != ingredient_name): continue
               
                new_item = system.make_item([], ingredient_type, 0 , {}, {})
                new_item.add_ingredient(base_ingredient, serving_size[ingredient_name], 1)
                items.append(new_item)
            else:
                if (ingredient_name not in form): continue
                if (form[ingredient_name] == ""): continue
                main.add_ingredient(base_ingredient, serving_size[ingredient_name], form[ingredient_name])

        
        items.append(main)

        for item in items:
            price += item.price
        

        if 'confirm' in form:
            return render_template('order_form.html', is_pay_stage=True, form=form, price=price, maxes = maxes, types = base_ingredient_type)
        elif 'pay' in form:
            order = system.place_order(items, price)
            with open('db.txt', 'wb') as f:
                pickle.dump(system, f)
            return redirect(url_for("track", order_id = order.order_id))
            
                
    with open('db.txt', 'wb') as f:
        pickle.dump(system, f)
    return render_template('order_form.html', is_pay_stage=False, form = None, maxes = maxes, types = base_ingredient_type)



