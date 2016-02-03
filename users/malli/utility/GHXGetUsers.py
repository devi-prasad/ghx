import requests
import json
import sys

def bootloader():
	if (len(sys.argv) == 3):
		get_user_names()
	else:
		print('usage: <filename> <user file> <repo file')


def get_user_names():
	url = 'https://api.github.com/users?per_page=100'
	since = '6269'

	for i in range(1,11):
		url = 'https://api.github.com/users?per_page=100&since=' + str(since)		
		resp = requests.get(url)
		_json = resp.json()

		for r in _json:
			uname = r['login']
			repo_url = r['repos_url']
			since = r['id']
			f_user = open(sys.argv[1],'a+')
			f_user_repo = open(sys.argv[2],'a+')
			f_user.write(uname +"\n")
			f_user_repo.write(repo_url +'\n')
			f_user.close()
			f_user_repo.close()
	print(since)
if __name__ == "__main__":
	print('Welcome to GHXUsers')
	bootloader()
	
