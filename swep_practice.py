def filter(*args):
    data = []
    counter = 0
    for i in args:
        if i == 6:
            data.append(i)
        elif i == 5.5:
            data.append(i)
        else:
            data.append(i)
        counter += 1
        if counter == 7:
            break
    print(data)


def filter2(*args):
    seats = {6:0, 5.5:0, 4:0}
    for i in args:
        if i == 4:
            seats[i] += 1
        elif i == 5.5:
            seats[i] += 1
        elif i == 6:
            seats[i] += 1
    return seats

# print(filter2(5,6,6,5.5,4.5,4,5.5,6,4))

