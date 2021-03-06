'''Functions to analyze H1B visa application information.'''

import csv
from collections import Counter


def read_visas(visas, fields):
    '''Process a file object with visa application information.

    Args:
      visas: file_object, first line has fields of visa information and
        remaining lines contain instances of applications.
      fields: dictionary with strings of fields to be processed as
        keys and names of those fields in the output file as values.

    Returns:
      top_10s: dictionary containing strings with information on the top 10
        most common occurrences of fields in the visa file.

    '''

    # Use csv reader to parse file.
    visa_reader = csv.reader(visas, delimiter=';', quotechar='"')

    # Find the fields in the file.
    file_fields = next(visa_reader)

    # Find the index of field with STATUS in the name.
    for idx, file_field in enumerate(file_fields):
        if "STATUS" in file_field.upper():
            case_idx = idx
            break
    else:
        raise MissingFieldError("STATUS field not found in csv header.")

    # Find the indices of the requested fields.
    field_idxs = {}
    for field in fields:
        for idx, file_field in enumerate(file_fields):
            if field.upper() in file_field.upper():
                field_idxs[field] = idx
                break
        else:
            raise MissingFieldError("Field not found in csv header.")

    # Create counter objects for the fields.
    field_counters = {field: Counter() for field in fields}

    # Iterate through the remaining lines of the file, incrementing
    # the counter for the appropriate fields.
    n_certified = 0
    for record in visa_reader:
        # Ignore empty lines and uncertified applications.
        if len(record) > 1 and record[case_idx].upper() == 'CERTIFIED':
            n_certified += 1
            for field in fields:
                field_counter = field_counters[field]
                field_idx = field_idxs[field]
                field_content = record[field_idx]  # Content of the record.
                # Only include nonempty fields.
                if field_content != '':
                    field_counter[field_content] += 1

    # Process the counters to produce the output strings.
    top_10s = produce_top_10s(field_counters, fields, n_certified)

    return top_10s


def produce_top_10s(counters, fields, n_certified):
    '''Produce strings of top 10 info from counters.

    Args:
      counters: dictionary of Counter objects.
      fields: dictionary with strings of fields to be processed as
        keys and names of those fields in the output file as values.
      n_certified: int, the total number of certified applications.

    Returns:
      tops_10s: list of strings with information about the top 10 items in
        each field.
    '''

    # Find the 10 most common field values in the counters.
    top_10s = {}
    for field in fields:
        counter = counters[field]
        output_name = fields[field].upper()

        # To sort the field values, we use the fact that sorting on a
        # tuple compares first entry, then the next, and so on.
        sorted_field_values = sorted(
            counter, key=lambda x: (-counter[x], x))
        top_10_values = sorted_field_values[:10]

        # For each field, create lists with top 10 counts and fractions.
        top_10_counts = [counter[value] for value in top_10_values]
        top_10_fractions = [count/n_certified for count in top_10_counts]

        # Create the header of the output.
        header = ('TOP_' + output_name + ';' +
                  'NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

        # Create the body of the output.
        body = '\n'.join('{};{};{:2.1%}'.format(value.upper(), count, fraction)
                         for value, count, fraction
                         in zip(top_10_values,
                                top_10_counts,
                                top_10_fractions))

        # Create the output.
        top_10s[output_name] = header + body + '\n'

    return top_10s


class MissingFieldError(Exception):
    '''Raise this error if a required field does not exist in the csv.'''
    pass
