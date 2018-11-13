'''Analyze H1B visa application information.'''

from collections import Counter


def read_visas(visas, fields, top_10_names):
    '''Process a file object with visa application information.

    Args:
      visas: file_object, first line has fields of visa information and
        remaining lines contain instances of applications.
      fields: tuple with strings of fields to be processed.

    Returns:
      top_10s: tuple containing strings with information on the top 10
        most common occurrences of fields in the visa file.
    '''

    # Find the fields in the file, and casefold them.
    first_line = next(visas)
    file_fields = first_line.strip().split(';')
    file_fields = [field.casefold() for field in file_fields]

    # Find the indices of the requested fields.
    field_idxs = {field: file_fields.index(field.casefold())
                  for field in fields}

    # Create counter objects for the fields.
    field_counters = {field: Counter() for field in fields}

    # Iterate through the remaining lines of the file, incrementing
    # the counter for the appropriate fields.
    for visa in visas:
        record = visa.strip().split(';')
        # Ignore empty lines.
        if len(record) > 1:
            for field in fields:
                field_counter = field_counters[field]
                field_idx = field_idxs[field]
                field_content = record[field_idx]  # Content of the record.
                field_counter[field_content] += 1

    # Process the counters to produce the output strings.
    top_10s = produce_top_10s(field_counters, top_10_names)

    return top_10s


def produce_top_10s(counters, top_10_names):
    '''Produce strings of top 10 info from counters.

    Args:
      counters: dictionary of Counter objects.
      top_10_names: tuple of names for the output file.

    Returns:
      tops_10s: tuple of strings with information about the top 10 items in
        each field.
    '''

    return
