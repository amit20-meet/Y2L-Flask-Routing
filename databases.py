from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(id, name, price, picture_link):
	declarative_base = Product(
		id=id,
		name=name,
		price=price,
		picture_link=picture_link)
	session.add(declarative_base)
	session.commit()
###
def add_cart( id, name, price):
	declarative_base = Cart(
		id_cart= id ,
		name_cart=name,
		price_cart=price)
	session.add(declarative_base)
	session.commit()


#add_product(1, 'bear1', 350, 'bear1.png')
#add_product(2, 'bear2', 500, 'bear2.jpg')
#add_product(3, 'bear3', 200, 'bear3.jpg')
#add_product(4, 'bear4', 1200, 'bear4.jpg')
#add_product(5, 'bear5', 220, 'bear5.jpg')
#add_product(6, 'bear6', 3030, 'bear6.jpg')


def update_product(id, name, price, picture_link):
	declarative_base = session.query(
		base).filter_by(
		id=id).first()
	declarative_base.name = name
	declarative_base.price = price
	declarative_base.picture_link = picture_link 

def query_all():
	products = session.query(
		Product).all()
	return products
def query_all_cart():
	carts = session.query(
		Cart).all()
	return carts


print(query_all())




