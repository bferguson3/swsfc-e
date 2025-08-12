
class TLWord():
    def __init__(self, _loc, _len, _tl, buff=True, sjis=False):
        self.loc = _loc 
        self.len = _len 
        self.original = []
        self.translation = _tl
        self.sjis = sjis
    ###
###

words = []

words.append(TLWord(0x23ced, 32, "Who will level up? ", sjis=True))
words.append(TLWord(0x24277, 6, "Dex. ", sjis=True))
words.append(TLWord(0x24290, 6, "Agil.", sjis=True))
words.append(TLWord(0x242a9, 6, "Int. ", sjis=True))
words.append(TLWord(0x242c2, 6, "Str. ", sjis=True))
words.append(TLWord(0x242db, 6, "Life ", sjis=True))
words.append(TLWord(0x242f4, 6, "Ment.", sjis=True))