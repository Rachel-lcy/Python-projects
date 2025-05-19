import urllib.request
import json
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving", url)

uh = urllib.request.urlopen(url, context= ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
total = 0
count_list = info["comments"]
print("Count:", len(count_list))

for item in count_list:
  total += item["count"]

print("Sum:", total)