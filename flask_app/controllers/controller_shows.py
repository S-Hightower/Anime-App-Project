from flask_app import app
from flask import render_template

from flask_app.models.model_show import Show

#display route
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
