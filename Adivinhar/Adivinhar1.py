import random  #Serve para sortear um número.
import sys  #Serve para que o programa se encerre.
n1=random.randint(0,9)  #Servem para sortear um número inteiro entre 0 e 9.
n2=random.randint(0,9)
n3=random.randint(0,9) 
n4=random.randint(0,9) 
n5=random.randint(0,9)
comp='{}{}{}{}{}'.format(n1,n2,n3,n4,n5) #Substitui as chaves pelas variáveis depois do .format.
global teste        
global tentativas      
global jogada
tentativas=0 
jogada=0   
mostra=''  
usuario='' 
teste=0  

while(tentativas<10):  #Diz que deve-se repetir o que está dentro deste while enquanto o número de tentativas for menor que 10.
    expo=0
    usuario=''
    jogada=0
    while jogada<5:  #Diz que deve-se repetir o que está dentro deste while enquanto o número de jogadas for menor que 5.  #Rever porque não tenho certeza quanto as jogadas.#
         x=input('Digite um número: ')  #Pede para o usuário digitar o primeiro número da senha.
         jogada=jogada+1  #Serve para dizer que jáfoi uma jogada.
         usuario=usuario+x
         print(usuario)
    while teste <5:
        if usuario[expo]==comp[expo]:  
            mostra=mostra+' +1 '  #Está no lugar certo.
        elif usuario[expo]== comp[0] or usuario[expo]== comp[1] or usuario[expo]== comp[2] or usuario[expo]== comp[3] or usuario[expo]== comp[4]:
            mostra=mostra+ ' 0 '  #Está na senha mas não no lugar certo.
        else:
            mostra=mostra+' -1 '  #Não está na senha.
        expo=expo+1
        teste=teste+1
    if usuario==comp:
        print('Você conseguiu!')  #Mostra que a pessoa conseguiu.
        sys.exit()  #Serve para sair do programa.
    print(mostra)  #Imprime na tela o mostra.
    tentativas=tentativas+1  #serve para dizer que já foi uma tentativa.
    usuario=''  #É uma string vazia, oou seja, ainda não está definido o que está dentro dela.
    mostra=''  #É uma string vazia, oou seja, ainda não está definido o que está dentro dela.
    teste=0  
    expo=0
    
