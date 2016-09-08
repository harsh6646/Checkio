def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    total = 0
    for x in range(len(array)):
        if len(array) == 0:
            break
        else:
            if x % 2 == 0:
                total += array[x]
                print (total, x)
    if len(array) != 0:
        print('wew')
        total *= array[len(array)-1]
        print(total, len(array)-1)
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
print("it's good")