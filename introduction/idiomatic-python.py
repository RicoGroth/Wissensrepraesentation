#######
import this

# incorrect: namespace pollution
from scipy import *

# correct
from scipy import integrate
value, err = integrate.quad(func=pow, a=0., b=1., args=(5,))
value
# integral of x^5 over [0,1]

# or
import scipy
value, err = scipy.integrate.quad(func=pow, a=0., b=1., args=(5,))


import numpy as np

####################
from __future__ import braces

# Quelle: Raymond Hettinger: Transforming Code into Beautiful, Idiomatic Python 
# http://www.youtube.com/watch?v=OSGv2VnC0go&feature=youtu.be

# and David Goodger: idiomatic python
# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#building-strings-from-substrings

# swap values
temp = a
a = b
b = temp

# better with tupels
b, a = a, b

###################

# not this:
if x == True:
  pass
# do this:        
if x:             
  pass               


# Looping with for (foreach):

for i in [0, 1, 2]:
   print " i ist " , i

for i in range(3):
   print " i ist " , i

# in python3: xrange -> range
for i in xrange(3):
   print " i ist " , i

# looping over collections

# here list
colors = ['rot', 'gruen', 'blau', 'gelb']

# c-style (don't do it)
for i in range (len(colors)):
  print colors[i]
  
# python style
for color in colors:
  print colors 


 
# looping reverse 
# c-style (don't do it)
for i in range(len(colors)-1,-1,-1):
  print colors[i]

# python style  
for color in reversed(colors):
  print colors  
  
# looping over collection and indicies  
# with indicies (don't do it)
for i in range(len(colors)):
  print i, '-->', colors[i]

for i, color in enumerate(colors):
  print i, '-->', colors[i]
  
# looping over two collections

names = ['andrea', 'karl', 'lisa']

# with indicies (don't do it)
n = min(len(names), len(colors))
for i in rangen:
  print names[i], '-->', colors[i]

# the lisp way 
for name, color in zip(names, colors):
  print name, '-->', color

# python way opimized (L1-cache!)
from itertools import izip
for name, color in izip(names, colors):
  print name, '-->', color

#looping in sorted order
for colors in sorted(colors):
 print colors

#looping in sorted order
for colors in sorted(colors, reverse=True):
 print colors


#custom sort order
def compare_length(c1, c2):
  if len(c1) < len(c2): return -1
  if len(c1) > len(c2): return 1
  return 0

print sorted(colors, cmp=compare_length)

# faster with key-function
print sorted(colors, key=len)


###
# String concatenation

#ineffient
result = ''
for s in colors:
    result += s
    
result = ''.join(colors)
   

# simple profiling 
import timeit

jointimer = timeit.Timer("string_test.join_test('test', 5)", "import string_test")
print "Join method took %f seconds" % jointimer.timeit()



##################################################################
##################################################################

f = open('workfile', 'r')

blocks = []
while True:
  block = f.read(32)
  if block =='':
    break
  blocks.append(block)

# better:  
  
blocks = []
for block in iter(partial(f.read, 32), ''):
  blocks.append(block)
  
####################

def find(seq, target):
  found = False
  for i, value in enumerate(seq):
    if value == tgt:
      found = True
      break
  if not found 
    return -1
  return i    
 
 # better : for with else
 def find(seq, target):
  for i, value in enumerate(seq):
    if value == tgt:
      break
  else: # nobreak
    return -1
  return i    
 
#####################

#looping over dictionary keys
d = {'lisa':'blue', 'clara':'white', 'thomas':'red'}

for k in d:
  print k

# mutating dictionaries:
for k in d.keys():
  if k.startswth('r'):
    del d[k]

d = { k : d[k] for k in d if not k.startswith('t') }

# looping of keys and values
for k in d:
 print k, '-->', d[k]

#better (no lookups)
for k, v in d.items():
 print k, '-->', v

# without big list
for k, v in d.iteritems():
 print k, '-->', v

# constructing dictionaries
d = dict(izip(names, colors))

d = dict(enumerate(names))
##

#counting with dictionaries

colors = ['red', 'green', 'red', 'blue', 'white', 'blue']
d = {}
for color in colors:
  if color not in d:
    d[color] = 0
  d[color] += 1  

# shorter
d = {}
for color in colors:
  d[color] = d.get(color, 0) + 1
  
# grouping with dictionaries
names = {'raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'carlie'}
d = {}  
for name in names:
  key = len(name)
  if key not in d:
    d[key] = []
  d[key].append(name)
 
import collections 
d = collections.defaultdict(list)
for name in names:
  key = len(name)
  d[key].append(name)

##################################


A = np.ones([8, 10])
A[[0,1],[8,9]] = 0
A[range(1,8), range(0,7)] = range(1,8)

########################
## beauty in brevity 
########################

## veeeeery long:
def scale(A):
  shape = A.shape
  m = shape[0]
  n = shape[1]
  for i in rangen:
    x = A[0, i]
    A[0,i] = x * 2
  for i in rangen:
    x = A[m-1, i]
    A[m-1, i ] = x * 2
  if m < n:
    k = m
  else: k = n
  for i in range(k):
    x = A[i,i]
    A[i, i] = x * 5
  
### use *= etc.
def scale(A):
  shape = A.shape
  m = shape[0]
  n = shape[1]
  for i in rangen:
    A[0, i] *= 2
  for i in rangen:
    A[m - 1, i] *= 2
  if m < n:
    k = m
  else:
    k = n
  for i in range(k):
  A[i, i] *= 5  
  
### use build-in functions 
def scale(A):
  shape = A.shape
  m = shape[0]
  n = shape[1]
  for i in rangen:
    A[0, i] *= 2
  for i in rangen:
    A[m - 1, i] *= 2
  k = min(m, n)
  for i in range(k):
    A[i, i] *= 5
 
### use syntax of data structures

def scale(A):
  A[0, :] *= 2
  A[-1, :] *= 2
  shape = A.shape
  m = shape[0]
  n = shape[1]
  k = min(m, n)
  for i in range(k):
    A[i, i] *= 5

### avoid variables
def scale(A):
  A[0, :] *= 2
  A[-1, :] *= 2
  for i in range(min(A.shape)):
    A[i, i] *= 5

### use advanced syntax
def scaleB(A): 
  A[[0, -1], :] *= 2
  for i in range(min(A.shape)):
    A[i, i] *= 5
  
# with build-in functions 
def scale(A):
  A[[0, -1], :] *= 2
  np.fill_diagonal(A, 5 * np.diag(A))  
###  
