from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
def hhh():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	print('session created!')
	return session

def add_product(session, name, price, picture_link):
	declarative_base = Product(
		name=name,
		price=price,
		picture_link=picture_link)
	session.add(declarative_base)
	print("added")
	session.commit()

def add_cart(session, Id, name, price):
	declarative_base = Cart(
		id_cart= Id ,
		name_cart=name,
		price_cart=price)
	session.add(declarative_base)
	session.commit()

#add_product('bear1', 350, 'bear1.png')
#add_product('bear2', 500, 'bear2.jpg')
#add_product( 'bear3', 200, 'bear3.jpg')
#add_product('bear4', 1200, 'bear4.jpg')
#add_product('bear5', 220, 'bear5.jpg')
#add_product('bear6', 3030, 'bear6.jpg')


def update_product( session, id, name, price, picture_link):
	declarative_base = session.query(
		base).filter_by(
		id=id).first()
	declarative_base.name = name
	declarative_base.price = price
	declarative_base.picture_link = picture_link 

def query_all(session):
	products = session.query(
		Product).all()
	return products
def query_all_cart(session):
	carts = session.query(
		Cart).all()
	return carts







