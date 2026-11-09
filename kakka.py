import json
import urllib.request

pyynto = urllib.request.urlopen("https://users.metropolia.fi/~peterh/kurssit.json")
data = pyynto.read()

print(len(data))

json_data = json.loads(data)
data.append("name")

