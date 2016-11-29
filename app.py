from flask import Flask,render_template,request
from indexSearch import search
from flask_googlemaps import GoogleMaps
from flask.views import View

import urllib2
import json

app = Flask(__name__)

tweets = ""

app.config['GOOGLEMAPS_KEY'] = "AIzaSyAd8WV2aBmnx0C3ncG-QpVsFn_KvhM-NvU"

GoogleMaps(app)

f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)

@app.route("/")
def main():
    return render_template('index.html')

from flask_googlemaps import Map, icons
@app.route("/",methods=["POST"])
def mapview():
    text = request.form['text']
    res = search(text,10)
    tweet = ""
    for r in res:
        tweet +=  str(r[1]) + " " +  r[0] + " " +  '<br>'
        print tweet
    trdmap = Map(
        identifier="trdmap",
        lat=location['latitude'],
        lng=location['longitude'],
        markers=[
            {
                'icon': icons.alpha.A,
                'lat':  location['latitude'],
                'lng':  location['longitude'],
                'infobox': "Hello I am USER"
            },
            {
                'icon': icons.dots.blue,
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am < b style='color:blue;'>BLUE< / b >!"
            },
            {
                'icon': icons.dots.yellow,
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am < b style='color:#ffcc00;'> YELLOW < / b >!"
                    "< h2 >It is HTML title< / h2 >"
                    "< img src=' //placehold.it/50' >"
                    "< br >Images allowed!"
                )
            }
        ]
    )
    return render_template('example.html', trdmap=trdmap,tweet=tweet)

    

if __name__ == "__main__":
    app.run()
