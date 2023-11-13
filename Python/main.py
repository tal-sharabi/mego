'''
מפת המטמון
בתרגיל זה אתם תכתבו מטריצה של 3 על 3, והמשתמש יצטרך לסמן X בקואורדינטה שם לדעתו יושב המטמון
הגישה תיעשה באמצעות פניה לאינדקס עמודה ואז שורה
האינדוקס יהיה אינטואיטיבי למשתמש , יתחיל ב- 1 גם עבור השורה וגם עבור העמודה

מהלך התוכנית:
התוכנית תראה למשתמש את המפה
ותשאל אותו היכן יושב האוצר
(היכן להטמינו)

נניח, המשתמש בחר לשים אותו בעמודה השניה בשורה הראשונה
---------

לולאה

מעבר על כל הפריטים ברשימה
for item in list_of_items:
  do_something()


list_of_items = ["Tesla", "Ford", "Volkswagen"]
for item in list_of_items:  # for...in loop
    print(item)

range() function

# i stands for iterator
for i in range(1, 51):  # [1,4)
    print(f"{i}: I've been a bad boy")   # the print() func. implicitly incl. the '\n' escape char.

# עליכם לכתוב תוכנית המדפיסה אף ורק את המס' הזוגיים שבין 0 ל- 100 כולל
# תשובות בצ'אט בפרטי ולא לכולם!!!

# הצעת פתרון
for i in range(1, 101):
    if(i % 2 == 0):
        print(i)

מותר לנו לכתוב ביטוי בתוך הסוגריים


a = 12
b = 3
for i in range(1, a // b):
    print(i)


# תרגיל
עליכם לכתוב תוכנית המבקשת מהמשתמש ציונים של 4 סטודנטים, התוכנית תדפיס
את הציון הממוצע של הכיתה, עד 2 ספרות לאחר הנקודה


גודל הצעד
ניתן להגדיר גם את גודל הצעד
step size
למשל
אם היינו רוצים להציג את כל הכפולות של 3, בטווח המספרים שבין 3 ל- 30

for num in range(3, 31, 3):
    print(num)

תרגילון
כתבו תוכנית שתדפיס את סכום כל המספריים הזוגיים בין 0 ל- 100

תרגיל 7-בום!
בגרסת המתכנתים
כל פעם שמגיעים למספר שמכיל את הספרה 7, או שמתחלק ב 7 ללא שארית - מדפיסים בום!
אחרת, מדפיסים את המספר עצמו
1, 2, 3, 4, 5, 6, BOOM!,...,  16, BOOM!
20, BOOM!, 69, BOOM! BOOM! BOOM! BOOM! BOOM! BOOM! BOOM! BOOM! BOOM!, 80, ... 100

solution(?):
----------
for number in range(1, 1000):
    if (number % 7 == 0 or number / 7 == 1.0 or number / 10 == 7.0
            or number % 10 == 7 or number // 10 == 7) or str(7) in str(number):
        print("Boom!")
    else:
        print(number)
'''
import random
# random.choice()
# camelCase
list_of_annoying_students = [1, 2, 3]
a_random_element = random.choice(list_of_annoying_students)
print(type(a_random_element))
# print(a_random_element)



