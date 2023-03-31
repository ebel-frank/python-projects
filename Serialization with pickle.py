import pickle

dict1 = {'a':100,
         'b':200,
         'c':300}

list1 = [400,500,600]

print(dict1)
print(list1)

output = open('C:/Users/ebeledike/Desktop/IMG-20181001-WA0001.jpg', 'wb')

pickle.dump(dict1, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, output, pickle.HIGHEST_PROTOCOL)

output.close()

print('--------------------------------------------------------')

inputFile = open('C:/Users/ebeledike/Desktop/IMG-20181001-WA0001.jpg', 'rb')

dict2 = pickle.load(inputFile)
list2 = pickle.load(inputFile)

inputFile.close()

print(dict2)
print(list2)
