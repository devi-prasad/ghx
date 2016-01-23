import http.client
import json
import simplejson

def prettyPrint(s):
       #"""Prettyprints the json response of an HTTPResponse object"""
    
      # HTTPResponse instance -> Python object -> str
      print(simplejson.dumps(json.loads(s.read().decode('utf8')), sort_keys=True, indent=4))

class CouchDBResponse(object):
     """
     docstring for CouchDBResponse
     
     signature: HTTPResponse -> CouchDBResponse
     """
     # HTTPResponse -> CouchDBResponse
     def __init__(self, http_resp):
         self._http_resp = http_resp
         self._resp_json = json.loads(http_resp.read().decode('utf8'))

     # CouchDBResponse -> JSON
     def json(self): return self._resp_json
     # CouchDBResponse -> Integer
     def status(self): return self._http_resp.status
     # CouchDBResponse -> String
     def reason(self): return self._http_resp.reason
            
class CouchDB:
#"""Basic wrapper class for operations on a couchDB"""
 
     def __init__(self, host, port=5984, options=None):
         self.host = host
         self.port = port
 
     def connect(self):
         return http.client.HTTPConnection(self.host, self.port)# No close()
 

     # Database operations
     
     #String -> CouchDBResponse   
     def create(self, name):
         r = self._put(''.join(['/', name, '/']), "")
         assert(r.status == 201)
         return CouchDBResponse(r)

     # String -> CouchDBResponse
     def delete(self, name):
        return CouchDBResponse(self._delete(''.join(['/', name, '/'])))
 

     def list(self):
         """List the databases on the server"""
         #prettyPrint(self._get('/_all_dbs'))
         return CouchDBResponse(self._get('/_all_dbs'))

         #return simplejson.dumps(json.loads((self._get('/_all_dbs')).read().decode('utf8')))
         #return json.loads((self._get('/_all_dbs')).read())
    
     # dbName = database name
     def info(self, dbName):
         """Returns info about the couchDB"""
         r = self._get(''.join(['/', dbName, '/']))
         #prettyPrint(r)
         return r

     # Document operations
     # dbName = database name
     def listDoc(self, dbName):
         """List all documents in a given database"""
         r = self._get(''.join(['/', dbName, '/', '_all_docs']))
         #prettyPrint(r)
         return simplejson.dumps(json.loads((self._get(''.join(['/', dbName, '/', '_all_docs']))).read().decode('utf8')))
     
     # dbName = database name, docId = document name
     def openDoc(self, dbName, docId):
         """Open a document in a given database"""
         r = self._get(''.join(['/', dbName, '/', docId,]))
         #prettyPrint(r)
         return r
     
     # dbName = database name, body = original document content, docId = document name
     def saveDoc(self, dbName, body, docId=None):
         """Save/create a document to/in a given database"""
         if docId:
             r = self._put(''.join(['/', dbName, '/', docId]), body)
         else:
             r = self._post(''.join(['/', dbName, '/']), body)
         #prettyPrint(r)
         return r
     
     # dbName = database name, docId = document name
     def deleteDoc(self, dbName, docId):
         # XXX Crashed if resource is non-existent; not so for DELETE on db. Bug?
         # XXX Does not work any more, on has to specify an revid
         #     Either do html head to get the recten revid or provide it as parameter
         r = self._delete(''.join(['/', dbName, '/', docId, '/']))
         #prettyPrint(r)
         return r


     # Basic http methods
 
     def _get(self, uri):
         c = self.connect()

         headers = {"Accept": "application/json"}
         c.request("GET", uri, None, headers)
         return c.getresponse()
 
     def _post(self, uri, body):
         c = self.connect()
         headers = {"Content-type": "application/json"}
         c.request('POST', uri, body, headers)
         return c.getresponse()
 
     def _put(self, uri, body):
         c = self.connect()
         assert(c != None)
         #print(uri)
         if len(body) > 0:
             headers = {"Content-type": "application/json"}
             c.request("PUT", uri, body, headers)
         else:
             c.request("PUT", uri, body)
         return c.getresponse()
 
     def _delete(self, uri):
         c = self.connect()
         assert(c != None)
         c.request("DELETE", uri)
         return c.getresponse()
