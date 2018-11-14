#!/bin/bash
#
# Execute the python script to investigate the top 10 most common
# occupations and states for certified H1B visa applications.
#
# To perform the analysis on a new dataset, place it in the ./input/
# directory and name the file h1b_input.csv.

python3 ./src/h1b_script.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
