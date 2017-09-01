def encode(text, shift) :
  n = 0
  listob = []
  if len(text) <= 3 :
    text = 'try another :p'
  for i in text :
    n += 2
    obfus = hex(ord(i) + int(shift) + n)
    listob.append(obfus)
  encode = '|'.join(map(str, listob))
  return encode

##### poby shift 7 = 0x79|0x7a|0x6f|0x88 #####
# text = 'poby'
# shift = 7
# print(encode(text, shift))
##############################################

def decode(text, shift) :
  n = 0
  listwo = []
  text = text.split('|')
  if len(text) <= 3 :
    decode = 'try another :p'
    return decode
  for i in text :
    obfus = int(i, 16)
    n -= 2
    dect = chr(obfus - int(shift) + n)
    listwo.append(dect)
  decode = ''.join(map(str, listwo))
  return decode

##### 0x79|0x7a|0x6f|0x88 shift 7 = poby #####
# text = '0x79|0x7a|0x6f|0x88'
# shift = 7
# print(decode(text, shift))
##############################################
