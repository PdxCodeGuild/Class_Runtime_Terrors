

# def double_letters(word):
#   wordlist = list(word)
#   for x in range(len(wordlist)):
#     print(wordlist[x],end="")
#     print(wordlist[x],end="")

# print('P1')
# print(double_letters('hello')) # hheelllloo


# def count_letter(letter, word):
#     count = 0
#     for x in word:
#         if x == letter:
#             count += 1
#     return count

# print('P2')
# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2

# def latest_letter(word):
#     wordlist = list(word)
#     bigasc = 0 
#     for x in range(len(wordlist)):
#         newasc = ord(wordlist[x]) #Char to ascii valve
#         if newasc > bigasc:
#             bigasc = newasc
#     return chr(bigasc) #Return ascii valve to char

# print('P3')
# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v

# # def count_hi(text):


# def count_hi(text):
#     textlist = list(text)
#     counthi = 0
#     for x in range(len(textlist)):
#         y = x + 1
#         if textlist[x] == "h" and textlist[y] == "i":
#             counthi = counthi + 1
#     return counthi

# print('P4')
# print(count_hi('hihi')) # 2


# def snake_case(text):
#     return text.lower()

# print('P5')
# print(snake_case('Hello World!')) # hello_world
# print(snake_case('This is another example.')) # this_is_another_example


# def camel_case(text):
#     punc = ""'!()-[]{};:'"\, <>. /?@#$%^&*_~''"
#     for x in text:
#         if x in punc:
#             text = text.replace(x, "")
#     return text

# print('P6')
# print(camel_case('Hello World!')) # helloWorld
# print(camel_case('This is another example.')) # thisIsAnotherExample

# # def alternating_case(text):
# #     for x in text:
# #         if x = 0
    
# # print(alternating_case('Hello World!')) # HeLlO WoRlD!
# # print(alternating_case('This is another example.')) # ThIs iS AnOtHeR ExAmPle.

