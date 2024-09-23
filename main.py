import login

def main():
    print("\n\n================== Welcome to the Demo Marketplace ==================\n")

    while(True):
        print("\n\t\t---------- Press Key ----------\n")
        print("\t\t1 : Create Admin")
        print("\t\t2 : Create User")
        print("\t\t3 : Admin Log in")
        print("\t\t4 : User Log in")
        print("\t\t5 : Exit\n")
        
        user_input = int(input("\nEnter value :"))

       
        match user_input:

            case 1: 
                login.CreateAdmin()

            case 2:
                login.CreateUser()

            case 3:
                login.AdminLogIn()

            case 4:
                login.UserLogIn()
            case 5:
                exit()



if __name__ == "__main__":
    main()