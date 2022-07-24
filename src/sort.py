import numpy as np
import cv2
import math
import mysql.connector
from matplotlib import pyplot as plt
import os
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='dbmovie',
                                              user='root',
                                              password='')
    sql_select_Query = "SELECT id,his FROM movie "
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    min = []
    id = []
    for row in records:

        p = []
        q = []
        f = open('data5.txt', 'r')
        s = f.read()
        p = s.split(" ")
        f.close()

        # item = str(records)
        item = str(row[1])
        q = item.split(" ")
        sum =0
        sum1 =0
        answer = 0
        percent = 0
        sump =0
        sumq = 0
        sum_2 =0
        answer_2 =0

        q[0] = q[0].replace("[('",'')
        for i in range(0, 864):
            p[i] = int(p[i])
            q[i] = int(q[i])
            # 1
            sum1 = sum1 + ((p[i]+q[i]))
            sum = sum + ((p[i]-q[i])**2)
            #2
            sum_2 = sum_2 +(p[i]*q[i])
            sump = sump +(p[i]**2)
            sumq = sumq + (q[i] ** 2)
        #1
        percent = 100-((sum/sum1)*100)
        answer = math.sqrt(sum)
        #2
        answer_2 = sum_2/(math.sqrt(sump)*math.sqrt(sumq))
        # print("ค่าใกล้ 0 : " , answer)
        # print("ค่าใกล้ 1 : ",answer_2)
        # print("หนังเรื่องที่ :",row[0])
        min.append(answer)
        id.append(row[0])

    # print(sorted(zip(min, id)))
    minid = sorted(zip(min, id))
    print(minid)
    print(minid[0][1])
    cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mySQLconnection.is_connected()):
        print("MySQL connection is closed")


cv2.waitKey(0)
cv2.destroyAllWindows()