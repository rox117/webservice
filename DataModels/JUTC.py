from JsonSerializable import JsonSerializable
from flask.ext.mongokit import MongoKit, Document


class JRoute(Document, JsonSerializable):

    """Route information for JUTC busses passing UWI"""

    def __init__(self, RouteNum, Origin, Destination,RouteList):
        self.__RouteNum = RouteNum
        self.__Origin = Origin
        self.__Destination = Destination
        self.__RouteList=RouteList
    structure = {
        '__RouteNum': str,
        '__Origin': str,
        '__Destination': str,
        '__RouteList':str
    }

    required_fields = ['__Destination', '__RouteNum', '__Origin','__RouteList']
