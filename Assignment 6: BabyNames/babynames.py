"""
File: babynames.py
------------------
This program builds and populates the name_data dictionary for storing our data
from a list of filenames.
The dictionary is formed as {name : {year : rank}}
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dictionary.

    Input:
        name_data (dictionary): dict holding baby name data
        year (int): the year of the data entry to add
        rank (int): the rank of the data entry to add
        name (str): the name of the data entry to add

    >>> name_data = {}
    >>> add_data_for_name(name_data, 2000, 10, 'Nick')
    >>> name_data
    {'Nick': {2000: 10}}
    >>> add_data_for_name(name_data, 2000, 200, 'Sonja')
    >>> name_data
    {'Nick': {2000: 10}, 'Sonja': {2000: 200}}
    """
    if name in name_data:
        if year in name_data[name]:
            if name_data[name][year] > rank:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
    else:
        name_data[name] = {}
        name_data[name][year] = rank

def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dictioary with the data found in the file.

    Input:
        name_data (dictionary): dictionary holding baby name data
        filename (str): name of the file holding baby name data

    >>> name_data = {}
    >>> add_file(name_data, 'data/small/small-2000.txt')
    >>> name_data
    {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> name_data = {}
    >>> add_file(name_data, 'data/small/small-2010.txt')
    >>> name_data
    {'C': {2010: 1}, 'D': {2010: 1}, 'A': {2010: 2}, 'E': {2010: 2}}
    >>> name_data = {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> add_file(name_data, 'data/small/small-2010.txt')
    >>> name_data
    {'A': {2000: 1, 2010: 2}, 'B': {2000: 1}, 'C': {2000: 2, 2010: 1}, 'D': {2010: 1}, 'E': {2010: 2}}
    """
    with open(filename) as file:
        year = int(file.readline().strip())
        for line in file:
            line = line.strip()
            items = line.split(',')
            rank = int(items[0].strip())
            boy_name = items[1].strip()
            girl_name = items[2].strip()
            add_data_for_name(name_data, year, rank, boy_name)
            add_data_for_name(name_data, year, rank, girl_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dictionary and then returns that dictionary.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dictionary): the dictionary storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dictionary that stores baby name information and a target string,
    returns a list of all names in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dictionary): a dictionary containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    target = target.lower()
    matching_names = []
    for name in name_data:
        if target in name.lower():
            matching_names.append(name)
    return matching_names


def print_names(name_data):
    """
    (This function is provided for you)
    Given a name_data dictionary, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dictionary): a dictionary containing baby name data organized by name
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (This function is provided for you)

    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
