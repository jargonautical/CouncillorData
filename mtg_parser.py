from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen("http://democracy.devon.gov.uk/mgWebService.asmx/GetMeeting?lMeetingId=243") as response:
   markup = response.read()
#soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(markup, "xml")
#print (soup)
#pretty = soup.b.prettify()
#headsup = soup.head
#bodybag = soup.body
#bbody = soup.body.b
#abody = soup.body.a
#for tag in soup.find_all(True):
#    print(tag.name)
#print (soup.find_all(["b"]))
#section = soup.body.section
#print (section)
#print (soup)
all_b = soup.find_all("minutesitemnumber")
print (all_b)
#stripped = soup.stripped_strings
for foo in all_b:
    for desc in foo.descendants:
        print (foo, " ", desc, "\n")
#for string in stripped:
#    print(repr(string), "\n")
#for foo in all_b.contents:
#    print(foo)