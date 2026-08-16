# reinsert2.py
import numpy,sys,os,json
from PIL import Image, ImageDraw

# 0x9f09a : このオランの街は
# アレクラスト大陸で最大の街さ。

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

print("Loading modified rom...", end="")
f = open("swsfc2-e.sfc", "rb")
rom = f.read()
f.close()
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
                    print("warning, test", s)
        elif s[i] == ord('\n'):
            s = s[:i] + b'\x04' + s[i+1:]
        i += 1
    return bytes(s).decode("sjis")
###

#print(U8ToSWSFC("Adventure On"))

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
print("Loaded tlbank 2...")



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
        if w['text'] == "{f}":
            newf.lines.append(TLWord(int(w['address'], 16), int(w['size']), U8ToSWSFC(w['text']), False))
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
ind = 0x50 #0x50 # 
i = 0
ct = 0
multi = 0
while i < len(all_cmb):
    all_cmb[i].index = ind 
    ct += 1
    ind += 1
    if(ind == 0xc0): # skip dakuten bc they dont space - actually skip all of c0
        ind += 0x10
    #if(ind == 0xc8): # for ! and ? in full width
    #    ind += 2
    if(ind > 0xff)and(ind < 0x1000):
        ind = 0x1000
    if(ind == 0x103c): # skip 103e and 103f TESTING BUGFIX?
        ind += 4
    if(all_cmb[i].count > 1):
        multi += 1
    #print(hex(all_cmb[i].index), all_cmb[i].txt) # shows the new combos 
    i += 1
# IF YOU SKIP INDEXES, YOU HAVE TO SKIP GRAPHIC INSERTION AS WELL

def BackToNative(_addr, _sz, s):
    c = 0
    o = []
    while c < len(s):
        f = False
        if s[c] >= 'A' and s[c] <= 'Z':
            o.append(ord(s[c]) - 0x11)
            f = True
        elif s[c] == '\n':
            o.append(4)
            f = True
        elif s[c] == '\x0f':
            o.append(0xf)
            f = True
        else:
            for b in all_cmb:
                if b.txt[0] == s[c]:
                    if b.txt[1] == s[c+1]:
                        if b.index < 0x100:
                            o.append(b.index)
                        else:
                            o.append((b.index & 0xff00) >> 8)
                            o.append(b.index & 0xff)
                        c += 1
                        f = True
                        break
        if not f:
            print("CANT FIND THIS COMBMO", s[c], s[c+1], c)
            c = 999
            os.exit()
            break
        c += 1
    if len(o) > _sz:
        print("FAIL AT SIZING!")
        os.exit()
    else:
        while len(o) < _sz:
            o.append(0x20)
        global rom 
        rom = rom[:_addr] + bytes(o) + rom[_addr+len(o):]
####

BackToNative(0x00012DB3, 3, "SLW")
BackToNative(0x00012DC3, 3, "SLW")
BackToNative(0x00012DD3, 3, "SLW")

BackToNative(0x00012DBD, 3, "FST")
BackToNative(0x00012DCD, 3, "FST")
BackToNative(0x00012DDD, 3, "FST")
#BackToNative(0x000128D2, 10, "Bright level ")
#BackToNative(0x000128E2, 18, "Window color ")
#BackToNative(0x000128FA, 14, "Sound output ")

BackToNative(0x000130A1, 14, "mark displayed")
BackToNative(0x000130B3, 14, "mark displayed")
BackToNative(0x000130C2, 21, "Burst mark is\ndisplayed ")
BackToNative(0x000130DB, 14, "mark displayed")
BackToNative(0x000130EA, 23, "Poison bottle\nicon displayed")
BackToNative(0x00013102, 26, "Horned demon icon\ndisplayed ")
BackToNative(0x0001311D, 21, "Sk ull icon is \ndisplayed ")

BackToNative(0x0001340B, 29, "Affects attack hit chance. \x0f")
BackToNative(0x00013429, 34, "Affects damage with\nattacks.\x0f")
BackToNative(0x0001344C, 33, "The lower this number, \nthe more critical hits. \x0f")
BackToNative(0x0001346E, 32, "Additional damage to \nattacks.\x0f")
BackToNative(0x0001348F, 31, "Makes it easier to \ndodge attacks.\x0f")
BackToNative(0x000134AF, 39, "The bigger this is, the\nfewer attacks you take. \x0f")
BackToNative(0x000134d7, 31, "Damage taken is reduced\nby this num.\x0f")
BackToNative(0x000134F7, 33, "Gained from quests.\nNeeded to raise skills.\x0f")
BackToNative(0x00013519, 44, "Manual dexterity.\nAffects accuracy and \ntrap removal. \x0f")
BackToNative(0x00013546, 35, "Physical speed.\nAffects order in combat. \x0f")
BackToNative(0x0001356A, 38, "Intelligence. Affects\nmagic pow and trap\ndisarming.\x0f")
BackToNative(0x00013591, 48, "Increases weight of\nequippable items and\ndamage dealt. \x0f")
BackToNative(0x000135C2, 33, "How much damage\nyour body can take. \x0f")
BackToNative(0x000135E4, 38, "Consumed when using\nmagic. Affects mag\nresist. \x0f")
BackToNative(0x0001360B, 41, "Resistance to ailments.\nHigher the better. \x0f")
BackToNative(0x00013635, 37, "Resistance to magic. \nHigher the better. \x0f")

BackToNative(0x13755, 38, "Average stats, but can \nlearn all skills. \x0f")
BackToNative(0x0001377E, 55, "Talented with magic, \nbut weak in body. Cannot \nlearn Priest.\x0f")
BackToNative(0x000137B6, 53, "Hardy in body and mind.\nCannot learn Sorcerer or\nShaman skills. \x0f")
BackToNative(0x000137EC, 47, "An agile, dextrous race. \nCannot learn skills\nthat use magic. \x0f")
BackToNative(0x0001381C, 48, "A race in between elves\nand humans. Skills they\nlearn depend on upbringing. \x0f")
BackToNative(0x000139BD, 38, "Can use equipment up to\nStr value. \nNo restrictions. \x0f")
BackToNative(0x000139E4, 48, "Good at opening doors\nand removing traps. \nCan't use heavy equip\x0f")
BackToNative(0x00013A15, 59, "Skill for the outdoors.\nUses thrown weapons, not \ngood with melee.\x0f")
BackToNative(0x00013A51, 44, "Skill for all encompassing \nknowledge of things.\nNo restrictions. \x0f")
BackToNative(0x00013A7E, 60, "Knowledgeable on all lands \nand music. Can use\nsongs with an instrument. \x0f")
BackToNative(0x00013ABB, 53, "Uses ancient magic. Needs a\nmage staff equipped to\ncast spells.\x0f")
BackToNative(0x00013AF1, 40, "Uses spirit magic. Needs\nat least one hand free\nto cast spells. \x0f")
BackToNative(0x00013B1A, 20, "Uses holy magic. \nNo restricts \x0f")
BackToNative(0x00013B2F, 43, "The prime goddess. Domains\nof order and justice. \nFights evil. \x0f")
BackToNative(0x00013B5B, 52, "God of battle. Approves of\njust combat, disavows \ncowardice and dishonesty. \x0f")
BackToNative(0x00013B90, 36, "God of knowledge.\nTeaches civilised living.\x0f")
BackToNative(0x00013BB5, 35, "God of commerce. \nDislikes taking\nadvantage of others.\x0f")
BackToNative(0x00013BD9, 34, "Mother goddess.\nPrefers humans in a\nnatural state.\x0f")

BackToNative(0x0001315D, 61, "Like on tabletop dice\nare rolled for characters \nin combat.\nTakes longer.\x0f")
BackToNative(0x0001319B, 36, "Results displayed in text. \nNormal speed.\x0f")
BackToNative(0x000131C0, 48, "Results are shown with \nnumbers and icons.\nFaster battles.\x0f")
BackToNative(0x000131F1, 38, "Check meanings of icons\nfrom action mode here.\x0f")
BackToNative(0x142a8, 110, "Dead \n\x0f KO\n\x0fStop \n\x0fStone\n\x0fFell \n\x0fSlp\n\x0fPoi\n\x0fConfu\n\x0fTerr \n\x0fFell \n\x0fMute \n\x0fBlind\n\x0fDeaf \n\x0fBersk\n\x0fSick \n\x0fCurse\n\x0f")
BackToNative(0x00013FD9, 4, "Mal")
BackToNative(0x00013FDe, 4, "Fem")
BackToNative(0x00013FEE, 3, "Hum")
#゛人間\fエルフ\fト゛ワーフ\fク゛ラスランナー\fハーフエルフ／人間\fハーフエルフ／エルフ\f\fレヘ゛ル
BackToNative(0x00013FEE, 50, "Hum\x0fElf\x0fDwarf\x0fGrassr \x0fHalf-Elf (H) \x0fHalf-Elf (E) \x0f\x0fLevel\x0f")



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
                # reduce ascii caps from 0x41 to 0x30
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
## I DONT THINK THIS WORKS
#for f in scr_files:
#    i = 0
#    while i < len(f.lines):
#        if f.lines[i].sjis == True:
#            nw = []
#            for w in f.lines[i].translation: 
#                for b in jdict:
#                    if (ord(w) == int(b[0], 16)):
#                        _b = bytes(b[1], encoding="sjis")
#                        nw.append(_b)
#                        break
#            f.lines[i].translation = []
#            for l in nw:
#                for b in l:
#                    f.lines[i].translation.append(b)
#        i += 1


# fix captials
addr = 0xB1180 # testing for sfc2 b1180 == 0x30 = A
i = 0
while i < len(output_caps):
    l = len(output_caps[i].bytes)
    rom = rom[:addr] + bytes(output_caps[i].bytes) + rom[addr+l:]
    addr += 0x30
    i += 1

print("Inserting charmap... ", end="")
addr = 0xb1480 # 0xb1480 = 0x50 , so 0xB1780 == 0x70, 0xB1A80 = 0x90, 0xB1D80 = 0xB0, 0xB1F00=0xC0
i = 0
while i < len(output_chr):
    l = len(output_chr[i].bytes)
    rom = rom[:addr] + bytes(output_chr[i].bytes) + rom[addr+l:]
    addr += 0x30
    if(addr == 0xb1f00): # NO - skip all Cx!!
        addr += 0x180 # skip c0 and c1 # 0x180 = skip 16 chars
    #if(addr == 0xb1fc0):
    #    addr += 0x30 # skip c8 and c9
    # 103e-f ?? 
    if(addr == 0xb2aa0):
        addr += 0x60
    i += 1

#print(hex(addr - 0xb1000),"of max",hex(0xb7000 - 0xb1000))
print("New charmap inserted.")

# TODO:
# Pointer table adjustment here, if possible!
print("Adjusting pointer tables...")
pt = 0
it = 0
for f in scr_files:
    #print(hex(f.table.loc))
    if len(f.table.ptrs) != 0: # skip file 0 
        if(len(f.table.ptrs) != len(f.lines)):
            #print("fail: not enough lines for", len(f.table.ptrs), len(f.lines))
            continue
        else:
            #print("adjusting",hex(f.table.loc))
            _p = 1
            if f.table.ptrs[0].val != len(f.table.ptrs)*2:
                print("error! pointer table doesnt make sense!")
            longest = f.table.ptrs[len(f.table.ptrs)-1].val
            while _p < len(f.lines):
                if f.lines[_p].sjis != True: # this is translated
                    s = f.lines[_p-1].translation.encode("raw_unicode_escape")
                    f.table.ptrs[_p].val = f.table.ptrs[_p-1].val + len(s)
                    #print("Updated pointer: ",hex(f.table.ptrs[_p].val))
                    if f.table.ptrs[_p].val > longest:
                        print("warning: final pointer is too far ahead!")
                    #else:
                        #if _p == len(f.table.ptrs) - 1:
                            
                _p += 1
            print("size remaining ", hex(f.table.ptrs[0].loc), longest - f.table.ptrs[len(f.table.ptrs)-1].val)
    #it += 1

for f in scr_files:
    if len(f.table.ptrs) > 0:
        if(len(f.table.ptrs) == len(f.lines))and(f.table.loc != 0x8244a): # skip intro block
            _p = 0
            pt += 1
            while _p < len(f.table.ptrs):
                st_add = f.table.loc 
                rom = rom[:st_add + (2*_p)] + bytes([(f.table.ptrs[_p].val & 0xff),((f.table.ptrs[_p].val & 0xff00) >> 8)]) + rom[st_add+2+(2*_p):]
                _p += 1
print(pt, "pointer tables updated.")

print("Writing new script...")
for f in scr_files:
    for word in f.lines:
        if len(f.table.ptrs) != len(f.lines):
            if word.sjis != True:
                s = word.translation.encode("raw_unicode_escape")
                if len(s) > word.len:
                    # only if we didnt use pointer math 
                    # and we want to skip the intro text, as it hard uses ptrs
                    print("too long! truncated ", len(s), word.len)
                    print(word.original)#, len(s), word.len)
                    print(hex(word.loc))
                    s = s[:word.len] # 
                        
                while len(s) < word.len:
                    s += b'\x20'
                rom = rom[:word.loc] + s + rom[word.loc+len(s):]
        #else: # if its an sjis conversion, leave it alone
        #    s = bytes(word.translation)
        #    while len(s) < word.len:
        #        s += b'\x81\x40'
        #        if len(s) > word.len:
        #            s = s[:len(s)-2] + b'\x0f'
        #    if len(s) > word.len:
        #        print("Too long! truncated")
        #        print(word.original, len(s), word.len)
        #        s = s[:s]
        #    rom = rom[:word.loc] + s + rom[word.loc+len(s):]
print("Writing updated ptr scripts...")
for f in scr_files:
    if len(f.table.ptrs) == len(f.lines):
        w = 0
        ploc = f.table.ptrs[0].val
        while w < len(f.lines):
            s = f.lines[w].translation.encode("raw_unicode_escape")
            rom = rom[:f.table.ptrs[0].loc + f.table.ptrs[w].val] + s + rom[f.table.ptrs[0].loc + f.table.ptrs[w].val + len(s):]
            w += 1
print(" OK.")

# now try the manual / sjis strings...
print("Inserting SJIS strings back-converted...")
ii = 0
for w in scr_files[0].lines:
    # back convert 
    _o = []
    #print(bytes(w.translation, encoding="utf-8"))
    _c = 0
    while _c < len(w.translation):
        to = ord(w.translation[_c])
        if to == 0x10:
            if _c == len(w.translation)-1:
                print(hex(w.loc), w.len, w.original)
            to = 0x1000 + ord(w.translation[_c+1])
            _c += 1
        if to == 0x11:
            if _c == len(w.translation)-1:
                print(hex(w.loc), w.len, w.original)
            to = 0x1100 + ord(w.translation[_c+1])
            _c += 1  
        if to == 0x12:
            if _c == len(w.translation)-1:
                print(hex(w.loc), w.len, w.original)
            to = 0x1200 + ord(w.translation[_c+1])
            _c += 1  
        if to == 0x13:
            if _c == len(w.translation)-1:
                print(hex(w.loc), w.len, w.original)
            to = 0x1300 + ord(w.translation[_c+1])
            _c += 1    
        for b in jdict:
            if int(b[0],16) == to: # which jp table entry are we?
                #print(b[0], b[1], hex(to))
                sj = b[1].encode("sjis")
                for s in sj:
                    _o.append(s)
                break
        _c += 1
    if len(_o) <= w.len:
        ob = bytes(_o)
        while len(ob) < w.len:
            ob = ob + b'\x81\x40'
        if len(ob) <= w.len:
            rom = rom[:w.loc] + ob + rom[w.loc+len(ob):]
            #print("inserted: ", w.translation)
            ii += 1
        else:
            print("offset pushed us over!", hex(w.loc)) 
    else:
        print("too big!", hex(w.loc), len(_o), w.len) 
####
print(ii, "sjis strings of", len(scr_files[0].lines),"inserted")



f = open("swsfc2-e_out.sfc", "wb")
f.write(rom)
f.close()
print("swsfc2-e_out.sfc written.")
