#! /usr/bin/env python
# -*- coding: utf-8 -*-

# simulador experimental de redes completamente opticas
# Autor: Marielb Marquez - Jorge Ortega
# Cotutor: Andrés arsia
#
# -*- coding: utf-8 -*-

import sys, os
import random
import funtion as g
#import networkx as net
#import matplotlib.pyplot as plt

#g = net.Graph()
print ""
print ""
print ""
print "\tSimulador experimental de redes completamente opticas"
print ""
n = input("\tEscriba el tamaño de la red: ") # tamaño de la red
p = 6 #random.randint(5, 10) input("Escriba la cantidad de paquetes: ")
I = input("\tEscriba la cantidad de entradas: ") # números de entradas
e = []
In=I
nodos = n*n
E=0
while (In >0):
  h = input("\tEscriba el número del nodo de la entrada %d: " % (E+1))
  e.append(h)
  E += 1
  In -= 1

e_a = random.choice(e)

o = input("\tEscriba la cantidad de salidas: ")
s = []
ou=o
E=0
while (ou > 0):
  h = input("\tEscriba el número del nodo salida %d: " % (E+1))
  s.append(h)
  E += 1
  ou -= 1

itera= input("\tEscriba el número de iteraciones: ")

tecla = sys.stdin.read(1)
k=1
malla = []
caminos = []

for i in range(nodos):
    malla.append([])
    malla[i].append(k) # nodo actual
    malla[i].append(k+1) # nodo que esta al este
    malla[i].append(k+n) # nodo que esta al sur
    malla[i].append(k-1) # nodo que esta al oeste
    malla[i].append(k-n) # nodo que esta al norte
    malla[i].append(0)
    malla[i].append(0)
    k = k+1

t=n
t1 = n-malla[0][0]
for i in range(nodos):
  for j in range(5):
    if malla[i][0] == t :
      malla[i][1] = 0
    if malla[i][0] == t-t1:
      malla[i][3] = 0
    if malla[i][j] < 0 or malla[i][j] > n*n:
      malla[i][j] = 0
  if malla[i][0] == t:
    t=t+n

k=0
for i in range(nodos):
    c=0
    for j in range(1, 6):
      if malla[i][j] != 0:
        c += 1
        caminos.append([])
        caminos[k].append(str(malla[i][0])+'-'+str(malla[i][j]))
        caminos[k].append(0)
        k += 1
    malla[i][5]=c

os.system('clear')
evento = open('eventos.txt', 'w')
evento.write('E0: ')
e1=[]
l1=p/I
l=0
for i in range(p):
  e1.append([])
  e1[i].append('p'+str(i+1))
  e1[i].append(e[l])
  evento.write('    p%d llega a %d\n' % (i+1, e[l]))
  print "   p%d llega a %d\n" % (i+1, e[l])
  e1[i].append(0)
  malla[e[l]-1][6] += 1
  if i == i:
    l += 1
  if l > I-1:
    l=0

t=s[0]
i=0
c=1

tecla = sys.stdin.read(1)
dmalla = g.crearmalla(n)
g.graficarmalla(dmalla, e, s)
#for  i in dmalla:
  #for j in i:
    #print j,
  #print ""

#net.draw(g)
#plt.show()
#net.draw(g)
#plt.savefig("networkx1.png")
tecla = sys.stdin.read(1)
os.system('clear')

i=i1=q=0
while (malla[t-1][6] < p and itera>0):
  if e1[i][0] == 'p'+str(i+1):
    h=e1[i][1]
    if h != malla[t-1][0]:
      for j in range(1, 5):
       for k in caminos:
        if k[0] == str(h)+'-'+str(malla[h-1][j])  and e1[i][2] != malla[h-1][j]:
         if k[1]==0 and e1[i][2] != h:
          k[1] = -1
          e1[i][2] = e1[i][1]
          e1[i][1] = malla[h-1][j]
          malla[h-1][6] -= 1
          malla[e1[i][1]-1][6] += 1
          q += 1
          evento.write("E%s: Moviendo el paquete p%s al nodo %s  |  bloqueo camino %s\n" % (str(q), str(i+1), str(malla[h-1][j]), k[0]))
          print "E%s: Moviendo el paquete p%s al nodo %s  |  bloqueo camino %s\n" % (str(q), str(i+1), str(malla[h-1][j]), k[0])
          dmalla = g.cambiarmalla(dmalla, n, h, malla[h-1][j])
          g.graficarmalla(dmalla, e, s)
          tecla = sys.stdin.read(1)
          itera -= 1
          break;
         break;
       #break;
  i += 1

  if i == p:
    i=0
    q += 1
    evento.write('E%s:' % str(q))
    for c in caminos:
      if c[1] != 0:
        c[1]=0
        evento.write('  Desbloqueado el camino %s\n' % c[0])
        print '  Desbloqueado el camino %s\n' % c[0]
    dmalla = g.crearmalla(n)
    g.graficarmalla(dmalla, e, s)

    tecla = sys.stdin.read(1)

evento.close()
for i in malla:
  print "\t ", i
