f = open("swsfc2-j.sfc", "rb")
rombytes = f.read()
f.close()

i = 0
_len = 0
while i < len(rombytes) - 1:
    try:
        _sb = bytes([rombytes[i], rombytes[i+1]])
        if(_sb[0] >= 0x80):
            try:
                _sb = _sb.decode("sjis")# == '誰'):
                if(len(_sb) == 1):
                    print(_sb, end="")
                    _len += 1
                else:
                    if(_len > 1):
                        print(", ", hex(i))
                    _len = 0
                i += 1
            except Exception as e:
                i += 1
                continue
        if(_sb[0] < 0x20):
            if(_len > 1):
                print("{" + hex(_sb[0]) + "}", end="")
            
    except Exception as e:
        i += 1
        continue
    i += 1