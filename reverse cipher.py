# Reverse cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# Generators

massage = input()
translated = ''

i = len(massage) - 1
while i >= 0:
    translated = translated + massage[i]
    i = i -1
     
print(translated)

# Iterators

class reverse_iter:
    def __init__(self, lists):
        self.lists = lists
        self.list1 = self.lists[-1::-1]
        self.num = 0

    def __next__(self):
        Iter = iter(self.list1)
        list2 = list(Iter)
        
        if self.num<len(self.list1):
            list3 = list2[self.num]
            self.num += 1
            return list3
        else:
            raise StopIteration()

#>>> it = reverse_iter([1, 2, 3, 4])
#>>>  it.__next__()
