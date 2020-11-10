def count_hi(text):
    word_list = []
    hi_count = 0
    x = 0
    count = 0
    for char in text:
        word_list += [char]
        count += 1
        if count >=2: #skips first iteration to keep from breaking index out of range
            if word_list[x - 1] == 'h': #returns one letter back to check for 'h'
                if word_list[x] == 'i': #if 'h' was found it looks for 'i'
                    hi_count += 1 #counts 'hi' if both conditions were found
        x += 1
    return hi_count

text = input('Input a sentence with several \'hi\'s in it: ')
hi_count = count_hi(text)
print(f'There were {hi_count} \'hi\'s in your sentence!')