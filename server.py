from sqlite3 import connect
from flask import render_template
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html", token="Please connect")

if __name__=="__main__":
    app.run(debug=True)