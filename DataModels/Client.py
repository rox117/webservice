from flask.ext.mongokit import MongoKit, Document

class Client(Document):
    
    __collection__='Client'
    
    structure={
        'name':str,
        'description':str,
        'user_id':int,
        'client_secret':str,
        'client_key':str,
        'realms':str,
        'redirect_uris':str
    }

 



    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_realms(self):
        if self._realms:
            return self._realms.split()
        return []