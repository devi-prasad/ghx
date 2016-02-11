import requests
import json
import GHXUserNames

#
#	signature string, integer -> list[] 
#
#listofusers
class BuildList(object):
	def __init__(self, name, offset):		
		self._list = None
		self._urls =[]
		self._name = name
		self._offset = int(offset)
	#
	# void -> int
	# reads file to get current number of urls already downloaded
	#

	def _get_count_(self):
		count = 0
		try:
			f = open('count.txt', 'r')
		except:
			print('can\'t find file count.txt')
		else:
			count = int(f.read())
			f.close()
		
		return count
	
	#
	# string -> string[]
	# takes mode: whether from net or file	returns: bunch of urls of users
	#
	
	def get_urls(self, mode):
		try:
			self._list = [self._list.rstrip('\n') for self._list in open(self._name)]
		except:
			print('can\'t find the file')
		start = self._get_count_()
		count = 1
		limit = start + self._offset
		for name in self._list:
			if count > limit :
				break
			if count > start:
				if (mode == 'net'):
					self._urls.append(name)	
				else:
					self._urls.append(name +'.txt')
			count = count + 1
		return self._urls
	#
	#	Takes GHXUsersRepo object 
	#

class UserJson(object):
	def __init__(self,UserRepo):
		self._r = UserRepo
		self._details = {}
	#
	#	void ->  dictionary
	#	build a dictionary of informations about user repo
	#

	def build_user_json(self):
		self._details['login'] = self._r.repo_login()
		self._details['repo'] = self._r.repo_name()
		self._details['created_date'] = self._r.repo_created_date()
		self._details['pushed_last'] = self._r.repo_pushed_date()
		self._details['size'] = self._r.repo_size()
		self._details['stars'] = self._r.repo_stars()
		self._details['language'] = self._r.repo_language()
		self._details['forks'] = self._r.repo_forks()
		self._details['open_issues_count'] = self._r.repo_issue_count()
		#_contributors = self._r.repo_contributors()
		#self._details['_contributors'] = _contributors

		return self._details

