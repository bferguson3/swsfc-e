import os,sys,json

filelist = [
0x80c00, 
0x80e39,
0x80f40,
0x810f8,
0x81399,
0x81997,
0x81c49,
0x81ef3,
0x82090,
0x8244a,
0x82a66,
0x82fe6,
0x832e6,
0x837df,
0x844bf,
0x84cb1,
0x85265,
0x858d4,
0x86217,
0x86a0c,
0x86d1a,
0x872f4,

0x88000,
0x88863,
0x89660,
0x8a945,
0x8af53,
0x8b6bc,
0x8c27f,
0x8cb20,
0x8d055,
0x8dc2f,
0x8e3a6,
0x8eb81,
0x8f1d3,
0x8f85e,

0x90000,
0x90bad,
0x90d17,
0x90e55,
0x90fae,
0x91543,
0x917f8,
0x918a3,
0x92229,
0x92298,
0x9232f,
0x92a27,
0x92e96,
0x93547,
0x938be,
0x94405,
0x94957,
0x94d2b,
0x95065,
0x9529f,
0x9561e,
0x95ae3,
0x95e1d,
0x962b8,

0x98000,
0x9A165,
0x9A1FA,
0x9A284,
0x9A83B,
0x9AFB4,
0x9B053,
0x9B159,
0x9B1D0,
0x9B24B,
0x9B2CF,
0x9B34A,
0x9B3DA,
0x9B970,
0x9BD0B,
0x9CCE0,
0x9CEE6,
0x9d7ca,
0x9d920,
0x9dcc3,
0x9ded4,
0x9e12d,
0x9e3ce,
0x9e627,
0x9e879,
0x9e959,
0x9ea4e,
0x9ec29,
0x9ee21,
0x9ef5f,
0x9efd2,
0x9f03d,
0x9f1e4,
0x9f596,
0x9f808,
0x9f827,
0x9f860,
0x9f87f,
0x9f888,
0x9f927,
0x9f9b0,
0x9fa01,
0x9fa38,
0x9fa85,
0x9fd20,
0x9fe46,

0xA0000,
0xA01df,
0xA02f4,
0xA0328,
0xA03fe,
0xA04b1,
0xA05b0,
0xA06ac,
0xA09e0,
0xA0c9d,
0xA0cc7,
0xA0dd2,
0xA0e2c,
0xA0e87,
0xA0ee6,
0xA0f13,
0xA0f57,
0xA0f96,
0xA0fca,
0xA1024,
0xA1049,
0xA10DE,
0xA1453,
0xA1479,
0xA14B1,
0xA14E5,
0xA14FC,
0xA1504,
0xA16C6,
0xA1728,
0xA17A2,
0xA17B6,
0xA17DC,
0xA1804,
0xA1898,
0xA18BB,
0xA1901,
0xA1C2F,
0xA1C69,
0xA1D9C,
0xA1DBC,
0xA1DEF,
0xA1F87,
0xA2190,
0xA22CF,
0xA2355,
0xA2552,
0xA2571,
0xA2958,
0xA2B47,
0xA2B90,
0xA2F5A,
0xA32D0,
0xA383D,
0xA3DAA,
0xA42FA,
0xA436A,
0xA4416,
0xA44E5,
0xA45C1,
0xA4664,
0xA4692,
0xA46E7,
0xA475C,
0xA47AF,
0xA4813,
0xA483A,
0xA48AE,
0xA48EB,
0xA4963,
0xA4A5F,
0xA4B05,
0xA4B7B,
0xA4D01,
0xA4E59,
0xA4F46,
0xA4FF3,
0xA502A,
0xA512E,
0xA51DF,
0xA5258,
0xA5287,
0xA52B8,
0xA5304,
0xA53AC,
0xA545F,
0xA559D,
0xA55F2,
0xA59D4,
0xA5D90,
0xA6141,
0xA614E,
0xA61D1,
0xA6339,
0xA66D9,
0xA670F,
0xA6794,
0xA67EF,
0xA6868,
0xA69CA,
0xA6AD5,
0xA6C63,
0xA6F43,
0xA6FD7,
0xA720A,
0xA721D,
0xA72ED,
0xA7BC8,
0xA7CDB,
0xA7D00,
0xA7D20,
0xA7D66,
0xA7DA5,
0xA7DDF,
0xA7DF9,
0xA7E3D,
0xA7F67,

0xA8000,
0xA80BB,
0xA8183,
0xA81C8,
0xA82CA,
0xA8372,
0xA842E,
0xA8726,
0xA88D9,
0xA8A28,
0xA8F81,
0xA8FA7,
0xA901F,
0xA90B7,
0xA9105,
0xA9191,
0xA91CF,
0xA9246,
0xA92D8,
0xA9306,
0xA9413,
0xA9F03,
0xA9FE0,
0xAA069,
0xAA201,
0xAA24D,
0xAA5C1,
0xAA608,
0xAA66C,
0xAA7B1,
0xAA952,
0xAAB5E,
0xAACD8,
0xAB10E,
0xAB2CA,
0xAB3FD,
0xABAAD,
0xABAE3,
0xABB90,
0xABC6C,
0xABD7D,
0xABE3D,
0xAC122,
0xAC15B,
0xAC20B,
0xAC2BF,
0xAC474,
0xAC48C,
0xAC5FE,
0xAC6E2,
0xAC84A,
0xAC9DE,
0xACCAA,
0xACD46,
0xACDBA,
0xACDDB,
0xACE15,
0xACE4C,
0xAD050,
0xAD068,
0xAD083,
0xAD0A1,
0xAD0B5,
0xAD177,
0xAD5AA,
0xAD79E,
0xAD808,
0xAD9F3,
0xADBAA,
0xADCEA,
0xADD31,
0xADD56,
0xADD78,
0xADD9E,
0xADE86,
0xAE1E3,
0xAE22A,
0xAE78A,
0xAE84F,
0xAE91E,
0xAE926,
0xAEB7C,
0xAEC9D,
0xAECF6,
0xAEDC0,
0xAEE43,
0xAEF36,
0xAF37F,
0xAF3F1,
0xAF427,
0xAF6E3,
0xAF7D9,
0xAF98C,
0xAF9F5,
0xAFA57,
0xAFAA5,
0xAFAF7,
0xAFBAB,
0xAFBB6,
0xAFBC1,
0xAFBCB,
]

f = open("swsfc2-e.sfc", "rb")
rom = f.read()
f.close()


flist = []

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

# populate dictionary
jdict = []
f = open("swsfc2.tbl", "r")
line = f.readline()
i = 0
while line != "":
    l = line.split("=")
    l[1] = l[1].rstrip()
    if(l[0] == "20"):
        l[1] = "  "
    jdict.append([l[0], l[1]])
    line = f.readline()


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
        return "{f}" # 060fh is END 
    if m == 0x4:
        return "\n" # 04h is NEWLINE
    for p in jdict:
        #print(no, p[0])
        if(p[0] == no):
            #print("found", p[1])
            return p[1]
            break
    return "{"+hex(m)[2:]+"}"

# 
# 0F endline
# 1B end file 

i = 0
while i < len(filelist):
    if (rom[filelist[i]-1] != 0x1b)and(filelist[i]!=0x80c00)and(filelist[i]!=0x88000)and(filelist[i]!=0x90000)and(filelist[i]!=0x98000)and(filelist[i]!=0xa0000)and(filelist[i]!=0xa8000):
        print("did not dump: ", hex(filelist[i]), hex(rom[filelist[i]]))
        i += 1
        file=[]
        flist.append(file)
        continue
    else:
        # ok, we found the final byte
        bc = filelist[i]
        # first two bytes are offset from this location to str
        ofs = rom[bc + 1] << 8 | rom[bc]
        num = int(ofs/2)
        file=[]
        j = 0
        while j < num:
            sf = SWFile()
            _ofs = (rom[bc + 1] << 8) | rom[bc]
            sf.address = _ofs + filelist[i] 
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
            elif(w.bytes[b] == 0x13):
                a = b''
                a = a + bytes([w.bytes[b]])
                a = a + bytes([w.bytes[b+1]])
                s += getjis(a)
                b+=1
            else:
                s += getlowjis(w.bytes[b])
            b +=1
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