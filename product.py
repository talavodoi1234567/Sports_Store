from database import db
from peewee import *
from category import Category


class Product(Model):
    productID = IntegerField(primary_key=True)
    productName = TextField()
    categoryID = ForeignKeyField(Category, column_name='categoryID')
    price = IntegerField()
    stock = IntegerField()
    pic = TextField()

    class Meta:
        database = db
        table_name = 'products'

    @staticmethod
    def create_product(productName, categoryID, price, stock, pic):
        return Product.create(productName=productName, categoryID=categoryID, price=price, stock=stock, pic=pic)

    @staticmethod
    def read_product(productID):
        return Product.select().where(Product.productID == productID).get()

    @staticmethod
    def update_product(productID, productName, categoryID, price, stock, pic):
        return Product.update(productName=productName, categoryID=categoryID, price=price, stock=stock, pic=pic).where(Product.productID == productID).execute()

    @staticmethod
    def delete_product(productID):
        return Product.delete().where(Product.productID == productID).execute()