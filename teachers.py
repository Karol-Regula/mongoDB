from pymongo import MongoClient
import csv, db_builder


server = MongoClient('159.89.150.100')
#server.drop_database("KiloByte")
db = server.KiloByte
c = db.students

db_builder.v2()

d3 = csv.DictReader(open("teachers.csv"))

teacherCol = db.teachers

def insert():
    info = {} #one dictionary per peep
    for stuff in d3:
        info['name'] = stuff['teacher']
        info['period'] = stuff['period']
        info['code'] = stuff['code']
        info['studentID'] = []
        for stu in server.db.students.find({'courses.code':info['code']}):
            info['studentID'].append(stu['id'])
    
    teacherCol.insert_one(info)

def checkerV3(): #creds to Evukelj for the boss checker
  print "Checking that everything was sent accurately! Printing contents\n"
  for doc in teacherCol.find(): #.find() returns all contents
    print "Teacher: " + doc['name']
    print "period: " + str(doc['period'])
    print "code: " + str(doc['code'])
    print "student in class:"
    for student in doc['studentID']:
      print course + " student ID: " + str(doc['studentID'][student])

insert()
checkerV3()





