height = float(input("Enter you height in cm = "))
weight = float(input("Enter your weight in kg = "))
bmi = weight/(height/100)**2
print("Your BMI is ",bmi)

if bmi <= 18.4:
    print("Your under Weight.")
elif bmi <= 29.4:
    print("Your weight is Normal.")
elif bmi <= 29.9:
    print("You are over Weight.")
elif bmi <= 34.9:
    print("You are Obese.")
else:
    print("You are extremely Obese.")