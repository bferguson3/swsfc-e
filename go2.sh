mv ../swsfc2_dump.json ./
python3 ./reinsert2.py
./makeips ./swsfc2-j.sfc ./swsfc2-e_out.sfc
mv out.ips swsfc2-j.ips
