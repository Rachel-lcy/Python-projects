import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href')


print("Retrieving:", url)
