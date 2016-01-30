import requests
import json

class GHXUserEnumerator(object):
	def __init__(self,url):
		self._url =  'https://api.github.com/users/'+ url + '/repos'
		self._json = None
		self._unames = []

	def fill(self):
		resp = requests.get(self._url)
		if (resp.status_code == requests.codes.ok):
			self._json = resp.json()
			assert(self._json != None)		

	def __iter__(self):
		assert(self._json != None)
		return GHXUserIterator(self._json)

	def get_user_names(self):
		for r in self._json:
			full_name = r['login']
			self.GHXUser_unames.append(full_name)
		return self._unames

class GHXUserFileEnumerator(object):
    def __init__(self,fname):
        self._json = None
        self._file = fname
        
    def reset(self):
       self._last_ = 1

    def fill(self):
        infile=open(self._file,'r+')
        self._json=json.load(infile)
        
    def __iter__(self):
        if (self._json is not None):
            return GHXUserIterator(self._json)	


class GHXUserIterator(object):
	def __init__(self,jsonres):
		self._json = jsonres
		assert(self._json != None)
		self._index = 0;
		self._len = len(jsonres)
		self._iter = iter(jsonres)

	def __iter__(self):
		return self

	def __next__(self):
		return GHXUserRepos(self._iter.__next__())

class GHXUserRepos(object):
	def __init__(self,repo):
		self._r = repo

	def repo_name(self): return self._r['name']
	def repo_size(self): return self._r['size']
	def repo_language(self): return self._r['language']
	def repo_forks(self): return self._r['forks']
	def repo_created_date(self): return self._r['created_at']
	def repo_pushed_date(self): return self._r['pushed_at']
	def repo_stars(self): return self._r['stargazers_count']
	def repo_issue_count(self): return self._r['open_issues_count']
	def repo_login(self): return self._r['owner']['login']

	def repo_contributors(self):
		clist = [] 		
		url = self._r['contributors_url']
		resp = requests.get(url)
		for r in resp.json():
			data = r['login']
			clist.append(data)
		
		return clist


			

