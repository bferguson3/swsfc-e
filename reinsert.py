import numpy,sys,os,json
from PIL import Image, ImageDraw

#NOTE : 01h is newline

# get the dictionary 
print("Loading dictionary... ", end="")
jdict = []
f = open("swsfc.tbl", "r", encoding="utf8")
line = f.readline()
i = 0
while line != "":
    l = line.split("=")
    l[1] = l[1].rstrip()
    if(l[0] == "20"):
        l[1] = "  "
    jdict.append([l[0], l[1]])
    line = f.readline()
print(" OK.")

class TLWord():
    def __init__(self, _loc, _len, _tl, buff=True):
        self.loc = _loc 
        self.len = _len 
        self.original = []
        self.translation = _tl
        #self.count = 1
        #if(buff == True):
        #    if (len(self.translation)) % 2 != 0:
        #        self.translation += " "
    ###
###

# test 
print("Populating translations... ", end="")

words = []

##

def U8ToSWSFC(s):
    s = s.encode("sjis") # TODO FIXME: change from SJIS to actual TBL 
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
            s = s[:i] + b'\x01' + s[i+1:]
        i += 1
    return bytes(s).decode("sjis")
###

import tlbank 
words = tlbank.words 

# now load in the json file 
print("Loading script from JSON...", end="")
f = open("swsfc_dump.json", "r", encoding="utf8")
js = f.read()
f.close()
js = json.loads(js)
ct = 0
for w in js['words']:
    if(w['translation'] != ''):             # if we have a translation to insert,
        ct += 1
        s = U8ToSWSFC(w['translation'])         # convert it to SWSFC format,
        words.append(TLWord(int(w['address'], 16),  # and make a TLWord
                    int(w['size']), 
                    s, 
                    False)) 
    ###
print("(" + str(ct) + ")", end="")
##



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

for word in words:
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

ind = 0x50
# sort all_cmb here!!!
all_cmb.sort(key=lambda x: x.count, reverse=True)
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
    i += 1
print(" OK.\nMax index: ", hex(ind), "of",ct,"(max 960)/ duplicated",multi,"combinations")

# convert all combinations to tile data format 
# interleave every two!
output_chr=[] # IMAGES ONLY 
class OutputImg():
    def __init__(self):
        self.bytes = None
        self.index = 0
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
print("Converting / compressing",str(len(words)) + "(" + str("{:.2f}".format(len(words)/35.35)) + "%) lines to SFC format... ", end="")
for word in words:
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

# start at 0x50 * 0x30 = 0xF00 + FA000
#名前を入力してください
#E nter  your  name :
print("Loading rom...", end="")
f = open("swsfc-e.sfc", "rb")
rom = f.read()
f.close()
print(" OK.")

# fix captials
# start at 0x30-0x20 + 0x18 = 180h = FA180h
addr = 0xFA180
i = 0
while i < len(output_caps):
    l = len(output_caps[i].bytes)
    rom = rom[:addr] + bytes(output_caps[i].bytes) + rom[addr+l:]
    addr += 0x30
    i += 1
    
# starting at 0xFA800 for 0x50, start inserting the new charmap.
print("Inserting charmap... ", end="")
addr = 0xFA480 # 0xFA000 + 0x30 per 2 chars * (0x50 - 0x20)
# 18h x 30h = 480h
i = 0
#print(len(rom))
while i < len(output_chr):
    l = len(output_chr[i].bytes)
    rom = rom[:addr] + bytes(output_chr[i].bytes) + rom[addr+l:]
    addr += 0x30
    i += 1

print(hex(addr - 0xfa000),"of max",hex(0x100000 - 0xfa000))
print("New charmap inserted.")

print("Writing new script...", end="")
for word in words:
    s = word.translation.encode("raw_unicode_escape")
    if len(s) > word.len:
        print("too long! truncated")
        print(word.original, len(s), word.len)
        s = s[:s]
    while len(s) < word.len:
        s += b'\x20'
    rom = rom[:word.loc] + s + rom[word.loc+word.len:]
print(" OK.")

# finally, replace the character map
print("Writing new tile bitmap...", end="")
# load in as pillow images 
tileimg = Image.open("f8000bank.png")
tiles = []
h = 0
while h < tileimg.size[1]:
    w = 0
    while w < tileimg.size[0]:
        _i = Image.new("RGB", (8,8), (0, 0, 0))
        y = 0
        while y < 8:
            x = 0
            while x < 8:
                _i.putpixel((x, y), tileimg.getpixel((w+x, h+y)))
                x += 1
            y += 1
        tiles.append(_i)
        w += 8
    h += 8
# convert to byte array 
by = []
i = 0
while i < len(tiles):
    y = 0
    while y < tiles[i].size[1]:
        _bh = ''
        _bl = ''
        x = 0
        while x < tiles[i].size[0]:
            # HHHHHHHH LLLLLLLL
            # 0,0,0       : 00
            # 102,102,102 : 10
            # 187,187,187 : 01
            # 255,255,255 : 11 
            if(tiles[i].getpixel((x, y)) == (255, 255, 255)):
                _bh += '1'
                _bl += '1'
            elif(tiles[i].getpixel((x, y)) == (187, 187, 187)):
                _bh += '0'
                _bl += '1'
            elif(tiles[i].getpixel((x, y)) == (102, 102, 102)):
                _bh += '1'
                _bl += '0'
            else:
                _bh += '0'
                _bl += '0'
            x += 1
        by.append(_bh)
        by.append(_bl)
        _b = ''
        y += 1
    i += 1
nby=[]
for b in by:
    b = int(b, 2)
    nby.append(b)
by = bytes(nby)
# insert at F8000
sz = len(by)
rom = rom[:0xf8000] + by + rom[0xf8000 + sz:]
print(" OK.")

f = open("swsfc-e_out.sfc", "wb")
f.write(rom)
f.close()
print("swsfc-e_out.sfc written.")