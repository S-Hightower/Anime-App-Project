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
        # response comes back as dictionary
        # pprint(responseData.items())
        # print('*********testing results**********')
        # print('data' in responseData)
        # pprint(responseData['data'])
        # print('title' in responseData['data'])
        # print(*responseData['data'], sep = ", ")
        print('*********working response list**********')
        # response successfully saved as list
        responseList = [responseData['data']]
        pprint(len(responseList))
        i = 0
        for i in range(len(responseList)):
            image_url = (responseList[0][0]['images']['jpg']['image_url'])
            title =(responseList[0][0]['title'])
            title_english = (responseList[0][0]['title_english'])
            title_japanese = (responseList[0][0]['title_japanese'])
            type = (responseList[0][0]['type'])
            airing = (responseList[0][0]['airing'])
            synopsis = (responseList[0][0]['synopsis'])

    return render_template('index.html', image_url=image_url, title=title, title_english=title_english, title_japanese=title_japanese, type=type, airing=airing, synopsis=synopsis)

if __name__=="__main__":
    app.run(debug=True)