f = open("roma", "r")
lines = f.read()
f.close()

f = open("swsfc.tbl", "r")
tbl = f.read()
f.close()
tbl = tbl.split("\n")
jistable = []
i = 0
while i < len(tbl):
    p = tbl[i].split("=")
    jistable.append((p[0], p[1]))
    i += 1

def getjis(k):
    if(k >= 0x8200):
        print(k)
    for t in jistable:
        if k == t[1]:
            return t[0]
    return 0

lines = lines.split("\n")
out=[]
for l in lines:
    i = 0
    while i < len(l):
        if(ord(l[i]) >= 0x40)and(ord(l[i])<=0x59):
            n = ord(l[i]) - 0x11
        elif(ord(l[i])==0x2e):
            n = 0xc7
        elif(l[i] == '-'):
            n = 0x2c
        else:
            n = ord(l[i])
        out.append(n)
        i += 1
    out.append(0x0f)
f = open("o.bin", "wb")
f.write(bytes(out))
f.close()