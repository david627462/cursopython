def dividir(z1,z2):
     return(z1/z2)

def multipricar(l1,l2):
     return(l1*l2)

def subtrair(m1,m2):
     return(m1-m2)

def somar(n1, n2):
     return(n1+n2)

def menu():
     print('1 . somar')
     print('2 . subtrair')
     print('3 . multipricar')
     print('4 . dividir')
     print('5 . sair')
     try:
        
          opcao = int(input("digite sua opcao"))
          return opcao 
         
     except:
          return 0

if __name__ == "__main__":
     while True:     
          r = menu()
          if r == 0:
               print("opcao invalida")
          if r == 5:
               exit()
          if r == 1:
               b = int(input("digite o valor a "))
               n = int(input("digite o valor b "))
               print(somar(b,n))
          if r == 2:
               f = int(input("digite o valor f "))
               e = int(input("digite o valor e "))
               print(subtrair(f,e))
          if r == 3:
               c = int(input("digite o valor c "))
               k = int(input("digite o valor k "))
               print(multipricar(c,k))     
          if r == 4:
               d = int   


     