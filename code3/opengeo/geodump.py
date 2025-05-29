# import sqlite3
# import json
# import codecs

# conn = sqlite3.connect('opengeo.sqlite')
# cur = conn.cursor()

# cur.execute('SELECT * FROM Locations')
# fhand = codecs.open('where.js', 'w', "utf-8")
# fhand.write("myData = [\n")
# count = 0
# for row in cur :
#     data = str(row[1].decode())
#     try: js = json.loads(str(data))
#     except: continue

#     if len(js['features']) == 0: continue

#     try:
#         lat = js['features'][0]['geometry']['coordinates'][1]
#         lng = js['features'][0]['geometry']['coordinates'][0]
#         where = js['features'][0]['properties']['display_name']
#         where = where.replace("'", "")
#     except:
#         print('Unexpected format')
#         print(js)

#     try :
#         print(where, lat, lng)

#         count = count + 1
#         if count > 1 : fhand.write(",\n")
#         output = "["+str(lat)+","+str(lng)+", '"+where+"']"
#         fhand.write(output)
#     except:
#         continue

# fhand.write("\n];\n")
# cur.close()
# fhand.close()
# print(count, "records written to where.js")
# print("Open where.html to view the data in a browser")
import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

for row in cur:
    data = row[1].decode()
    try:
        js = json.loads(data)
    except:
        continue

    # 过滤空结果
    if not js.get('features'):
        continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]

        # 优先使用 formatted_address（如果有）
        props = js['features'][0].get('properties', {})
        display_name = props.get('display_name', '')
        formatted_address = props.get('formatted', '')

        # 取更详细的地址
        if formatted_address:
            where = formatted_address
        else:
            where = display_name

        # 清理可能的单引号
        where = where.replace("'", "")

    except Exception as e:
        print('Unexpected format:', e)
        print(js)
        continue

    try:
        print(where, lat, lng)

        count += 1
        if count > 1:
            fhand.write(",\n")
        output = f"[{lat},{lng}, '{where}']"
        fhand.write(output)
    except Exception as e:
        print('Write error:', e)
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
