from pymongo import MongoClient
import csv

server = MongoClient('159.89.150.100')
db = server.dbName
c = db.students

d1 = csv.DictReader(open("peeps.csv"))
d2 = csv.DictReader(open("courses.csv"))



for temp1 in d1:
  print temp1
  d2 = csv.DictReader(open("courses.csv"))
  for temp2 in d2:
    if temp1['id'] == temp2['id']:
      print temp2

      ##adding to mongo:

  print "-----------"
