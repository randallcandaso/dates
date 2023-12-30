'''

File: dates.py
Author: Randall Candaso
Course/Section: CSC 120-002
Purpose: This program takes an inputted file that contains
specific dates and events. Depending on what the file asks,
the program is able to store or return events for a specific date
inputted.

'''

import sys

class Date:

    def __init__(self, date, event):
        '''

        Parameter: date - inputted date to be read
        event - inputted event to be matched with the
        date

        Initializes the date and event variables. Also
        initializes a list.

        '''
        self._day = date
        self._event = event
        self._list = self.add_event()

    def add_event(self):
        '''

        Creates a list for the date, containing a
        specific event.

        return: the created list

        '''
        self._collection = []
        self._collection.append(self._event)
        return self._collection

    def collection(self):
        '''

        Return: the date variable and its matching
        list

        '''
        return self._day, self._list

    def __str__(self):
        '''

        Return: A string matching the date and the
        specific event

        '''
        return "{}: {}".format(self._day, self._event)


class DateSet:
    def __init__(self):
        '''

        Creates an empty dictionary

        '''
        self._empty = {}

    def add_date(self, date, collection):
        '''

        Parameter: date - inputted date to be read
        collection - a list containing an event
        occuring on that date

        Determines whether or not the date is already
        stored in the dictionary, then stores an event
        into the dictionary using that date.

        '''
        if date not in self._empty:
            self._empty[date] = collection
        else:
            self._empty[date].insert(0, collection[0])

    def events(self, date):
        '''

        Parameter: date - inputted date to be read

        Determines if the date is in the dictionary.

        Return: nothing if the date is not in the
        dictionary or returns all the events on that
        date

        '''
        if date not in self._empty:
            return
        else:
            return self._empty[date]

    def __str__(self, date):
        '''

        Parameter: date - inputted date to be read

        Return: A string formatted with the date and its
        events.

        '''
        return "{}: {}".format(date, self._empty[date])


def main():
    file = input()
    reading(file)


def reading(file):
    '''

    Parameter: file - the inputted file containing
    dates to be read

    Reads in the inputted file, splits each line and
    determines whether the line should be stored or
    given values to print back out.

    '''
    to_read = open(file, 'r')
    new = DateSet()
    for i in to_read.readlines():
        check = i.split(' : ')
        temporary = []
        part_1 = None
        if len(check) > 1:
            temporary = check
            part_1 = temporary[0].split()
        else:
            x = check[0].split(':')
            for i in x:
                temporary.append(i)
            part_1 = temporary[0].split()
        if part_1[0] == 'I':
            temp_1, temp_2 = addition(temporary, part_1)
            new.add_date(temp_1, temp_2)
        elif part_1[0] == 'R':
            current, canonical = returning(part_1, new)
            empty = []
            for i in sorted(current):
                print("{}: {}".format(canonical, i))
        else:
            print('Error - Illegal operation.')


def addition(temporary, part_1):
    '''

    Splits the read-in line

    :param temporary: unorganized, inputted line
    :param part_1: temporarily organized version
    of the line
    :return: specific date and list of events
    '''
    if len(temporary) >= 3:
        part_2 = temporary[1].lstrip(' ') + ':'
        part_2 += temporary[2].rstrip('\n')
    else:
        part_2 = temporary[1].lstrip(' ').lstrip('\t').\
            rstrip('\n')
    canonical = ''
    blank = ''
    if len(part_1) == 4:
        for i in range(1, len(part_1), 1):
            if i + 1 == len(part_1):
                blank += part_1[i]
            else:
                blank += part_1[i] + ' '
        canonical += convert(blank)
    else:
        canonical += convert(part_1[1])
    one_date = Date(canonical, part_2)
    temp_1, temp_2 = one_date.collection()
    return temp_1, temp_2


def returning(line, new):
    '''

    Reads in the date on the given line, and
    returns the events that are stored in the
    date contained in the DataSet object.

    :param line: desired date for events
    :param new: DateSet object
    :return: converted date and list of
    events
    '''
    canonical = ''
    blank = ''
    if len(line) == 4:
        for i in range(1, len(line), 1):
            if i + 1 == len(line):
                blank += line[i]
            else:
                blank += line[i] + ' '
        canonical += convert(blank)
    else:
        canonical += convert(line[1])
    current = new.events(canonical)
    if current == None:
        sys.exit(0)
    else:
        return current, canonical


def convert(date_str):
    '''

    Parameter: date_str - a string containing a date

    Takes a date string and converts it to a
    canonical date that can be used in a later dictionary

    Return: a canonical date string

    '''
    months = {'Jan': 1, "Feb": 2, 'Mar': 3, 'Apr': 4,
              'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
              'Nov': 11, 'Dec': 12}
    if '/' in date_str:
        new = date_str.split('/')
    elif '-' in date_str:
        new = date_str.split('-')
    else:
        new = date_str.split()
    mm = ''
    dd = ''
    yyyy = ''
    i = 0
    while i < len(new):
        if new[i].isalpha() == True:
            mm += str(months[new[i]])
            dd += new[i + 1]
            yyyy += new[i + 2]
            i = len(new)
        else:
            if int(new[i]) > 31:
                yyyy += new[i]
                mm += new[i + 1]
                dd += new[i + 2]
                i = len(new)
            else:
                mm += new[i]
                dd += new[i + 1]
                yyyy += new[i + 2]
                i = len(new)
    return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm),
                                   int(dd))


main()