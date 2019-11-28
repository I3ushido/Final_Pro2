from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return '<h1>Welcome to Project Car_Detection :)</h1>'

@app.route('/hello')
def helloIndex():
    return '<h1>Bank_HumNoi_888/18</h1>'

if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=9900)
