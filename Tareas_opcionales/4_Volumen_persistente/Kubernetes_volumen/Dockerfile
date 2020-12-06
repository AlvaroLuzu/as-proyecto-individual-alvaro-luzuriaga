FROM python:3
WORKDIR /couchdb
RUN apt-get update
RUN apt-get install python3
COPY $pwd/requirements.txt /couchdb/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5984
COPY $pwd/app-client.py /couchdb/app-client.py
CMD [ "python", "./app-client.py" ]