from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        input = request.form['input']

        jikan_url = requests.get(
            f'https://api.jikan.moe/v4/anime?q={input}')

        responseData = jikan_url.json()

        image_url = (responseData['images']['jpg']['image_url'])
        title = (responseData['title'])
        title_english = (responseData['title']['title_english'])
        title_japanese = (responseData['title']['title_japanese'])
        type = (responseData['type'])
        airing = (responseData['airing'])
        synopsis = (responseData['synopsis'])

    return render_template('index.html', image_url=image_url, title=title, title_english=title_english, title_japanese=title_japanese, type=type, airing=airing, synopsis=synopsis)

if __name__=="__main__":
    app.run(debug=True)