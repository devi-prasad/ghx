from couchpy import couchdbcode

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
    assert(cdbr.status() == 200 and len(cdbr.json())==3)
    #db.delete('mydb')
     

#test - save a document into the database
def test_save_doc():
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
    cdbr = db.savedoc('mydb', doc, 'mydoc')
    assert(cdbr.status() == 201)
    cdbr = db.listdoc('mydb')
    assert(cdbr.status() == 200 and cdbr.docscount() == 1)
    

#test - open a document from the database
def test_open_doc():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    cdbr = db.opendoc('mydb', 'mydoc')
    assert(cdbr.status() == 200)

#test - delete a document
def test_delete_doc():
    db = couchdbcode.CouchDB('127.0.0.1', '5984')
    assert(db != None)
    db.deletedoc('mydb', 'mydoc')
    


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
    test_save_doc()
    test_open_doc()
    test_delete_doc()
    test_delete_all_db()


