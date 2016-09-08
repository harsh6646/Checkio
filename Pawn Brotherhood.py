import string
def safe_pawns(pawns):
    safe = 0
    for pair in pawns:
        x = int((string.ascii_lowercase).find(pair[0])) + 1
        y = int(pair[1])
        for check in pawns:
            if pair != check:
                checkx = int((string.ascii_lowercase).find(check[0])) + 1
                checky = int(check[1])
                if y-checky == 1 and (x-checkx == 1 or x - checkx == -1):
                    print(pair,check)
                    safe += 1
                    break
    print(safe)
    return safe
                
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6,"1"
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1,"2"
