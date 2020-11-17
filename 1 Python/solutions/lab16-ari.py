
import requests
import re
import string
import math





def count_characters1(text):
    counter = 0
    for char in text:
        if char in string.ascii_letters:
            counter += 1
    return counter


def count_characters2(text):
    matches = re.findall(r'[a-zA-Z]', text)
    return len(matches)


def count_words1(text):
    words = text.split()
    # print(words[2000:4000])
    return len(words)

def count_words2(text):
    words = re.findall('[\w’-]+', text)
    return len(words)




def count_sentences1(text):
    return text.count('.') + text.count('!') + text.count('?')

    # counter = 0
    # for char in text:
    #     if char in '.!?':
    #         counter += 1
    # return counter

    # return sum([1 if char in '.!?' else 0 for char in text])

def count_sentences2(text):
    return len(re.findall('[\.!?]', text))


response = requests.get('https://www.gutenberg.org/files/62917/62917-0.txt')
response.encoding = 'utf-8'
text = response.text

match = re.search(r'\*\*\*.+\*\*\*', text)
text = text[match.end():]
match = re.search(r'\*\*\*.+\*\*\*', text)
text = text[:match.start()]
text = text.lower()
text = text.replace('—', ' ')


num_words = count_words1(text)
num_characters = count_characters1(text)
num_sentences = count_sentences1(text)

ari = 4.71*(num_characters/num_words) + 0.5*(num_words/num_sentences) - 21.43
print(ari)

ari = math.ceil(ari)
# ari = int(ari + 1)


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print(ari_scale[ari]['grade_level'])



















