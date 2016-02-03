import requests

import sys
#import GHXUserNames
#import GHXUtility
from couchpy import couchdbcode
import simplejson as json

def testmyghx():

	#Creating gitusers document and inserting users names into the document
	
	db = couchdbcode.CouchDB('127.0.0.1', '5984')
	url = 'https://api.github.com/users?per_page=100'
	cdbr = db.listdoc('mydb')
	#print(cdbr.json())
	if cdbr.checkdocname('gitusers'):
		cdbr = db.opendoc('mydb','gitusers')
		#print(cdbr.json())
		since = ''
		#since = str(len(cdbr.json()["repousers"]))
		#print(since)
		check = '0'
		for k in cdbr.json()["repousers"]:
			if k > check:
				since = k
				check = k
		print(str(since))
		
	else:
		since = '0'

	"""	
		
	_json_names = {}
	_json_local_dict = {}

	for i in range(1,3):
		url = 'https://api.github.com/users?per_page=100&since=' + str(since) + '&order=asc'		
		resp = requests.get(url)
		_json = resp.json()
		count = 0
		for r in _json:
			#_json_local_dict[(r["id"])] = r["login"]  		
			_json_local_dict[("'" + str(r["id"]) + "'")] = r["login"]
			since = r["id"]
		
	
	cdbr = db.listdoc('mydb')
	print(cdbr.json())
	if cdbr.checkdocname('gitusers'):	
		cdbr = db.opendoc('mydb','gitusers')
		_json_names["_rev"] = cdbr.json()["_rev"]
		_json_rev = {}
		_json_rev = cdbr.json()["repousers"]
		_json_rev.update(_json_local_dict)
		_json_names["repousers"] = _json_rev
		
		cdbr = db.updatedoc('mydb', json.dumps(_json_names), 'gitusers')
		print(cdbr.json())
	else:
		_json_names["repousers"] = _json_local_dict	
		cdbr = db.savedoc('mydb', json.dumps(_json_names), 'gitusers')
		print(cdbr.json())							

	"""
	

	#update counter value for the document 'count'
	"""
	if cdbr.checkdocname('count'):
		cdbr = db.opendoc('mydb','count')
		print(cdbr.json())
		print(cdbr.json()["counter"])
		_json_count = {}
		_json_count["_rev"] = cdbr.json()["_rev"]
		_json_count["counter"] = (cdbr.json()["counter"] + 1)
		print(_json_count)
		cdbr = db.updatedoc('mydb', json.dumps(_json_count), 'count')
		print(cdbr.json())
	else:
		
		_json_count = {}
		_json_count["counter"] = 0
		cdbr = db.savedoc('mydb', json.dumps(_json_count), 'count')
		print(cdbr.json())
	"""

	#displaying the existing document details
	"""if (len(sys.argv)==2):
		docname = sys.argv[1]
		
		if cdbr.checkdocname(docname):
			cdbr = db.opendoc('mydb',docname)
			#print(cdbr.json()['repo'])
			print('Repo Name: ' + cdbr.json()['repo']['repo'])
			print('Size: ' + str(cdbr.json()['repo']['size']))
			print('Language: ' + cdbr.json()['repo']['language'])
			print('Forks: ' + str(cdbr.json()['repo']['forks']))
			print('Created at: ' + cdbr.json()['repo']['created_date'])
			print('Pushed at: ' + cdbr.json()['repo']['pushed_last'])
			print('Stargazers count: ' + str(cdbr.json()['repo']['stars']))
			print('Open issues count: ' + str(cdbr.json()['repo']['open_issues_count']))

		else:
			print('file not found in database')
	else:
		print('usage: <filename> <document name>')
	
	"""
	
	#print(cdbr.json())
	#_json= cdbr.json()
	#_docid =[]
	#_docid = _json
	#for id in _docid['rows']:
	#	print(id['id'])
	#print(_docid)
		
		

if __name__ == '__main__':
	testmyghx()