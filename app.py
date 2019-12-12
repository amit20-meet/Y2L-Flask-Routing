from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


##### Code here ######
products = query_all(hhh())
carts=query_all_cart(hhh())

@app.route('/')
def home():
	return render_template("home.html")
@app.route('/store')
def store():
	return render_template("store.html",products = products )
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/cart')
def cart():
	return render_template("cart.html", carts = carts )

@app.route('/add_to_cart/<string:name>/<int:Id>/<float:price>')
def add_to_cart( name, price, Id):
	add_cart(hhh(), Id, name, price)
	return store()

@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['userName'] != 'gever' or request.form['password'] != 'gever123':
			error = 'Please try again.'
			return render_template("home.html")
		else:
			return render_template("change.html" )
	else:
		return render_template('login.html', error=error)

@app.route('/change' ,  methods=['GET', 'POST'])
def change():
	if request.method == 'POST':
		name =request.form["Name"]
		price = request.form["Price"]
		picture_link= request.form["Picture_link"]
		#uptade_the_product(hhh(), name, price, picture_link)
		add_product(hhh(),name, price, picture_link)
		return render_template("store.html")



#####################


if __name__ == '__main__':
	app.run(debug=True)