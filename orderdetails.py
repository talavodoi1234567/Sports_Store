from database import db
from peewee import *
from orders import Orders
from product import Product


class OrderDetails(Model):
    orderDetailID = IntegerField(primary_key=True)
    orderID = ForeignKeyField(Orders, column_name='orderID')
    productID = ForeignKeyField(Product, column_name='productID')
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'orderdetails'

    @staticmethod
    def create_order_detail(orderID, productID, price, quantity):
        return OrderDetails.create(orderID=orderID, productID=productID, price=price, quantity=quantity)

    @staticmethod
    def read_order_detail(orderDetailID):
        return OrderDetails.select().where(OrderDetails.orderDetailID == orderDetailID).get()

    @staticmethod
    def update_order_detail(orderDetailID, orderID, productID, price, quantity):
        return OrderDetails.update(orderID=orderID, productID=productID, price=price, quantity=quantity).where(OrderDetails.orderDetailID == orderDetailID).execute()

    @staticmethod
    def delete_order_detail(orderDetailID):
        return OrderDetails.delete().where(OrderDetails.orderDetailID == orderDetailID).execute()