import math


def cos(num1):
    num1= int(num1)
    sum = math.cos(num1)
    sum = checkInt(sum)
    print(sum)


def sin(num1):
    num1 = int(num1)
    sum = math.sin(num1)
    sum = checkInt(sum)
    print(sum)


def tan(num1):
    num1 = int(num1)
    sum = math.tan(num1)
    sum = checkInt(sum)
    print(sum)


def add(num1, num2):
    sum = num1 + num2
    sum = checkInt(sum)
    print(sum)


def div(num1, num2):
    sum = num1 / num2
    sum = checkInt(sum)
    print(sum)


def mul(num1, num2):
    sum = num1 * num2
    sum = checkInt(sum)
    print(sum)


def less(num1, num2):
    sum = num1 - num2
    sum = checkInt(sum)
    print(sum)


def hezka(num1, num2):
    sum = num1 ** num2
    sum = checkInt(sum)
    print(sum)


def checkOP(mathOP):
    if mathOP == "+":
        print("Enter the second number")
    elif mathOP == "/":
        print("Enter the second number")
    elif mathOP == "*":
        print("Enter the second number")
    elif mathOP == "-":
        print("Enter the second number")
    elif mathOP == "**":
        print("Enter the second number")
    elif mathOP == "cos":
        print("Enter the second number")
    elif mathOP == "sin":
        print("Enter the second number")
    elif mathOP == "tan":
        print("Enter the second number")
    else:
        print("The commend is not readily available")


def check(mathOP):
    if mathOP == "+":
        add(num1, num2)
    elif mathOP == "/":
        div(num1, num2)
    elif mathOP == "*":
        mul(num1, num2)
    elif mathOP == "-":
        less(num1, num2)
    elif mathOP == "**":
        hezka(num1, num2)
    elif mathOP == "cos":
        cos(engle)
    elif mathOP == "sin":
        sin(engle)
    elif mathOP == "tan":
        tan(engle)
    else:
        print("The commend is not readily available")


def checkInt(sum):
    if sum % 1 == 0:
        sum = int(sum)
        return sum
    else:
        return sum


print("If you want to calculate Trigo Enter 't'")
print("else enter something else...")
OrNot = input()

if OrNot == "t":

    print("Enter the math operation , cos , sin , tan")
    trigoMathOp = input()
    print("Enter the engle")
    engle = input()
    check(trigoMathOp)
else:
    print("enter the first number")
    num1 = input()
    num1 = float(num1)
    print("enter the math operation ")
    print("+ = veod ")
    print("- = pahot ")
    print("* = kaful ")
    print("/ = helkey")
    print("** = hezka ")
    mathOP = input()
    checkOP(mathOP)
    num2 = input()
    num2 = float(num2)
    check(mathOP)
