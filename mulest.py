import sqlite3
connection = sqlite3.connect("moviedb.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS MOVIES( Name TEXT, Actor TEXT, Actress TEXT,Director TEXT, Year INTEGER )")
cursor.execute("INSERT INTO MOVIES VALUES('96','Vijay Sethupathi','Trisha','Premkumar',2018)")
cursor.execute("INSERT INTO MOVIES VALUES('Karnan','Dhanush','Rajisha Vijayan','Mari Selvaraj',2021)")
cursor.execute("INSERT INTO MOVIES VALUES('Kaththi','Vijay','Samantha Ruth Prabhu','A.R. Murugadoss',2014)")
cursor.execute("INSERT INTO MOVIES VALUES('Paiyaa','Karthi','Tamannaah','N. Linguswamy',2010)")
cursor.execute("INSERT INTO MOVIES VALUES('Don','Sivakarthikeyan','Priyanka Mohan','Cibi Chakaravarthi',2022)")
cursor.execute("INSERT INTO MOVIES VALUES('Maaran','Dhanush','Malavika Mohanan','Karthick Naren',2020)")
cursor.execute("INSERT INTO MOVIES VALUES('Master','Vijay','Malavika Mohanan','Lokesh Kanagaraj',2021)")
cursor.execute("INSERT INTO MOVIES VALUES('Petta','Rajinikanth','Simran & Trisha','Karthik Subbaraj',2019)")
cursor.execute("INSERT INTO MOVIES VALUES('Bigil','Vijay','Nayanthara','Atlee',2019)")
print("\n\t\t\t\tMOVIE DETAILS DATABASE\n")
allData = cursor.execute("SELECT * FROM MOVIES").fetchall()
for i in allData:
    name, actor, actress, director, releasedYear = i
    print("{na:<20}{a:<25}{ats:<25}{d:<25}{yr:<5}".format(na=name, a=actor, ats=actress, d=director, yr=releasedYear))
print("\n\n\t\t\t\tACTOR QUERY\n")
actorQuery = cursor.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Vijay'").fetchall()
for i in actorQuery:
    name, actor, actress, director, releasedYear = i
    print("{na:<20}{a:<25}{ats:<25}{d:<25}{yr:<5}".format(na=name, a=actor, ats=actress, d=director, yr=releasedYear))
