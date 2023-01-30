import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore ssl certificaiton error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
count = int(input("Enter count: "))
postion = int(input("Enter position: ")) -1
print("Retrieving: ",url)

for i in range(count):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print("Retrieving: ",tags[postion].get('href',None))
    url = tags[postion].get('href',None)
    