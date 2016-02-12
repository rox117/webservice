from JsonSerializable import JsonSerializable
from mongokit import Document, Connection


class TaxiService(Document, JsonSerializable):

    """Information for Registered Taxi services in the
    Kingston and St Andrew area"""

    def __init__(self, Numbers, Name, Email):
        self.__Numbers = Numbers
        self.__Name = Name
        self.__Email = Email

    structure = {
        '__Email': str,
        '__Name': str,
        '__Numbers': str
    }

    required_fields = ['__Numbers', '__Name', '__Email']
