from __future__ import print_function
text = raw_input('text ? ')
# teks = 'ggwp'
s = -9
for i in text :
  c = (ord(i) + s)
  print (chr(c), end='')

print (' ')
