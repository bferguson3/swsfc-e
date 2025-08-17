
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

words = [ 
    TLWord(0x23ced, 32, "Who will level up? ", sjis=True),
    
    TLWord(0x24277, 6, "Dex. ", sjis=True),
    TLWord(0x24290, 6, "Agil.", sjis=True),
    TLWord(0x242a9, 6, "Int. ", sjis=True),
    TLWord(0x242c2, 6, "Str. ", sjis=True),
    TLWord(0x242db, 6, "Life ", sjis=True),
    TLWord(0x242f4, 6, "Ment.", sjis=True),
    
    TLWord(0x6cd07, 4, "Wt ", sjis=True),
    TLWord(0x6cd0e, 8, "Items  ", sjis=True),
    TLWord(0x6cd19, 4, "Atk", sjis=True),
    TLWord(0x6cd20, 8, "Equip. ", sjis=True),
    TLWord(0x6cd2b, 4, "Mag", sjis=True),
    TLWord(0x6cd32, 10, "Status   ", sjis=True),

    TLWord(0x6ce55, 14, "Encounter!!", sjis=True),

    TLWord(0x6e725, 16, "Mage Staff", sjis=True),

    TLWord(0x6f11a, 10, "Harp ", sjis=True),
    TLWord(0x6f12b, 8, "Lute ", sjis=True),
    TLWord(0x6f13a, 10, "Flute", sjis=True),

    TLWord(0x6f9cf, 6, "M.Stn", sjis=True),
    TLWord(0x6f9d6, 8, "FtrHrb", sjis=True),
    TLWord(0x6f9df, 8, "Antidt", sjis=True),
    TLWord(0x6f9e8, 8, "Tonic", sjis=True),
    TLWord(0x6f9f1, 14, "Healstone", sjis=True),
    TLWord(0x6fa00, 14, "Heal Rod", sjis=True),
    TLWord(0x6fa0f, 10, "MagYarn", sjis=True),
    TLWord(0x6fa1a, 12, "WingStatue", sjis=True),
    TLWord(0x6fa27, 10, "MageHeart", sjis=True),
    TLWord(0x6fa32, 10, "ThiefWis", sjis=True),
    TLWord(0x6fa3d, 14, "MyriiCharm", sjis=True),
    TLWord(0x6fa4c, 14, "MarfaCharm", sjis=True),
    TLWord(0x6fa5b, 14, "RahdaTeach", sjis=True),
    TLWord(0x6fa6a, 16, "ChaZaTeach", sjis=True),
    TLWord(0x6fa7b, 4, "Hly", sjis=True),
    TLWord(0x6fa80, 18, "Cloud Egg", sjis=True),
    TLWord(0x6fa93, 14, "Charm Ring ", sjis=True),
    TLWord(0x6faa2, 10, "WindStone", sjis=True),
    TLWord(0x6faad, 10, "FireStone", sjis=True),
    TLWord(0x6fab8, 10, "WatrStone", sjis=True),
    TLWord(0x6fac3, 10, "Ice Stone", sjis=True),
    TLWord(0x6face, 14, "WindCrystal", sjis=True),
    TLWord(0x6fadd, 16, "EartCrystal", sjis=True),
    TLWord(0x6faee, 14, "WatrCrystal", sjis=True),
    TLWord(0x6fafd, 14, "FireCrystal", sjis=True),
    TLWord(0x6fb0c, 14, "DarkCrystal", sjis=True),
    TLWord(0x6fb1b, 14, "Ice Crystal", sjis=True),
    TLWord(0x6fb2a, 4, "Mrc", sjis=True),
    TLWord(0x6fb30, 4, "Gem", sjis=True),
    TLWord(0x6fb35, 8, "Dress", sjis=True),
    TLWord(0x6fb3e, 10, "Necklace ", sjis=True),
    TLWord(0x6fb49, 14, "Bracelet ", sjis=True),
    TLWord(0x6fb58, 8, "Tiara", sjis=True),
    TLWord(0x6fb61, 10,"Opal ", sjis=True),
    TLWord(0x6fb6b, 12,"RandDrug ", sjis=True),
    TLWord(0x6fb78, 8, "HeroBa", sjis=True),
    
    TLWord(0x6fcfe, 8, "Talk ", sjis=True),
    TLWord(0x6fd07, 12, "Hire merc", sjis=True),
    TLWord(0x6fd68, 20, "Hire a mercenary?", sjis=True),

    TLWord(0x70fc8, 55, "Let me know if you see \x04anything strange. ", sjis=True),
    
]
