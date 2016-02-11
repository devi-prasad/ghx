import requests
import json
import sys
import GHXUserNames
import GHXUtility

def start_load():
	if (len(sys.argv) == 4):
		utl = GHXUtility.BuildList(sys.argv[2], sys.argv[3])
		count = 0
		user_urls = []
		if (sys.argv[1] == 'net'):
			user_urls = utl.get_urls('net')
			count = get_details_net(user_urls)			
		elif (sys.argv[1] == 'file'):
			user_urls = utl.get_urls('file')
			count = get_details_file(user_urls)
		else:
			print('usage: <filename> <mode> <input file> <offset>')
		#if (count == len(user_urls)):
		#	update_file(sys.argv[3])
		#else:
		#	print('Error')


def write_user_json(enum):
	enum.fill()
	uit = iter(enum)
	_json = []
	_user_name_=''
	for r in uit:
		user = GHXUtility.UserJson(r)
		_user_json = user.build_user_json()
		_user_name_ = _user_json['login']
		_json.append(_user_json)
	try:
		f = open('./json/' + _user_name_ + '_spare.txt','a+')
	except:
		print('Not able to create file')
	else:
		f.write(json.dumps(_json))
		f.close()



def get_details_net(urls):
	count = 0
	for url in urls:
		res = GHXUserNames.GHXUserEnumerator(url)
		write_user_json(res)
		count += 1
		update_file(count)
		print(count)
	return count

def get_details_file(urls):
	count = 0
	for url in urls:
		res = GHXUserNames.GHXUserFileEnumerator(url)
		write_user_json(res)
		count += 1
		update_file(count)
	return count

"""
def update_count(count):
	f = open ('count.txt', 'w')
	f.write(str(count))
	f.close()
"""

def update_file(offset):
	count = 0
	try:
		f = open('count.txt', 'r')
	except:
		print('can\'t open file cout.txt')
	else:
		count = int(f.read())
		f.close()
	count += 1
	try:
		f = open('count.txt', 'w')
	except:
		print('can\'t open file count.txt')
	else:
		f.write(str(count))
		f.close()


if __name__ == "__main__":
	print('Welcome to GHXUsers')
	start_load()

