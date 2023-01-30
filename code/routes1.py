from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        if(request.form.get('action') == 'c_burg'):
            return render_template('custom_burger.html')
        if(request.form.get('action') == 'c_wrap'):
            return render_template('custom_wrap.html')    
    
    return render_template('home.html')

@app.route("/custom_burger" , methods=["GET", "POST"])
def Cust_b():
    if request.method == 'POST':
        pass
        
    
    return render_template('custom_burger.html')    
