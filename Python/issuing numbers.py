#ככה נוציא כל מספר בנפרד
x_float=(0123.456)
x_int=int(x_float)
print(x_int//1000%10)#0אלפים
print(x_int//100%10)#מאיות1
print(x_int//10%10)#2עשרות
print(x_int%10)#3יחידות
print(int(x_float*10%10))#עשרוני4
print(int(x_float*100%10))#5
print(int(x_float*1000%10))#6
input('bye')