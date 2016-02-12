from JsonSerializable import JsonSerializable
from mongokit import Document, Connection


class Restaurant(Document, JsonSerializable):

    """Restaurant on UWI campus"""

    def __init__(self, businessHours, location, name, fav, coord, category):
        self.__name = name
        self.__location = location
        self.__businessHours = businessHours
        self.__fav = fav
        self.__coord = coord
        self.__category = category

    structure = {
        '__name': str,
        '__location': str,
        '__businessHours': str
    }

    required_fields = ['__businessHours', '__location', '__name']
