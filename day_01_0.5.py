weight_in_kg=float(input("enter weight:"))
Height_in_m=float(input("enter height:"))
BMI=weight_in_kg/(Height_in_m*Height_in_m)
matching_category=0
if BMI<18.5:
    matching_category="underweight.uppercase()"
elif BMI>=18.5 and BMI<=24.9:
    matching_category="normal weight.uppercase()"
elif BMI>=25.0 and BMI<=29.9:
    matching_category="overweight.uppercase()"
else:
    matching_category="obese.uppercase()"
print("Calculated BMI score:",BMI)
print("Matching Category:",matching_category)