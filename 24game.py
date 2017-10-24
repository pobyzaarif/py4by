import random
import re
import sys

def validateisnumber(inputt) :
  try:
    c = eval(inputt) # validate isnumber?
    return True
  except :
    return False

def validatelist(answertoparse) :
  regex = re.compile(r'[1-9]\d*')
  listN = regex.findall(answertoparse)
  data = map(int, listN)
  return data

def validatemap(map1, map2) :
  c = set(map1) - set(map2)
  if (len(c) == 0) :
    flag = True
  else :
    flag = False
  return flag

def validateanswer(countthis) :
  is24 = eval(countthis)
  if (is24 == 24) :
    flag = True
  else :
    flag = False
  return flag

quest = []
bnumb = ['1st', '2nd', '3rd', '4th']
for x in range (4) :
  a = random.randint(1, 10)  # Integer from 1 to 10, endpoints included
  quest.append(a)
  index = [x+1, bnumb[x]]
  print bnumb[x], 'card :', a
# print quest

loop = True
while loop :
  answer = raw_input('count? ')
  if answer == 'skip' :
    sys.exit();
  isnumber = validateisnumber(answer)
  if isnumber :
    isfour = validatelist(answer)
    if (len(isfour) == 4) :
      isvalid = validatemap(isfour, quest)
      if isvalid :
        is24 = validateanswer(answer)
        if is24 :
          print 'correct answer'
          loop = False
        else :
          print 'incorrect answer'
      else :
        print 'invalid number'
    else :
      print 'should be 4 numbers'
  else :
    print 'data error'
