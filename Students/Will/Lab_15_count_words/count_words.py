import string
f = "C:/Users/17196/Desktop/345.txt"

with open (f, 'r') as document:
    document_content = document.read()
    document_content = document_content.lower()

punctuation = list(string.punctuation)
document_content = list(document_content)

no_punc = []
for char in document_content:
    if char not in punctuation:
        no_punc.append(char)
no_punc = str(''.join(no_punc))
no_punc.replace('\n', '')
no_punc.replace('  ', ' ')
word_list = no_punc.split(' ')
word_list = r' '.join(word_list)
print(word_list)