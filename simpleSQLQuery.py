from database import *
from datetime import datetime
import psycopg2


def insert_product(productName, categoryID, price, stock, pic=None):
    record = Product(
        productName=productName,
        categoryID=categoryID,
        price=price,
        stock=stock,
        pic=pic
    )
    record.save()


def insert_category(categoryName):
    record = Category(
        categoryName=categoryName
    )
    record.save()


def insert_orders(customerID, orderDate):
    record = Orders(
        customerID=customerID,
        orderDate=datetime.strptime(orderDate, '%d-%m-%Y')
    )
    record.save()


def insert_customer(firstname, lastname, email, phone):
    record = Customers(
        firstname=firstname,
        lastname=lastname,
        email=email,
        phone=phone
    )
    record.save()


def insert_order_details(orderID, productID, quantity):
    record = OrderDetails(
        orderID=orderID,
        productID=productID,
        quantity=quantity
    )
    record.save()


if __name__ == '__main__':
    # for record in select_all_product():
    insert_product("ABC", 3, 123, 456)
    # insert_orders(1, '2-3-2000')
    # insert_customer('A', 'B', 'abc@email.com', '0123456789')
