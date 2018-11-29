# Author: https://github.com/k1000o23
f = open('hash.txt','r')
o = open('formatted_hashes.txt','w')
l = f.read().strip().split(',')
for i in l:
  o.write(i.split(':')[1][2:-1] + '\n') 
f.close()
o.close()