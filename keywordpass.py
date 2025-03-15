n=int(input("Enter a range: "))
for x in range(n):
    if x % 2 == 0 :
        print("twist")
    elif x % 15 == 0 :
        pass
    elif x % 3 == 0 :
        print("flizz")
    else:
        print("buzz")