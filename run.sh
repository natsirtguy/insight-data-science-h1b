#!/bin/bash
#
# Execute the python script to generate the occupation and state files.

python3 ./src/h1b_script.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
