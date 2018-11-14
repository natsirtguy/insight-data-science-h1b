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
states (given by their two-letter postal code abbreviations) for
certified H1B applications according to the input file, while
``top_10_occupations.txt`` will contain a list of the top 10 most
common occupations (given by their Standard Occupational
Classification names) for certified H1B applications according to the
input file.

After the first line, each line in the output files will correspond to
a single state/occupation. The line will contain the state/occupation,
its frequency count amongst the certified applications in the input
file, and its percentage of the total certified applications. These
fields will be separated by semicolons. The first line will contain
the titles of these three fields, also separated by semicolons. In
each case, the states/occupations will be listed in order of
decreasing frequency. When there are multiple states/occupations with
the same number of occurrences, the ordering will be alphabetical. If
there are fewer than 10 unique states/occupations in the input file,
the output files will only list the given states/occupations. Note
that the states/occupations will be in uppercase in the output files.

<!--  LocalWords:  md sh csv txt
 -->
