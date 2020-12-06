import couchdb2

server =  couchdb2.Server(href='http://127.0.0.1:5985/', username='admin', password='admin', use_session=True, ca_file=None)

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
volumen()

def volumen():

        # Escritura de ficheros
        f= open("fichero1.txt","w+")
        for i in range(2):
                f.write("Este es el fichero 1, linea numero %d\r\n" % (i+1))
        f.close()
        f = open("fichero2.txt", "a")
        f.write("Este es el fichero 2 \n")
        f.close()