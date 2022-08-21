# Program make a simple calculator
from itertools import combinations, combinations_with_replacement
from itertools import permutations
from collections import Counter
import statistics
import numpy as np
import unittest
global nm
global factorial


# This function adds two numbers


def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


def ANDOpertation(x, y):
    x = bin(x).replace("b", "")
    y = bin(y).replace("b", "")
    x = str(x)
    y = str(y)
    multiplication = int(x, 2)*int(y, 2)
    binar = bin(multiplication)
    print(x, y)
    print(binar)


def OROperation(x, y):
    x = bin(x).replace("b", "")
    y = bin(y).replace("b", "")
    x = str(x)
    y = str(y)
    multiplication = int(x, 2)+int(y, 2)
    binar = bin(multiplication)
    print(x, y)
    print(binar)


def NOROperation(x, y):
    x = bin(x).replace("b", "")
    y = bin(y).replace("b", "")
    x = str(x)
    y = str(y)
    orop = int(x, 2)+int(y, 2)
    binar = bin(orop).replace("b", "")
    binar = int(binar)
    print("X", x, "y", y)
    print("OR", binar)

    # convert NOR

    togg = ""
    while(binar):
        t = binar % 10
        if t == 1:
            togg = togg+"0"
        else:
            togg = togg+"1"
        binar = int(binar/10)
    print("NOR", togg[::-1])

    # print(~int(binar))


def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact*i
    return fact


def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def permutation(A):
    seq = permutations(A)
    for p in list(seq):
        print(p)


def IntReverse(n):
    nume = n
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    print("The Reverse number of ",
          nume, " is ", rev)


def combination(A, len):
    seq = combinations_with_replacement(A, len)
    for p in list(seq):
        print(p)


def mean_med_mode(n):

    # Mean
    nlen = len(n)
    index = nlen//2
    n.sort()
    get_sum = sum(n)
    mean = get_sum / nlen
    print("Mean / Average is: " + str(mean))

    # Median
    if nlen % 2 == 0:
        median = sorted(n)[index]
    else:
        median = sum(sorted(n)[index-1: index+1])/2

    print("Median is:- ", median)

    # Mode
    mode = statistics.multimode(n)
    # data = Counter(n)
    # mode = [k for k, v in data.items() if v == data.most_common(1)[0][1]]
    print("Mode is:- ", mode)


def dictVar_StdDev(A):

    vari = np.var(A)
    # print(vari)

    # mean = sum(A)/len(A)
    # variance = sum([((x - mean)**2)for x in A])/len(A)
    # res = variance**0.5

    print("Variance is:- ", vari)

    std = np.std(A)
    print("Standard Deviation is:- ", std)


print("-----------------------------------------------------Scientific Calculator-------------------------------------------------")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.AND Operation")
print("6.OR Operation")
print("7.NOR Operation")
print("8.Factorial")
print("9.Fibonacci")
print("10.Permutation")
print("11.Integer Reverse")
print("12.Combination")
print("13.Mean. Median, Mode")
print("14.Dictionary, Variance and Standard Deviation")
print("15.Testing Operation")


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'):

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))
            lastans = add(num1, num2)

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))
            lastans = subtract(num1, num2)

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))
            lastans = multiply(num1, num2)

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))
            lastans = divide(num1, num2)

        elif choice == '5':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            ANDOpertation(num1, num2)

        elif choice == '6':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            OROperation(num1, num2)

        elif choice == '7':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            NOROperation(num1, num2)

        elif choice == '8':
            num1 = int(input("Enter number: "))
            print("The Factorial of ", num1, " is ", factorial(num1))

        elif choice == '9':
            num1 = int(input("Enter number: "))
            print("The Fibonacci number of ",
                  num1, " is ", fibonacci(num1))

        elif choice == '10':
            A = []
            no = int(input("Enter number of elements: "))
            for i in range(0, no):
                ele = int(input())
                A.append(ele)
            permutation(A)

        elif choice == '11':
            num = int(input("Enter number to reverse: "))
            IntReverse(num)

        elif choice == '12':
            A = []
            no = int(input("Enter number of elements: "))
            len = int(input("Enter lenght of permutation: "))
            for i in range(0, no):
                ele = int(input())
                A.append(ele)
            combination(A, len)

        elif choice == '13':
            A = []
            no = int(input("Enter number of elements: "))
            for i in range(0, no):
                ele = int(input())
                A.append(ele)
            mean_med_mode(A)

        elif choice == '14':
            A = []
            no = int(input("Enter number of elements: "))
            print("Enter elements in the key value pair:- e.g('a'=> key and '1'=> value)")
            d = dict(input().split() for x in range(no))
            print(d)
            for value in d.values():
                A.append(value)
            intmap = map(int, A)
            B = list(intmap)
            print(B)
            dictVar_StdDev(B)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break

    else:
        print("Invalid Input")
