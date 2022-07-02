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
print("\t\t\t\tMOVIE DETAILS DATABASE")
allData = cursor.execute("SELECT * FROM MOVIES").fetchall()
for i in allData:
    title, actor, actress, director, releasedYear = i
    print("{t:<20}{a:<25}{ats:<25}{d:<25}{yr:<5}".format(t=title, a=actor, ats=actress, d=director, yr=releasedYear))
print("\n\n\t\t\t\tACTOR QUERY")
actorQuery = cursor.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Vijay'").fetchall()
for i in actorQuery:
    title, actor, actress, director, releasedYear = i
    print("{t:<20}{a:<25}{ats:<25}{d:<25}{yr:<5}".format(t=title, a=actor, ats=actress, d=director, yr=releasedYear))
