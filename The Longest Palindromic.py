def longest_palindromic(text):
    words = []
    for x in range(len(text)):
        for y in range(len(text)):
                if text[x:y] == text[y:x:-1]:
                    print(text[x:y+1])
                    print(x,y+1)
                    words.append(text[x:y+1])
    temp = 0
    text = ""
    for x in words:
        if len(x) > temp:
            text = x
            temp = len(x)
    print(text)
    return text
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "error"