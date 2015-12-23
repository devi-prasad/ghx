import requests
from getpass import getpass
import json

# Note that credentials will be transmitted over a secure SSL connection

#retrieve all public repositories
#url = 'https://api.github.com/repositories?since=364'
url = 'https://api.github.com/users/sois/repos'
response = requests.get(url)


print(json.dumps(response.json()[2], indent=1))
print()
print()

repo = response.json()[2];
print(repo["full_name"])

print()
