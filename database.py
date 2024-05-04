from peewee import *

db = PostgresqlDatabase(
    'Sports_Store',
    user='postgres',
    password='talavodoi',
    host='localhost',
    port=5432
)


class Customers(Model):
    customerID = IntegerField(primary_key=True)
    firstname = TextField()
    lastname = TextField()
    email = TextField()
    phone = TextField()

    class Meta:
        database = db
        table_name = 'customers'


class Orders(Model):
    orderID = IntegerField(primary_key=True)
    customerID = ForeignKeyField(Customers, column_name='customerID')
    orderDate = DateField()

    class Meta:
        database = db
        table_name = 'orders'


class Category(Model):
    categoryID = IntegerField(primary_key=True)
    categoryName = TextField()

    class Meta:
        database = db
        table_name = 'category'


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


class OrderDetails(Model):
    orderDetailID = IntegerField(primary_key=True)
    orderID = ForeignKeyField(Orders, column_name='orderID')
    productID = ForeignKeyField(Product, column_name='productID')
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'orderdetails'


if __name__ == '__main__':
    for record in Category.select():
        print(record.categoryID, record.categoryName)