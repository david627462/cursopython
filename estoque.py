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

     
