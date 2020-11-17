



# print(int(13e45))


import re

with open('odyssey.txt', 'r', encoding='utf-8') as file:
    text = file.read()


match = re.search(r'\*\*\*.+\*\*\*', text)
text = text[match.end():]
match = re.search(r'\*\*\*.+\*\*\*', text)
text = text[:match.start()]

text = text.lower()
words = re.findall(r'\w+', text)
print(words[:100])



