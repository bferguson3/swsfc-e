import os,sys,json

filelist = [
    0x43be1
]
'''
0x41eee,
    0x41e20,
    0x41d59,
    0x41c6e,
    0x41b61,
    0x41aa0,
    0x419c5,
    0x418fa,
    0x4183d,
    0x41779,
0x40600-1,
0x41fa0,
0x43dc5,
0x44323,
0x446bf,
0x44d66,
0x451d6,
0x456dc,
0x45c4b,
0x45ff1,
0x46233,
0x470cd, #space
0x48000-1,
0x48a0e,
0x48a79,
0x48ff3,
0x49a8d,
0x49f4d,
0x4a6a2,
0x4b0eb,
0x4b590,
0x4b850,
0x4bf19,
0x4c2be,
0x4c6a5,
0x4c9b2,
0x4cfe3,
0x4d577,
0x4db9b,
0x4e1cd,
0x4e359,
0x4e473,
0x4e4e9,
0x4e588,
0x4e77e,
0x4e796,
0x4e847,
0x4ea29,
0x4eb18,
0x4eb20,
0x4ec09,
0x4eca8,
0x4ecf0,
0x4edbc,
0x4ef76,
0x4f055,
0x4f08a,
0x4f0ba,
0x4f11c,
0x4f14d,
0x4f1ff,
0x4f211,
0x4f5af,#space
0x50000-1,
0x50772,
0x50af0,
0x50cc0,
0x50cdb,
0x51093,
0x51c52,
0x51e1a,
0x51f77,
0x52023,
0x52085,
0x52704,
0x527eb,
0x5297b,
0x52a56,
0x52ca5,
0x52f56,
0x530e8,
0x53194,
0x53747,
0x537a1,
0x537e4,
0x5385c,
0x53a1e,
0x53a68,
0x53b0e,
0x53b2f,
0x53ba3,
0x53bfd,
0x53c6d,
0x53c71,
0x53d47,
0x53d71,
0x53d99,
0x53dac,
0x53dd1,
0x53e15,
0x53e6b,
0x541b6,
0x545a7,
0x545c8,
0x545f2,
0x5467f,
0x548c7,
0x54982,
0x551b6,
0x553d7,
0x554d9,
0x554f7,
0x5555d,
0x55ac6,
0x55b81,
0x55c2d,
0x55cae,
0x55cef,
0x55d5f,
0x55db7,
0x55ff2,
0x56066,
0x56174,
0x5618c,
0x561a1,
0x563e9,
0x5641c,
0x56467,
0x56957,
0x56a33,
0x56b7b,
0x56c51,
0x56f57,
0x5721f,
0x57449,
0x5751a,
0x57563,
0x575a3,
0x575cc,
0x57939,
0x57a00,
0x57a62,
0x57ac6,
0x57af4,
0x57b33,
0x57c29,
0x57c6f,
0x57cc7,
0x57d1a,
0x57d49,
0x58000-1,
0x5845f,
0x58467,
0x584be,
0x584c2,
0x584dc,
0x585ca,
0x58739,
0x58749,
0x58769,
0x58d08,
0x58d6a,
0x58de2,
0x58e83,
0x58ee7,
0x58f8b,
0x59605,
0x59736,
0x598c6,
0x59ba6,
0x59e3a,
0x59fa9,
0x59feb,
0x5a02a,
0x5a053,
0x5a0a7,
0x5a185,
0x5a1d1,
0x5a230,
0x5a263,
0x5a2bc,
0x5a3ba,
0x5a427,
0x5a481,
0x5a53d,
0x5a8b2,
0x5b030,
0x5b0d3,
0x5b142,
0x5b1c3,
0x5b217,
0x5b230,
0x5b41f,
0x5b485,
0x5b517,
0x5b8e8,
0x5bce5,
0x5be22,
0x5bec6,
0x5c2ef,
0x5c4d0,
0x5c57f,
0x5c861,
0x5cd5c,
0x5cecb,
0x5d0d8,
0x5d249,
0x5d4b9,
0x5d7b1,
0x5d986,
0x5d9a7,
0x5da19,
0x5da7f,
0x5e4cc,
0x5e6cd,
0x5e803,
0x5e83f,
0x5e879,
0x5e8b7,
0x5eaa5,
0x5eb44,
0x5ebad,
0x5ebe4,
0x5ed35,
0x5eef0,
0x5ef47,
0x5ef4f,
0x5ef57,
0x5ef5f,
0x5efb7,
0x5efe8,
0x5f06d,
0x5f179,
0x5f270,
0x5f300,
0x5f3ae,
0x5f56f,
0x5f5d1,
0x5f698,
0x5f703,
0x5f739,
0x5f7d5,
0x5f867,
0x5f8a7,
0x5f8e9,
0x5f92d,
0x5f979,
'''

f = open("swsfc-e.sfc", "rb")
rom = f.read()
f.close()

jdict = []

f = open("swsfc.tbl", "r")
line = f.readline()
i = 0
while line != "":
    l = line.split("=")
    l[1] = l[1].rstrip()
    if(l[0] == "20"):
        l[1] = "  "
    jdict.append([l[0], l[1]])
    line = f.readline()

class SWFile:
    def __init__(self):
        self.address = 0
        self.size = 0
        self.bytes = []
        self.text = ""
        self.translation = ""
    ###
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4,
            ensure_ascii=False)
    ###
###

flist = []

def getjis(m):
    no = hex(m[0] << 8 | m[1])[2:]
    for p in jdict:
        #print(no, p[0])
        if(p[0] == no):
            #print("found", p[1])
            return p[1]
            break
    return "?"

def getlowjis(m):
    no = hex(m)[2:]
    if m == 0xf:
        return "{f}" #0fh is END
    if m == 0x1:
        return "\n" # 01h is NEWLINE
    for p in jdict:
        if(p[0] == no):
            return p[1]
            break
    return "{"+hex(m)[2:]+"}"

# 03: blue color?
# 0300: reset color
# 06: next page
# 060F: end dialogue
# 08: begin mf sequence
# 0B: male
# 0A: female
# 07: end mf sequence
# 0C/0C00: hero name?


i = 0
while i < len(filelist):
    if (rom[filelist[i]] != 0xe) and (i != 0)and (filelist[i] != 0x57fff)and (filelist[i] != 0x4ffff)and (filelist[i] != 0x47fff):
        print("did not dump: ", hex(filelist[i]), hex(rom[filelist[i]]))
        i += 1
        file=[]
        flist.append(file)
        continue
    else:
        # ok, we found the final byte
        bc = filelist[i] + 1
        # first two bytes are offset from this location to str
        ofs = rom[bc + 1] << 8 | rom[bc]
        num = int(ofs/2)
        file=[]
        j = 0
        while j < num:
            sf = SWFile()
            _ofs = (rom[bc + 1] << 8) | rom[bc]
            #print(hex(filelist[i] + 1 + _ofs))
            sf.address = _ofs + filelist[i] + 1 
            b = sf.address
            while rom[b] != 0xf:
                sf.bytes.append(rom[b])
                b += 1
            sf.bytes.append(0xf)
            sf.size = len(sf.bytes)
            file.append(sf) 
            bc += 2
            j += 1
        flist.append(file)
    i += 1

## now convert them, using .tbl 
for fi in flist:
    for w in fi:
        s = ""
        b = 0
        while b < len(w.bytes):
            if(w.bytes[b] == 0x10):
                a = b''
                a = a + bytes([w.bytes[b]])
                a = a + bytes([w.bytes[b+1]])
                s += getjis(a)
                b+=1
            elif(w.bytes[b] == 0x11):
                a = b''
                a = a + bytes([w.bytes[b]])
                a = a + bytes([w.bytes[b+1]])
                s += getjis(a)
                b+=1
            elif(w.bytes[b] == 0x12):
                a = b''
                a = a + bytes([w.bytes[b]])
                a = a + bytes([w.bytes[b+1]])
                s += getjis(a)
                b+=1
            else:
                s += getlowjis(w.bytes[b])
            b +=1
        #print(s)
        w.text = s

## now write them as files 
outstr = "{\n\"words\":["
i = 0
while i < len(flist):
    j = 0
    #f = open(str(i)+"_"+hex(filelist[i]) + ".str", "wb")
    while j < len(flist[i]):
        del flist[i][j].bytes 
        flist[i][j].address = hex(flist[i][j].address)
        outstr += flist[i][j].toJSON()+",\n"
        #f.write(bytes(flist[i][j].decoded.encode("shiftjis")))
        j += 1
    #f.close()
    i += 1
outstr = outstr[:len(outstr)-2]
outstr += "\n]\n}"
print(outstr)