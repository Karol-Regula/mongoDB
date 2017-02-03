from pymongo import MongoClient
import csv

server = MongoClient('159.89.150.100')
db = server.dbName
c = db.students

d1 = csv.dictReader
