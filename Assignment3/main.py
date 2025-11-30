def exercise1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Numbers between them:")
    if a < b:
        for num in range(a+1, b):
            print(num, end=" ")
    else:
        for num in range(b+1, a):
            print(num, end=" ")
    print()


def exercise2():
    n = int(input("Enter a number: "))

    total = 0
    for i in range(1, n):
        if i % 2 == 1:
            total += i

    print("Sum of odd numbers less than", n, "is:", total)


def exercise3():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    count = 0
    if a < b:
        for num in range(a+1, b):
            if num % 7 == 0:
                count += 1
    else:
        for num in range(b+1, a):
            if num % 7 == 0:
                count += 1

    print("Count of multiples of 7 between numbers:", count)


def exercise4():
    print("Two-digit numbers whose ones digit > tens digit:")
    for num in range(10, 100):
        tens = num // 10
        ones = num % 10
        if ones > tens:
            print(num, end=" ")
    print()


def exercise5():
    print("Numbers between 1 and 100 that are multiples of 3 and 5:")
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(num, end=" ")
    print()



def main():
    print("Choose exercise from series 3 (1-5):")
    print("1. Numbers between two inputs")
    print("2. Sum of odd numbers less than input")
    print("3. Count multiples of 7 between two inputs")
    print("4. Two-digit numbers with ones digit > tens digit")
    print("5. Numbers between 1 and 100 that are multiples of 3 and
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
    else:
        print("Invalid choice.")



main()
