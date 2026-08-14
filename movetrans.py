# moves translations from one file to another (for redumps)
import sys,os,json

f = open("swsfc2_dump.json", "r", encoding="utf-8")
oldjs = f.read()
f.close()
oldjs = json.loads(oldjs)

f = open("swsfc2_dump_new.json", "r", encoding="utf-8")
newjs = f.read()
f.close()
newjs = json.loads(newjs)

for f in oldjs:
    _fn = ""
    _ln = ""
    for k in oldjs[f]:
        _fn = f 
        _ln = k["address"]
        tra = k["translation"]
        for m in newjs:
            if m == _fn:
                for nk in newjs[m]:
                    if _ln == nk["address"]:
                        nk["translation"] = tra 
                        break
                break

print(json.dumps(newjs, ensure_ascii=False))