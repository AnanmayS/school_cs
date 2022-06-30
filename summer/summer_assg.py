from math import sqrt
import sys
import os
import subprocess

finder = True
finding = True

def try_again():
    ans = 'pp'
    while ans.lower()[0] != 'y' or ans.lower()[0] == 'n':
        ans = input("Do you try again?(y or n): ")
        if ans.lower()[0] == 'n':
            sys.exit("BYE")
    if ans.lower()[0] == 'y':
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
                        sys.argv[1:])

def per(sideA, sideB, sideC):
    return print(f'The perimeter is {sideA + sideB + sideC}')


def area(sideA, sideB):
    area_ = (sideA * sideB) / 2
    return print(f'The area is {area_}')


def angle_find(angle1, angle2):
    return 180 - angle1 - angle2


def side_find_c(side1, side2):
    return sqrt((side1 ** 2) + (side2 ** 2))


def side_find_not_c(sideC, sideLeg):
    return sqrt((sideC ** 2) - (sideLeg ** 2))


while finder:
    try:
        A = int(input("What is the side length for side A: "))
        B = int(input("What is the side length for side B: "))
        C = int(input("What is the side length for side C: "))
        finder = False
    except ValueError:
        print("Please Input a number")
        finder = True

while finding:
    try:
        a = int(input("What is the angle measure for angle a: "))
        b = int(input("What is the angle measure for angle b: "))
        c = int(input("What is the angle measure for angle c: "))
        finding = False
    except ValueError:
        print("Please Input a number")
        finding = True


# Angle Check
if a > 180 or b > 180 or c > 180:
    print("Invalid Triangle")
    try_again()

# Finding Angles
if a != 0 and b != 0 and c == 0:
    c = angle_find(a, b)

elif a == 0 and b != 0 and c != 0:
    a = angle_find(b, c)

elif a != 0 and b == 0 and c != 0:
    b = angle_find(a, c)

# Finding C
if A != 0 and B != 0 and C == 0:
    if a == 90:
        C = side_find_not_c(A, B)
    elif b == 90:
        C = side_find_not_c(B, A)
    elif c == 90:
        C = side_find_c(A, B)
    else:
        C = 'Side C can not be found'

# Finding A
elif A == 0 and B != 0 and C != 0:
    if a == 90:
        A = side_find_c(C, B)
    elif b == 90:
        A = side_find_not_c(B, C)
    elif c == 90:
        C = side_find_not_c(C, B)
    else:
        A = 'Side A can not be found'

# Finding B
elif A != 0 and B == 0 and C != 0:
    if a == 90:
        B = side_find_not_c(A, C)
    elif b == 90:
        B = side_find_c(A, C)
    elif c == 90:
        C = side_find_not_c(C, A)
    else:
        A = 'Side A can not be found'

# Area and Perimeter
if A != 0 and B != 0 and C != 0:
    per(A, B, C)
    if c == 90:
        area(A, B)
    elif a == 90:
        area(B, C)
    elif b == 90:
        area(A, C)

print(f'Side A = {str(A)} Side B = {str(B)} Side C = {str(C)}')
print(f'Angle a = {str(a)} Angle b = {str(b)} Angle c = {str(c)}')
