costprice=input("enter the cp:")
sellingprice=input("enter the sp:")
if(sellingprice>costprice):
    print("Profit!!")
elif(sellingprice==costprice):
    print("No profit no loss!")
else:
    print("Loss!!")