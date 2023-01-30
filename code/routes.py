from flask import Flask, redirect, render_template, request
from server import app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        desc = request.form["desc"]
        return render_template("hello.html", name=name, id=ZID, desc = desc)
    return render_template("index.html")

@app.route("/Hello/<name>/<id>/<desc>")
def hello(name, id, desc):
    return render_template("hello.html", name=name, id=id, desc=desc)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Add to cart
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        cart = fetch_session_cart()
        cart._items.append(Order(id,qty))
        print("no: ", len(cart._items))
        return render_template('home.html', items=cart._items,length=len(cart._items))
    else:
        return render_template('home.html')

if _name__=='__main_':
    app.run(debug=True)