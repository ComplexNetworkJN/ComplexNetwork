#!/bin/bash
#rename .txt .align *.txt # only when not using converse.py
sh max_result.sh > max_result_iid5.txt
python3 format_max_result.py
rm max_result_iid5.txt
