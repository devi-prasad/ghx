import requests
import json
import sys
import GHXUserNames
import GHXUtility
from couchpy import couchdbcode
import simplejson

def start_load():
	if (len(sys.argv) == 4):
		utl = GHXUtility.BuildList(sys.argv[2], sys.argv[3])
		count = 0
		user_urls = []
		if (sys.argv[1] == "net"):
			user_urls = utl.get_urls("net")
			count = get_details_net(user_urls)
		elif (sys.argv[1] == "file"):
			user_urls = utl.get_urls("file")
			count = get_details_file(user_urls)
		else:
			print("usage: <filename> <mode> <input file> <offset>")


def write_user_json(enum):
	enum.fill()
	uit = iter(enum)
	_json = {}
	_user_name_=""
	db = couchdbcode.CouchDB("127.0.0.1", "5984")
	cdbr = db.list()
	
	if not cdbr.checkdbname("mydb"):
		cdbr = db.create("mydb")
	
	_user_name_=""
	_repo_name_=""

	for r in uit:
		user = GHXUtility.UserJson(r)
		_user_json = user.build_user_json()
		_user_name_ = _user_json["login"]
		_repo_name_ = _user_json["repo"]
		_json["'"+_repo_name_+"'"] = _user_json
	try:
		f = open("./ghxuser/json/" + _user_name_ + "_spare.txt","w")
	except:
		print('can\'t open file')
	else:
		f.write(json.dumps(_json))
		f.close()

	repo_json = {}
	repo_json["repo"] = _json
	cdbr = db.savedoc("mydb",json.dumps(repo_json),_user_name_)
	#assert(cdbr.status()==201)

	
def get_details_net(urls):
	count = 0
	for url in urls:
		print(url)
		res = GHXUserNames.GHXUserEnumerator(url)
		write_user_json(res)
		count += 1
		update_file()
	return count

def get_details_file(urls):
	count = 0
	for url in urls:
		res = GHXUserNames.GHXUserFileEnumerator(url)
		write_user_json(res)
		count += 1
		update_file()
	return count

def update_file():
	count = 0
	try:
		f = open("./ghxuser/count.txt", "r")
	except:
		print('can\'t open file')
	else:
		count = int(f.read())
		f.close()
	count += 1
	try:
	    f = open("./ghxuser/count.txt", "w")
	except:
		print('can\'t open file')
	else:
		f.write(str(count))
		f.close()

def update_couchdb():
	db = couchdbcode.CouchDB('127.0.0.1', '5984')
	cdbr = db.listdoc('mydb')

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

if __name__ == "__main__":
	print("Welcome to GHXUsers")
	start_load()

