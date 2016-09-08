def checkio(words):
    new = words.split(' ')#splits the string by spaces
    three = False#boolean for 3 continuous words
    count = 0#word counter
    for  x in new:#iterates through list made from 'words'
        if x.isdigit():#checks if the substring is a number
            count =0#resets the counter as a number is inbetween words
        else:#if x is a word 
            count += 1#counter increses by 1
            if count == 3:#if there are three words in a row then the condition is met
                three = True#sets boolean for 3 words in a row to True
    return three

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
print("it's good")