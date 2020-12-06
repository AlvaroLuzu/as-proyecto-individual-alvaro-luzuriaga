#!/bin/bash

read -p "Introduzca su usuario de CouchDB: " usr
read -p "Introduzca su contraseña de CouchDB: " psw
echo ""
echo "Bienvenido a CouchDB"
echo ""
curl http://127.0.0.1:5984/
echo ""

while true; do
    echo "Opciones:"
    echo "1) GET"
    echo "2) PUT"
    echo "3) DELETE"
    echo ""
    read -p "Seleccione una opcion " op
    case $op in
        #GET
        1) echo "Opción Seleccionada GET"
        echo ""
        curl -X GET http://$usr:$psw@127.0.0.1:5984/_all_dbs
        echo ""
        read -p "Seleccione una base de datos a leer: " get
        curl -X GET http://$usr:$psw@127.0.0.1:5984/$get
        break;;
        #PUT
        [2]* ) echo "Opción Seleccionada PUT"
        echo ""
        read -p "Indique el nombre de la base de datos a crear: " put
        curl -X PUT http://$usr:$psw@127.0.0.1:5984/$put
        break;;
        #DELETE
        [3]* ) echo "Opción Seleccionada DELETE"
        echo ""
        curl -X GET http://$usr:$psw@127.0.0.1:5984/_all_dbs
        echo ""
        read -p "Seleccione una base de datos a leer: " del
        curl -X DELETE http://$usr:$psw@127.0.0.1:5984/$del
        break;;
        * ) echo "Seleccione una opcion .";;
    esac
done

echo "¡Hasta otra!"