height=float(input("enter your height:"))
weight=float(input("enter your weight:"))
BMI = weight / (height/100)**2
print("Your BMI is:",BMI)
if BMI<=18.4:
    print("You are Underweight")
elif BMI<=24.9:
    print("You are Healthy")
elif BMI<=29.9:
    print("You are bulky")
elif BMI<=34.9:
    print("You are severely overweight")
elif BMI<=39.9:
    print("You are seriously overweight")
else:
    print("You are a planet")