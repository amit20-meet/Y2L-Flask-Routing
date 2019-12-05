from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


##### Code here ######
products = query_all()
carts=query_all_cart()

@app.route('/')
def home():
	return render_template("home.html")
@app.route('/store')
def store():
	return render_template("store.html",products = products)
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/cart')
def cart():
	return render_template("cart.html", carts = carts)

@app.route('/add_to_cart<string:name>/<int:id>/<float:price>')
def add_to_cart(name,price,id):
	add_cart(name,price,id)
	return store()


#####################


if __name__ == '__main__':
	app.run(debug=True)