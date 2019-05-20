FROM python:3.7
ADD AllFunctions.py /sud/
ADD UserDataCollections_working.py /sud/
RUN apt-get update && apt-get install vim -y
RUN pip install pymongo
# CMD [ "python", "/sud/UserDataCollections_working.py" ]
