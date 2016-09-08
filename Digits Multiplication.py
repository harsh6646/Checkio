def checkio(number):
    if number == 0:
        return 0
    total = 1
    number = str(number)
    for x in number:
        if int(x) != 0:
            total *= int(x)
            print(total)
    return total
print(checkio(123123))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
