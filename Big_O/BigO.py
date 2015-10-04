from graph import *


def fillList(size):
	list1 = []
	for i in range(1, size + 1):
		list1.append(i)
	return list1

def O1(input):
    count = 0
    result = input[len(input) / 2]
    count += 1
    return count


def OlogN(input):
    def search(length, count):
        count += 1
        length /= 2
        if length == 1 or length == 0:
            return 1 + count
        else:
            return 1 + search(length, count)
    return 1 + search(len(input), 1)

def ON(input, check):
    count = 0
    for number in input:
        count += 1
        if number == check:
            return 1 + count

def ON2(input):
    count = 0
    for i in input:
        count += 1
        for j in input:
            count += 1
    return 1 + count

def ON3(input):
    count = 0
    for i in input:
        count += 1
        for j in input:
            count += 1
            for k in input:
                count +=1
    return 1 + count


x_values = []
plots = []


'''
#O1
title = 'O(1)'
for i in range(10, 105, 5):
	plots.append(O1(fillList(i)))
	x_values.append(i)'''


'''
#OlogN
title = 'O(logN)'
for i in range(10000, 500000, 10000):
	plots.append(OlogN(fillList(i)))
	x_values.append(i)'''

'''
#ON
title = 'O(N)'
for i in range(1000, 50000, 1000):
    plots.append(ON(fillList(i), i))
    x_values.append(i)'''

'''#ON^2
title = 'O(N^2)'
for i in range(100, 1000, 10):
    plots.append(ON2(fillList(i), fillList2(i)))
    x_values.append(i)'''

#ON^3
title = 'O(N^3)'
for i in range(1, 100, 2):
    plots.append(ON3(fillList(i)))
    x_values.append(i)


graph(x_values, plots, title, 'foo')

