from JsonSerializable import JsonSerializable
from flask.ext.mongokit import MongoKit, Document

class GuildRoute(Document,JsonSerializable):
    """Represents a Route for the Guild bus service"""
    
    def __init__(self,title,route,cost,departure_time):
        self.__routetitle=title
        self.__routelist=route
        self.__cost=cost
        self.__departure_time=departure_time
        
        
        
        structure={
            "__routetitle":str,
            "__routelist":list,
            "__cost":str,
            "__departure_time":str
        }
        
        
        
        required_fields=["__cost","__routetitle","__routelist","__departure_time"]