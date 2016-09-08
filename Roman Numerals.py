def checkio(data):
    ind = {1:["I","V"],2:["X","L"],3:["C","D"],4:["M"]}
    length = len(str(data))
    num = int(str(data)[0])
    number = ""
    if length > 1:
        next = int(str(data)[1:])
    if num > 0 and num < 4:
        number = ind[length][0]*num
    elif num == 4:
        number = ind[length][0] + ind[length][1]
    elif num > 4 and num < 9:
        number = ind[length][1] + ind[length][0]*(num-5)
    elif num == 9:
        number = ind[length][0] + ind[length+1][0]
    if length != 1:
        print(number+checkio(next))
        return number + checkio(next)
    else:
        return number


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(9) == "IX", "9"
    assert checkio(99) == 'XCIX',"99"
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'