import pandas as pd 


ProductFilePath = "Products.xlsx"

def ProductList():
    df = pd.read_excel(ProductFilePath)
    print()
    print(df)

ProductList()



def addItemInCart():

    ...
    

def SeeCart():
    df = pd.read_excel("userCartDetails.xlsx")
    print()
    print(df)

    exit()








while(True):
        print("\n\t\t---------- Press Key ----------\n")
        print("\t\t1 : Add items in cart")
        print("\t\t2 : See Cart")
        print("\t\t3 : See Product List")
        print("\t\t4 : Exit")
        
        user_input = int(input("\nEnter value :"))

       
        match user_input:

            case 1: 
                addItemInCart()

            case 2:
                SeeCart()
            
            case 3: 
                ProductList()

            case 4:
                exit()




     



'''

items=[]
quantity=[]

p1= int(input("\nEnter Product Id of the item which you want to Buy :"))
q1= int(input("Enter the quantity of the item (in kg):"))


items.append(p1)
quantity.append(q1)

ans = input("\nDo You want to more Item (Y/N):")

while(ans in "Yy"):
    p= int(input("\nEnter Product Id of the item which you want to Buy :"))
    q= int(input("Enter the quantity of the item (in kg):"))
    items.append(p)
    quantity.append(q)

    ans = input("\nDo You want to more Item (Y/N):")


print(items)
print(quantity)
'''