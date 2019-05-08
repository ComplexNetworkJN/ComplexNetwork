#!/bin/bash


/home/sana/bin/resnik -a human-mouse.align > ./result_human_mouse.txt
/home/sana/bin/resnik -a human-rat.align > ./result_human_rat.txt
/home/sana/bin/resnik -a mouse-rat.align > ./result_mouse_rat.txt

sh resnik_result.sh > resnik_result_iid3.txt
python3 format_resnik_result.py
rm resnik_result_iid5.txt
