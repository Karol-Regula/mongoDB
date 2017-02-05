from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.KiloByte
c = db.students

d1 = csv.DictReader(open("peeps.csv"))
d2 = csv.DictReader(open("courses.csv"))

#so I nested the course dictionaries in the student dictionary



for temp1 in d1:
  print "Student: " + str(temp1)
  d2 = csv.DictReader(open("courses.csv"))
  i = 0
  for temp2 in d2:
    if temp1['id'] == temp2['id']:
      i += 1
      temp1['course' + str(i)] = temp2
      print "Course: " + str(temp2)
  print "Final??: " + str(temp1)
  db.c.insert_one(temp1) # breaks because it can't connect to the db
  print "-----------"

print str(db.students.count())
