import psycopg2

conn = psycopg2.connect(
    dbname='Sports_Store',
    user='postgres',
    password='talavodoi',
    host='localhost',
    port=5432
)

cur = conn.cursor()

def select_all_product():
    try:
        cur.execute("""SELECT "productName", price, stock, "categoryName", pic
                    FROM products 
                    JOIN category ON category."categoryID" = products."categoryID"
                    """)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e.__str__())


def get_customer(customerID):
    try:
        cur.execute(f"""SELECT "customerID"
                    FROM customer 
                    WHERE customerID = {customerID}
                    """)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e.__str__())


if __name__ == '__main__':
    # cur.execute("SELECT * FROM products")
    # rows = cur.fetchall()
    #
    # # In ra kết quả
    # for row in rows:
    #     print(row)
    print([record for record in select_all_product()])

    # Đóng kết nối
    cur.close()
    conn.close()


