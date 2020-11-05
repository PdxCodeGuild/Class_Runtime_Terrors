# PDX Fullstack Practice 2: Strings
# Problem 1: Double print a string
import string

def double_letters(word):
    new_word = ''
    for i in range(len(word)):
        new_word = new_word + (word[i] * 2)
    return((new_word))

#fred = input("Enter a word: ")
#print(double_letters(fred))

# Problem 2: return number of times a letter occurs in a string
def count_letter(letter, word):
    x = 0
    for i in range(len(word)):
        if (letter == word[i]):
            x += 1
        else:
            continue
    return(x)


#print(count_letter('i', 'antidisestablishmentterianism'))
#print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))

# Problem 3: return the latest occurence of a letter
def latest_letter(word):
    hold = 'a'
    for i in range(len(word)):
        if hold < word[i]:
            hold = word[i]
    return(hold)


#print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis'))

# Problem 4: catch number of times 'hi' occurs in a given string
def count_hi(word):
    count = 0
    yep = 'hi'
    nope = ''
    for i in range(len(word)):
        try:
            nope = word[i] + word[i+1]
            print(nope)
            if nope == 'hi':
                count += 1
        except IndexError:
            return(count)
        nope = ''
    return(count)


#print(count_hi('hihi'))

# Problem 5: snake case conversion
def snake_case(text):
    unsafe = (string.punctuation) + '.'
    word = text.lower()
    word = word.replace(" ", "_")
    word = word.replace(unsafe, "")
    word = word.replace(".", "") # for some reason the line above ignores '.'
    return(word)


#print(snake_case('Hello World'))
#print(snake_case('This is another example.'))

# Problem 6: camel case conversion
def camel_case(text):
    unsafe = (string.punctuation)
    word = ''
    # get rid of punctuation
    for i in range(len(text)):
        #print(text[i])
        if (text[i] not in string.punctuation):
            word = word + text[i]
    # uppercase all words
    word = word.title()
    # lowercase first word [ASCII lower is 32 above upper]
    word = word.replace(word[0], word[0].lower())
    # join without spacing 
    word = word.replace(' ', '')
    return(word)

#print(camel_case('Hello World!')) # print helloWorld
#print(camel_case('This is another example.'))   #print thisIsAnotherExample

# Problem 7: Alternating case conversion
def alternating_case(text):
    word = text.lower()
    for i in range(len(word)):
        # if EVEN then .lower else .upper
        if (i % 2): # even
            word = word.replace(word[i], word[i].lower())
        else:
            word = word.replace(word[i], word[i].upper())
    return(word)

print(alternating_case('Hello World!')) #print HeLlO WoRlD!
print(alternating_case('This is another example.')) # print ThIs AnOtHeR...