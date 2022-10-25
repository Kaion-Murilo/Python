import sqlite3
from tkinter.tix import Select
from unicodedata import numeric
banco=sqlite3.connect("banco_1_.db")
cursor=banco.cursor()
cursor.execute(f"CREATE TABLE IF NOT EXISTS Aluno (id integer,nome vachar[50] not NULL,matricula integer not null,CPF VARCHAR[30] NOT NULL,numero integer ,idade intege,sexo text) ")

# id=2
# nome="kaion"
# quant=222
# Data="2012-04-03"
# matricula_1=111
# idade=11
# sexo="masculino"
# mensalidade=2
# numero=999999999999
# cpf=11111111
# cursor.execute(f"INSERT INTO Aluno (id ,nome,matricula,CPF,numero,idade,sexo) VALUES ({id},'{nome}',{matricula_1},{cpf},{numero},{idade},'{sexo}')")
# banco.commit()

# cursor.execute("Select * FROM Aluno")
# print(cursor.fetchall())
nome="mmil"
Data="2011-02-02"#data=ano/dias/mes
quant=900
valor=1220
totap=2
matricula=654321
idade=3555
mensalidade=2
sexo="masculino"
cursor.execute(f"UPDATE aluno SET nome='{nome}',idade={idade} where id = 2")
banco.commit()

cursor.execute(f"DELETE FROM aluno WHERE  id={1}")
banco.commit()  

