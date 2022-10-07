import sqlite3
connect = sqlite3.connect('db.sqlite3')
cur = connect.cursor()
sql = '''
CREATE TABLE phone
(
    Id SERIAL PRIMARY KEY,
    Brand varchar(30),
    Model varchar(30),
    System varchar(30),
    Display  numeric(2, 2),
    Price numeric(6, 2)
);
'''
cur.execute(sql)
sql1 = '''
INSERT INTO phone (Brand,Model,System, Display, Price) VALUES ('Samsung', 'Galaxy', 'Android', 5.6, 400),
('Apple', 'X', 'IQS', 5.6, 1400),
('Huawei', 'P smart', 'Android', 5.5, 500);
'''
cur.execute(sql1)
sql_result = '''
SELECT * FROM phone
'''

connect.commit()
cur.execute(sql_result)
print(cur.fetchall())
f = cur.fetchall()

with open('Phones.txt', 'w') as file:
    for elem in f:
        file.write(f'{elem[0]}:{elem[1:]}\n')
        print(elem[0])
connect.close()
