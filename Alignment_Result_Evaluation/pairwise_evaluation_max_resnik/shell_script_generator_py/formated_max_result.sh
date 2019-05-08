#!/bin/bash
sh max_result.sh > max_result_iid11.txt
python3 format_max_result.py
rm max_result_iid11.txt
