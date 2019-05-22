from pymongo import MongoClient
client = MongoClient()
db = client['UserDataDB'] # Creating new Data base 


class ModelClasss:
    users = {}
    def insertUser(self, uInput):
        self.uInput = uInput
        result = db.UserCollections.insert_one(uInput)
        if (result.acknowledged):
            return True
        else:
            return False

    def displayAllUser(self):        
        uCollections = db.UserCollections.find()
        for allrecord in uCollections:
            users = allrecord
            return users
    p = {'Name': 'hi', 'Address': 'shgd'}
    r = insertUser(p)
    print(r)