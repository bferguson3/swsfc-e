import numpy,sys,os,json
from PIL import Image, ImageDraw

#NOTE : 01h is newline

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

# now load in the json file 
print("Loading script from JSON...", end="")
f = open("swsfc_dump.json", "r")
js = f.read()
f.close()
js = json.loads(js)
for w in js['words']:
    if(w['translation'] != ''):             # if we have a translation to insert,
        s = U8ToSWSFC(w['translation'])         # convert it to SWSFC format,
        words.append(TLWord(int(w['address'], 16),  # and make a TLWord
                    int(w['size']), 
                    s, 
                    False)) 
    ###
print("(" + str(len(words)) + ")", end="")
##

words.append(TLWord(0x299ca, 18, "Is this OK?        Y       N "))
words.append(TLWord(0x67a8, 10, "HfElf(El)")) # 10 spaces
words.append(TLWord(0x679d, 10, "HfElf(Hu)")) # 10 spaces
words.append(TLWord(0x8cbc, 11, "Item        Stats"))
words.append(TLWord(0x8cc8, 12, "Magic       System "))
words.append(TLWord(0x8cd5, 16, "Equipment   Options"))

words.append(TLWord(0x1b1e0, 2, "En "))

words.append(TLWord(0x5f07c, 29, "Oran is the largest city \x01on all of Alecrast."))
words.append(TLWord(0x2993b, 16, "Choose a race: "))
words.append(TLWord(0x15932, 10, "Adventure on "))
words.append(TLWord(0x159f1, 10, "Adventure on "))
words.append(TLWord(0x1593f, 10, "New character"))
words.append(TLWord(0x1594a, 13, "Erase adventure"))
words.append(TLWord(0x1595a, 14, "Copy adventure "))
words.append(TLWord(0x16439, 14, "Copy adventure "))
words.append(TLWord(0x15afb, 10, "New character"))
words.append(TLWord(0x16420, 10, "New character"))
words.append(TLWord(0x1642b, 13, "Erase adventure"))
words.append(TLWord(0x15d38, 17, "Erase save?    Yes  No "))
words.append(TLWord(0x15d4a, 13, "Erase adventure"))
words.append(TLWord(0x153b7, 41, "Save game  FormatnMessage history \x01Toss item "))

words.append(TLWord(0x165d0, 7, "Empty"))

words.append(TLWord(0x2994e, 3, "Hu  "))
words.append(TLWord(0x29950, 4, "Elf  "))
words.append(TLWord(0x29954, 5, "  Dwarf"))
words.append(TLWord(0x29959, 8, "  Grassrunner"))
words.append(TLWord(0x29965, 13, "HalfElf   (Hu)"))
words.append(TLWord(0x29973, 7, "   (El)"))

words.append(TLWord(0x299b4, 7, "MalFem"))

words.append(TLWord(0x19c70, 4,  "Song"))

words.append(TLWord(0x299e7, 4, " Born "))
words.append(TLWord(0x299eb, 6, "  Exp.   "))
words.append(TLWord(0x299f0, 6, "  Gam. "))

words.append(TLWord(0x29a46, 15, "Raise which skills?"))
words.append(TLWord(0xb52f, 6, "Exp. "))

words.append(TLWord(0x29cc6, 4, "Wild"))
words.append(TLWord(0x29cce, 7, "Magician "))
words.append(TLWord(0x29cd9, 4, "Thug "))
words.append(TLWord(0x29ce1, 3, "Tra "))
words.append(TLWord(0x29ce8, 3, "Hnt"))
words.append(TLWord(0x29cef, 7, "Civilian "))
words.append(TLWord(0x29cfa, 8, "Gentry "))
words.append(TLWord(0x29d06, 4, "Merc"))
words.append(TLWord(0x29d0e, 4, "Priest "))
words.append(TLWord(0x29d16, 5, "Tarot"))
words.append(TLWord(0x29d1f, 8, "Nobility "))

words.append(TLWord(0x29a34, 17, "Choose a deity:"))
words.append(TLWord(0x29a24, 15, "Select spellsongs:"))
words.append(TLWord(0x29a56, 18, "Is this OK?        Y       N "))

words.append(TLWord(0x16415, 10, "Adventure on "))
words.append(TLWord(0x1f10d, 12, "Who will search? "))
words.append(TLWord(0x1f11a, 10, " cannot search."))
words.append(TLWord(0x1ef96, 24, "There's nothing there.\x0f"))
words.append(TLWord(0x19f06, 21,  "No spellsongs for out of \x01btl"))
words.append(TLWord(0x19c5e, 8,  "Spirit Mgc"))
words.append(TLWord(0x19c53, 10, "Ancient M"))
words.append(TLWord(0x19c67, 8,  "Holy Magic"))
words.append(TLWord(0x19dd8, 15,  "Not wielding a staff!"))
words.append(TLWord(0x19ef1, 15,  "Need an instrument!"))

words.append(TLWord(0x2992b, 16, "Enter your name: "))
words.append(TLWord(0x1b1d0, 4, "Tgt"))

words.append(TLWord(0x678a, 3,  "Elf"))
words.append(TLWord(0x6786, 3,  "Hum"))
words.append(TLWord(0x678e, 5,  "Dwarf "))
words.append(TLWord(0x6794, 8,  "  Grassrunner"))
words.append(TLWord(0x6771, 4, "Male "))#\x0fFem"))
words.append(TLWord(0x6776, 3, "Fem"))
words.append(TLWord(0x67b3, 4, "Level")) # 10 spaces
words.append(TLWord(0x299a1, 16, "Choose a gender: "))
words.append(TLWord(0x15ea8, 16, "No save data!"))
words.append(TLWord(0x159e0, 16, "No save data!"))
words.append(TLWord(0x1601b, 14, "Copy adventure"))
words.append(TLWord(0x15ff8, 17, "Select destination "))
words.append(TLWord(0x1600a, 16, "Data already exists. "))
words.append(TLWord(0x15aea, 16, "Data already exists. "))
#bard:
words.append(TLWord(0x1a1b8, 26, "Awaken bravery, \x01improve strength"))
words.append(TLWord(0x1a1d3, 27, "Weakens will, \x01lowering attack power"))
words.append(TLWord(0x15e19, 38, "Also erase cleared \x01scenario data?\x02\x02\x02Yes      No "))
words.append(TLWord(0x1abfd, 25, "Checks active spirits \x01in the area."))
# 1a667 : ancient magic descriptions
# 1aa9c : spirit magic descs
# 1ae70 : holy magic descs 
words.append(TLWord(0x1ae6e, 6, "Heals."))

words.append(TLWord(0x1b1d6, 4, "Self "))
words.append(TLWord(0x1b1db, 4, "Ally "))
words.append(TLWord(0x1b1e3, 6, "Any"))
words.append(TLWord(0x1b1ea, 4, "Other"))
words.append(TLWord(0xec2c, 14, "Save the game? "))
words.append(TLWord(0xedaa, 13, "Game saved."))
words.append(TLWord(0xedf6, 17, "Couldn't save data!"))
words.append(TLWord(0x1bd55, 11, "\x01spirits are here"))
words.append(TLWord(0x1bd75, 3, "Ea"))
words.append(TLWord(0x1bd7b, 2, "F"))
words.append(TLWord(0x1bd95, 4, "other"))
words.append(TLWord(0xa975, 1, "s"))

words.append(TLWord(0x2ce3f, 7, "Leave Oran "))
words.append(TLWord(0x2ce83, 8, "Back to Oran "))

words.append(TLWord(0x2cab7, 3, "Oran "))
words.append(TLWord(0x2cabb, 4, "Pada "))
words.append(TLWord(0x2cac0, 4, "Kasv "))
words.append(TLWord(0x2cac5, 4, "Hope "))
words.append(TLWord(0x2caca, 5, "Namgor "))
words.append(TLWord(0x2cad0, 4, "Rex"))
words.append(TLWord(0x2cad5, 14, "Gate to Anc.Kg "))
words.append(TLWord(0x2cae4, 13, "Brilliant Home "))
words.append(TLWord(0x2caf2, 5, "Tower"))
words.append(TLWord(0x2caf8, 9, "Thief Guild"))
words.append(TLWord(0x2cb02, 8, "Pharis Tpl"))
words.append(TLWord(0x2cb0b, 8, "Marfa Tpl"))
words.append(TLWord(0x2cb14, 8, "Myrii Tpl"))
words.append(TLWord(0x2cb1d, 8, "Rahda Tpl"))
words.append(TLWord(0x2cb26, 9, "Cha-Za Tpl"))
words.append(TLWord(0x2cb30, 7, "Wpn Shop "))
words.append(TLWord(0x2cb38, 7, "Mir Shop "))
words.append(TLWord(0x2cb40, 2, "Pt "))
words.append(TLWord(0x2cb43, 10, "RuinsGuard Inn"))
words.append(TLWord(0x2cb4e, 14, "Uncovered Trsr. Inn"))
words.append(TLWord(0x2cb69, 8, "Duck Inn"))
words.append(TLWord(0x2cb72, 6, "Fire Inn"))
words.append(TLWord(0x2cb79, 5, "RvrInn"))
words.append(TLWord(0x2cb7f, 6, "Torga"))
words.append(TLWord(0x2cb86, 10, "Barracks"))
words.append(TLWord(0x2cb91, 7, "Korshi's"))
words.append(TLWord(0x2cb99, 9, "Coastal Cave"))
words.append(TLWord(0x2cb5d, 11, "Sorcerers Guild"))
words.append(TLWord(0x2cba3, 5, "Market"))
words.append(TLWord(0x2cba9, 9, "Cha-Za C"))
words.append(TLWord(0x2cbb3, 8, "Slum Bar"))
words.append(TLWord(0x2cbbc, 6, "Trade:"))
words.append(TLWord(0x2cbc3, 10, "Osborne Mns"))
words.append(TLWord(0x2cbce, 4, "Hwy"))
words.append(TLWord(0x2cbd3, 3, "Sl"))
words.append(TLWord(0x2cbd7, 6, "W.Tower"))
words.append(TLWord(0x2cbde, 10, "Border Ruins"))
words.append(TLWord(0x2cbe9, 6, "Ein's"))
words.append(TLWord(0x2cbf0, 4, "Sewer"))
words.append(TLWord(0x2cbf5, 8, "Mansion"))
words.append(TLWord(0x2cbfe, 5, "Hdout"))
words.append(TLWord(0x2cc04, 10, "Garud's Estate"))

words.append(TLWord(0xd802, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xd855, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xdc29, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xdc89, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xdcd0, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xdd17, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xdd9f, 17, "Welcome. \x01How can I help?"))
words.append(TLWord(0xddde, 17, "Welcome. \x01How can I help?"))

words.append(TLWord(0xaa38, 24, "Find  Work \x01Rest \x01Level Up "))
words.append(TLWord(0xaac8, 48, "First gather some allies. \x01I can't give work to less \x01than 5 companions."))
words.append(TLWord(0xab3d, 14, "No work for now. "))
words.append(TLWord(0xa806, 9, "Rest? "))
words.append(TLWord(0xa810, 10, "Another night?"))
words.append(TLWord(0xa942, 8, "'s HP \x0f"))
words.append(TLWord(0xa95d, 11, " fully healed."))
words.append(TLWord(0xa94b, 7, " MP \x0f'"))
words.append(TLWord(0xa953, 8, "pts healed."))
words.append(TLWord(0xa96a, 9, " not healed."))

words.append(TLWord(0x18276, 23, "Both    Right   Left    Body    Other"))
words.append(TLWord(0x18455, 23, "Both    Right   Left    Body    Other"))
words.append(TLWord(0x1bd79, 1, " "))

words.append(TLWord(0xadbc, 17, "Who will level up?\x0f"))
words.append(TLWord(0xaedf, 25, "Level up skill\x01Raise ability score "))
words.append(TLWord(0xb030, 19, "Level which skill?\x0f"))
words.append(TLWord(0xb405, 6, " Fgtr\x0f"))
words.append(TLWord(0xb40c, 4, " Thief"))
words.append(TLWord(0xb411, 7, " Ranger\x0f"))
words.append(TLWord(0xb419, 5, " Sage\x0f"))
words.append(TLWord(0xb41f, 6, " Bard\x0f"))
words.append(TLWord(0xb426, 6, " Sorcerer"))
words.append(TLWord(0xb42d, 6, " Shaman\x0f"))
words.append(TLWord(0xb434, 7, " Priest\x0f"))
words.append(TLWord(0xb43c, 19, " will level to\x01\x0f. Is this OK?"))
words.append(TLWord(0xb4ed, 12, "Skill is maxed."))
words.append(TLWord(0xb52d, 15, " not enough \x01experience"))
words.append(TLWord(0xb643, 15, "Raise which ability?"))
words.append(TLWord(0x8f59, 20, "Cant change formation alone."))
words.append(TLWord(0x8f4a, 12, "Swap who?"))
# 95a0 : magic items , 9800 - descriptions, a110 - heal stone stuff
words.append(TLWord(0xd150, 8, "History"))
words.append(TLWord(0xd195, 20, "No message history!"))
# 6060h - char names
words.append(TLWord(0x1302b, 37, "Wait    Item \x01Attack   Status \x01Magic   Formtn."))
# 13230 - battle text
words.append(TLWord(0x3b5e5, 17, "Toss item \x01Toss equipment"))
words.append(TLWord(0x3b79a, 16, "\x01tossed. \x01Is this OK?"))
words.append(TLWord(0x3b7ab, 23, " pieces of equip. \x01Toss which?"))
words.append(TLWord(0x3b7c5, 10, "No equipment."))
words.append(TLWord(0x4dd2, 11, ": Recruit? "))

words.append(TLWord(0x1553f, 4, "Talk"))

words.append(TLWord(0x15543, 12, "MessageSpd  "))
words.append(TLWord(0x15550, 4, "Batt"))
words.append(TLWord(0x15554, 7, "Music"))
words.append(TLWord(0x1555c, 11, "Swap Buttons"))
words.append(TLWord(0x15567, 4, "  Back"))
words.append(TLWord(0x1556b, 4, "OK"))
words.append(TLWord(0x1556f, 4, "Ster"))
words.append(TLWord(0x15573, 4, "Mono"))

words.append(TLWord(0x18f29, 46, "Attack Adj.1H     2H \x01Strike Adj.1H     2H \x01Critical # "))
words.append(TLWord(0x18f58, 8, "(Throw) "))
words.append(TLWord(0x18fa8, 19, "Attack Adj. \x01Evade Adj."))
words.append(TLWord(0x19017, 29, "Evade Adj. \x01DFP Adj. \x01Damage Red."))
words.append(TLWord(0x18e42, 9, "Unequipped"))
words.append(TLWord(0x19d19, 22, "No known \x01non-combat magic."))
words.append(TLWord(0x19ca6, 12, " is unconscious!"))
words.append(TLWord(0x19c97, 12, " can't use magic"))
words.append(TLWord(0x19e64, 14, "Both hands occupied"))
words.append(TLWord(0x19e78, 17, "Wearing metal armor!"))
words.append(TLWord(0x1c51e, 6, "    MP "))
words.append(TLWord(0x1c527, 13, "Not enough MP!"))
words.append(TLWord(0x1c56c, 8, "Expand tgt "))
words.append(TLWord(0x1c576, 10, "Expand dmg "))
words.append(TLWord(0x1c582, 12, "Expand dur "))
words.append(TLWord(0x1c590, 10, "Inc. success "))
words.append(TLWord(0x1c59c, 10, "MP Given"))
words.append(TLWord(0x3843c, 26, "Buy item \x01Sell item\x01Instruments"))
words.append(TLWord(0x3859c, 15, "Harp \x01Lute \x01Flute"))
words.append(TLWord(0x385ac, 10, "Sell which?"))
words.append(TLWord(0x385b8, 20, "Buy who's mage \x01staff?"))
words.append(TLWord(0x385cd, 8, "Mage Staff"))
words.append(TLWord(0x385d6, 34, " does not have\x01Sorcerer, so will be used\x01as a weapon."))
words.append(TLWord(0x385fb, 14, "Nothing to sell"))
words.append(TLWord(0x3860c, 11, "G total. OK? "))
words.append(TLWord(0x38933, 13, "Thank you. "))
words.append(TLWord(0x38941, 9, "\x01Purchase?"))
words.append(TLWord(0x38951, 5, "Harp "))
words.append(TLWord(0x38957, 4, "Lute "))
words.append(TLWord(0x3895c, 4, "Flute"))
words.append(TLWord(0x38967, 5, "MagStn"))
words.append(TLWord(0x3896d, 9, "Wizard Heart"))
words.append(TLWord(0x38994, 16, " will be\x01tossed. Sure?"))
words.append(TLWord(0x389a5, 17, "\x01Toss item to \x01make room?"))
words.append(TLWord(0x389b7, 7, " obtained."))
words.append(TLWord(0x389bf, 7, " obtained."))
words.append(TLWord(0x389c9, 6, " left."))
words.append(TLWord(0x389d8, 6, " left."))
words.append(TLWord(0x386b0, 18, "Arrow (24) \x01Bow ammo."))
words.append(TLWord(0x386c3, 23, "Quarrel (24) \x01For crossbows. "))
words.append(TLWord(0x386e1, 23, "MagStn (10) \x01Stone holding MP. "))
words.append(TLWord(0x386f9, 23, "MagStn (20) \x01Stone holding MP. "))
words.append(TLWord(0x38711, 23, "Wizard Heart \x01+1 to mental power. "))
words.append(TLWord(0x38735, 23, "MagStn (30) \x01Stone holding MP. "))
words.append(TLWord(0x3874d, 31, "Magic Yarn \x01Exit from dungeons."))
words.append(TLWord(0x3876d, 34, "Warrior's Medicine \x01Raises ATP as HP\x01decreases."))
words.append(TLWord(0x38790, 16, "Antidote \x01Cures poison."))
words.append(TLWord(0x387a1, 19, "Tonic\x01Returns consciousness. "))
words.append(TLWord(0x387b5, 15, "Heal Stone\x01Heals wounds."))
words.append(TLWord(0xd8a8, 38, "Welcome to the Sorcerers\x01Guild. How can I help?\x0f"))
words.append(TLWord(0xd8fd, 45, "Need a \"Thief Wisdom\"? \x01For 2000 gamel it'll \x01raise your agility. "))
words.append(TLWord(0xd92c, 14, "Then leave already."))
words.append(TLWord(0x3889c, 13, "Then leave already."))
words.append(TLWord(0x388aa, 19, "Buy \"Thief Wisdom\"? "))
words.append(TLWord(0x388c6, 37, "Buy magic item \x01Buy mage staff \x01Buy common rune\x0f"))
words.append(TLWord(0x388f7, 26, "Enchant Rune \x01Protect Rune \x01Defense Rune \x0f"))
words.append(TLWord(0x38918, 8, "Enchant Rune "))
words.append(TLWord(0x38921, 8, "Protect Rune "))
words.append(TLWord(0x3892a, 8, "Defense Rune "))

words.append(TLWord(0x38977, 4, "Oh?"))
words.append(TLWord(0x3897c, 23, " already has\x01divine protection."))

words.append(TLWord(0xd969, 23, "No info for now. \x01Go on, then. "))
words.append(TLWord(0xdd4e, 23, "No info for now. \x01Go on, then. "))

words.append(TLWord(0xd9d1, 10, "How can I help?"))
words.append(TLWord(0xd9dc, 20, "Go with the protection \x01of Pharis."))
words.append(TLWord(0xda41, 13, "Myrii is justice."))
words.append(TLWord(0xda9f, 10, "Can I help?"))
words.append(TLWord(0xdaaa, 15, "With Rahda's wisdom."))

words.append(TLWord(0xdaff, 10, "Can I help?"))
words.append(TLWord(0xdb0a, 23, "Go with the protection \x01of Cha-Za."))

words.append(TLWord(0xdb73, 10, "Something wrong? "))
words.append(TLWord(0xdb7e, 20, "Go with the blessings\x01of Marfa. "))
words.append(TLWord(0xdbd0, 7, "Welcome. "))
words.append(TLWord(0xdbd8, 9, "Come again."))
words.append(TLWord(0xda36, 10, "Can I help?"))

words.append(TLWord(0x1f37e, 12, "Disarm trap? "))
words.append(TLWord(0x1f38b, 22, "I disarmed the trap. \x0f"))
words.append(TLWord(0x1f3a2, 22, "The trap is disarmed.\x0f"))
words.append(TLWord(0x1f495, 22, "It's locked. \x0f"))
words.append(TLWord(0x1f4ac, 10, "Pick the lock? "))
words.append(TLWord(0x1f4b7, 23, "It's open! \x0f"))
words.append(TLWord(0x1f4cf, 46, "Sorry... \x01I tried, but I couldn't \x01get it open."))
words.append(TLWord(0x1f759, 10, "Open the chest?"))
words.append(TLWord(0x1f765, 6, "found."))
words.append(TLWord(0x1f76e, 12, "Inventory is full"))
words.append(TLWord(0x1f7cb, 27, "Looks like the chest \x01is empty. "))

words.append(TLWord(0x1fb38, 22, "It's locked. \x0f"))
words.append(TLWord(0x1fb4f, 10, "Pick the lock? "))
words.append(TLWord(0x1fb5a, 23, "It's open! \x0f"))
words.append(TLWord(0x1fb72, 46, "Sorry... \x01I tried, but I couldn't \x01get it open."))
words.append(TLWord(0x20178, 12, "Not enough gamel."))
words.append(TLWord(0x1d0b9, 17, "'s\x01spells are sealed!"))
words.append(TLWord(0x1d110, 14, "\x01cannot move!"))
words.append(TLWord(0x1d12e, 16, "\x01can't use magic!"))
words.append(TLWord(0x1d14e, 8, "\x01dodged! "))

words.append(TLWord(0x1d188, 10, "Critical hit!"))
words.append(TLWord(0x1d1a5, 11, " was\x01unaffected! "))
words.append(TLWord(0x1d1c0, 7, "\x01defeated! "))
words.append(TLWord(0x1d20d, 6, "attacked"))
words.append(TLWord(0x1d223, 8, "\x01resisted! "))
words.append(TLWord(0x1d265, 4, " taken"))
words.append(TLWord(0x1d279, 7, " not taken"))
words.append(TLWord(0x1d292, 6, "\x01sleeps"))
words.append(TLWord(0x1d2c2, 8, "\x01is confused."))
words.append(TLWord(0x1d2dc, 8, "\x01fell over!"))
words.append(TLWord(0x1d2f6, 5, " raised."))
words.append(TLWord(0x1d30d, 5, " lowered. "))
words.append(TLWord(0x1d324, 10, "'s\x01STP"))
words.append(TLWord(0x1d340, 23, "'s\x01STP vs undead\x01"))
words.append(TLWord(0x1d369, 10, "'s\x01dexterity "))
words.append(TLWord(0x1d385, 8, "'s\x01 strength "))
words.append(TLWord(0x1d39f, 10, "'s\x01agility "))
words.append(TLWord(0x1d3bb, 8, "'s  LFP\x01"))
words.append(TLWord(0x1d3d5, 13, "'s\x01critical number \x01"))
words.append(TLWord(0x1d3f2, 14, "'s\x01 damage reduction "))
words.append(TLWord(0x1d432, 8, "p recovered!"))
words.append(TLWord(0x1d43b, 11, " fully healed!"))
words.append(TLWord(0x1d447, 11, " recovery failed"))
words.append(TLWord(0x1d453, 14, " effect \x01cleansed"))

words.append(TLWord(0x1e1f8, 5, " died!"))
words.append(TLWord(0x148aa, 7, " died!"))
words.append(TLWord(0x1e20f, 3, " stn"))
words.append(TLWord(0x1e224, 4, " fell!"))
words.append(TLWord(0x148b4, 7, " fell!"))
words.append(TLWord(0x148be, 9, " was poisoned!"))
words.append(TLWord(0x148ee, 13, "\x01evaded the attack!"))
words.append(TLWord(0x13f19, 12, " had\x01no effect!"))
words.append(TLWord(0x13f26, 10, " stood up."))

words.append(TLWord(0x1e2a7, 54, "Banish which spirit? \x01  Earth\x01  Water\x01  Fire \x01  Wind \x0f"))
words.append(TLWord(0x1e444, 5, "Sound"))
words.append(TLWord(0x1e448, 15, "'s\x01melody resounds.\x0f"))
words.append(TLWord(0x1e8a3, 10, "Unlocked!\x0f"))
words.append(TLWord(0x1e8ae, 14, "Couldn't unlock it.\x0f"))
words.append(TLWord(0x1e8bd, 10, "No effect. \x0f"))
words.append(TLWord(0x1f29a, 37, "Watch out!!\x01There's a trap!\x0f"))
words.append(TLWord(0x1f2c0, 20, "I don't sense a trap.\x0f"))
words.append(TLWord(0x1f878, 5, "Oh no! "))
words.append(TLWord(0x1f87e, 16, "A small arrow shoots out!\x0f"))
words.append(TLWord(0x1fa4d, 20, "It's a secret door!\x0f"))
words.append(TLWord(0x13235, 2, "\x20\x20\x20\x20"))
words.append(TLWord(0x13231, 2, "\x20\x20\x20\x20"))
words.append(TLWord(0x13239, 7, " attacked!"))
words.append(TLWord(0x13302, 6, " thrown!"))
words.append(TLWord(0x13309, 14, "\x01hit an obstacle!"))
words.append(TLWord(0x133dc, 12, " held \x01and equipped"))
words.append(TLWord(0x13442, 5, " lost."))
words.append(TLWord(0x134b3, 5, " lost."))
words.append(TLWord(0x134d8, 10, "No arrows! "))
words.append(TLWord(0x13518, 12, "No quarrel!"))
words.append(TLWord(0x135ad, 7, " readied. "))
words.append(TLWord(0x13802, 3, "arrw"))
words.append(TLWord(0x13806, 5, "quarrel "))
words.append(TLWord(0x1380c, 1, "st"))
words.append(TLWord(0x1380e, 11, "  \x01fired at\x01\x05"))
words.append(TLWord(0x1381a, 13, "\x01hit an obstacle!"))
words.append(TLWord(0x13985, 5, " left."))
words.append(TLWord(0x1398c, 7, " has\x01died. "))
words.append(TLWord(0x13994, 8, " fell!\x0f"))
words.append(TLWord(0x13be2, 14, "\x01continue singing? "))
words.append(TLWord(0x13cd3, 18, "Returning to last position."))

words.append(TLWord(0x13de8, 13, "'s\x01enchanted weapon"))
words.append(TLWord(0x13df6, 12, "'s\x01counter magic "))
words.append(TLWord(0x13e03, 10, "'s\x01protection"))
words.append(TLWord(0x13e0e, 11, "'s\x01fire weapon "))
words.append(TLWord(0x13e1a, 9, "'s\x01sharpness "))
words.append(TLWord(0x13e24, 7, "'s\x01dullness"))
words.append(TLWord(0x13e2c, 8, "'s\x01strength"))

words.append(TLWord(0x1d24e, 7, " damage \x0f"))

words.append(TLWord(0x1e135, 16, "The def stone shattered"))
words.append(TLWord(0x1e147, 13, "\x01completely healed!"))

words.append(TLWord(0x3800c, 14, "Heal    Destone        \x01"))
words.append(TLWord(0x3801a, 14, "Resrct  Buy item "))
words.append(TLWord(0x38029, 13, "Sanctify \x0f"))

words.append(TLWord(0x6096, 4, "Ratelia"))
words.append(TLWord(0x609b, 3, "Toure"))
words.append(TLWord(0x609f, 3, "Gara "))
words.append(TLWord(0x60a3, 3, "Ein"))
words.append(TLWord(0x60a7, 4, "Tad"))
words.append(TLWord(0x60ac, 4, "Cianon "))
words.append(TLWord(0x60b1, 6, "Noland "))
words.append(TLWord(0x60b8, 4, "Gies "))
words.append(TLWord(0x60bd, 4, "Madera "))
words.append(TLWord(0x60c2, 4, "Lloyd"))
words.append(TLWord(0x60c7, 3, "Ciel "))
words.append(TLWord(0x60cb, 4, "Kuld "))
words.append(TLWord(0x60d0, 7, "Valrud "))
words.append(TLWord(0x60d8, 4, "Laud "))
words.append(TLWord(0x60dd, 4, "Macroy "))
words.append(TLWord(0x60e2, 3, "Sai"))
words.append(TLWord(0x60e6, 7, "Barland"))
words.append(TLWord(0x60ee, 6, "Felzen "))
words.append(TLWord(0x60f6, 4, "Dory "))
words.append(TLWord(0x60fa, 6, "Dinker "))
words.append(TLWord(0x6101, 4, "Recp "))
words.append(TLWord(0x6106, 4, "Shop \x0f"))
words.append(TLWord(0x610b, 10, "Salty Dog\x0f"))
words.append(TLWord(0x6116, 7, "Bluod"))
words.append(TLWord(0x611e, 4, "OldMan"))
words.append(TLWord(0x6123, 8, "Pharis Pr \x0f"))
words.append(TLWord(0x612c, 8, "Myrii Pr \x0f"))
words.append(TLWord(0x6135, 8, "Rahda Pr "))
words.append(TLWord(0x613e, 9, "Cha-Za Pr \x0f"))
words.append(TLWord(0x6148, 8, "Marfa Pr "))
words.append(TLWord(0x6151, 4, "Bein "))
words.append(TLWord(0x6156, 5, "Erunda "))
words.append(TLWord(0x615c, 7, "Dark Elf"))
words.append(TLWord(0x6164, 5, "Dwarf"))
words.append(TLWord(0x616a, 6, "Kobold "))
words.append(TLWord(0x6171, 6, "Goblin "))
words.append(TLWord(0x6178, 11, "Goblin Shaman "))
words.append(TLWord(0x6184, 3, "Wolf "))
words.append(TLWord(0x6188, 8, "Guardsman"))
words.append(TLWord(0x6191, 4, "Kadi "))
words.append(TLWord(0x6196, 4, "Corsi"))
words.append(TLWord(0x619b, 8, "Initiate "))
words.append(TLWord(0x61a4, 5, "Sogran "))
words.append(TLWord(0x61aa, 4, "Imp"))
words.append(TLWord(0x61af, 4, "Thief"))
words.append(TLWord(0x61b4, 10, "Skeleton Warrior"))
words.append(TLWord(0x61bf, 4, "Shop \x0f"))
words.append(TLWord(0x61c4, 4, "Bcat "))
words.append(TLWord(0x61c9, 5, "Nelder "))
words.append(TLWord(0x61cf, 2, "Man"))
words.append(TLWord(0x61d2, 4, "Barry"))
words.append(TLWord(0x61d7, 5, "Mardy"))
words.append(TLWord(0x61dd, 3, "Man"))
words.append(TLWord(0x61e1, 6, "Dorval "))
words.append(TLWord(0x61e8, 8, "Nightshade "))
words.append(TLWord(0x61f1, 5, "Kains"))
words.append(TLWord(0x61f7, 7, "Osborne"))
words.append(TLWord(0x61ff, 4, "Merc "))
words.append(TLWord(0x6204, 4, "Thief"))
words.append(TLWord(0x6209, 3, "Celia"))
words.append(TLWord(0x620d, 5, "Messenger"))
words.append(TLWord(0x6213, 3, "Man"))
words.append(TLWord(0x6217, 5, "Delia"))
words.append(TLWord(0x621d, 4, "Assn "))
words.append(TLWord(0x6222, 9, "Assn Leader "))
words.append(TLWord(0x622c, 4, "Bat"))
words.append(TLWord(0x6231, 7, "Gargoyle "))
words.append(TLWord(0x6239, 9, "Killer Creeper"))
words.append(TLWord(0x6243, 5, "Zombie "))
words.append(TLWord(0x6249, 3, "Wight"))
words.append(TLWord(0x624d, 6, "Crimson"))
words.append(TLWord(0x6254, 10, "Giant Rat"))
words.append(TLWord(0x625f, 11, "Creeping Tree "))
words.append(TLWord(0x626b, 9, "Lil Fungus "))
words.append(TLWord(0x6275, 10, "Lesser Fungus "))
words.append(TLWord(0x6280, 14, "Giant Spider "))
words.append(TLWord(0x628f, 5, "Blob "))
words.append(TLWord(0x6295, 3, "Hyu"))
words.append(TLWord(0x6299, 3, "Curt "))
words.append(TLWord(0x629d, 5, "Harmond"))

words.append(TLWord(0x62a3, 3, "Nalia"))
words.append(TLWord(0x62a7, 4, "Stia "))
words.append(TLWord(0x62ac, 4, "Teela"))
words.append(TLWord(0x62b1, 5, "Skard"))
words.append(TLWord(0x62b7, 4, "Lancer "))
words.append(TLWord(0x62bc, 6, "Dinker "))
words.append(TLWord(0x62c3, 10, "Stone Servant"))
words.append(TLWord(0x62ce, 5, "Navigator"))
words.append(TLWord(0x62d4, 5, "Lookout"))
words.append(TLWord(0x62da, 3, "Sea"))
words.append(TLWord(0x62de, 3, "Cook "))
words.append(TLWord(0x62e2, 6, "Bagnan "))
words.append(TLWord(0x62e9, 4, "Pirate "))
words.append(TLWord(0x62ee, 4, "Recp."))
words.append(TLWord(0x62f3, 7, "Magician "))
words.append(TLWord(0x62fb, 5, "Madden "))
words.append(TLWord(0x6301, 4, "GDog"))
words.append(TLWord(0x6306, 1, "W"))
words.append(TLWord(0x6308, 4, "Kersh"))
words.append(TLWord(0x630d, 4, "Luza "))
words.append(TLWord(0x6312, 6, "Garud"))
words.append(TLWord(0x6319, 10, "Fake Nightshade "))
words.append(TLWord(0x6324, 7, "Argenta"))
words.append(TLWord(0x623c, 3, "Anna "))
words.append(TLWord(0x6330, 4, "Bolt "))
words.append(TLWord(0x6335, 8, "Lindgulm "))
words.append(TLWord(0x633e, 7, "Hucania"))
words.append(TLWord(0x6346, 5, "Skeleton "))
words.append(TLWord(0x634c, 4, "Ghoul"))
words.append(TLWord(0x6351, 10, "Captain Conrad "))
words.append(TLWord(0x635c, 3, "Nal"))
words.append(TLWord(0x6360, 15, "Giant Centipede"))
words.append(TLWord(0x6370, 4, "Ash"))
words.append(TLWord(0x6375, 4, "Zack "))
words.append(TLWord(0x637a, 5, "Guard"))
words.append(TLWord(0x6380, 10, "Black Hound"))
words.append(TLWord(0x638b, 3, "Guy"))
words.append(TLWord(0x638f, 4, "Alec "))
words.append(TLWord(0x6394, 4, "Myza "))
words.append(TLWord(0x6399, 4, "Zenon"))
words.append(TLWord(0x639e, 3, "Dai"))

words.append(TLWord(0x63a2, 2, "Al "))
words.append(TLWord(0x63a5, 4, "Shyra"))
words.append(TLWord(0x63aa, 5, "Martoli"))
words.append(TLWord(0x63b0, 7, "Beldis "))
words.append(TLWord(0x63b8, 2, "Man"))
words.append(TLWord(0x63bb, 10, "Guard Captain"))
words.append(TLWord(0x63c6, 6, "Dorid"))
words.append(TLWord(0x63cd, 7, "Robed Man"))
words.append(TLWord(0x63d5, 5, "Ascart "))
words.append(TLWord(0x63d8, 6, "Guard"))
words.append(TLWord(0x63e2, 8, "Thug "))
words.append(TLWord(0x63eb, 5, "Gurnel "))
words.append(TLWord(0x63f1, 4, "Garden "))
words.append(TLWord(0x63f6, 6, "Gazarn "))
words.append(TLWord(0x63fd, 7, "Undine "))
words.append(TLWord(0x6405, 10, "Giant Ant"))
words.append(TLWord(0x6410, 7, "Crocodile"))
words.append(TLWord(0x6418, 4, "Toad "))
words.append(TLWord(0x641d, 9, "Killer Octopus"))
words.append(TLWord(0x6427, 5, "Forsyth"))
words.append(TLWord(0x642d, 4, "Ryza "))
words.append(TLWord(0x6432, 5, "Kevin"))
words.append(TLWord(0x6438, 6, "Manticore"))
words.append(TLWord(0x634f, 4, "Soldier"))
words.append(TLWord(0x6444, 13, "Paladin of Pharis "))
words.append(TLWord(0x6452, 4, "Boy"))
words.append(TLWord(0x6457, 8, "Leader of C"))
words.append(TLWord(0x6460, 2, "C"))
words.append(TLWord(0x6463, 9, "Stone Golem"))
words.append(TLWord(0x646d, 3, "Mum"))
words.append(TLWord(0x6471, 5, "Sogran "))
words.append(TLWord(0x6477, 4, "Priest "))
words.append(TLWord(0x647c, 4, "Mazai"))
words.append(TLWord(0x6481, 6, "Adventurer "))
words.append(TLWord(0x6488, 4, "Merc "))
words.append(TLWord(0x648d, 5, "Mana Rai"))
words.append(TLWord(0x6493, 4, "Valen"))
words.append(TLWord(0x6498, 5, "Skeleton "))
words.append(TLWord(0x649e, 6, "Dullahan "))
words.append(TLWord(0x64a5, 11, "Lesser Vampire"))
words.append(TLWord(0x64b1, 10, "Flesh Golem"))
words.append(TLWord(0x64bc, 5, "Mirleaf"))
words.append(TLWord(0x64c2, 11, "Giant Wasp "))
words.append(TLWord(0x64ce, 6, "Viper"))
words.append(TLWord(0x64d5, 9, "Hobgoblin"))
words.append(TLWord(0x64df, 8, "Lizardman"))
words.append(TLWord(0x64e8, 5, "Harpy"))
words.append(TLWord(0x64ee, 11, "Vampire Bat"))
words.append(TLWord(0x64fa, 10, "Goblin Lord "))
words.append(TLWord(0x6506, 3, "Orc"))
words.append(TLWord(0x6509, 11, "Giant Bat"))
words.append(TLWord(0x6515, 5, "Ogre "))
words.append(TLWord(0x651b, 7, "Grizzly"))
words.append(TLWord(0x6523, 6, "Medusa "))
words.append(TLWord(0x652a, 5, "Wbear"))
words.append(TLWord(0x6530, 7, "Salamander "))
words.append(TLWord(0x6538, 4, "Chimera"))
words.append(TLWord(0x653d, 7, "Hellhound"))
words.append(TLWord(0x6545, 11, "Giant Crab "))
words.append(TLWord(0x6551, 15, "Mutant Big Ape"))
words.append(TLWord(0x6561, 10, "Shadow Stalker"))
words.append(TLWord(0x656c, 6, "Gryphon"))
words.append(TLWord(0x6573, 4, "Troll"))
words.append(TLWord(0x6578, 6, "Minotaur "))
words.append(TLWord(0x657f, 11, "Jack-o-lantern "))
words.append(TLWord(0x658b, 10, "Sogran Zombie "))

words.append(TLWord(0x95a0, 5, "MagStn")) #9515h: ->959Fh
words.append(TLWord(0x95a6, 8, "Magic Yarn "))
words.append(TLWord(0x95b0, 7, "Warrior Meds "))
words.append(TLWord(0x95b8, 7, "Antidote "))
## TONIC PTR HAS BEEN SWITCHED WITH HOLY WATER 
words.append(TLWord(0x9608, 3, "Tonic")) #951D -> 95B8::
words.append(TLWord(0x95c7, 7, "Heal Stone")) #95c0
words.append(TLWord(0x95cf, 9, "Wizard Heart"))
words.append(TLWord(0x95d9, 9, "Thief Wisdom "))
words.append(TLWord(0x95e3, 8, "Myrii Guard"))
words.append(TLWord(0x95ec, 8, "Marfa Guard"))
words.append(TLWord(0x95f5, 8, "Rahda Mind "))
words.append(TLWord(0x95fe, 9, "Cha-Za Mind "))
words.append(TLWord(0x95c0, 6, "Holy Water")) #952D -> 95FE::
words.append(TLWord(0x960c, 8, "Battle Horn "))
words.append(TLWord(0x9615, 8, "SleepFlute"))
words.append(TLWord(0x961e, 7, "ChaosFlute"))
words.append(TLWord(0x9626, 11, "Defense Tablet "))
words.append(TLWord(0x9632, 7, "Wing Statue "))
words.append(TLWord(0x963a, 9, "Cloud Egg"))
words.append(TLWord(0x9644, 7, "Heal Rod"))
# not done!

words.append(TLWord(0x38059, 22, "Recover life \x01Recover MP"))
words.append(TLWord(0x3807e, 22, "Recover whose\x01life points?"))
words.append(TLWord(0x38095, 23, "Recover whose\x01mental power? "))
words.append(TLWord(0x380ad, 16, "Depetrify whom?"))
words.append(TLWord(0x380be, 15, "Resurrect whom?"))
words.append(TLWord(0x380ce, 26, " has no need\x01to recover MP. "))
words.append(TLWord(0x380e9, 25, " has no need\x01to recover life."))
words.append(TLWord(0x38103, 14, " is \x01not petrified."))
words.append(TLWord(0x38112, 20, " does not need\x01to be revived."))
words.append(TLWord(0x38127, 24, " gamels, please.\x01Is this OK? "))
words.append(TLWord(0x38142, 14, "Inventory is full. "))
words.append(TLWord(0x38155, 14, "Equipment is full. "))
words.append(TLWord(0x38171, 7, "Holy Water"))
words.append(TLWord(0x38188, 7, "Holy Water"))
words.append(TLWord(0x3819f, 7, "Holy Water"))
words.append(TLWord(0x38179, 14, "Buy Myrii Guard"))
words.append(TLWord(0x38190, 14, "Buy Marfa Guard"))
words.append(TLWord(0x381a7, 14, "Buy Rahda Mind "))

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
print("Converting / compressing",str(len(words)),"lines to SFC format... ", end="")
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