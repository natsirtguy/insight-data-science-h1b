'''Script to analyze H1B visa application information.'''
import sys
from getopt import getopt
from h1b_counting import read_visas


if __name__ == "__main__":
    opts, input_output_files = getopt(sys.argv[1:], '')
    try:
        input_file = input_output_files[0]
        output_files = input_output_files[1:]
    except IndexError:
        print('Plese specify input and output files.')
        exit()
else:
    print('This program is meant to be run as a script. '
          'Call it using `python3 h1b_script input_file '
          'output_file1 output_file2.')
    exit()

with open(input_file, 'r') as visas:
    top_10s = read_visas(visas,
                         {'SOC_NAME': 'OCCUPATIONS',
                          'WORKSITE_STATE': 'STATES'})
    with open(output_files[0], 'w') as occupation_file:
        occupation_file.write(top_10s['OCCUPATIONS'])
    with open(output_files[1], 'w') as state_file:
        state_file.write(top_10s['STATES'])
