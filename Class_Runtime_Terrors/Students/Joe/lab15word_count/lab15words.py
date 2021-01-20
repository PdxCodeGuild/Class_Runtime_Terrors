import requests

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
document_content = response.text

def dakine (dakine):#run funciton 
  punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''#unacceptable punctuation
    
  for ele in dakine:  #for loop to compare text to unacceptable punctuation
      if ele in punc:  
          dakine = dakine.replace(ele, " ") #remove the punctuation  
  dakine = dakine.lower()#turn into lowercase
  dakine = dakine.split()#turn string into a list
  #print(dakine)
  #dakine = ' '.join(dakine)#turn back into a string to be able to run dict() method
  counts = dict()#create an empty dictionary 
  #dakine = dakine.split()
  for word in dakine:#loop to see if word in list is also in counts
      if word in counts:#loop to see if word in list is also in counts
          counts[word] += 1#add +1 if not in count dictionary 
      else:
          counts[word] = 1#add if not in count dictionary
  #print(counts) #print to show user 
  return counts #return value of functtion  

output = dakine(document_content)

words = list(output.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

#print (output)










