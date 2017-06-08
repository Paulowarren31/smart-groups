import requests
import json
import itertools

token = '8553~7G6yIufBJhp30vX9A6NYC68aHSEeBxlm0LalJI1ARASZ4UWFq9bXBhWZGx3dPZiV'

r = requests.get('https://umich-dev.instructure.com/api/v1/courses/22/students?access_token='+token)

r2 = requests.get('https://umich-dev.instructure.com/api/v1/courses/23/students?access_token='+token)

students = json.loads(r.content.decode('utf-8'))
students2 = json.loads(r2.content.decode('utf-8'))

pairs = list(itertools.product(students, students2))

for pair in pairs:
  print(pair)
