    
 FROM python:2.8
 ADD AllFunctions.py /sud/
 ADD UserDataCollections_working.py /sud/
 RUN apt-get update && apt-get install vim -y
 RUN pip install pystrich
 RUN pip install pymongo==2.8
 EXPOSE 8081
 CMD [ "python", "/sud/UserDataCollections_working.py" ]
