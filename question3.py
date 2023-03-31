# Question
'''
Create a class that holds a: 
name, 
age, 
and a list of friends that can be added too!

The output should print the names alongside their ages
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    global friends
    friends = []

def Names():
    global persons
    persons = [Person("Frank", 17),
              Person("Victor", 18),
              Person("Lot Marcus", 16)]
        
    for person in persons:
        friends.append(person.name)
    print('Names:', friends)

    for person in persons:
        print(person.name,'is', str(person.age), 'years old.')
    

if __name__=='__main__':
    Names()


