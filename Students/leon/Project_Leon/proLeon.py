# PDX Code Guild Python Project
# Webscrape Monster.com for Software Developer job postings

import requests
from bs4 import BeautifulSoup

#URL = 'https://www.monster.com/jobs/search/?q=software+developer&where=salt+lake+city'  # Software Developer SLC UT
URL = 'https://www.monster.com/jobs/search/?q=python+developer&where=' # Python Developer no specified location
page = requests.get(URL)
#pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.get_text()) # alt getText
results = soup.find(id='ResultsContainer')
#print(results.get_text())
#jobElems= results.find_all('section', class_='card-content')
# for jobElem in jobElems:
#     print(jobElem.get_text(), end='\n\*2')
# for jobElem in jobElems:
#     titleElem = jobElem.find('h2', class_='title')
#     companyElem = jobElem.find('div', class_='company')
#     locationElem = jobElem.find('div', class_='location')
#     if None in (titleElem, companyElem, locationElem):
#         continue
#     print(titleElem.text.strip())
#     print(companyElem.text.strip())
#     print(locationElem.text.strip())
#     print()

python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
#print(len(python_jobs)) # had to use a Pyton Developer specific URL 
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")