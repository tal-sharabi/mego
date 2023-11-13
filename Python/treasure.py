"""
פסאודו קוד
בדיקת  = BMI
BMI=weight(kg)/height(M)^
1)נבדוק האם מתחת לגיל 65
 2)אם כן, אם bmi פחות מ18.5 הוא תת משקל
 אחרת,אם הוא מתחת ל25 משקל תקין
 אחרת אם הוא מתחת ל-30 משקל יתר
 אחרת השמנת יתר)
 3)אם לא נבדוק אם הוא מתחת ל75
 4)נבדוק אם פחות מ22 תת משקל
 אחרת אם פחות מ27 משקל תקין
 אחרת אם פחות מ30 משקל יתר
 אחרת השמנת יתר
 5)אחרת נבדוק אם הוא פחות או שווה 23 תת משקל
 אחרת אם הוא פחות מ28 משקל תקין
 אחרת אם פחות מ30 משקל יתר
 אחרת השמנת יתר
"""
#print("Your BMI is: {:.2f}".format(BMI))

age = int(input("Enter your age please: "))
weight = int(input("Enter your weight: "))
height = float(input("Enter your height(in Meters): "))
bmi = weight/height**2
if age < 65:
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}, you are underweight")
    elif bmi < 25:
        print(f"Your result is  {bmi:.2f}, Your weight is normal")
    elif bmi < 30:
        print(f"Your BMI is {bmi:.2f}, you are overweight")
    else:
        print(f"Your BMI is  {bmi:.2f}, You are obese")
elif age < 75:
    if bmi < 22:
        print(f"Your BMI is  {bmi:.2f}, you are underweight")
    elif bmi < 27:
        print(f"Your result is  {bmi:.2f}, Your weight is normal")
    elif bmi < 30:
        print(f"Your BMI is  {bmi:.2f}, you are underweight")
    else:
        print(f"Your BMI is  {bmi:.2f}, You are obese")
else:
    if bmi <= 23:
        print(f"Your BMI is  {bmi:.2f}, you are underweight")
    elif bmi < 28:
        print(f"Your result is  {bmi:.2f}, Your weight is normal")
    elif bmi < 30:
        print(f"Your BMI is  {bmi:.2f}, you are underweight")
    else:
        print(f"Your BMI is  {bmi:.2f}, You are obese")


