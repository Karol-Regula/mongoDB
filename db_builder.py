from pymongo import MongoClient
import csv


server = MongoClient('127.0.0.1')
server.drop_database("KiloByte")
db = server.KiloByte
c = db.students

d1 = csv.DictReader(open("peeps.csv"))
d2 = open("courses.csv")



#so I nested the course dictionaries in the student dictionary

def v1():
  for temp1 in d1:
    print "Student: " + str(temp1)
    d2.seek(0)
    dicti = csv.DictReader(d2)
    i = 0
    for temp2 in dicti:
      if temp1['id'] == temp2['id']:
        i += 1
        temp1['course' + str(i)] = temp2
    print "Final??: " + str(temp1)
    c.insert_one(temp1)
    print "-----------"
  checkerV1()


def checkerV1(): #creds to Evukelj for the boss checker
  print "Checking that everything was sent accurately! Printing contents\n"
  for doc in c.find(): #.find() returns all contents
    print doc
    print "--"

def checkerV2(): #creds to Evukelj for the boss checker
  print "Checking that everything was sent accurately! Printing contents\n"
  for doc in c.find(): #.find() returns all contents
    print "Student: " + doc['name']
    print "id: " + str(doc['id'])
    print "age: " + str(doc['age'])
    print "course grades:"
    for course in doc['courses']:
      print course + " grade: " + str(doc['courses'][course])

def v2():
  for peep in d1:
    info = {} #one dictionary per peep
    info['name'] = peep['name']
    info['age'] = peep['age']
    info['id'] = peep['id']
    info['courses'] = {}
    d2.seek(0) #look at courses from beginning
    courses = csv.DictReader(d2)
    for student in courses:
      if peep['id'] == student['id']:
        info['courses'][student['code']]=student['mark']#filling courses section of peep's dict with the course and grade
    c.insert_one(info)
  #checkerV2()

#v1()
#v2()
