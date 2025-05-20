import urllib.request
import urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Service URL
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Encode address into URL parameters
    address = address.strip()
    parms = {'q': address}
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=2))


    if not js or 'plus_code' not in js or 'global_code' not in js['plus_code']:
        print('Failed to retrieve plus code')
        continue

    plus_code = js['results'][0]['plus_code']['global_code']
    print('Plus code', plus_code)
