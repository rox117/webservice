from JsonSerializable import JsonSerializable
from flask.ext.mongokit import MongoKit, Document


class ShuttleRoute(Document, JsonSerializable):

    """Class representing Schedule for UWI shuttle buses"""

    def __init__(self, route, operationTimes, frequency, routeDescrpition):
        self.__Route = route
        self.__OperationTimes = operationTimes
        self.__Frequency = frequency
        self.__RouteDescription = routeDescrpition

    structure = {
        '__Route': str,
        '__OperationTimes': str,
        '__Frequency': str,
        '__RouteDescription': str
    }

    required_fields = [
        '__RouteDescription', '__OperationTimes', '__Route', '__Frequency']
