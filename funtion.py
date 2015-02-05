#! /usr/bin/env python
# -*- coding: utf-8 -*-

# funciones para el simulador experimental de redes completamente opticas
# Autor: Marielb Marquez - Jorge Ortega
# Cotutor: Andrés Arcia-Moret
#
# -*- coding: utf-8 -*-

def crearmalla(n):
  n = n
  a = []
  l = 0
  t=k = 0
  nodos = 2*n-1

  for j in range(nodos):
    l += 1
    for i in range(n):
      a.append([])
      if l%2 != 0:
        t += 1
        a[k].append(t)
        if i < n-1:
          a[k].append('-')
      else:
        a[k].append('|')
        a[k].append(' '),
    k  += 1
    
  return a

def cambiarmalla(malla, n, a, b):
  malla = malla
  n = n
  a = a
  b = b
  nodos = 2*n-1
  for i in range(nodos):
    for j in range(nodos):
      if malla[i][j] == a:
        x=i
        y=j

  for i in range(nodos):
    if malla[x][i] == b:
      if a < b:
        malla[x][i-1] = ' => '
      else:
        malla[x][i+1] = ' <= '
      break;
    if malla[i][y] == b:
      if a < b:
        malla[i-1][y] = '||'
      else:
        malla[i+1][y] = ' || '
      break;

  return malla

def mayordispo(malla, pos, salida):
  malla = malla
  pos = pos
  salida = salida

  mayor = 0

  for k in range(1, 5):
   if malla[pos][k] != 0:
    if salida == malla[pos][k]:
      mayor = salida
    else:
      if salida - malla[pos][k] < salida - malla[pos][k+1]:
        if salida - malla[pos][k] > 0:
          mayor = malla[pos][k]
        else:
          mayor = malla[pos][k+1]
      else:
        if salida - malla[pos][k] < 0:
          mayor = malla[pos][k+1]
        else:
          mayor = malla[pos][k]

  return mayor

def graficarmalla(malla, e, s):
  malla = malla
  e = e
  s = s
  h=0
  for i in malla:
    for j in i:
      h=0
      for k in e:
        if k == j:
          h=k
      if h == 0 and s[0] != j:
        print j,
      elif h==j:
        print str(j)+'E',
      else:
        print str(j)+'S',
    print ""
