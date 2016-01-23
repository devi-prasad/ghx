import couchdbcode

#def test():
    #db = couchdb.CouchDB('127.0.0.1', '5984')
 
    #print("\nCreate database 'mydb':")
    #db.create('mydb')
 
    #print("\nList databases on server:")
    #db.list()
 
    #print("\nCreate a document 'mydoc' in database 'mydb':")
    #doc = """
    #{
    #     "value":
    #     {
    #         "Subject":"I like Planktion",
    #         "Author":"Rusty",
    #         "PostedDate":"2006-08-15T17:30:12-04:00",
    #         "Tags":["plankton", "baseball", "decisions"],
    #         "Body":"I decided today that I don't like baseball. I like plankton."
    #     }
    #}
    #"""
    #db.saveDoc('mydb', doc, 'mydoc')
 
    #print("\nCreate a document, using an assigned docId:")
    #db.saveDoc('mydb', doc)
 
    #print("\nList all documents in database 'mydb'")
    #db.listDoc('mydb')
 
    #print("\nRetrieve document 'mydoc' in database 'mydb':")
    #db.openDoc('mydb', 'mydoc')

    #print("\nDelete document 'mydoc' in database 'mydb':")
    #db.deleteDoc('mydb', 'mydoc')
 
    #print("\nList all documents in database 'mydb'")
    #db.listDoc('mydb')
 
    #print("\nList info about database 'mydb':")
    #db.info('mydb')
 
    #print("\nDelete database 'mydb':")
    #db.deleterepo('mydb')
 
    #print("\nList databases on server:")
    #db.list()

#test - initial database count
def test_emptydb():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    cdbr = db.list()
    assert(cdbr.status() == 200 and len(cdbr.json()) == 2)

#test - database creation
def test_create_one_db():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    cdbr = db.create('mydb')
    assert(cdbr.status() == 201)
    cdbr = db.list()
    assert(cdbr.status() == 200)
    assert(len(cdbr.json()) == 3)
    db.delete('mydb')
     
#test - database information
def test_dbinfo():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    i=db.info('mydb')
    assert(i.status==200)

#test - save a document into the database
def test_savedoc():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    
    doc = """
    {
         "value":
         {
             "Subject":"I like Planktion",
             "Author":"Rusty",
             "PostedDate":"2006-08-15T17:30:12-04:00",
             "Tags":["plankton", "baseball", "decisions"],
             "Body":"I decided today that I don't like baseball. I like plankton."
         }
    }
    """
    r=db.saveDoc('mydb', doc, 'mydoc')
   
    assert(r.status==201)
    
    r=db.listDoc('mydb')
    

#test - open a document from the database
def test_opendoc():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    db.openDoc('mydb', 'mydoc')
    

#test - delete a document
def test_deletedoc():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    db.deleteDoc('mydb', 'mydoc')
    db.listDoc('mydb')


#test - database deletion
def test_delete_all_db():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    cdbr = db.delete('mydb')  
    assert(cdbr.status() == 200)
    cdbr = db.list()
    assert(cdbr.status() == 200 and len(cdbr.json()) == 2)


if __name__ == "__main__":
    test_emptydb()
    test_create_one_db()
    #testdbinfo()
    #testsavedoc()
    #testopendoc()
    #testdeletedoc()
    #test_delete_all_db()


