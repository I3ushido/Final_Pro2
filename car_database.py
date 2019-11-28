from mysql.connector import (connection)

con_x = connection.MySQLConnection(user='kheow', password='262540',host='206.189.46.191',port=3306,database='Car',charset='utf8mb4')
# con_x = connection.MySQLConnection(user='joe', database='test')
# con_x = connection.MySQLConnection(host='206.189.46.191',database='Car',user='kheow', password='262540')

print(con_x)

con_x.commit()
con_x.close()






