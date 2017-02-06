from pymongo import MongoClient
import csv
import db_builder


server = MongoClient('127.0.0.1')
#server.drop_database("KiloByte")
db = server.KiloByte
c = db.students

def average_calc(): #creds to Evukelj for the boss checker
  print "Checking that everything was sent accurately! Printing contents\n"
  for doc in c.find(): #.find() returns all contents
    count = 0
    average = 0
    print "Student: " + doc['name']
    print "id: " + str(doc['id'])
    print "age: " + str(doc['age'])
    #print "course grades:"
    for course in doc['courses']:
      average += int(doc['courses'][course])
      count += 1
      #print course + " grade: " + str(doc['courses'][course])
    print "Average: " + str(average/count)

db_builder.v2()
#db_builder.checkerV2()
average_calc()
