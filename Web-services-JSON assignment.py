import urllib.request , urllib.parse, urllib.error
import json

url = input('Enter - ')
print("Retrieving: ",url)
data = urllib.request.urlopen(url).read().decode()
print(f'Retrieved {len(data)} characters')
info = json.loads(data)
sum = 0
for item in info["comments"]:
    sum+=item['count']

print('Count:', len(info["comments"]))
print('Sum', sum)
