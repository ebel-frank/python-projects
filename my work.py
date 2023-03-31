# compination
print('HELLO WORLD')
print('My name is EBELEDIKE PC, because i belong to EBELEDIKE')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('so')
print('today we are going to do someting called REVERSE CIPHER')
print('so type anything and I will show you the reverse of what you typed')

massage = input('Enter massage: ')
translated = ''

i = len(massage) - 1
while i >= 0:
    translated = translated + massage[i]
    i = i -1

print(translated)

print('and there you go!!!')
print('cool isn\'t it?')
met = input('(yes or no): ')
met = met.lower()
if met[0] == 'y':
    print ('Thanks')
else:
    print ('Fuck off')
