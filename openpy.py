import pandas as pd
ProductFilePath = "Products.xlsx"


def addItemInCart():

    p1= int(input("\nEnter Product Id of the item which you want to Add in Cart :"))
    q1= int(input("Enter the quantity of the item (in kg):"))

    data = {
        'ProductID': [p1],
        'Quantity': [q1],
    }


    df1 = pd.DataFrame(data)
    df2 = pd.read_excel(ProductFilePath)


    result_inner = pd.merge(df1, df2, on='ProductID', how='inner')
    print(result_inner)
    
    result_inner.to_excel('userCartDetails.xlsx', sheet_name='MySheet', index=False)

addItemInCart()