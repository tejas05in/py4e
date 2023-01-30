import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retrieving', url)
html = urllib.request.urlopen(url,context=ctx).read()
print(f'Retrieved {len(html)} characters')
tree = ET.fromstring(html)

counts = tree.findall('.//count')
print("counts: ",len(counts))

sum = 0
for count in counts:
    sum+=int(count.text)
print("Sum: ",sum)