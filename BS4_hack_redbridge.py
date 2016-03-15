# import libraries
# I don't know if I need all of these, but they are in the scrape scripts so I will include 
# them and comment out until the script stops working

import os
import errno
import requests
import sys
import csv

# this one is an HTTP client that gets the contents from a url
import urllib.request

# python library that makes sense of the parsed html or xml for you
from bs4 import BeautifulSoup

# define the document using urllib2
response = urllib.request.urlopen('http://moderngov.redbridge.gov.uk/ieListDocuments.aspx?CId=516&MId=6937&Ver=4')
html_doc = response.read()

# run Beautiful Soup, don't forget to define the file and parser to use
# BS4 author recommends lxml for both xml and html (now installed)
# soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(html_doc, 'lxml') # this one works fine with examples so far


# print out and prettify the soup
# print(soup.prettify())

# extract something from the soup by tag
# print(soup.p)
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all('p'))
# print(soup.head)
# print(soup.body)

#list all the div types
# print('HERE ARE ALL THE DIV TYPES:')
# div_tag = soup.div
# for child in div_tag.children:
#     print(child)

# gets all the links
# print('HERE ARE ALL THE LINKS:')
# for link in soup.find_all('a'):
#     print(link.get('href'))
    
# get all the text and strip the white spaces
# print('HERE IS THE TEXT WITH THE WHITESPACE STRIPPED OUT:')
# for string in soup.stripped_strings:
#     print(repr(string)) 

# testing the parent finder
# print('TESTING THE PARENT FINDER FOR A LINK')
# link = soup.a
# link
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
        
# testing the child finder
# print('TESTING THE CHILD FINDER')
# for child in soup.head.children:
#     print(child)


# testing the sibling finder
# print('FINDING ALL THE SIBLINGS:')
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))   

# get all the text
# print('HERE IS ALL THE TEXT INCLUDING WHITESPACE:')
# print(soup.get_text()) 

# find out what tags there are and what data is under each one, maybe do them all by turns
table_tag = soup.table
print(table_tag.text)

with open("Output.txt", "w") as text_file:
    print((table_tag.text), file=text_file)



