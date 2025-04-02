import qrcode
import csv
def lerarquivo():
     with open("lista.csv",newline="",encoding="utf-8") as file:
          arquivo=csv.reader(file)
          for linha in arquivo:
               gerarqr(linha)

def gerarqr(bav):
     print(bav[1])
     name = "seu nome : " +bav[1]
     email = "seu email : " +bav[2]
     msg = name + "\n" + email
     arquivo = bav[0]+ ".png" 
     img = qrcode.make(msg)
     img.save(arquivo)



if __name__ == "__main__":
     lerarquivo()