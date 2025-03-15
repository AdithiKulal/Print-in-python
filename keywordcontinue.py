var= int(input("Enter a number: "))
for x in range(var):
   var-=1
   if var==5:
        continue
   print("Current value estimated is: ",var)
print("Goodbye")