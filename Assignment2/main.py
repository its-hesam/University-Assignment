def exercise1():
    n = int(input("Enter a number: "))
    if 100 <= abs(n) <= 999:
        print("The number is 3-digit.")
    else:
        print("The number is NOT 3-digit.")


def exercise2():
    print("Enter 5 numbers:")
    even_number = None
    for i in range(5):
        num = int(input(f"Number {i+1}: "))
        if num % 2 == 0 and even_number is None:
            even_number = num
    if even_number is not None:
        print("First even number is:", even_number)
    else:
        print("No even number found.")


def exercise3():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")


def exercise4():
    n = int(input("Enter a number: "))
    if n % 5 == 0 and n % 2 == 0:
        print("Yes")
    elif n % 5 == 0:
        print("No")
    else:
        print("Not acceptable")


def exercise5():
    nums = []
    for i in range(4):
        nums.append(float(input(f"Enter number {i+1}: ")))
    print("The smallest number is:", min(nums))


def exercise6():
    total = 0
    print("Enter 3 numbers:")
    for i in range(3):
        n = int(input(f"Number {i+1}: "))
        if n % 2 != 0:
            total += n
    print("Sum of odd numbers is:", total)


def exercise7():
    n = input("Enter a 3-digit number: ")
    total = sum(int(d) for d in n)
    print("Sum of digits =", total)



def main():
    print("Choose exercise (1-7):")
    print("1. Check 3-digit number")
    print("2. First even number from 5 inputs")
    print("3. Triangle type")
    print("4. Divisibility check")
    print("5. Smallest of 4 numbers")
    print("6. Sum of odd numbers from 3 inputs")
    print("7. Sum of digits of a 3-digit number")
    choice = int(input("Your choice: "))

    if choice == 1:
        exercise1()
    elif choice == 2:
        exercise2()
    elif choice == 3:
        exercise3()
    elif choice == 4:
        exercise4()
    elif choice == 5:
        exercise5()
    elif choice == 6:
        exercise6()
    elif choice == 7:
        exercise7()
    else:
        print("Invalid choice.")



main()
