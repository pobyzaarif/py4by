# Inspired by MATEMATIKA VERSI BARU, check comment text below XD

# Entah siapa yg membuat rumus seperti ini, tp ini emang keren banget*
# MATEMATIK VERSI BARU...
# Jika:
# A = 1%
# B = 2%
# C = 3%
# D = 4%
# E = 5%
# F = 6%
# G = 7%
# H = 8%
# I  = 9%
# J  = 10%
# K = 11%
# L = 12%
# M = 13%
# N  = 14%
# O  = 15%
# P = 16%
# Q = 17%
# R = 18%
# S =  19%
# T =  20%
# U = 21%
# V = 22%
# W = 23%
# X = 24%
# Y = 25%
# Z = 26%
# apakah yg membuat kesuksesan/ keberhasilan hidup menjadi 100%.......???
# H+A+R+D+W+O+R+K (Kerja Keras) : 8+1+18+4+23+15+18+11 = 98%
# K+N+O+W+L+E+D+G+E (Pengetahuan) :
# 11+14+15+23+12+5+4+7+5 = 96%
# L+O+V+E (Cinta) :
# 12+15+22+5 = 54%
# L+U+C+K (Nasib) :
# 12+21+3+11 = 47%
# Tidak ada yang jadi 100%.
# Apa yang membuatnya jadi 100%..???
# Adakah money..?
# M+O+N+E+Y =
# 13+15+14+5+25 = 72%    NO..!!!
# Leadership..?
# L+E+A+D+E+R+S+H+I+P =
# 12+5+1+4+5+18+19+8+9+16 = 97%  NO...!!!
# Ternyata apa yang membuat menjadi 100% adalah :
# Coba lihat yang ini...
# S+E+D+E+K+A+H+J+A+R+I+A+H 19+5+4+5+11+1+8+10+1+18+9+1+8 = 100%
# ( nilai saham akhirat kita. )
# KEBETULAN atau TIDAK...?  tapi itulah MATEMATIKA
# Semangat menjemput rezeki  , jangan lupa SEDEKAH yaaa...
# Sssaaabbbaaarrr...!!!
# Ternyata yang bisa membuatnya menjadi 100% ada lagi :
# I S T R I   D U A
# 9+19+20+18+9+4+21+1 = 100%
# atau
# B O J O   T E L U
# 2+15+10+15+20+5+12+21 = 100%
# Maka beristri dua atau duwe bojo telu akan membuat hidup kita bisa berhasil mencapai nilai 100% !!!
# KEBETULAN atau TIDAK ... ?  tapi itulah mainan MATEMATIKA-nya !!!
# Dan jawaban para istri adalah :
# L A M B E M U   M A S
# 12+1+13+2+5+13+21+13+1+19 = 100% juga

import string
a = string.lowercase[:26]
b = range(1, 27)
d = dict(zip(a, b))

t = raw_input('teks? ')
list(t)

numb = 0

for i in t :
  if i in d :
    numb += d.get(i)

print numb,'%'

