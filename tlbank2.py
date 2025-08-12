
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
#誰か゛レヘ゛ルアッフ゜しますか？
#FQRSPTUPV
