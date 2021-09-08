import mysql.connector as connector

myDB = connector.connect(
    host= 'localhost',
    port=3306,
    user = 'root',
    password='password',
    database='sakila'
)
select_all = "Select * from Actor where actor_id > %s order by first_name"
value = ('200',)

mycursor = myDB.cursor()
mycursor.execute(select_all, value)

for eachRow in mycursor.fetchmany(10):
    print(eachRow[0], eachRow[1])

mycursor.close()
myDB.close()
