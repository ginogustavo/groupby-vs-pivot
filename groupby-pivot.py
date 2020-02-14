import pandas as pd
sales=pd.read_csv("Sales.csv")
groupByCust=sales.groupby("CustName")
print(groupByCust.sum())

firstDate = sales.pivot_table(
    values = "OrderDate",
    index = "ProdID",
    columns = "CustName" ,
    aggfunc = "first"
)
print(firstDate)
