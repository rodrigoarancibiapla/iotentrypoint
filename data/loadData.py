import csv
import requests
csvfile = open('people.csv', newline='') 
spamreader = csv.reader(csvfile, delimiter=',')
header=['firstname','lastname','city','state','country']
for row in spamreader: 
    params= dict(zip(header, row))
    requests.post(url = '<put here your url http://x.x.x.x>', params = params)