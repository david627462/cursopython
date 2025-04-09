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

@app.post("/incluir_produto")
def adicionar_produto(codigo: str,nome: str,quantidade: int,preco: float):
    try: 
        con = sqlite3.connect("/home/ijovem02/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" insert into produtos ( codigo, nome, quantidade, preco) values (?,?,?,?) """ ,(codigo , nome , quantidade, preco,) )
        con.commit()
        con.close
        return {True}
    except:
        return False      
@app.get("/consultar_estoque")
def revisar_estoque():

    try:
        con = sqlite3.connect("/home/ijovem02/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(" select id, codigo, nome, quantidade from produtos  "  )
        rows=cur.fetchall()
        con.close
        return {rows}
    except:
        return False

    
@app.put("/alterar_produto")
def alterar_produto(id: int,codigo: str, nome:str):
    try:
        con = sqlite3.connect("/home/ijovem02/hackers/database/mercado.db")
        cur = con.cursor()
        cur.execute(""" update  produtos set codigo=?, nome=? where id=?  """ ,   (codigo, nome, id ) ) 
        con.commit()
        con.close
        return {True}
    except:
        return False


