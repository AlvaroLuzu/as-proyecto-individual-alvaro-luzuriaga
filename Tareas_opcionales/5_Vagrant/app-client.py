import couchdb2

server =  couchdb2.Server(href='http://127.0.0.1:5985/', username='admin', password='admin', use_session=True, ca_file=None)
#1.
db = server.create('test')
#2.
doc1 = {'_id': 'myid', 'name': 'mydoc', 'level': 4}
db.put(doc1)
doc = db['myid']
assert doc == doc1
#3.
doc2 = {'name': 'another', 'level': 0}
db.put(doc2)
print(doc2)
#4.
db.put_design('mydesign',
            {"views":
                {"name":
                    {"map": "function (doc) {emit(doc.name, null);}"}
                }
            })
result = db.view('mydesign', 'name', key='another', include_docs=True)
assert len(result) == 1
print(result[0].doc)