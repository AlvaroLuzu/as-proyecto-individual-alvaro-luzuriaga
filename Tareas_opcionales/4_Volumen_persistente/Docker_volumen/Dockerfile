FROM python:3
WORKDIR /couchdb
ADD . /couchdb
RUN apt-get update
RUN apt-get install python3
RUN pip install virtualenv
RUN pip install -r requirements.txt
EXPOSE 5984
CMD [ "python", "./app-client.py" ]