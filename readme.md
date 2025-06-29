## Sword World SFC 1/2 tools

Expects "swsfc-e.sfc" in project folder. Original Japanese ROM checksum is 0xC11B. 

### extract.py
dumps script text only to json for sfc1

### extract2.py
dumps script text only to json for sfc2

### reinsert.py
reinserts json and tlbank.py to sfc1
note: binary edits not included, output file will not be complete

### reinsert2.py
[coming soon]

### file list
- 8x16romaji.png: actually 6x16, used for translation
- f8000bank.png: bitmap text for sfc1
- *.ips: current IPS (reports that the output IPS may not be good, beware)
- *_dump.json: script dumps (does not include system text)
- *.tbl: character tables 
- swsfcman-eng.txt: WIP translation of SFC1 manual
- tlbank.py: inline text bank
- tool.html: script (json) translation tool 

