f = open("swsfc2-j.sfc", "rb")
inby = f.read()
f.close()

i = 0
while i < len(inby):
    if inby[i+1] == inby[i]+0x13:
        if inby[i+2] == inby[i]-0x1a:
            if inby[i+3]== inby[i]-0xc:
                print(hex(i), "possible faita")
    i += 1