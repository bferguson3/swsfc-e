#caps are 30h to 49h

#50-bf and
#d0-ff to be filled with most common

#$2992B
#名前を入力してください < 16 bytes
#E.nt.er. y.ou.r .na.me.: < 9 bytes 

import numpy,sys,os 
from PIL import Image, ImageDraw

# get the dictionary 
print("Loading dictionary... ", end="")
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
print(" OK.")

class TLWord():
    def __init__(self):
        self.loc = 0
        self.len = 0
        self.original = []
        self.translation = []
        #self.count = 1

    def __init__(self, _loc, _len, _tl):
        self.loc = _loc 
        self.len = _len 
        self.original = []
        self.translation = _tl
        #self.count = 1
        if (len(self.translation))%2!=0:
            self.translation+=" "
    ###
###


# test 
print("Populating translations... ", end="")
words=[]
words.append(TLWord(0x1bd79, 1, "Wa"))
words.append(TLWord(0x1b1e0, 2, "Enmy"))
words.append(TLWord(0x5f07c, 29, "Oran is the largest city \x01on all of Alecrast."))
words.append(TLWord(0x2993b, 16, "Choose a race:"))
words.append(TLWord(0x15932, 10, "Adventure on"))
words.append(TLWord(0x159f1, 10, "Adventure on"))
words.append(TLWord(0x1593f, 10, "New character"))
words.append(TLWord(0x1594a, 13, "Erase adventure"))
words.append(TLWord(0x1595a, 14, "Copy adventure"))
words.append(TLWord(0x16439, 14, "Copy adventure"))
words.append(TLWord(0x15afb, 10, "New character"))
words.append(TLWord(0x16420, 10, "New character"))
words.append(TLWord(0x1642b, 13, "Erase adventure"))
words.append(TLWord(0x15d38, 17, "Erase save?     Yes   No"))
words.append(TLWord(0x15d4a, 13, "Erase adventure"))

words.append(TLWord(0x165d0, 7, "Empty"))
words.append(TLWord(0x2994e, 3, "Hum."))
words.append(TLWord(0x29950, 3, "Elf   "))
words.append(TLWord(0x29954, 6, "Dwarf"))
words.append(TLWord(0x29958, 8, "Grassrunner"))
words.append(TLWord(0x29965, 13, "Half Elf   -    Human"))
words.append(TLWord(0x29973, 7, "Elven"))

words.append(TLWord(0x299b4, 7, "MaleFem"))

words.append(TLWord(0x299ca, 18, "Is this OK?         Yes     No"))

words.append(TLWord(0x299e7, 4, " Birth"))
words.append(TLWord(0x299eb, 6, " Exp."))
words.append(TLWord(0x299f0, 6, "Gamel"))


words.append(TLWord(0x29a46, 15, "Raise which skills?"))
words.append(TLWord(0xb52f, 6, "Exp. "))
words.append(TLWord(0x29cc6, 4, "Wildling"))
words.append(TLWord(0x29cef, 7, "Civilian"))
words.append(TLWord(0x29cce, 7, "Magician"))
words.append(TLWord(0x29cd9, 4, "Thug"))
words.append(TLWord(0x29d06, 4, "Merc."))
words.append(TLWord(0x29a34, 17, "Choose a deity :"))
words.append(TLWord(0x29a56, 18, "Is this OK?          Yes    No"))

words.append(TLWord(0x8cbc, 11, "Item        Status"))
words.append(TLWord(0x8cc8, 12, "Magic       System"))
words.append(TLWord(0x8cd5, 16, "Equipment   Options"))


words.append(TLWord(0x16415, 10, "Adventure on"))
words.append(TLWord(0x1f10d, 12, "Who will search?"))
words.append(TLWord(0x1f11a, 10, " cannot search."))
words.append(TLWord(0x1ef96, 24, "There's nothing there.\x0f"))
words.append(TLWord(0x19f06, 21,  "No spellsongs for outside \x01battle"))
words.append(TLWord(0x19c5e, 8,  "Spirit Mgc"))
words.append(TLWord(0x19c53, 10, "Ancient Mg"))
words.append(TLWord(0x19c67, 8,  "Holy Magic"))
words.append(TLWord(0x19c70, 4,  "Spellsng"))
words.append(TLWord(0x19dd8, 15,  "Not wielding a staff!"))
words.append(TLWord(0x19ef1, 15,  "Need an instrument!"))

words.append(TLWord(0x2992b, 16, "Enter your name:\x03\x03\x4d\x03"))
words.append(TLWord(0x1b1d0, 4, "Tgt:"))

words.append(TLWord(0x678a, 3,  "Elf"))
words.append(TLWord(0x6786, 3,  "Hum"))
words.append(TLWord(0x678e, 5,  "Dwarf"))
words.append(TLWord(0x6794, 8,  "Grassrunner"))
words.append(TLWord(0x6771, 4, "Male"))#\x0fFem"))
words.append(TLWord(0x6776, 3, "Fem"))
words.append(TLWord(0x67a8, 10, "Half-Elf (Elven)")) # 10 spaces
words.append(TLWord(0x679d, 10, "Half-Elf (Human)")) # 10 spaces
words.append(TLWord(0x67b3, 4, "Level")) # 10 spaces
words.append(TLWord(0x299a1, 16, "Choose a gender:"))
words.append(TLWord(0x15ea8, 16, "No save data!"))
words.append(TLWord(0x159e0, 16, "No save data!"))
words.append(TLWord(0x1601b, 14, "Copy adventure"))
words.append(TLWord(0x15ff8, 17, "Select destination"))
words.append(TLWord(0x1600a, 16, "Data already exists."))
words.append(TLWord(0x15aea, 16, "Data already exists."))

#bard:
words.append(TLWord(0x1a1b8, 26, "Awaken bravery, \x01improving strength"))
words.append(TLWord(0x1a1d3, 27, "Weakens will, \x01lowering attack power"))
words.append(TLWord(0x15e19, 38, "Also erase cleared \x01scenario data?\x02\x02\x02Yes      No "))
words.append(TLWord(0x1abfd, 25, "Checks active spirits \x01in the area."))
# 1a667 : ancient magic descriptions
# 1aa9c : spirit magic descs
# 1ae70 : holy magic descs 
words.append(TLWord(0x1ae6e, 6, "Heals."))


words.append(TLWord(0x1b1d6, 4, "Self"))
words.append(TLWord(0x1b1db, 4, "Ally"))
words.append(TLWord(0x1b1e3, 6, "Any"))
words.append(TLWord(0x1b1ea, 4, "Other"))
words.append(TLWord(0x153b7, 41, "Save game   Formatn.Message history \x01Toss item "))
words.append(TLWord(0xec2c, 14, "Save the game?"))
words.append(TLWord(0xedaa, 13, "Game saved."))
words.append(TLWord(0xedf6, 17, "Couldn't save data!"))
words.append(TLWord(0x1bd55, 11, " \x01spirits are here."))
words.append(TLWord(0x1bd75, 3, "Ea"))
words.append(TLWord(0x1bd7b, 2, "Fi"))
words.append(TLWord(0x1bd95, 4, "other"))


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
#print(roma_img[ord('a')].show()) # 0x61

# scan the input script and later organize by priority
# combine any non-capitals

def findincmb(c):
    for a in all_cmb:
        if c == a.txt:
            #print(c, a.txt)
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

# sort all_cmb here!!!
all_cmb.sort(key=lambda x: x.count, reverse=True)

print("Creating combination chars... ", end="")
# if its lowercase, make it a combination!

for word in words:
    i = 0
    while i < len(word.translation)-1:
        #if (word.translation[i] < 'a'):
        #    i += 1
        #    continue 
        #else:
        if(word.translation[i] >= ' ') and (word.translation[i+1] >= ' '):
            if(i == len(word.translation)-1):
                s = word.translation[i] + ' '
            else:
                s = word.translation[i]
                s += word.translation[i+1]
            i += 1
            if(findincmb(s)==False):
                c = Combo(s)
                all_cmb.append(c)
        i += 1

ind = 0x50
# sort all_cmb here!!!
all_cmb.sort(key=lambda x: x.count, reverse=True)
i = 0
multi = 0
while i < len(all_cmb):
    all_cmb[i].index = ind 
    ind += 1
    if(ind > 0xff)and(ind < 0x1000):
        ind = 0x1000
    if(all_cmb[i].count > 1):
        multi += 1
    i += 1
print(" OK.\nMax index: ", hex(ind), "/ duplicated",multi,"combinations")

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
    #print(all_cmb[i].txt, hex(all_cmb[i].index), all_cmb[i].count)
    #if(i != len(all_cmb)-1):
    #    print(all_cmb[i+1].txt, hex(all_cmb[i+1].index), all_cmb[i].count)
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
print(len(output_chr),"images created OK (~850 max).")

def getcmb(s):
    for p in all_cmb:
        if s == p.txt:
            return p.index
    return -1

# now replace the texts in every tlword
print("Replacing / compressing text ... ", end="")
for word in words:
    i = 0
    while i < len(word.translation)-1:
        #if (word.translation[i] >= 'A') and (word.translation[i] <= 'Z'):
        #    word.translation = word.translation[:i] + chr(ord(word.translation[i]) - 0x11) + word.translation[i+1:]
        #elif(word.translation[i] >= 'a'):
        if(word.translation[i] >= ' ') and (word.translation[i+1] >= ' '):
            if(i == len(word.translation)-1):
                s = word.translation[i]+' '
            else:
                s = word.translation[i]+word.translation[i+1]
            j = 0
            while j < len(all_cmb):
                if all_cmb[j].txt == s: 
                    if all_cmb[j].index < 0x100:
                        word.translation = word.translation[:i] + chr(all_cmb[j].index) + word.translation[i+2:]
                    else:
                        word.translation = word.translation[:i] + chr((all_cmb[j].index & 0xff00) >> 8) + chr((all_cmb[j].index & 0xff)) + word.translation[i+2:]
                    #print(word.translation)
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
#print(len(rom)) # < 2x check
print("New charmap inserted.")

print("Writing new script...", end="")
#print(len(rom))
for word in words:
    s = word.translation.encode("raw_unicode_escape")
    if len(s) > word.len:
        print("too long! truncated")
        print(s, len(s), word.len)
        s = s[:s]
    while len(s) < word.len:
        s += b'\x20'
    rom = rom[:word.loc] + s + rom[word.loc+word.len:]
print(" OK.")
#print(len(rom))

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
#print(len(rom))
rom = rom[:0xf8000] + by + rom[0xf8000 + sz:]
#print(len(rom))
print(" OK.")


f = open("swsfc-e_out.sfc", "wb")
f.write(rom)
f.close()
print("swsfc-e_out.sfc written.")