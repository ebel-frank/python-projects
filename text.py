# class Person:
#     __instance = None
#
#     @staticmethod
#     def instance(name, age):
#         if Person.__instance is None:
#             Person.__instance = Person(name, age)
#         return Person.__instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person.instance("Frank", 56)
# p2 = Person.instance("David", 61)
# print(p1 is p2)
# print(p1.name)
# print(p1.age)
# print(""""------------------------""")
# print(p2.name)
# print(p2.age)

import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])


