x = [1,3,2,2,1,5,1,24,12,124,12,21,32,15]
print('list sebelum di filter : ', x)

def sort_odd_even(x):
    odds = []
    evens = []
    for i in x:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    odds.sort()
    evens.sort()
    evens.reverse()
    return odds + evens

print('list sesudah di filter : ', sort_odd_even(x))