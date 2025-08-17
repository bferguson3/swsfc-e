# reinsert2.py
import numpy,sys,os,json
from PIL import Image, ImageDraw

#NOTE : 04h is newline
# get the dictionary 
print("Loading dictionary... ", end="")
jdict = []
f = open("swsfc2.tbl", "r", encoding="utf8")
line = f.readline()
i = 0
while line != "":
    l = line.split("=")
    l[1] = l[1].rstrip()
    if(l[0] == "20"):
        l[1] = "  " # replace single space with double half
    jdict.append([l[0], l[1]])
    line = f.readline()
print(" OK.")


class TLWord():
    def __init__(self, _loc, _len, _tl, buff=True, sjis=False, filenum=0):
        self.loc = _loc 
        self.len = _len 
        self.original = []
        self.translation = _tl
        self.sjis = sjis
        self.filenum = filenum
    ###
###
print("Populating translations... ", end="")

words = []

##

def U8ToSWSFC(s):
    s = s.encode("sjis")
    i = 0
    while i < len(s):
        if s[i] == ord('{'):
            if i < len(s) - 2:
                if(s[i+2] == ord('}')):
                    n = int(chr(s[i+1]), 16)
                    s = s[:i] + bytes([n]) + s[i+3:]
                    i -= 1 # to pretend like the byte was always there
                elif(s[i+3] == ord('}')):
                    c = chr(s[i+1]) + chr(s[i+2])
                    n = int(c, 16)
                    s = s[:i] + bytes([n]) + s[i+4:]
                    i -= 1 # testing
                    print("error")
        elif s[i] == ord('\n'):
            s = s[:i] + b'\x04' + s[i+1:]
        i += 1
    return bytes(s).decode("sjis")
###


class Ptr():
    def __init__(self, loc=0, val=0):
        self.loc = loc # physical address of ptr
        self.val = val # value of ptr (2 bytes)
    ###
###
class PtrTable():
    def __init__(self, loc=0, ptrs=[]):
        self.loc = loc   # physical address of table start
        self.ptrs = ptrs # array of Ptr()
    ###
###
class ScrFile():
    def __init__(self, table=PtrTable()):
        self.table = table  # PtrTable()
        self.lines = []     # array of TlWord()s
    ###
###

scr_files = []

import tlbank2 

_tf = ScrFile(table=PtrTable(loc=0, ptrs=[]))
_tf.lines = tlbank2.words 
scr_files.append(_tf)

# now load in the json file 
print("Loading script from JSON...", end="")
f = open("swsfc2_dump.json", "r", encoding="utf8")
js = f.read()
f.close()
js = json.loads(js)

for f in js:
    newf = ScrFile(table=PtrTable(loc=0, ptrs=[]))
    newf.table.ptrs = []
    newf.table.loc = int(f, 16)
    for w in js[f]:
        newf.table.ptrs.append(Ptr(loc=int(w['ptr_loc'],16), val=int(w['ptr_val'],16)))
        if w['translation'] != '':
            newf.lines.append(TLWord(int(w['address'], 16), int(w['size']), U8ToSWSFC(w['translation']), False))
    scr_files.append(newf)


print(" OK.")

# convert char table to Image object list
print("Creating character map... ", end="")
img = Image.open("8x16romaji.png")
roma_img = []
h = 0
while h < 0x20:
    roma_img.append([])
    h += 1
h = 0
while h < img.size[1]:
    w = 0 
    while w < img.size[0]:
        char = Image.new("RGB", (6, 16))
        y = 0
        while y < 16:
            x = 0
            while x < 6:
                char.putpixel((x,y), img.getpixel((w+x,h+y)))
                x += 1
            y += 1
        roma_img.append(char)
        w += 6
    h += 16
print(" OK.")

# scan the input script and later organize by priority
# combine any non-capitals

def findincmb(c):
    for a in all_cmb:
        if c == a.txt:
            a.count += 1
            return True
    return False

all_cmb = []

class Combo():
    def __init__(self, st):
        self.img=None
        self.txt=st
        self.index=0
        self.count = 1
        self.makeImg()
    ###
    def makeImg(self):
        im = Image.new("RGB",(12,16))
        a = roma_img[ord(self.txt[0])]
        b = roma_img[ord(self.txt[1])]
        y = 0
        while y < 16:
            x = 0
            while x < 6:
                im.putpixel((x,y),a.getpixel((x,y)))
                x += 1
            x = 0
            while x < 6:
                im.putpixel((x+6,y),b.getpixel((x,y)))
                x += 1
            y += 1
        self.img = im
        #
###

capsletters = []
i = 0
while i < 26:
    capsletters.append(Combo(" " + chr(0x41 + i)))
    i += 1

# sort all_cmb here!!!
all_cmb.sort(key=lambda x: x.count, reverse=True)

print("Creating combination chars... ", end="")
# if its lowercase, make it a combination!
for f in scr_files:
    for word in f.lines:
        i = 0
        while i < len(word.translation)-1:
            if word.translation[i] >= 'A':
                if word.translation[i] <= 'Z':
                    i += 1
                    continue 
            if(word.translation[i] >= ' ') and (word.translation[i+1] >= ' '):
                if(i == len(word.translation)-1):
                    s = word.translation[i] + ' '
                else:
                    s = word.translation[i]
                    s += word.translation[i+1]
                i += 1
                if(findincmb(s)==False):
                    #print(word.translation)
                    c = Combo(s)
                    all_cmb.append(c)                
            i += 1

# sort all_cmb here!!!
all_cmb.sort(key=lambda x: x.count, reverse=True)

# set indexes
ind = 0x50
i = 0
ct = 0
multi = 0
while i < len(all_cmb):
    all_cmb[i].index = ind 
    ct += 1
    ind += 1
    if(ind > 0xff)and(ind < 0x1000):
        ind = 0x1000
    if(all_cmb[i].count > 1):
        multi += 1
    #print(hex(all_cmb[i].index))
    i += 1
print(" OK.\nMax index: ", hex(ind), "of",ct,"(max 1026)/ duplicated",multi,"combinations")

# convert all combinations to tile data format 
# interleave every two!
output_chr=[] # IMAGES ONLY 
class OutputImg():
    def __init__(self):
        self.bytes = None
        self.index = 0
    ###
###
print("Creating image set... ", end="")
i = 0
while i < len(all_cmb):
    _img = OutputImg()
    char = []
    h = 0
    while h < all_cmb[i].img.size[1]:
        b = ''
        w = 0
        while w < all_cmb[i].img.size[0]:
            if(all_cmb[i].img.getpixel((w,h)) == (0,0,0)):
                b+='1'
            else:
                b+='0'
            if(len(b)==8):
                char.append(int(b,2))
                b = '' 
            w += 1
        # b is half done
        if(i == len(all_cmb)-1):
            w = 0
            while w < 12:
                b += '0'
                if(len(b)==8):
                    char.append(int(b,2))
                    b = ''
                w += 1
        else:
            w = 0
            while w < all_cmb[i+1].img.size[0]:
                if(all_cmb[i+1].img.getpixel((w,h)) == (0,0,0)):
                    b+='1'
                else:
                    b+='0'
                if(len(b)==8):
                    char.append(int(b,2))
                    b = '' 
                w += 1
        if(len(b) > 0):
            print("bit length:",len(b))
            b=''
            char.append(int(b,2))
        h += 1
    _img.bytes = char
    output_chr.append(_img)
    i += 2
lenofimg = 0
for k in output_chr:
    lenofimg += len(k.bytes)
print(len(output_chr),"images created OK.")
output_caps = []
i = 0
while i < len(capsletters):
    _img = OutputImg()
    char = []
    h = 0
    while h < capsletters[i].img.size[1]:
        b = ''
        w = 0
        while w < capsletters[i].img.size[0]:
            if(capsletters[i].img.getpixel((w,h)) == (0,0,0)):
                b+='1'
            else:
                b+='0'
            if(len(b)==8):
                char.append(int(b,2))
                b = '' 
            w += 1
        # b is half done
        if(i == len(capsletters)-1):
            w = 0
            while w < 12:
                b += '0'
                if(len(b)==8):
                    char.append(int(b,2))
                    b = ''
                w += 1
        else:
            w = 0
            while w < capsletters[i+1].img.size[0]:
                if(capsletters[i+1].img.getpixel((w,h)) == (0,0,0)):
                    b+='1'
                else:
                    b+='0'
                if(len(b)==8):
                    char.append(int(b,2))
                    b = '' 
                w += 1
        if(len(b) > 0):
            print("bit length:",len(b))
            b=''
            char.append(int(b,2))
        h += 1
    _img.bytes = char
    output_caps.append(_img)
    i += 2

def getcmb(s):
    for p in all_cmb:
        if s == p.txt:
            return p.index
    return -1

# now replace the texts in every tlword
print("Converting / compressing to SFC format... ", end="")
for f in scr_files:
    for word in f.lines:
        i = 0
        word.original = word.translation
        newword = ''
        while i < len(word.translation)-1:
            if(word.translation[i] >= 'A') and (word.translation[i] <= 'Z'):
                word.translation = word.translation[:i] + chr(ord(word.translation[i]) - 0x11) + word.translation[i+1:]
                i += 1
                continue
            if(word.translation[i] >= ' ') and (word.translation[i+1] >= ' '):
                if(i == len(word.translation)-1):
                    s = word.translation[i]+' '
                else:
                    s = word.translation[i]+word.translation[i+1]
                j = 0
                found = False
                while j < len(all_cmb):
                    if all_cmb[j].txt == s: 
                        #print(s)
                        if all_cmb[j].index < 0x100:
                            word.translation = word.translation[:i] + chr(all_cmb[j].index) + word.translation[i+2:]
                        else:
                            word.translation = word.translation[:i] + chr((all_cmb[j].index & 0xff00) >> 8) + chr((all_cmb[j].index & 0xff)) + word.translation[i+2:]
                            i += 1
                        #print(bytes(word.translation.encode("raw_unicode_escape")))
                        break
                    j += 1
            i += 1
print("OK.")

# replace sjis version strings with their equivalent
for f in scr_files:
    i = 0
    while i < len(f.lines):
        if f.lines[i].sjis == True:
            nw = []
            for w in f.lines[i].translation: 
                for b in jdict:
                    if (ord(w) == int(b[0], 16)):
                        _b = bytes(b[1], encoding="sjis")
                        nw.append(_b)
                        break
            f.lines[i].translation = []
            for l in nw:
                for b in l:
                    f.lines[i].translation.append(b)
        i += 1

print("Loading rom...", end="")
f = open("swsfc2-e.sfc", "rb")
rom = f.read()
f.close()
print(" OK.")

# fix captials
addr = 0xB1180 # testing for sfc2
i = 0
while i < len(output_caps):
    l = len(output_caps[i].bytes)
    rom = rom[:addr] + bytes(output_caps[i].bytes) + rom[addr+l:]
    addr += 0x30
    i += 1

print("Inserting charmap... ", end="")
addr = 0xb1480 
i = 0
while i < len(output_chr):
    l = len(output_chr[i].bytes)
    rom = rom[:addr] + bytes(output_chr[i].bytes) + rom[addr+l:]
    addr += 0x30
    i += 1

#print(hex(addr - 0xb1000),"of max",hex(0xb7000 - 0xb1000))
print("New charmap inserted.")

# TODO:
# Pointer table adjustment here, if possible!

print("Writing new script...", end="")
for f in scr_files:
    for word in f.lines:
        if word.sjis != True:
            s = word.translation.encode("raw_unicode_escape")
            if len(s) > word.len:
                print("too long! truncated")
                print(word.original, len(s), word.len)
                s = s[:s]
            while len(s) < word.len:
                s += b'\x20'
            rom = rom[:word.loc] + s + rom[word.loc+word.len:]
        else: # if its an sjis conversion, leave it alone
            s = bytes(word.translation)
            while len(s) < word.len:
                s += b'\x81\x40'
                if len(s) > word.len:
                    s = s[:len(s)-2] + b'\x0f'
            if len(s) > word.len:
                print("Too long! truncated")
                print(word.original, len(s), word.len)
                s = s[:s]
            rom = rom[:word.loc] + s + rom[word.loc+word.len:]
print(" OK.")


f = open("swsfc2-e_out.sfc", "wb")
f.write(rom)
f.close()
print("swsfc2-e_out.sfc written.")
