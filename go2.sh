mv ../swsfc2_dump.json ./
./makeips ./swsfc2-j.sfc ./swsfc2-e.sfc
mv out.ips binary_edits2.ips
python3 ./reinsert2.py
#./makeips ./swsfc2-j.sfc ./swsfc2-e_out.sfc
#mv out.ips swsfc2-j.ips
#echo renamed swsfc2-j.ips.
echo did not make final ips 