import base64

from flask import Flask, jsonify, request, redirect, render_template
from simpleSQLQuery import *
from datetime import datetime
import uuid
import os
import psycopg2
# from peewee import DataError
import advanceSQLQuery
from category import Category
from product import Product
from test_base64 import convert_pic


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'picture')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# API cho app

# @app.route('/insert_product', methods=['POST'])
# def insertProductAPI():
#     try:
#         productName = request.form.get('productName')
#         categoryID = request.form.get('categoryID')
#         price = request.form.get('price')
#         stock = request.form.get('stock')
#         file = request.files['file']
#         pic = None
#         if file.filename != '':
#             pic = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic))
#         insert_product(productName, categoryID, price, stock, pic)
#         return jsonify({
#             'status': 'Insert product success'
#         })
#     except Exception as e:
#         return jsonify({
#             'error': e.__str__()
#         })


@app.route('/insert_category')
def insertCategoryAPI():
    try:
        categoryName = request.get_json().get('categoryName')
        insert_category(categoryName)
        return jsonify({
            'status': 'Insert category success'
        })
    except Exception as e:
        return jsonify({
            'error': e.__str__()
        })


@app.route('/insert_order')
# insert_order(customerID, productID, quantity, orderDate)
def insertOrderAPI():
    try:
        data = request.get_json()
        customerID = data.get('customerID')
        orderDate = data.get('orderDate')
        productID = data.get('productID')
        quantity = data.get('quantity')
        # record = Orders.create(customerID=customerID, orderDate=datetime.strptime(orderDate, "%d-%m-%Y"))
        insert_orders(customerID, orderDate)
        insert_order_details(record.orderID, productID, quantity)
        return jsonify({
            'status': 'Insert order success'
        })
    except Exception as e:
        return jsonify({
            'error': e.__str__()
        })


@app.route('/insert_customer')
def insertCustomerAPI():
    try:
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        phone = data.get('phone')
        insert_customer(firstname, lastname, email, phone)
        return jsonify({
            'status': 'Insert customer success'
        })
    except Exception as e:
        return jsonify({
            'error': e.__str__()
        })


@app.route('/select_product')
def selectProductAPI():
    # result = []
    # for record in select_all_product():
    #     result.append({
    #         'productID': record.productID,
    #         'productName': record.productName,
    #         'price': record.price,
    #         'stock': record.stock,
    #         'categoryID': record.categoryID
    #     })
    pass


# phần dành cho web quản trị
@app.route('/')
def test():
    return render_template('/login.html')


@app.route('/lc_ql')
def lc_ql():
    return render_template('lc_ql.html')


@app.route('/qlsp')
def qlsp():
     list_category = [[record_category.categoryID, record_category.categoryName] for record_category in Category.select()]
     list_product = [record_product for record_product in advanceSQLQuery.select_all_product()]
     return render_template('/qlsp.html', list_category=list_category, list_product=list_product)


@app.route('/them_sp')
def them_sp():
    list_category = [[record_category.categoryID, record_category.categoryName] for record_category in Category.select()]
    return render_template('/them_sp.html', list_category=list_category)


@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        image_file = request.files['formFileLg']
        product_name = request.form['ProductName']
        price = request.form['Price']
        stock = request.form['Stock']
        category = request.form['category']
        #chuyển đổi file thành base64
        pic = 'abcdef' + '.' + image_file.filename.split('.')[-1]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], pic)
        image_file.save(file_path)
        image_file.close()
        with open(file_path, 'rb') as f:
            file_content = f.read()
            picture = f"data:image/{image_file.filename.split('.')[-1]};base64," + base64.b64encode(file_content).decode()
        product = Product.create_product(product_name, int(category), price, stock, picture)
        return render_template('/them_sp_thanh_cong.html')
    except Exception as e:
        return e.__str__()


if __name__ == '__main__':
    app.run()