from flask import Flask, jsonify
from staticInfo import *
from os.path import realpath
from os.path import getmtime
from os import getenv
import time
from flask_oauthlib.provider import OAuth2Provider
from flask import request
from werkzeug.contrib.cache import SimpleCache



  

service = Flask(__name__)
oath=OAuth2Provider(service)
coordinates = ''
FILEPATH = '/home/rreid/mona_X_api/webservice/staticInfo.py'


def isFileMod(datemodified):
    if round(getmtime(FILEPATH), 2) > round(float(datemodified), 2):
        return True
    else:
        return False


@service.route('/service/shuttle_routes/')
def getShuttleRoutes():
    response = jsonify(
        {'Shuttlelist': [i.JsonSerialize() for i in shuttle_list]})
    return response
    
@service.route("/service/guild_routes")
def getGuildRoutes():
    response=jsonify({"GuildList":[i.JsonSerialize() for i in guild_list]})


@service.route('/service/taxi_services/')
def getTaxiServices():
    response = jsonify({'TaxiList': [i.JsonSerialize() for i in taxi_list]})
    return response


@service.route('/service/jutc_routes/')
def getJUTCRoutes():
    response = jsonify({'JUTCList': [i.JsonSerialize() for i in JUTCList]})
    return response


@service.route('/service/position/', methods=['POST'])
def getTrackingInfo():
    coordinates = request.get_json()


@service.route('/service/coordinates')
def getCoordinates():
    return jsonify(coordinates)


@service.route('/service/eateries')
def getEateriesList():
    response = jsonify(
        {'RestaurantList': [i.JsonSerialize() for i in eateries_list]})
    return response

if __name__ == "__main__":
    service.run(host = getenv('IP','0.0.0.0'), port=int(getenv('PORT',8080)))