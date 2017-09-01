import sys
from invoker_quas import *
from invoker_wex import *
from invoker_exort import *

def first() :
  text = raw_input('text : ')
  shift = raw_input('shift : ')
  # poby shift 7 = 0x79|0x7a|0x6f|0x88
  b = encode(text, shift)
  # poby shift 7 = 79|7a|6f|88
  c = delete(b, '0x')
  # poby shift 7 = 79|7p|6h|88
  d = chiper(c)
  print ('result : ' + d)
  main(7)

def second() :
  text = raw_input('text : ')
  shift = raw_input('shift : ')
  # poby shift 7 = 0x79|0x7a|0x6f|0x88
  b = unchiper(text)
  # poby shift 7 = 79|7a|6f|88
  c = replace(b, '0x')
  # poby shift 7 = 79|7p|6h|88
  d = decode(c, shift)
  print ('result : ' + d)
  main(7)

def main(options) :
  if options == '1' :
    first()
  elif options == '2' :
    second()
  elif options == '0' :
    sys.exit(0)
  else :
    x = raw_input('options : ')
    main(x)


x = raw_input('options : ')
main(x)
