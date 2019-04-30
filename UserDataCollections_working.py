from pymongo import MongoClient
from AllFunctions import SubClass
client = pymongo.MongoClient('mongodb://python3:27017/')
db = client['UserDataDB'] # Creating new Data base 
subobj = SubClass(db)
          
print("---Welcome to User Data Collections Menu---")
print("Please select any one of the below option: ")
print("1. Inser user data")
print("2. Update existing data")
print("3. Delete existing record")
print("4. Exit")
try:
    choice = int(input("Please enter your choice: ")) # Accepting input from user

    if (choice == 1):
        uInput = subobj.userInput()
        print("You have entered the following details: \n", uInput)     
    
        result = subobj.findUser(uInput)
        
        if (result == 1):
            print("User already exist...... Insertion Failed!!!")
            exit
        else:
            subobj.insertUser(uInput)
            subobj.displayAllUser()

    if (choice == 2):
        uInput = {}
        print("Enter the name of the user which you want to update: ")
        uname = str(input("Enter User Name: "))
        uInput['Name'] = uname
        result = subobj.findUser(uInput)
        if (result != 1):
            print("User Does not exist......")
            exit
        else:
            # subobj.displayOneUser(uInput)
            print("Please enter the new address: ")
            uaddress = str(input('Enter user address: '))
            uInput['Address'] = uaddress
            subobj.updateUser(uInput)
            subobj.displayAllUser()

    if(choice == 3):
        uInput = {}
        print("Enter the name of the user which you want to delete: ")
        uname = str(input("Enter User Name: "))
        uInput['Name'] = uname
        result = subobj.findUser(uInput)
        if (result != 1):
            print("User Does not exist......")
            exit
        else:
            subobj.deleteUser(uInput)
            subobj.displayAllUser()
            
    if (choice == 4):
        exit
    if (choice != 1 and choice != 2 and choice != 3 and choice != 4):
        print("Invalid Input!!! Please enter a number between 1 to 4")
except ValueError:
    print("Invalid Input!!! Strings are not allowed")
except EOFError:
    print("An error occured while connecting DB")      
# finally:
#     print('An error occured while running the program please try again!')  
