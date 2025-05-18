import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter Location: ")
print("Retrieving", url)

response = urllib.request.urlopen(url)
data = response.read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for count in counts:
  total += int(count.text)

print("Count:", len(counts))
print("Sum:", total)