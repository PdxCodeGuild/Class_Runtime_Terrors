# PDX Fullstack Practice: Four Dictionaries
# Problem 1: BOOL check for a given key


def has_key(text, val):
    if val in text:
        return True
    else:
        return False


#print(has_key({'a': 1, 'b': 2}, 'a'))
#print(has_key({'a': 1, 'b': 2}, 'c'))

# Problem 2: BOOL check if -dict- is empty
def is_empty(text):
    if text:
        return True
    else:
        return False

#print(is_empty({}))
#print(is_empty({'a': 1, 'b': 2}))

# Problem 3: return key for a given value, else 'none'
def find_key(text, val):
    for key, value in text.items():
        if val == value:
            return key
    return "Key does not exist"


#print(find_key({'a': 1, 'b': 2}, 1))
#print(find_key({'a': 1, 'b': 2}, 3))

# Problem 4: rtn dict with keys and values reversed
def reverse_dict(text):
    k = (text.keys())
    v = (text.values())
    n = dict(zip(v,k))

    return(n)


#print(reverse_dict({'a': 1, 'b': 2}))

# Problem 5: merge two lists in a new dict
def merge(text1, text2):
    n = {}
    for i in range(len(text1)):
        n[text1[i]] = text2[i]
    return(n)

#print(merge(['a', 'b'], [1, 2]))

# Problem 6: <<repeate of previous exercise??>> 

def merge(text1, text2):
    n = dict(zip(text1,text2))
    return(n)

#print(merge(['a', 'b'], [1, 2]))

# Problem 7: rtn w/o less than 10's
def remove_less_than_10(text):
    n = {}
    for key, value in text.items():
        if (value > 9):
            n[key] = value

    return(n)


#print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12}))

# Problem 8: avg of the lists in a dict
def avg_values(text):
    for key in text:
        text[key] = int(sum(text[key]) / (len(text[key])))
    return(text)

#print(avg_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]}))

# Problem 9: create new -dict- where val++ if same key
def merge_dict(text1, text2):
    n = text1.copy()
    for key, value in text2.items():
        if key in n:
            n[key] += text2[key]
    return(n)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
#print(merge_dict(d1, d2))

# Problem 10: count number of occurunces in a string
def count_votes(text):
    n = {}
    for i in range(len(text)):
        x = text.count(text[i])
        if text[i] not in n:
            n[text[i]] = x
    return(n)


votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
print(count_votes(votes))