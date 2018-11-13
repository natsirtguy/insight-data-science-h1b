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

# Approach

Use the collections.Counter object from the Python standard library to
count the number of occurrences of the occupations and states as we
parse the input data files.

# Run instructions

After placing the appropriate input files in the `input` directory,
execute `run.sh` to run the script. The `output` directory will
contain the resulting files.

<!--  LocalWords:  md sh
 -->
