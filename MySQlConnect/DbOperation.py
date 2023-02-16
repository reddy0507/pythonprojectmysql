import mysql.connector

con = mysql.connector.connect(host="localhost", port=3306, user="root",passwd="root", database="mydb")
curs = con.cursor()
curs.execute("insert into student(id,SName) values(3,'reddy')")
con.commit()
con.close()
print("Finished --------")