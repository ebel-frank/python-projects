import time

def wait(question, delay):
    time.sleep(delay)
    print(question)
    return input("#: ")

print(
"""This is a program to predict the love percentage between two persons,
Note that characters must all be alphabets.
""")

name1 = input("Enter your name: ")
name1set = set(name1)
name2 = input("Enter your crush name: ")
name2set = set(name2)

if(name1=='' or name2==''):
    print("please try again")
    raise SystemExit()

print("\nPermit me to ask you this few questions.")

Y = wait("How long have you guys known each other? #enter the number in years eg. 2", 2)
Hm = wait("Rate your honesty in that relationship? #on a scale of 1 to 10", 2)
Hf = wait("Rate your crush honesty in that relationship? #on a scale of 1 to 10", 2)
G = wait("How much importance do you attach to good looks? #on a scale of 1 to 100", 2) 

nameUnion = name1set.union(name2set)

nameDiff1 = name1set.difference(name2set)
nameDiff2 = name2set.difference(name1set)
D = len(nameDiff1) + len(nameDiff2)

countname = float(len(nameUnion))

if Y=="" or Hm=="" or Hf=="" or G=="":
    print("please all entries are required.")
    raise SystemExit()
else:
    Y = float(Y)
    Hm = float(Hm)
    Hf = float(Hf)
    G = float(G)
    lovePercent = (10*Y) - (0.2*countname) + (0.9*Hm) + (0.3*Hf) + (0.5*G) - (0.3*D)
    if(lovePercent>90): lovePercent = 90.00
    print("\nThe love percentage between", name1, "and", name2, "is", "%.2f" % lovePercent+"%")

print("We're Done")
