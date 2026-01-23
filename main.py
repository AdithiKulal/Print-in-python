from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def details():
    location = input("Enter the location here: ")
    api_key = 'AQw4sNOX1A9KQf6L5TTn_2Ggsrgc63hY04_h8ps'

    try:
        source = urllib.request.urlopen(
            'https://geocode.search.hereapi.com/v1/geocode?apikey=' + api_key + '&q=' + location
        ).read()

        responseData = json.loads(source)

        data = {
            "latitude": str(responseData['items'][0]['position']['lat']),
            "longitude": str(responseData['items'][0]['position']['lng']),
        }
        return render_template('index.html', data=data, apikey=api_key)
    except (Exception):
        return render_template('index.html', error="Give the correct location")

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)