"""
print("Welcome to the Movie Theater")
while True:     # True is used to make it a continuous loop
    age = int(input("What is your age: "))
    if age < 0:
        print("please enter a valid age")
        continue
    if age <= 3:
        print("The ticket is free")
    elif age > 3 and age <= 12:
        print("the ticket is 10$")
    else:
        print("The ticket is 15$")

"""
def find_winner(**kwargs):
    return max(min(kwargs, key=kwargs.get(2)))

h = find_winner(5)
print(h)
