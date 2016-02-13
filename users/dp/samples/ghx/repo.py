import requests
import json

class Repo(object):
    def __init__(self, repo):
        self._r = repo
    def id(self): return self._r['id']
    def url(self): return self._r['url']

class RepoIterator(object):
    def __init__(self, jsonres):
        self._json = jsonres
        self._index = 0
        self._len = len(jsonres)
        self._iter = iter(jsonres)

    def __iter__(self):
        return self	

    def next(self):
        return Repo(self._iter.next())

    def count(self): return self._len

#
# 'https://api.github.com/repositories'
#
class RepoEnumerator(object):
    def __init__(self, url, bsize):
        assert(url is not None)
        assert(bsize > 0)
        self._last = 0
        self._next = 0
        self._url = url
        self._batch_size = bsize
        self._json = None

    def reset(self):
       self._last = 1

    def fill(self):
        since = {'since': self._next}
        resp = requests.get(self._url, params=since)
        print(resp.url)
        if (resp.status_code == requests.codes.ok):
            self._last = self._next
            self._json = resp.json()
            self._next = self._largest_repo_id_(self._json)

    def _largest_repo_id_(self, resp):
    	max = self._last
        for r in resp:
            if (r['id'] > max): max = r['id']
        return (max + 1)

    def __iter__(self):
        return RepoIterator(self._json)


if __name__ == '__main__':
    print("scripting repo")

