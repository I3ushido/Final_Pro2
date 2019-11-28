from flask import Flask, render_template, url_for,redirect
import pymysql
import os

app = Flask(__name__, static_url_path='/static')
conn = pymysql.connect('localhost', 'cars99', 'admin99', 'cars99')

# mycursor.execute("INSERT INTO projectcar (name, speed, color) VALUES (\"honda\",\"99\",\"black\")")  #working
@app.route('/inserts')
def insert_data():
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO projectcar (name, speed, color, path) VALUES (%s ,%s ,%s, %s)"
        val = [("Bank_Nanthawat", "100", "Black", "images/bankdark.jpg"), ("Arts_Phisanurat", "99", "white", "images/arts.jpg")]
        cur.executemany(sql, val)
        conn.commit()
        print(cur.rowcount, "record was inserted")
        return render_template('insert.html')

@app.route('/')
def hello_world():
    # status = "user_"
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM projectcar")
        rows = cur.fetchall()
        return render_template('index.html', datas=rows)

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/delete')
def delete_():
    with conn:
        cursor= conn.cursor()
        cursor.execute("TRUNCATE TABLE `projectcar`")
        return render_template('delete.html')

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete_data(id_data):
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM `projectcar` WHERE id=%s",(id_data))
        conn.commit()
        return redirect(url_for('hello_world'))

@app.route('/home')
def home():
    images = os.listdir(os.path.join(app.static_folder,"images"))
    print(images)
    return render_template('home.html', images=images)

@app.route('/test')
def test_file():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host="206.189.46.191",port=443,debug=True)  #host="206.189.46.191",port=443,
