from database import db
from peewee import *
from customers import Customers


class Orders(Model):
    orderID = IntegerField(primary_key=True)
    customerID = ForeignKeyField(Customers, column_name='customerID')
    orderDate = DateField()

    class Meta:
        database = db
        table_name = 'orders'

    @staticmethod
    def create_order(customerID, orderDate):
        return Orders.create(customerID=customerID, orderDate=orderDate)

    @staticmethod
    def read_order(orderID):
        return Orders.select().where(Orders.orderID == orderID).get()

    @staticmethod
    def update_order(orderID, customerID, orderDate):
        return Orders.update(customerID=customerID, orderDate=orderDate).where(Orders.orderID == orderID).execute()

    @staticmethod
    def delete_order(orderID):
        return Orders.delete().where(Orders.orderID == orderID).execute()