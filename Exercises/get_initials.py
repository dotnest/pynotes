# Write a program that takes a full name, prints the initials of the first,
# middle, and last name. If the middle name is “NA”, then the program
# should print only the initials of the first and the last name.


def get_initials(name):
    """ Return initials of first, last and middle name.
    If the middle name is 'NA', return only the initials of the first and the last name.
    
    >>> get_initials("Alfred E. Newman")
    >>> 'A.E.N.'
    >>> get_initials("John NA Smith")
    >>> 'J.S.'
    """

    # your code here
    result = ''
    na = name.find(' NA ')
    if na != -1:
        name = name[:na] + name[na+3:]
    name += ' '
    while name.find(' ') != -1:
        result += name[0] + '.'
        name = name[name.find(' ')+1:]
    print(result)


get_initials("Alfred E. Newman")
get_initials("John NA Smith")
get_initials("Albus Percival Wulfric Brian Dumbledore")