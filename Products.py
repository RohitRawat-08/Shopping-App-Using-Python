import pandas as pd 


ProductFilePath = "Products.xlsx"

def ProductList():
    df = pd.read_excel(ProductFilePath)
    print()
    print(df)

ProductList()






def addItemInCart():

    item=[]
    quantity=[]


    ans = "yY"

    while(ans in "Yy"):
        p= int(input("\nEnter Product Id of the item which you want to Buy :"))
        q= int(input("Enter the quantity of the item (in kg):"))
        
        item.append[p]
        quantity.append[q]

        ans = input("\nDo You want to more Item (Y/N):")

    data = {
        'ProductID': item,
        'Quantity': quantity,
    }


    df1 = pd.DataFrame(data)
    df2 = pd.read_excel(ProductFilePath)


    result_inner = pd.merge(df1, df2, on='ProductID', how='inner')
    result_inner.to_excel('userCartDetails.xlsx', sheet_name='MySheet', index=False)
    # print(result_inner)
    

    
   





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