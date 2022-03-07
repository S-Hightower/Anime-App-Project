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

        responseList = [responseData['data']]
        # response successfully saved as list
        print('*********working response list**********')
        # pprint(responseList[0][0]['images']['jpg']['image_url'])
        # pprint(responseList[0][0]['title'])
        # pprint(responseList[0][0]['title_english'])
        # pprint(responseList[0][0]['title_japanese'])
        # pprint(responseList[0][0]['type'])
        # pprint(responseList[0][0]['airing'])
        # pprint(responseList[0][0]['synopsis'])

    return render_template('index.html', responseData=responseData, responseList=responseList)

if __name__=="__main__":
    app.run(debug=True)