alpha = 'abcdefghijklmnopqrstuvwxyz'
#rotation = int(input('How much rotation do you want in your encription? '))
user_word = input('What word do you wish to encode? ').lower()

inword = []
for letter in user_word:
    inword.append (letter)

abcs = []
for letter in alpha:
    abcs.append (letter)

answer = ''
for i in inword:
    indexs_a = alpha.find(i)
    indexs_b = indexs_a + 13  #rotation
    if indexs_b > 25:
        indexs_b -= 26
    new_letter = alpha[indexs_b]
    answer = answer + new_letter
print(f'Your encoded answer is: {answer}')
   