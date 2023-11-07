def multiply_3():
    x=int(input("First number: "))
    y=int(input("Second number: "))
    z=int(input("Third number: "))
    print(x*y*z)

def get_full_name():
    x=input("First name: ")
    y=input("Last name: ")
    print(f"{x} {y}")

def print_largest_number():
    x=int(input("First number: "))
    y=int(input("Second number: "))
    z=int(input("Third number: "))
    print(max(x,y,z))

def print_longest_name():
    x=input("First name: ")
    y=input("Second name: ")    
    z=input("Third name: ")  
    if len(x) > len(y):
        if len(x) > len(z):
            print(x)
        else:
            print(z)    
    elif len(y) > len(z):
        if len(y) > len(x):
            print(y)
    else:
        print(z)

def even_or_odd():
    x=(int(input("Enter a number: ")))
    if x % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
        
def calculate_circle_area():
    import math
    r = int(input("Enter a radius: "))
    area = (r**2*math.pi)
    print(f"The area is {area}")

    
