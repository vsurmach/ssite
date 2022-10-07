import sqlite3
from .models import Cars


def fn():
    connect = sqlite3.connect('db.sqlite3')
    corsor = connect.cursor()
    sql = '''SELECT * FROM lesson_cars'''
    corsor.execute(sql)
    cars = corsor.fetchall()
    connect.close()
    print(cars)
    items_car = []
    for i in cars:
        items_car.append(Cars(brand=i[1], model=i[2], color=i[3], price=i[4]))
    print(items_car[0].brand)
    return items_car