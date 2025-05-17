import urllib.request
import re

url = 'http://py4e-data.dr-chuck.net/regex_sum_2218052.txt'

response = urllib.request.urlopen(url)
data = response.read().decode()

numbers = re.findall(r'[0-9]+', data)

total = sum([int(num) for num in numbers])

print(" Sum:" , total)