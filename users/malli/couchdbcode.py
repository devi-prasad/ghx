import http.client
import json
import simplejson


class CouchDBResponse(object):
     """
     docstring for CouchDBResponse
     
     signature: HTTPResponse instace -> CouchDBResponse object
     """
     # HTTPResponse instace -> CouchDBResponse object
     def __init__(self, http_resp):
         self._http_resp = http_resp
         self._resp_json = json.loads(http_resp.read().decode('utf8'))
         

     # CouchDBResponse -> JSON
     def json(self): return self._resp_json
     # CouchDBResponse -> Integer
     def status(self): return self._http_resp.status
     # CouchDBResponse -> String
     def reason(self): return self._http_resp.reason
     #CouchDBResponse -> Integer
     def docscount(self): return self._resp_json['doc_count']
    
     
            
class CouchDB:
#"""Basic wrapper class for operations on a couchDB"""
 
     def __init__(self, host, port=5984, options=None):
         self.host = host
         self.port = port
         self.url = "https://"+ host + ":" + port
 
     def connect(self):
         return http.client.HTTPConnection(self.host, self.port)# No close()
 

     # Database operations
     
     #String -> CouchDBResponse   
     def create(self, name):
         r = self._put(self.url + '/' + name + '/', "")
         assert(r.status == 201)
         return CouchDBResponse(r)

     # String -> CouchDBResponse
     def delete(self, name):
        return CouchDBResponse(self._delete(self.url + '/' + name + '/'))
 
     # -> CouchDBResponse   
     def list(self):
         return CouchDBResponse(self._get(self.url + '/_all_dbs'))

     
     # Document operations

     # String -> CouchDBResponse
     def listdoc(self, dbName):
         return CouchDBResponse(self._get(self.url + '/' + dbName + '/'))
     
     # String, String -> CouchDBResponse
     def opendoc(self, dbName, docId):
         return CouchDBResponse(self._get(self.url + '/' + dbName + '/' + docId))
     
     # String, String, String -> CouchDBResponse
     def savedoc(self, dbName, body, docId=None):
         if docId:
             return CouchDBResponse(self._put(self.url + '/' + dbName + '/' + docId, body))
         else:
             return CouchDBResponse(self._post(self.url + '/' + dbName + '/', body))

     # String, String -> CouchDBResponse
     def deletedoc(self, dbName, docId):
         return CouchDBResponse(self._delete(self.url + '/' + dbName + '/' + docId + '/'))
         


     # Basic http methods
    
     # String -> HTTPResponse    
     def _get(self, uri):
         c = self.connect()
         headers = {"Accept": "application/json"}
         c.request("GET", uri, None, headers)
         return c.getresponse()
 
     # String, String -> HTTPResponse
     def _post(self, uri, body):
         c = self.connect()
         headers = {"Content-type": "application/json"}
         c.request('POST', uri, body, headers)
         return c.getresponse()
 
     # String, String -> HTTPResponse
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
    
     # String -> HTTPResponse
     def _delete(self, uri):
         c = self.connect()
         assert(c != None)
         c.request("DELETE", uri)
         return c.getresponse()
