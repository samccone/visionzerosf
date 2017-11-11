import json
import csv
import requests

accum = []

with open('2017_data_links.txt', 'r') as data:
    for line in data.read().splitlines():
        accum.append(json.loads(requests.get(line).text))

print(json.dumps(accum))
