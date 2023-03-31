"""
Name: testing.py
Author: Frank C. Ebeledike
Purpose: Test our module imports
"""
p = int(input("Type an integer:"))
def square(x):
    return x * x

if __name__ == '__main__':
    print('testing: square of 2 ==', square(p))
