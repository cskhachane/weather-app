from flask import Flask, render_template, request
import requests
import var
import os

app = Flask(__name__)

api_key = var.key

def get_weather(city,api_key):
    base_url="http://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city,
        "appid":api_key,
        "units":"metric"
    }

    try:
        response= requests.get(base_url,params=params)
        response.raise_for_status()
        data = response.json()

        if response.status_code==200:
            return data
        else:
            return None

    except Exception as e:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data=get_weather(city,api_key)
        return render_template('index.html', weather_data=weather_data)
    else:
        return render_template('index.html',weather_data=None)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=int(os.environ.get("port",8080)),host='0.0.0.0',debug=True)