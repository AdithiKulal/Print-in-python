base_num=int(input("Enter the base number: "))
max_power=int(input("Enter the maximum power: "))
print("The power of ",base_num," is: ")
for i in range(1,max_power+1):
    power=base_num**i
    print(f"{base_num}^{i} = {power}")