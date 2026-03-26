#Programa que lê o primeiro termo e a razão de uma PA utilizando while
t1=int(input('Digite o primeiro termo da PA: '))
r=int(input('Digite a razão da PA: '))
cont=1
while cont<11:
    print(t1, end=' ')
    t1+=r
    cont+=1
