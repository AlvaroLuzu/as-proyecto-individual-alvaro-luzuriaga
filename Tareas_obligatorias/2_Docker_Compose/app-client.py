import couchdb2
import time

retries = 10
while True:
    try:
        couchdb_conex()
    except couchdb.exceptions.ConnectionError as exc:
        if retries == 0:
            raise exc
        retries -= 1
        time.sleep(10)

def couchdb_conex():
    server =  couchdb2.Server(href='http://couchdb:5984/', username='admin', 
    password='admin', use_session=True, ca_file=None)
    db = server.create('test')

    doc1 = {'_id': 'myid', 'name': 'mydoc', 'level': 4}
    db.put(doc1)
    doc = db['myid']
    assert doc == doc1

    doc2 = {'name': 'another', 'level': 0}
    db.put(doc2)
    print(doc2)

    db.put_design('mydesign',
                {"views":
                    {"name":
                        {"map": "function (doc) {emit(doc.name, null);}"}
                    }
                })
    result = db.view('mydesign', 'name', key='another', include_docs=True)
    assert len(result) == 1
    print(result[0].doc)
