string = input("Please enter your own word : ")
char = input("Please enter your own character : ")
i=1
count=0
for i in range (len(string)):
    if (string[i]==char) :
        count= count+1
    i=i+1
print("The total number of times the character has occured = ", count)