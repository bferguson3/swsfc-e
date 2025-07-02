## Sword World SFC 1/2 tools

Expects "swsfc-e.sfc" in project folder. Original Japanese ROM checksum is 0xC11B. 

### extract.py
dumps script text only to json for sfc1

### extract2.py
dumps script text only to json for sfc2

### reinsert.py
reinserts json and tlbank.py to sfc1
note: binary edits not included, output file will not be complete. run binary_edits.ips FIRST.

### reinsert2.py
[coming soon]

### file list
- 8x16romaji.png: actually 6x16, used for translation
- f8000bank.png: bitmap text for sfc1
- binary_edits.ips: will change an unedited SFC1 rom into one ready for reinsert.py
- *.ips: current IPS (if you need a cmd line patcher: https://github.com/bferguson3/pips)
- *_dump.json: script dumps (does not include system text)
- *.tbl: character tables 
- swsfcman-eng.txt: WIP translation of SFC1 manual
- tlbank.py: inline text bank
- tool.html: script (json) translation tool 

