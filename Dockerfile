    
 FROM python:3.7
 ADD AllFunctions.py /sud/
 ADD UserDataCollections_working.py /sud/
 RUN pip install pystrich
 RUN pip install pymongo
 EXPOSE 8081
 CMD [ "python", "/sud/UserDataCollections_working.py" ]
