import requests
#use the html and grab different data
from bs4 import BeautifulSoup



#Get request to grab page
res = requests.get('https://news.ycombinator.com/news')
#Print all the html text
print(res.text)


#Parse the data:
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body)
print(soup.body.contents)
#Get all the divs
print(soup.find_all('div'))

#Get all the link tags
print(soup.find_all('a'))

#Get all the title tags
print(soup.find_all('title'))

#Get the ID
print(soup.id('_score_20514755_'))



#Get the first story
links = soup.select('.storylink')[0]
votes = soup.select('.score')
print(votes[0])