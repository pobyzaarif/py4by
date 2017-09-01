import re

def delete(text, pattern) :
  dell = re.sub(pattern, '', text)
  return dell

##### 5a4|5a9|5ae|5b7|5a8|5ba|5b0|5b5|5ba|5c3 #####
# text = '0x5a4|0x5a9|0x5ae|0x5b7|0x5a8|0x5ba|0x5b0|0x5b5|0x5ba|0x5c3'
# patt = '0x'
# print(delete(text, patt))
##############################################

def replace(text, pattern) :
  repp = text.split('|')
  list_txt = []
  for i in repp :
    merger = pattern + i
    list_txt.append(merger)
  txt = '|'.join(map(str, list_txt))
  return txt

##### 0x5a4|0x5a9|0x5ae|0x5b7|0x5a8|0x5ba|0x5b0|0x5b5|0x5ba|0x5c3 #####
# text = '5a4|5a9|5ae|5b7|5a8|5ba|5b0|5b5|5ba|5c3'
# patt = '0x'
# print(replace(text, patt))
##############################################
