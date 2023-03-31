"""

test_case = int(input("Enter test case: "))
result = ""
for i in range(test_case):
    def var(x):
        distance = 0
        rule = [i for i in x.strip("0")]
        rule.pop(0)
        for i in rule:
            if i == "0": distance += 1
            if i == "1":
                if distance <= 4:
                    global result
                    result += "NO\n"
                    return None
                else:
                    distance = 0
                    continue
        result += "YES\n"
    test_case = int(input("Enter N: "))
    a = input()
    var(a)

print(result)

// this is another question
def collatz(number):
    if (number % 2) == 0:
        print(number//2)
        return (number//2)
    elif (number % 2) == 1:
        print(3 * number + 1)
        return (3 * number + 1)

number = int(input("Enter number: "))

while(True):
    number = collatz(number)
    if (number == 1):
        break
"""
words = "hello this is fr%ank"
word_list = words.split(" ")
characters = "abcdefghijklmnopqrstuvwxyz "
new_word_list = []

for i in words:
    if i not in characters:
        print(i)
        words = words.replace(i, "")
        round()
    else:
        pass


