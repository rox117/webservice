from JsonSerializable import JsonSerializable
from mongokit import Document, Connection


class MenuItem(Document, JsonSerializable):

    """Restaurant MenuItem """

    def __init__(self, resName, price, itemName, mealDesc):
        self.__resname = resName
        self.__price = price
        self.__itemName = itemName
        self.__mealDesc = mealDesc

    structure = {
        '__resname': str,
        '__price': str,
        '__mealDesc': str,
        '__itemName': str
    }

    required_fields = ['__itemName', '__resname', '__price', '__mealDesc']
