from flask import Flask, jsonify
from staticInfo import *
from os.path import realpath
from os.path import getmtime
import time
from flask import request
service = Flask(__name__)
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
    try:
        if not isFileMod(request.headers.get('Last-Modified')):
            response.status_code = 304
    except Exception:
        pass
    response.headers[
        'Last-Modified'] = str(getmtime(FILEPATH))
    print response.headers.get('Last-Modified')
    print request.headers.get('Last-Modified')
    return response


@service.route('/service/taxi_services/')
def getTaxiServices():
    response = jsonify({'TaxiList': [i.JsonSerialize() for i in taxi_list]})
    try:
        if not isFileMod(request.headers.get('Last-Modified')):
            response.status_code = 304
    except Exception:
        pass
    response.headers[
        'Last-Modified'] = str(getmtime(FILEPATH))
    print response.headers.get('Last-Modified')
    print request.headers.get('Last-Modified')
    return response


@service.route('/service/jutc_routes/')
def getJUTCRoutes():
    response = jsonify({'JUTCList': [i.JsonSerialize() for i in JUTCList]})
    try:
        if not isFileMod(request.headers.get('Last-Modified')):
            response.status_code = 304
    except Exception:
        pass
    response.headers[
        'Last-Modified'] = str(getmtime(FILEPATH))
    print response.headers.get('Last-Modified')
    print request.headers.get('Last-Modified')
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
        {'EateriesList': [i.JsonSerialize() for i in eateries_list]})
    try:
        if not isFileMod(request.headers.get('Last-Modified')):
            response.status_code = 304
    except Exception:
        pass
    response.headers["Last-Modified"] = str(getmtime(FILEPATH))
    return response

if __name__ == "__main__":
    service.run()
