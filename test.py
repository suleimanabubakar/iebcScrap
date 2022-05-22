from scrap import *

payload = {}

print("Enter Id No:")
idno = input()
print("Enter YOB:")
yob = input()

payload['idno'] = idno
payload['yob'] = yob

data = execute(payload)
