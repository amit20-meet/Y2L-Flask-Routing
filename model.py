from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product(Base):
	__tablename__ = 'products'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	price = Column(Float)
	picture_link = Column(String)



class Cart(Base):
	__tablename__ = 'carts'
	id= Column(Integer,primary_key=True)
	id_cart = Column(Integer)
	name_cart = Column(String)
	price_cart = Column(Float)




