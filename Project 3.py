#BMI calculator
a=float(input("Enter your height in centimeters:"))
b=float(input("Enter your weight in kilograms:"))
c=b/(a/100)**2
print(c)
if(c<18.5):
    print("You are underweight")
elif(c>18.5 and c<24.9):
    print("You are normal weight")
elif(c>25.0 and c<29.9):
    print("You are overweight")
else:
    print("You are obese")
