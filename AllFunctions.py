class SubClass:
    def __init__(self, db):
        self.db = db
# >>>>>> --- User Menu --- <<<<<<    
    def userMenu(self):    
        print("---Welcome to User Data Collections Menu---")
        print("Please select any one of the below option: ")
        print("1. Inser user data")
        print("2. Update existing data")
        print("3. Delete existing record")
        print("4. Exit")
        choice = int(input("Please enter your choice: ")) # Accepting input from user
        
# >>>>>> --- Accepting user name and address here --- <<<<<<
    def userInput(self):
        userInput = {}
        uname = str(input("Enter User Name: "))
        uaddress = str(input('Enter user address: '))
        userInput['Name'] = uname
        userInput['Address'] = uaddress
        return userInput

# >>>>>> --- Checking for user if exists --- <<<<<<                    
    def findUser(self, uInput):
        count = self.db.UserCollections.count()
        if (count == 0):
            return 0
        else:
            uCollections = self.db.UserCollections.find({'Name': uInput['Name']})
            for uInput in uCollections:
                print(uInput)
                return 1 

# >>>>>> --- Display one user details --- <<<<<<
    def displayOneUser(self, uInput):
        uCollections = self.db.UserCollections.find({'Name': uInput['Name']})
        for uInput in uCollections:
            print(uInput)
            return uInput

# >>>>>> --- Insert user details to DB --- <<<<<<
    def insertUser(self, uInput):
        result = self.db.UserCollections.insert_one(uInput)
        if (result.acknowledged):
            print('User successfully added!!!\n \nUser Object ID is: ', str(result.inserted_id)) #Printing user object id
                
# >>>>>> --- Display all user details --- <<<<<<
    def displayAllUser(self):
        print('--------- Users Available in UserDataDB ---------')
        uCollections = self.db.UserCollections.find()
        for allrecord in uCollections:
            print(allrecord)
    

# >>>>>> --- Update the user Address --- <<<<<<
    def updateUser(self, uInput):
        self.db.UserCollections.update(
            {
                'Name': uInput['Name']
            },
            {
                '$set':{
                    'Address': uInput['Address']
                }

            }, multi = False
            )
        uCollections = self.db.UserCollections.find({'Name': uInput['Name']})
        for uInput in uCollections:
            print('Record updated successfully!!', uInput)

# >>>>>> --- Delete User Details --- <<<<<<
    def deleteUser(self, uInput):
        self.db.UserCollections.delete_one({
            'Name': uInput['Name']
        })
        print('!!!-----Record Deleted----!!!')
