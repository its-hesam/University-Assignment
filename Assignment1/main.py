def exercise1():
    age = int(input("Enter your age (years): "))
    hours_sleep_per_day = 8  
    total_sleep_hours = age * 365 * hours_sleep_per_day
    print(f"Total sleep in your lifetime: {total_sleep_hours} hours")



def exercise2():
    r = float(input("Enter radius: "))
    circumference = 2 * 3.14159265 * r
    area = 3.14159265 * (r ** 2)
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")


def exercise3():
    A = float(input("Enter number A: "))
    B = float(input("Enter number B: "))
    print(f"Before swap: A = {A}, B = {B}")
    A, B = B, A
    print(f"After swap: A = {A}, B = {B}")



def exercise4():
    weight = float(input("Enter rice amount (kg): "))
    price_per_kg = float(input("Enter price per kg: "))

    min_price = price_per_kg * 0.45   
    max_price = price_per_kg * 1.15   

    total_min = min_price * weight
    total_max = max_price * weight

    print(f"Minimum possible total price: {total_min}")
    print(f"Maximum possible total price: {total_max}")


def exercise5();
    r = 14  
    side = 2*r
    area_blue = side**2 - 3.14159265*r*r
    weight = area_blue * 8 
    price_per_gram = 58.27
    price = weight * price_per_gram
    print(f"Price of the blue area: {price}")


def main():
    print("Which exercise do you want to run?")
    print("1. Total sleep hours in lifetime")
    print("2. Circle circumference & area")
    print("3. Swap two numbers")
    print("4. Rice price fluctuation")
    print("5. Price of the blue area")

    choice = input("Enter exercise number (1-5): ")

    if choice == "1":
        exercise1()
    elif choice == "2":
        exercise2()
    elif choice == "3":
        exercise3()
    elif choice == "4":
        exercise4()
    elif choice == "5":
        exercise5()
    else:
        print("Invalid choice!")


main()
