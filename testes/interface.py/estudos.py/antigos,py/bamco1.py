import sqlite3
from sqlite3 import Error
import os 
pastainterface=os.path.dirname(__file__)
nomebanco=pastainterface+"\\teste.db"
def conexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomebanco)
    except Error  as ex :
        print(ex)
    return con
def dql(query):#slect
    vcon=conexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res
def dml(query):
    try:
        vcon=conexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        print("ddml concluida")
    except Error as ex:
        print(ex)
        