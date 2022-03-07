from flask import Flask, render_template, request
import requests
import json

from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        input = request.form['input']

        jikan_url = requests.get(
            f'https://api.jikan.moe/v4/anime?q={input}')

        responseData = jikan_url.json()

        pprint(responseData)

        

    return render_template('index.html', responseData=responseData)

if __name__=="__main__":
    app.run(debug=True)