'''Script to analyze H1B visa application information.'''
import sys
from getopt import getopt
from h1b_counting import read_visas, MissingFieldError


if __name__ == "__main__":
    opts, input_output_files = getopt(sys.argv[1:], '')
    try:
        input_file = input_output_files[0]
        output_file1 = input_output_files[1]
        output_file2 = input_output_files[2]
    except IndexError:
        print('Plese specify one input and two output files.')
        exit()
else:
    print('This program is meant to be run as a script. '
          'Call it using `python3 h1b_script input_file '
          'output_file1 output_file2.')
    exit()

# The conventions for the name of the occupation and state fields
# changes from year two year. This will handle the two cases in the
# given input data.
try:
    with open(input_file, 'r') as visas:
        top_10s = read_visas(visas,
                             {'SOC_NAME': 'OCCUPATIONS',
                              'WORKSITE_STATE': 'STATES'})
        with open(output_file1, 'w') as occupation_file:
            occupation_file.write(top_10s['OCCUPATIONS'])
        with open(output_file2, 'w') as state_file:
            state_file.write(top_10s['STATES'])
except MissingFieldError:
    # According to the file structure documentation at
    # https://www.foreignlaborcert.doleta.gov/performancedata.cfm, the
    # FY2008 information has yet another format for the fields.
    try:
        with open(input_file, 'r') as visas:
            top_10s = read_visas(visas,
                                 {'OCCUPATIONAL_TITLE': 'OCCUPATIONS',
                                  'WORKLOC1_STATE': 'STATES'})
            with open(output_file1, 'w') as occupation_file:
                occupation_file.write(top_10s['OCCUPATIONS'])
            with open(output_file2, 'w') as state_file:
                state_file.write(top_10s['STATES'])
    except MissingFieldError:
        with open(input_file, 'r') as visas:
            top_10s = read_visas(visas,
                                 {'SOC_NAME': 'OCCUPATIONS',
                                  'STATE_1': 'STATES'})
            with open(output_file1, 'w') as occupation_file:
                occupation_file.write(top_10s['OCCUPATIONS'])
            with open(output_file2, 'w') as state_file:
                state_file.write(top_10s['STATES'])
