#!/bin/bash

/home/sana/bin/resnik -a cow-dog.align > ./result_cow_dog.txt
/home/sana/bin/resnik -a cow-human.align > ./result_cow_human.txt
/home/sana/bin/resnik -a cow-mouse.align > ./result_cow_mouse.txt
/home/sana/bin/resnik -a cow-rat.align > ./result_cow_rat.txt
/home/sana/bin/resnik -a dog-human.align > ./result_dog_human.txt
/home/sana/bin/resnik -a dog-mouse.align > ./result_dog_mouse.txt
/home/sana/bin/resnik -a dog-rat.align > ./result_dog_rat.txt
/home/sana/bin/resnik -a human-mouse.align > ./result_human_mouse.txt
/home/sana/bin/resnik -a human-rat.align > ./result_human_rat.txt
/home/sana/bin/resnik -a mouse-rat.align > ./result_mouse_rat.txt

sh resnik_result.sh > resnik_result_iid5.txt
python3 format_resnik_result.py
rm resnik_result_iid5.txt
