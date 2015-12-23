import requests
from getpass import getpass
import json

# Note that credentials will be transmitted over a secure SSL connection
#url = 'https://api.github.com/users'
#url = 'https://api.github.com/users/satyamalli'
#url = 'https://api.github.com/users/defunkt'
url = 'https://api.github.com/users/sois'
response = requests.get(url)

#print(json.dumps(response.json()[1], indent=1))
print(json.dumps(response.json(), indent=1))
print()
print()
#for index in range(len(response.json()[1])):
#    print(response.json()[index])
for key in response.json():
    print(key)

print()
print()

print(len(response.json()))

print()
print()
print(response.json()['location'])
print()
