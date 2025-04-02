import hashlib
import random


def criptografar(chave):
     deve=random.randint(1,1000000)
     crip=chave
     
     
     senha = crip[1] + str(deve)
     objsenha = hashlib.sha512(senha.encode())
     hexsenha = objsenha.hexdigest()
     print(hexsenha)  

     return crip 

def entrada():
     saida = []
     usuario = input("digite o seu nome")
     senha = input("digite sua senha")
     saida.append(usuario)
     saida.append(senha)
     return saida

if __name__ == "__main__":
     criptografar(entrada())
     
