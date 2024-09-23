import createAdminUser
import json

AdminJsonFilePath = 'Admin.json'
UserJsonFilePath = 'User.json'

def CreateAdmin():
    createAdminUser.Add_New_Admin(AdminJsonFilePath)
    

def CreateUser():
    createAdminUser.Add_New_User(UserJsonFilePath)


def AdminLogIn():
    admin_name = input("Enter the Admin Name :")
    admin_password = input("Enter the Admin Password :")


    with open(AdminJsonFilePath,'r') as Json_file:
        AdminData = json.load(Json_file)
        # print(AdminData)

    for data in AdminData:
        # print(data)
        # print(data[admin_name])

        try:
            if data[admin_name] == admin_password:
                print("Admin login SuccessFully")
                
                
            else:
                print(f"{admin_name} ,You Entered wrong Password ")
        except KeyError:
            print(" -x-x-x-x-x-x- No Admin exist with this name -x-x-x-x-x-x- ")   


def UserLogIn():
    
    User_name = input("Enter the User Name :")
    User_password = input("Enter the User Password :")


    with open(UserJsonFilePath,'r') as Json_file:
        UserData = json.load(Json_file)
        # print(AdminData)

    for data in UserData:
        # print(data)
        # print(data[admin_name])

        try:
            if data[User_name] == User_password:
                print(f"========== {User_name} ,You login SuccessFully ==========")
            else:
                print(f"{User_name} ,You Entered wrong Password ")
        except KeyError:
            print(" -x-x-x-x-x-x- No User exist with this name -x-x-x-x-x-x- ")

