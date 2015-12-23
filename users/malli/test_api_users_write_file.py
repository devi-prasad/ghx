import requests
from getpass import getpass
import json

# Note that credentials will be transmitted over a secure SSL connection
url = 'https://api.github.com/users'

response = requests.get(url)

print(json.dumps(response.json()[1], indent=1))

print()
print()

for key in response.json()[1]:
    print(key)

print()
print()

print(len(response.json()))

print()
print()

#fo=open("demo.txt","w+")
#for (key,value) in response.json()[1]:
#    fo.write("%s : %s\n" %key %value)
#fo.close()

#writing json data into a file
with open('sample.txt','w+') as outfile:
    json.dump(response.json()[1],outfile)
    
print("successfully wirten....")
