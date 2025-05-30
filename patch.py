#!/usr/bin/python3
# patch.py 
import os,sys 

f = open(sys.argv[1], "rb")
base = f.read()
f.close()

f = open(sys.argv[2], "rb")
ips = f.read()
f.close()

_hdr = ips[:5]
if _hdr != b'PATCH':
    print("Not a valid IPS file!")
    sys.exit()

bc = 5

class patch:
    def __init__(self):
        self.offset = 0
        self.length = 0
        self.bytes = []
    ###
###
patches=[]
while ips[bc:bc+3] != b'EOF':
    p = patch()
    p.offset = (ips[bc] << 16)|(ips[bc+1] << 8)|(ips[bc+2]) 
    bc += 3
    p.length = (ips[bc] << 8)|ips[bc+1]
    bc += 2
    p.bytes = ips[bc:bc+p.length]
    bc += p.length 
    patches.append(p)

for p in patches:
    base = base[:p.offset] + p.bytes + base[p.offset+p.length:]

f = open(sys.argv[1]+".out", "wb")
f.write(base)
f.close()
print(sys.argv[1]+".out written.")