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

	for r in uit:
		user = GHXUtility.UserJson(r)
		_user_json = user.build_user_json()
		_user_name_ = _user_json["login"]
		_json["repo"] = _user_json
	f = open("./ghxuser/json/" + _user_name_ + "_spare.txt","w")
	f.write(json.dumps(_json))
	f.close()
	cdbr = db.savedoc("mydb", json.dumps(_json), _user_name_)
	assert(cdbr.status() == 201)


def get_details_net(urls):
	count = 0
	for url in urls:
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
	f = open("./ghxuser/count.txt", "r")
	count = int(f.read())
	count += 1
	f.close()
	f = open("./ghxuser/count.txt", "w")
	f.write(str(count))
	f.close()

if __name__ == "__main__":
	print("Welcome to GHXUsers")
	start_load()

