
class TLWord():
    def __init__(self, _loc, _len, _tl, buff=True, sjis=False):
        self.loc = _loc 
        self.len = _len 
        self.original = []
        self.translation = _tl
        self.sjis = sjis
        self.filenum = -1
    ###
###

words = []

# b0440 - tile location of HA small hiragana 


# NON SJIS: 
# 0x1dbe0: item names 
# 0x20430: non-sjis char names 
# 0x1ee58: item use text
# 0x1ec40: equip stats text
# 0x1c3a0: magic help text
# 0x1bc3e: magic names (0x1b730 - priest and spell descs )
# 0x1b170: sorc spells/descs
# 0x1a9d0: more (and 0x1a5e0)
# 0x19ed6: more 
# 0x19885: (items)
# 0x14292: status names
# 0x1309e: help text


words = [ 
####
 # NON-SJIS smalls at: 
# THESE MUST BE PATCHED INLINE WITH TABLE CODES.
    #TLWord(0x00014657, 5, "FGHTR", sjis=False),
    #TLWord(0x00023ef9, 5, "FGHTR", sjis=False),
    #TLWord(0x00024073, 5, "FGHTR", sjis=False),
    #thief
    #rangr
    #bard
    #sorcr
    #shamn
    #pries
# still need to do this row: this is small in char creation
#TLWord(0x0003B66B, 10, "Fighter", sjis=True),  
# also in char creation 
#TLWord(0x0003B5A4, 10, "Fighter", sjis=True), # not small / status 

####
    TLWord(0x2fe, 28, "Party annihilated! ", sjis=True),
    TLWord(0x000082EA, 32, "Its a secret door! ", sjis=True),
    TLWord(0x00008D47, 6, "Enter", sjis=True),
    TLWord(0x00008D4E, 6, "Exit ", sjis=True),
    
    # a050 - town names 
    # a2b0 - location names
    TLWord(0x0000A2B3, 12, "World Map", sjis=True),
    TLWord(0x0000A2C0, 16, "Gate to AncKng", sjis=True),
    TLWord(0x0000A2D1, 20, "Our Lovely Home", sjis=True),
    TLWord(0x0000A2E6, 16, "Magic Guild", sjis=True),
    TLWord(0x0000A2F7, 14, "Thief Guild", sjis=True),
    TLWord(0x0000A306, 12, "Pharis Tpl", sjis=True),
    TLWord(0x0000A313, 12, "Myrii Tpl", sjis=True),
    TLWord(0x0000A320, 12, "Rahda Tpl", sjis=True),
    TLWord(0x0000A32D, 14, "ChaZa Tpl", sjis=True),
    TLWord(0x0000A33C, 12, "Marfa Tpl", sjis=True),
    TLWord(0x0000A349, 8, "Equip", sjis=True),
    TLWord(0x0000A352, 8, "Miracle", sjis=True),
    TLWord(0x0000A35B, 2, "pt", sjis=True),
    TLWord(0x0000A35E, 14, "Whale Hill", sjis=True),
    TLWord(0x0000A36D, 12, "Silver Fox", sjis=True),
    TLWord(0x0000A37A, 14, "Brief Dream", sjis=True),
    TLWord(0x0000A389, 12, "Red Armor", sjis=True),
    TLWord(0x0000A396, 6, "Arena", sjis=True),
    TLWord(0x0000A39D, 12, "White Bear ", sjis=True),
    TLWord(0x0000A3AA, 14, "Merc Guild", sjis=True),
    TLWord(0x0000A3B9, 6, "Prisn", sjis=True),
    TLWord(0x0000A3C0, 10, "Moon Inn", sjis=True),
    TLWord(0x0000A3CB, 12, "Night Horse", sjis=True),
    TLWord(0x0000A3D8, 2, "vi", sjis=True),
    TLWord(0x0000A3DB, 8, "Mayors ", sjis=True),
    TLWord(0x0000A3E4, 8, "Ruins", sjis=True),
    TLWord(0x0000A3ED, 12, "Norn Manor", sjis=True),
    TLWord(0x0000A3FA, 6, "Slum ", sjis=True),
    TLWord(0x0000A401, 14, "Bandit Base ", sjis=True),
    TLWord(0x0000A410, 10, "Cyril Rvr", sjis=True),
    TLWord(0x0000A41B, 8, "Cap'ns ", sjis=True),
    TLWord(0x0000A424, 4, "Bch", sjis=True),
    TLWord(0x0000A429, 4, "Can", sjis=True),
    TLWord(0x0000A42E, 16, "Greenroof Inn", sjis=True),
    TLWord(0x0000A43F, 10, "Outskirts", sjis=True),
    TLWord(0x0000A44A, 4, "Mnt", sjis=True),
    TLWord(0x0000A44F, 6, "fogton", sjis=True),
    TLWord(0x0000A456, 2, "fo", sjis=True),
    TLWord(0x0000A459, 4, "mine", sjis=True),
    

    TLWord(0x0000CD73, 18, ": Recruit? ", sjis=True),
    TLWord(0x0000CECB, 22, "View stats?", sjis=True),
    TLWord(0x0000CF2A, 20, "Remove someone?", sjis=True),
    # more at cec0
    TLWord(0x0000CF8E, 20, "Remove who?", sjis=True),
    TLWord(0x0000CFED, 20, "Can't remove them! ", sjis=True),
    TLWord(0x0000D134, 8, "'s gamel", sjis=True),
    TLWord(0x0000D143, 10, " gamel", sjis=True),
    TLWord(0x0000D14E, 24, " added to party gold. ", sjis=True),
    TLWord(0x0000D223, 16, "Party's  ", sjis=True),
    TLWord(0x0000D23A, 10, " gamel", sjis=True),
    TLWord(0x0000D246, 14, "handed over.", sjis=True),
    
    
    
    
    # : 
    # e700 magicians guild
    TLWord(0x0000E701, 28, "This is the mage's guild.", sjis=True),
    TLWord(0x0000E725, 22, "Please come again. ", sjis=True),
    TLWord(0x0000E76C, 28, "Come for thieves' know-how?", sjis=True),
    TLWord(0x0000E790, 16, "Get out, then. ", sjis=True),
    TLWord(0x0000E828, 14, "Welcome. ", sjis=True),
    TLWord(0x0000E837, 38, "We got good mercenaries here.", sjis=True),
    TLWord(0x0000E865, 28, "Come back any time.", sjis=True),
    TLWord(0x0000E889, 14, "Welcome. ", sjis=True),
    TLWord(0x0000E898, 16, "Whatcha need?", sjis=True),
    TLWord(0x0000E8B0, 16, "Come again.", sjis=True),
    TLWord(0x0000E8DF, 26, "Sorry, no info for now.", sjis=True),
    TLWord(0x0000E8FA, 16, "Go on, then. ", sjis=True),
    TLWord(0x0000E929, 26, "Sorry, no info for now.", sjis=True),
    TLWord(0x0000E944, 16, "Go on, then. ", sjis=True),
    TLWord(0x0000E98A, 16, "Can I help you?", sjis=True),
    TLWord(0x0000E9A2, 34, "With the blessings of Pharis.", sjis=True),
    TLWord(0x0000E9FA, 20, "What's wrong?", sjis=True),
    TLWord(0x0000EA16, 22, "Myrii is justice.", sjis=True),
    TLWord(0x0000EA62, 20, "How can I help?", sjis=True),
    TLWord(0x0000EA7E, 26, "With Rahda's wisdom.", sjis=True),
    TLWord(0x0000EACE, 20, "How can I help?", sjis=True),
    TLWord(0x0000EAEA, 40, "With the blessings of Cha-Za.", sjis=True),
    TLWord(0x0000EB48, 20, "Is anything wrong? ", sjis=True),
    TLWord(0x0000EB64, 36, "Go with Marfa's blessings. ", sjis=True),
    TLWord(0x0000EBA2, 24, "Raising mental power ", sjis=True),
    TLWord(0x0000EBBB, 28, "requires a magician's heart.", sjis=True),
    TLWord(0x0000EBDC, 32, "Magistone will recover expended", sjis=True),
    TLWord(0x0000EBFD, 22, "mental energy.", sjis=True),
    TLWord(0x0000EC14, 32, "Definitely bring some with you.", sjis=True),
    
    
    
    
    
    # e920 other guilds, temples 
    # 106f0 - class restriction text 

    TLWord(0x000118E0, 28, "No save file!", sjis=True),
    TLWord(0x00011AFF, 10, "Erase", sjis=True),
    TLWord(0x00012581, 16, "Toss items ", sjis=True),
    TLWord(0x00012592, 12, "Toss equip ", sjis=True),
    TLWord(0x000126D6, 18, "equipment held. ", sjis=True),
    TLWord(0x000126E9, 16, "Toss which?", sjis=True),
    TLWord(0x00012727, 12, "Toss this? ", sjis=True),
    TLWord(0x00012764, 26, "Nothing to toss! ", sjis=True),
    TLWord(0x0001281C, 10, "Record ", sjis=True),
    TLWord(0x00012827, 8, "Formtn.", sjis=True),
    TLWord(0x00012830, 22, "Message history", sjis=True),
    TLWord(0x00012847, 14, "Toss items ", sjis=True),
    TLWord(0x00012858, 4, "help", sjis=True),
    
    TLWord(0x1159f, 30, "Sword World SFC 2", sjis=True),
    TLWord(0x115c2, 12, "Adventure", sjis=True),
    TLWord(0x0001167C, 12, "Adventure", sjis=True),
    
    TLWord(0x000115CF, 18, "Make Character", sjis=True),
    TLWord(0x000115E2, 16, "Erase File ", sjis=True),
    TLWord(0x000115F3, 24, "Copy File ", sjis=True),
    TLWord(0x00011725, 18, "Make Character", sjis=True),
    TLWord(0x000117E0, 16, "Erase adventure", sjis=True),
    TLWord(0x00011837, 24, "Copy adventure ", sjis=True),
    TLWord(0x0001189E, 30, "Copy file where? ", sjis=True),
    TLWord(0x000118C0, 26, "File already exists! ", sjis=True),
    
    # DO THESE
    # 128d0 ~ 13060

    # TLWord(0x23ced, 32, "Who will level up? ", sjis=True),
    TLWord(0x13298, 10, "Races", sjis=True),
    TLWord(0x132a3, 10, "Classes", sjis=True),
    TLWord(0x132ae, 12, "Stats", sjis=True),

    TLWord(0x1333b, 6, "AttkP", sjis=True),
    TLWord(0x13342, 6, "StrkP", sjis=True),
    TLWord(0x13349, 8, "CritNum", sjis=True),
    TLWord(0x13352, 8, "XtraDmg", sjis=True),
    TLWord(0x1335b, 6, "Evade", sjis=True),
    TLWord(0x13362, 6, "Def  ", sjis=True),
    TLWord(0x13369, 8, "DmgRed", sjis=True),
    TLWord(0x1337b, 6, "Dex  ", sjis=True),
    
    TLWord(0x000140BE, 6, "Dex  ", sjis=True),
    TLWord(0x13382, 6, "Agil ", sjis=True),
    TLWord(0x000140C5, 6, "Agil ", sjis=True),
    TLWord(0x13389, 4, "Int", sjis=True),
    TLWord(0x000140CC, 6, "Int", sjis=True),
    TLWord(0x1338e, 4, "Str", sjis=True),
    TLWord(0x000140D3, 6, "Str", sjis=True),
    TLWord(0x13393, 6, "Life ", sjis=True),
    TLWord(0x000140DA, 6, "Life ", sjis=True),
    TLWord(0x1339a, 6, "Mentl", sjis=True),
    TLWord(0x000140EB, 6, "Mentl", sjis=True),
    TLWord(0x133a1, 10, "Life Res", sjis=True),
    TLWord(0x000140FC, 10, "Life Res", sjis=True),
    TLWord(0x133ac, 10, "MentlRes", sjis=True),
    TLWord(0x00014107, 10, "MentlRes", sjis=True),
    TLWord(0x00014119, 8, "No jobs", sjis=True),

    #
    TLWord(0x136bd, 4, "Hum", sjis=True),
    TLWord(0x136c2, 6, "Elf", sjis=True),
    # more 
    # above doesnt seem to affect anything??

    TLWord(0x000138D3, 10, "Fighter", sjis=True),
    TLWord(0x000138DE, 6, "Thief", sjis=True),
    TLWord(0x000138E5, 12, "Ranger ", sjis=True),
    TLWord(0x000138F2, 8, "Sage ", sjis=True),
    TLWord(0x000138FB, 10, "Bard ", sjis=True),
    TLWord(0x00013908, 10, "Sorcerer ", sjis=True),
    TLWord(0x00013913, 10, "Shaman ", sjis=True),
    TLWord(0x0001391E, 12, "Priest ", sjis=True),
    TLWord(0x000136C9, 10, "Dwarf", sjis=True),
    TLWord(0x000136D4, 16, "Grassrunner", sjis=True),
    TLWord(0x000136E5, 22, "Half-Elf/Human", sjis=True),
    TLWord(0x000136FC, 24, "Half-Elf/Elven", sjis=True),
    TLWord(0x0001405E, 8, "Level", sjis=True),
    TLWord(0x00014067, 6, "AttkP", sjis=True),
    TLWord(0x0001406E, 6, "StrkP", sjis=True),
    TLWord(0x00014075, 8, "CritNum", sjis=True),
    TLWord(0x0001407E, 8, "XtraDmg", sjis=True),
    TLWord(0x00014087, 6, "Evade", sjis=True),
    TLWord(0x0001408E, 6, "Def  ", sjis=True),
    TLWord(0x00014095, 8, "DmgRed", sjis=True),
    
    #14920 - save and load 
    
    #15c20 main menu 
    TLWord(0x00015C29, 22, "Items      Status ", sjis=True),
    TLWord(0x00015C40, 20, "Magic      System ", sjis=True),
    TLWord(0x00015C55, 24, "Equipment  Options", sjis=True),
    

    #TLWord(0x00013930, 8, "PHAR", sjis=True), # this is small font , 4x caps only
    TLWord(0x0001393A, 10, "CHAZ ", sjis=True),
    TLWord(0x00013945, 10, "MYRI ", sjis=True),

    TLWord(0x24277, 6, "Dex  ", sjis=True),
    TLWord(0x24290, 6, "Agil ", sjis=True),
    TLWord(0x242a9, 6, "Int", sjis=True),
    TLWord(0x242c2, 6, "Str", sjis=True),
    TLWord(0x242db, 6, "Life ", sjis=True),
    TLWord(0x242f4, 6, "Mentl", sjis=True),
    # help screen text ?^　
    
    #24690 - level up?
    TLWord(0x000246D7, 10, "Fighter", sjis=True), # not small / status 

    # ??

   
    # char creation
    TLWord(0x3a4cf, 26, "Enter a name.          ", sjis=True),
    TLWord(0x3aa54, 26, "Select gender.         ", sjis=True),
    TLWord(0x3aa71, 12, "Male   Fem", sjis=True),
    TLWord(0x3aa9b, 26, "Select your race.      ", sjis=True),
    TLWord(0x3aabd, 4, "help", sjis=True),
    TLWord(0x3aac8, 8, "Human", sjis=True),
    TLWord(0x3aad3, 10, "Elven  ", sjis=True),
    TLWord(0x3aafe, 4, "Hum", sjis=True),
    TLWord(0x3ab04, 6, "Elf", sjis=True),
    TLWord(0x3ab0c, 10, "Dwarf  ", sjis=True),
    TLWord(0x3ab18, 16, "Grassru", sjis=True),
    TLWord(0x3ab2a, 12, "Half Elf", sjis=True),
    TLWord(0x3ab80, 6, "Human", sjis=True),
    TLWord(0x3ab89, 30, "Has average stats, but can ", sjis=True),
    TLWord(0x3abaa, 30, "train up ability scores.", sjis=True),
    TLWord(0x3abcc, 6, "Elf", sjis=True),
    TLWord(0x3abd7, 32, "Excellent with magic, but", sjis=True),
    TLWord(0x3abfa, 30, "weak in body. Cannot be", sjis=True),
    TLWord(0x3ac1b, 24, "Priest class.", sjis=True),
    TLWord(0x3ac37, 10, "Dwarf", sjis=True),
    TLWord(0x3ac46, 30, "Hardy in body and mind.", sjis=True),
    TLWord(0x3ac67, 28, "Cannot be Sorcerer or", sjis=True),
    TLWord(0x3ac86, 26, "Shaman classes.", sjis=True),
    TLWord(0x3aca4, 16, "Grassrunner", sjis=True),
    TLWord(0x3acb9, 30, "Agile, dextrous race.", sjis=True),
    TLWord(0x3acda, 30, "Cannot learn classes that", sjis=True),
    TLWord(0x3acfb, 12, "use magic.", sjis=True),
    TLWord(0x3ad0b, 12, "Half Elf", sjis=True),
    TLWord(0x3ad1c, 28, "Halfway between human and", sjis=True),
    TLWord(0x3ad3b, 30, "elf. Abilities change ", sjis=True),
    TLWord(0x3ad5c, 16, "based on origin.", sjis=True),
    TLWord(0x3ad82, 20, "Ability distr.?  ", sjis=True),
    TLWord(0x3ad99, 6, "Auto ", sjis=True),
    TLWord(0x3ada0, 10, "Manual ", sjis=True),
    TLWord(0x3adad, 4, "help", sjis=True),
    TLWord(0x3adc8, 6, "Auto ", sjis=True),
    TLWord(0x3add3, 30, "Auto-roll for stats, ", sjis=True),
    TLWord(0x3adf4, 24, "birth, money, etc.", sjis=True),
    TLWord(0x3ab68, 4, "help", sjis=True),
    TLWord(0x3ae10, 10, "Manual ", sjis=True),
    TLWord(0x3ae1f, 28, "Player performs all", sjis=True),
    TLWord(0x3ae3e, 32, "character creation rolls. ", sjis=True),
    TLWord(0x3ae62, 28, "Auto Stat Creation ", sjis=True),
    TLWord(0x3ae82, 32, "Manual Stat Creation ", sjis=True),
    TLWord(0x3af47, 6, "Dex  ", sjis=True),
    TLWord(0x3af50, 6, "Agil ", sjis=True),
    TLWord(0x3af59, 4, "Int", sjis=True),
    TLWord(0x3af60, 4, "Str", sjis=True),
    TLWord(0x3af67, 6, "Life ", sjis=True),
    TLWord(0x3af70, 6, "Mentl", sjis=True),
    TLWord(0x3af7a, 6, "Birth", sjis=True),
    TLWord(0x3af84, 6, "Money", sjis=True),
    TLWord(0x3af8e, 4, "OK", sjis=True),
    TLWord(0x3af97, 4, "help", sjis=True),
    #能力値や生まれ、所持金なと゛の
    # 3b440 birth etc.

    TLWord(0x0003B444, 6, "Dex  ", sjis=True),
    TLWord(0x0003B44B, 6, "Agil ", sjis=True),
    TLWord(0x0003B452, 4, "Int", sjis=True),
    TLWord(0x0003B457, 4, "Str", sjis=True),
    TLWord(0x0003B45C, 6, "Life ", sjis=True),
    TLWord(0x0003B463, 6, "Mentl", sjis=True),
    TLWord(0x0003B46D, 6, "Money", sjis=True),
    TLWord(0x0003B47D, 8, "Skills ", sjis=True),
    TLWord(0x0003B488, 18, "Is this ok?  ", sjis=True),
    TLWord(0x0003B4B2, 6, "Birth", sjis=True),
    TLWord(0x0003B4D2, 4, "Brb", sjis=True),
    TLWord(0x0003B4D7, 8, "Wizard ", sjis=True),
    TLWord(0x0003B4E0, 4, "Ev", sjis=True),
    TLWord(0x0003B4E5, 4, "Trv", sjis=True),
    TLWord(0x0003B4EA, 4, "Hnt", sjis=True),
    TLWord(0x0003B4EF, 8, "Citizen", sjis=True),
    TLWord(0x0003B4F8, 10, "Scholar", sjis=True),
    TLWord(0x0003B503, 4, "Mrc", sjis=True),
    TLWord(0x0003B508, 4, "Pri", sjis=True),
    TLWord(0x0003B50D, 6, "Shmn ", sjis=True),
    TLWord(0x0003B514, 10, "Kn/Noble", sjis=True),
    TLWord(0x0003B64B, 26, "Select skills", sjis=True),
    TLWord(0x0003B6E1, 4, "help", sjis=True),
    TLWord(0x0003BFAC, 16, "Save character ", sjis=True),
    TLWord(0x0003C03A, 6, "Dex  ", sjis=True),
    TLWord(0x0003C041, 6, "Agil ", sjis=True),
    TLWord(0x0003C048, 4, "Int", sjis=True),
    TLWord(0x0003C04D, 4, "Str", sjis=True),
    TLWord(0x0003C052, 6, "Life ", sjis=True),
    TLWord(0x0003C059, 6, "Mentl", sjis=True),
    TLWord(0x0003C060, 6, "Money", sjis=True),
    TLWord(0x0003C073, 8, "Record ", sjis=True),
    TLWord(0x0003C07C, 8, "Remake ", sjis=True),
    TLWord(0x0003C087, 4, "M  ", sjis=True),
    TLWord(0x0003C08F, 4, "F", sjis=True),

    TLWord(0x0003B739, 32, "Can equip up to Str. ", sjis=True),
    TLWord(0x0003B72C, 10, "Fighter", sjis=True),
    TLWord(0x0003B767, 14, "No restricts ", sjis=True),
    TLWord(0x0003B779, 6, "Thief", sjis=True),
    TLWord(0x0003B784, 28, "Good with traps and doors. ", sjis=True),
    TLWord(0x0003B7A3, 30, "Can't use heavy equipment. ", sjis=True),
    TLWord(0x0003B7D0, 12, "Ranger ", sjis=True),
    TLWord(0x0003B7E1, 22, "Skill for outdoors.", sjis=True),
    TLWord(0x0003B7FA, 32, "Mainly uses thrown weapons.", sjis=True),
    TLWord(0x0003B81D, 26, "No melee skill.", sjis=True),
    TLWord(0x0003B83B, 8, "Sage ", sjis=True),
    TLWord(0x0003B848, 30, "Has varied knowledge across", sjis=True),
    TLWord(0x0003B869, 20, "all disciplines.", sjis=True),
    TLWord(0x0003B880, 12, "No restrict", sjis=True),
    TLWord(0x0003B890, 10, "Bard ", sjis=True),
    TLWord(0x0003B89F, 28, "Knows music and performance", sjis=True),
    TLWord(0x0003B8BE, 30, "skills. Can use bard songs ", sjis=True),
    TLWord(0x0003B8DF, 24, "with spirit instruments.", sjis=True),
    TLWord(0x0003B8FB, 10, "Sorcerer ", sjis=True),
    TLWord(0x0003B90A, 30, "Can use ancient magic. ", sjis=True),
    TLWord(0x0003B92B, 30, "Requires a mage staff to ", sjis=True),
    TLWord(0x0003B94C, 26, "utilize spells. ", sjis=True),
    TLWord(0x0003B96A, 10, "Shaman ", sjis=True),
    TLWord(0x0003B979, 20, "Uses spirit magic. ", sjis=True),
    TLWord(0x0003B990, 32, "Needs both hands to", sjis=True),
    TLWord(0x0003B9B3, 14, "cast spells.", sjis=True),
    TLWord(0x0003B9C5, 12, "Priest ", sjis=True),
    TLWord(0x0003B9D6, 20, "Uses holy magic. ", sjis=True),
    TLWord(0x0003B9ED, 12, "No restrict", sjis=True),

    TLWord(0x00024694, 8, "level ", sjis=True),
    TLWord(0x000246A2, 16, "increase? ", sjis=True),
    TLWord(0x000246E2, 6, "Thief", sjis=True),

    
    
    # TLWord(0x6cd07, 4, "Wt ", sjis=True),
    # TLWord(0x6cd0e, 8, "Items  ", sjis=True),
    # TLWord(0x6cd19, 4, "Atk", sjis=True),
    # TLWord(0x6cd20, 8, "Equip. ", sjis=True),
    # TLWord(0x6cd2b, 4, "Mag", sjis=True),
    # TLWord(0x6cd32, 10, "Status   ", sjis=True),

    # TLWord(0x6ce55, 14, "Encounter!!", sjis=True),
    TLWord(0x6de7e, 8, "Talk ", sjis=True),
    TLWord(0x6de87, 8, "Heal ", sjis=True),
    TLWord(0x6de92, 8, "Destone", sjis=True),
    TLWord(0x6de9d, 6, "Reviv", sjis=True),
    # TLWord(0x6e725, 16, "Mage Staff", sjis=True),

    # TLWord(0x6f11a, 10, "Harp ", sjis=True),
    # TLWord(0x6f12b, 8, "Lute ", sjis=True),
    # TLWord(0x6f13a, 10, "Flute", sjis=True),

    # TLWord(0x6f9cf, 6, "M.Stn", sjis=True),
    # TLWord(0x6f9d6, 8, "FtrHrb", sjis=True),
    # TLWord(0x6f9df, 8, "Antidt", sjis=True),
    # TLWord(0x6f9e8, 8, "Tonic", sjis=True),
    # TLWord(0x6f9f1, 14, "Healstone", sjis=True),
    # TLWord(0x6fa00, 14, "Heal Rod", sjis=True),
    # TLWord(0x6fa0f, 10, "MagYarn", sjis=True),
    # TLWord(0x6fa1a, 12, "WingStatue", sjis=True),
    # TLWord(0x6fa27, 10, "MageHeart", sjis=True),
    # TLWord(0x6fa32, 10, "ThiefWis", sjis=True),
    # TLWord(0x6fa3d, 14, "MyriiCharm", sjis=True),
    # TLWord(0x6fa4c, 14, "MarfaCharm", sjis=True),
    # TLWord(0x6fa5b, 14, "RahdaTeach", sjis=True),
    # TLWord(0x6fa6a, 16, "ChaZaTeach", sjis=True),
    # TLWord(0x6fa7b, 4, "Hly", sjis=True),
    # TLWord(0x6fa80, 18, "Cloud Egg", sjis=True),
    # TLWord(0x6fa93, 14, "Charm Ring ", sjis=True),
    # TLWord(0x6faa2, 10, "WindStone", sjis=True),
    # TLWord(0x6faad, 10, "FireStone", sjis=True),
    # TLWord(0x6fab8, 10, "WatrStone", sjis=True),
    # TLWord(0x6fac3, 10, "Ice Stone", sjis=True),
    # TLWord(0x6face, 14, "WindCrystal", sjis=True),
    # TLWord(0x6fadd, 16, "EartCrystal", sjis=True),
    # TLWord(0x6faee, 14, "WatrCrystal", sjis=True),
    # TLWord(0x6fafd, 14, "FireCrystal", sjis=True),
    # TLWord(0x6fb0c, 14, "DarkCrystal", sjis=True),
    # TLWord(0x6fb1b, 14, "Ice Crystal", sjis=True),
    # TLWord(0x6fb2a, 4, "Mrc", sjis=True),
    # TLWord(0x6fb30, 4, "Gem", sjis=True),
    # TLWord(0x6fb35, 8, "Dress", sjis=True),
    # TLWord(0x6fb3e, 10, "Necklace ", sjis=True),
    # TLWord(0x6fb49, 14, "Bracelet ", sjis=True),
    # TLWord(0x6fb58, 8, "Tiara", sjis=True),
    # TLWord(0x6fb61, 10,"Opal ", sjis=True),
    # TLWord(0x6fb6b, 12,"RandDrug ", sjis=True),
    # TLWord(0x6fb78, 8, "HeroBa", sjis=True),
    
    # TLWord(0x6fcfe, 8, "Talk ", sjis=True),
    # TLWord(0x6fd07, 12, "Hire merc", sjis=True),
    # TLWord(0x6fd68, 20, "Hire a mercenary?", sjis=True),

    # TLWord(0x70fc8, 55, "Let me know if you see \x04anything strange. ", sjis=True),
    
]
