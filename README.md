# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run instructions](README.md#run-instructions)

# Problem

Given files with H1B visa application data, determine and report on
the 10 most common occupations among certified applications and the 10
states with the most certified applications. The first line of the
input file contains the fields for each of the subsequent lines, each
of which corresponds to a single application.
n
# Approach

Use the collections.Counter object from the Python standard library to
count the number of occurrences of the occupations and states as we
parse the input data files using the csv.reader object, also from the
Python standard library.

# Run instructions

After placing the semicolon-separated input file in the `input`
directory and naming it `h1b_input.csv` , execute `run.sh` to run the
script. The `output` directory will contain two files.
`top_10_states.txt` will contain a list of the top 10 most common
states for certified H1B applications according to the input file,
while ``top_10_occupations.txt`` will contain a list of the top 10
most common occupations for certified H1B applications according to
the input file. Note that the occupations will be in uppercase.

<!--  LocalWords:  md sh csv txt
 -->
