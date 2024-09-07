import json


# Adding Admin Data 
# AdminJsonFilePath = 'Admin.json'


def LoadAdminData(Filepath):
    try:
        with open(Filepath,'r') as Json_file:
            return json.load(Json_file)
    except FileNotFoundError:
        return [{}]

def Add_New_Admin(Filepath):

    data = LoadAdminData(Filepath)
    # print(data[0])

    admin_name = input("\tEnter Admin Name: ")
    admin_password = input("\tEnter Admin Password: ")

    data[0].update({admin_name:admin_password})

    # print(data)

    with open(Filepath,'w') as json_file:
        json.dump(data, json_file,indent=4)

    print("\t======== Successfull Added New Admin!!! ========")


# Add_New_Admin(AdminJsonFilePath)

# Adding User Data 
# UserJsonFilePath = 'User.json'


def LoadUserData(Filepath):
    try:
        with open(Filepath,'r') as Json_file:
            return json.load(Json_file)
    except FileNotFoundError:
        return [{}]

def Add_New_User(Filepath):
    
    data = LoadUserData(Filepath)
    # print(data)

    user_name = input("\tEnter User Name: ")
    user_password = input("\tEnter User Password: ")


    data[0].update({user_name:user_password})

    # print(data)

    with open(Filepath,'w') as json_file:
        json.dump(data, json_file,indent=4)

    print("\t======== Successfull Added New User!!! ========")







