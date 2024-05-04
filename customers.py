from database import db
from peewee import *


class Customers(Model):
    customerID = IntegerField(primary_key=True)
    firstname = TextField()
    lastname = TextField()
    email = TextField()
    phone = TextField()
    password = TextField()
    picture = TextField()

    class Meta:
        database = db
        table_name = 'customers'

    @staticmethod
    def create_customer(firstname, lastname, email, phone, password, picture):
        return Customers.create(firstname=firstname, lastname=lastname, email=email, phone=phone)

    @staticmethod
    def read_customer(customerID):
        return Customers.select().where(Customers.customerID == customerID).get()

    @staticmethod
    def update_customer(customerID, firstname, lastname, email, phone, password, picture):
        return Customers.update(firstname=firstname, lastname=lastname, email=email, phone=phone).where(Customers.customerID == customerID).execute()

    @staticmethod
    def delete_customer(customerID):
        return Customers.delete().where(Customers.customerID == customerID).execute()

