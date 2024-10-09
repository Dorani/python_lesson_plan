#searching for a specific thing in string

import re

string = 'search inside this'
#a match object will be outputed, provides information about 'this', specifies location as an index
a = re.search('this', string)

#Tells me where the string occurs as a tupple
print(a.span())

#Tells me where the string starts as a tupple
print(a.start())

#Tells me where the string ends as a tupple
print(a.end())

#For multiple searches
print(a.group())


#Create a patterns we want to explicitly check for:
pattern = re.compile('this')

b = pattern.search(string)
print(b)

#Create a patterns we want to check for:
c = pattern.findall(string)
d = pattern.findmatch(string)
f = pattern.match(string)


#check regex101 for reference guide