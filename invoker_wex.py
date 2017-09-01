import re

dictb = {
        'a' : 'p',
        'b' : 'z',
        'c' : 'w',
        'd' : 'n',
        'e' : 'l',
        'f' : 'h',
      }

def chiper(text) :
  alpha = ['a', 'b', 'c', 'd', 'e', 'f']
  enc = []
  for i in text :
    if i in alpha :
      enc.append(dictb[i])
    else :
      enc.append(i)
  enc = ''.join(map(str, enc))
  return enc

##### 5p4|5p9|5pl|5z7|5p8|5zp #####
# text = '5a4|5a9|5ae|5b7|5a8|5ba'
# print(chiper(text))
###################################

def unchiper(text):
  teta = ['p', 'z', 'w', 'n', 'l', 'h']
  unenc = []
  for i in text :
    if i in teta :
      unenc.append(dictb.keys()[dictb.values().index(i)])
    else :
      unenc.append(i)
  unenc = ''.join(map(str, unenc))
  return unenc

##### 5a4|5a9|5ae|5b7|5a8|5ba #####
# text = '5p4|5p9|5pl|5z7|5p8|5zp'
# print(unchiper(text))
###################################
