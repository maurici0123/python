import mysql.connector

meudb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aa'
)

cursor = meudb.cursor()

cursor.execute('SELECT Artist, max(sales) FROM aa.money_makers_bb WHERE year = 2020')

resultado = cursor.fetchall()

print(resultado)