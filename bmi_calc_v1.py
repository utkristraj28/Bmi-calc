weight = None
height = None

print("__________SELECT A WEIGHT CATEGORY___________")
w_selection = input("In Pound / kg: ").lower()
if w_selection == "kg":
    in_kg = float(input("Your Weight in KG: "))
    weight = in_kg
elif w_selection =="pound":
    in_pound = float(input("Your Weight in pound: "))
    weight = in_pound * 0.453592 
else:
    print("invalid selection!!")
    
print("__________SELECT A HEIGHT CATEGORY___________")
h_selection = input("In cm / feet / m: ").lower()
if h_selection == "m":
    in_m = float(input("Your Height in meter: "))
    height = in_m
elif h_selection == "cm":
    in_cm = float(input("Your Height in cm: "))
    height = in_cm / 100
elif h_selection == "feet":
    in_feet = float(input("Your Height in feet: "))
    height = in_feet / 3.28
else:
    print("Invalid Selection!!")

h_squared = height * height
bmi = weight / h_squared    
#print(weight)    
#print(round(height,2))
#print(round(bmi,2))
print(f"Your BMI: {round(bmi,2)}")

if bmi <= 16:
    print("You are Severely UnderWeight")
elif bmi>16.1 and bmi<=18.5:
    print("Your are UnderWeight")
elif bmi>18.6 and  bmi<=24.9:
    print("Your are Healthy")
elif bmi>25 and  bmi<=29.9:
    print("Your are OverWeight")
elif bmi>30 and  bmi<=39.9:
    print("Your are Obese")
else:
    print("Your are Morbidly Obese")
    
    