num=int(input("Enter the number: "))
number_digit=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**number_digit
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")