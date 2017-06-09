import requests
import json
import itertools

token = '8553~7G6yIufBJhp30vX9A6NYC68aHSEeBxlm0LalJI1ARASZ4UWFq9bXBhWZGx3dPZiV'

r = requests.get('https://umich-dev.instructure.com/api/v1/courses?access_token='+token)

#r2 = requests.get('https://umich-dev.instructure.com/api/v1/courses/23/students?access_token='+token)

classes = json.loads(r.content.decode('utf-8'))
#students2 = json.loads(r2.content.decode('utf-8'))

#gets a list of groupings who share n classes
# ex: [{'classes': 'class1, class2, class3', 
#       'students': [{'name': 'student1', 'id': id}, ...]}
#       ,...]
def student_share_n(n):
  people = {}


  for cl in classes:
    i_d = cl['id']
    r2 = requests.get('https://umich-dev.instructure.com/api/v1/courses/'+str(i_d)+'/students?access_token='+token)
    students = json.loads(r2.content.decode('utf-8'))

    for student in students:
      name = student['name']
      student_id = student['id']
      if student_id in people:
        people[student_id]['courses'].append(cl['name'])
      else:
        student = {
          'name': name,
          'courses': [cl['name']]
        }
        people[student_id] = student

  print(people)

  shared_classes = {}
  #now we have people
  for i_d, person in people.items():
    if len(person['courses']) >= n:
      joined_name = ''.join(sorted(person['courses']))
      if joined_name in shared_classes:
        shared_classes[joined_name]['students'].append(person)
      else:
        shared_classes[joined_name] = {}
        shared_classes[joined_name]['students'] = [person]


#student_share_n(2)
r = requests.get('https://umich-dev.instructure.com/api/v1/accounts/6/users?access_token='+token)
accounts = json.loads(r.content.decode('utf-8'))
print(accounts)



#pairs = list(itertools.product(students, students2))

#for student in students:
  #print(pair[0]['name'] + ' vs ' + pair[1]['name'])
  #print(student['name'])

#for student in students2:
  #print(student['name'])
