'''Analyze H1B visa application information.'''

from collections import Counter


def read_visas(visas, fields):
    '''Process a file object with visa application information.

    Args:
      visas: file_object, first line has fields of visa information and
        remaining lines contain instances of applications.
      fields: tuple with strings of fields to be processed.

    Returns:
      top10s: tuple containing strings with information on the top 10
        most common occurences of fields in the visa file.
    '''
    return
