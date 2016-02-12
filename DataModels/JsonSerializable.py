class JsonSerializable(object):

    """Superclass for all objects to be converted to json"""

    def JsonSerialize(self):
        """ the list of class attributes
        generated by 'dir()' are iterated through,
        converting each to json"""
        name_returned = "_" + self.__class__.__name__
        attr_list = [i.replace("_" + name_returned, "")
                     for i in dir(self) if name_returned in i]
        json_attr_dic = {}
        for i in attr_list:
            exec("attr=self.%s" % i)
            json_attr_dic.update({i.replace(name_returned + "__", ""): attr})
        return json_attr_dic
