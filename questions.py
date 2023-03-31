#Question 1
#if we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5 ,6 and 9. The sum of the multiples is 23. write a function to
#find the sum of all the multiples of 3 or 5 below 1000


numbers = list(range(1000))
lists = []

for i in numbers:
    if i%3 == 0 or i%5 == 0:
        if i != 0:
            lists.append(i)
    else:
        pass

lists.sort()
plus = sum(set(lists))

if __name__=="__main__":
    print(plus)


def multiple(x):
    total = 0
    for i in range(x):
        if (i % 3 == 0 or i % 5 == 0):
            total += i
    print(total)



#Question 2
"""
 Write a program that takes one or more filenames
 as arguments and prints all the lines which are
 longer than 40 characters
"""

import os

filename = input("Please enter a filename: ")
os.chdir(filename)
filenames = os.listdir()


def File(filenames):
    for f in filenames:
        handle = open(f)
        for lines in handle:
            if len(lines)<40:
                pass
            else:
                print(lines)
        handle.close()

if __name__=='__main__':
    File(filenames)

