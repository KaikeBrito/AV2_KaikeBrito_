import mysql.connector

# Conectando mysql com vscode/python
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="secao04", autocommit = True
)

# criando um cursor mysql
mycursor = mydb.cursor()
execsqlcmd = lambda cmd, mycursor: mycursor.execute(cmd)

# Fazendo os CREATE TABLE, INSERT´S, DELETE, SELECT
execcreatetable = lambda table, attrs, mycursor: execsqlcmd(
    f"CREATE TABLE {table} ({attrs}) ", mycursor
)
execselect = lambda attrs, table, whercond, mycursor: execsqlcmd(
    f"SELECT {attrs} FROM {table} WHERE {whercond}", mycursor
)
executeinsertinto = lambda table, attrs, values, mycursor: execsqlcmd(
    f"INSERT INTO {table} ({attrs}) VALUES ({values})", mycursor
)
execdelete = lambda tables, condition, mycursor: execsqlcmd(
    f"DELETE FROM {tables} WHERE {condition}", mycursor
)

#CREATE das Tabelas
execcreatetable("Company", "id_company int AUTO_INCREMENT PRIMARY KEY, nome varchar(100), country varchar(100)", mycursor)
execcreatetable("VideoGames", "id_console int AUTO_INCREMENT PRIMARY KEY, nome varchar(100), id_company int, FOREIGN KEY (id_company) REFERENCES Company(id_company), release_date date" ,mycursor)
execcreatetable("Games", "id_game int AUTO_INCREMENT PRIMARY KEY, title varchar(100), genre varchar(100), release_date date, id_console int, FOREIGN KEY (id_console) REFERENCES VideoGames(id_console)",mycursor)
execcreatetable("Users", "id int AUTO_INCREMENT PRIMARY KEY, nome varchar(100), country varchar(100), id_console int, FOREIGN KEY (id_console) REFERENCES VideoGames(id_console)", mycursor)

#ISERT INTO nas Tabelas em ordem
executeinsertinto("Company", "nome, country", "'Sony Entertainment', 'EUA'", mycursor)
executeinsertinto("Company", "nome, country", "'Microsoft', 'EUA'", mycursor)

executeinsertinto("VideoGames", "nome, id_company, release_date", "'PS4', 1, '2019-10-12' ", mycursor)
executeinsertinto("VideoGames", "nome, id_company, release_date", "'XBOX ONE', 2, '2018-09-10'", mycursor)

executeinsertinto("Games", "title, genre, release_date, id_console", "'God of War', 'Acao', '2019-10-12', 1", mycursor)
executeinsertinto("Games", "title, genre, release_date, id_console", "'Metal Slug', 'Tiro', '1995-09-10', 2", mycursor)

executeinsertinto("Users", "nome, country, id_console", "'Kaike Brito', 'Fortaleza', 1", mycursor)
executeinsertinto("Users", "nome, country, id_console", "'Marina Mattos', 'Fortaleza', 2", mycursor)

#DELETE das tabelas
#execdelete('Users', "nome = 'Marina Mattos'", mycursor)

mydb.commit()
print(mycursor.rowcount)

#SELECT das Tabelas/ para fazer os selects comente as outras linhas

#print(execselect('*', 'Company', 'true', mycursor))
#print(execselect('*', 'VideoGames', 'true', mycursor))
#print(execselect('*', 'Games', 'true', mycursor))
#print(execselect('*', 'Users', 'true', mycursor))

res = mycursor.fetchall()
print_result = lambda res: [print(x) for x in res]
print_result(res)
