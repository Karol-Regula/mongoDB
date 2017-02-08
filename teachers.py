from pymongo import MongoClient
import csv, db_builder


server = MongoClient('127.0.0.1')
server.drop_database("KiloByte")
db = server.KiloByte
c = db.students

d3 = csv.DictReader(open("teachers.csv"))

teacherCol = db.teachers

def insert():
  info = {} #one dictionary per teacher
  for stuff in d3:
    info['name'] = stuff['teacher']
    info['period'] = stuff['period']
    info['code'] = stuff['code']
    info['studentID'] = []
    for doc in c.find():
      for course in doc['courses']:
        if (course == info['code']):
          info['studentID'].append(int(doc['id']))
    #for stu in server.db.students.find({'courses.code':info['code']}):
      #info['studentID'].append(stu['id'])
    print str(info)
    teacherCol.insert_one(info.copy()) #found this fix, seems that pymongo gets confused when it tries to use the same dictionary over again

def checkerV3(): #creds to Evukelj for the boss checker
  print "Checking that everything was sent accurately! Printing contents\n"
  for doc in teacherCol.find(): #.find() returns all contents
    print "Teacher: " + doc['name']
    print "period: " + str(doc['period'])
    print "code: " + str(doc['code'])
    print "student in class:"
    print "- student ID: " + str(doc['studentID'])
    print " "

db_builder.v2()
#db_builder.checkerV2()
insert()
checkerV3()
