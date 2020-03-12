import mysql.connector

mydb =  mysql.connector.connect(host="localhost",user="root",passwd="",database="carrier")

mycursor = mydb.cursor()

mycursor.execute("TRUNCATE TABLE `job`")

mydb.commit()

mycursor.execute("TRUNCATE TABLE `subjects`")

mydb.commit()

mydb.close()