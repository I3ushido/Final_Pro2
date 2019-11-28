from flask import Flask, render_template, flash, redirect, render_template, request, session, abort

app = Flask(__name__)



@app.route("/")
def home():
    return "<h1>Welcome to Project Car_Detection :)</h1>" + "<p>Welcome to Project Car_Detection :)</p>"

@app.route("/about")
def about():
    return "<h1>Bank HumNoi_888/18</h1>"

    
if __name__ == "__main__":
    app.run(debug=True,host='localhost',port=9900)
