import sqlite3
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.put("/subtrair_estoque")
def subtrair(id:int, quant: int):
    try:
        con = sqlite3.connect("/Users/POSITIVO/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" update produtos set quantidade = quantidade - ? where id=? """, (quant, id) )
        con.commit()
        con.close()             
        return {True}
    except:
        return {False} 

     
@app.put("/adicionar_estoque")
def adicionar_estoque(id: int, qnt: int): 
    try:
        con = sqlite3.connect("/Users/POSITIVO/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" update produtos set quantidade = ? where id = ? """, (qnt, id))
        con.commit()
        con.close()
        return 1
    except:
        return -1

@app.put("/reajustar_preco_total")
def reajustar_preço_total(p: float):
    try: 
        con = sqlite3.connect("/Users/POSITIVO/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" update produtos set preco = preco + (preco / 100 * ?) """, (p,))
        con.commit()
        con.close()
        return 1
    except:
        return -1
