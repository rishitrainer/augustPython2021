import mysql.connector as connector

myDB = connector.connect(
    host= 'localhost',
    port=3306,
    user = 'root',
    password='password',
    database='sakila'
)
update_query = 'UPDATE actor SET first_name = %s,last_name = %s, last_update = CURRENT_TIMESTAMP WHERE actor_id = %s;'
values = ('ADAM', "AVENE", "225")
mycursor = myDB.cursor()

mycursor = myDB.cursor()
mycursor.execute(update_query, values)
# mycursor.executemany(insert_query, values)
myDB.commit()

print("No. of rows affected", mycursor.rowcount)

mycursor.close()
myDB.close()
