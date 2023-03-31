#!/usr/bin/python #SHEBANG!!!
"""

forms = ["animal", "mineral", "vegetable"]
answer = input("Are you animal, mineral, or vegetable? ")

if answer == forms[0]:
    print("You are an animal. GRR!")
elif answer == forms[1]:
    print("You are a mineral. You must be healthy.")
elif answer == forms[2]:
    print("You are a vegetable. Do you do anything at all")
else:
    print("You did not give a valid response.")


fmenu = {'spam':1.50, 'ham':1.99, 'eggs':0.99}

corder = input("What will you have today--spam, ham or eggs: ")

if corder == "spam":
    print("For the spam, that will be", "$" + "%.2f" % fmenu.get("spam"), "Please.")
elif corder == "ham":
    print("Your total for the ham is", "$" + "%.2f" % fmenu.get("ham"))
else:
    print("Eggs by default! Your total is", "$" + "%.2f" % fmenu.get("eggs"))


S = [x**2 for x in range(10)] #global name

def choice_a(x):
    print(S)
    return

def choice_b(x):
    V = [2**i for i in range(x)]
    print(V)
    return

def choice_c(y):
    M = [x for x in range(y) if x % 2 == 0]
    print(M)

def choice_d():
    raise SystemExit

print("Which Operation do you want to perform?\n")
print('''
a: x to the second power
b: 2 to the xth power
c: mod 2
d: quit program
''')
resp = input('Choice: ')
if resp == 'd':
    choice_d()
resp2 = int(input('Upper limit? '))

if resp == 'a':
    choice_a(resp2)
elif resp == 'b':
    choice_b(resp2)
elif resp == 'c':
    choice_c(resp2)
else:
    choice_d()


while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter Second nember: "))
        print('Division of the numbers is %.2f' % (a/b))
    except (ZeroDivisionError, IOError, TypeError, ValueError) as e:
        print("Error", e)
    else:
        break

"""

class MyError(Exception):
    '''
    This Error was created by Frank
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My Error occured. value:', e.value)


