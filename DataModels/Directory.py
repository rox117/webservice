from JsonSerializable import JsonSerializable
from mongokit import Document, Connection


class Directory(Document, JsonSerializable):

    """ Represents an entry in the uwi staff Directory"""

    def __init__(self, name, jobTitle):
        self.__name = name
        self.__jobTitle = jobTitle

    structure = {
        '__name': str,
        '__jobTitle': str
    }

    required_fields = ['__jobTitle', '__name']
