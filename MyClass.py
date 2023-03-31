class MyClass:
    name = "frank"
    number = 1234

me = MyClass()
me.name = "Tyler"
me.number = 456

friend = MyClass()
friend.name = "David"
friend.number = 234

empty = MyClass()

print("name: " + me.name + ", number:", me.number)
print("name: " + friend.name + ", number:", friend.number)
print("name: " + empty.name + ", number:", empty.number)
    
        
