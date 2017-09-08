"""Breach Clinical Developers Challenge.

This is a program for correctly interpreting arrays and their string contents
and recognising if a hospital is struggling with breaching patients in A&E.
"""
# import re


def formatList(line):
    """Format mangled text into a list.

    Take any line and remove any incorrect characters,
    convert it to lowercase and transform the string
    into a list based on the commas.
    """
    # Regex Version
    # cleaned = re.sub("'|\[|\]|\s|\n", "", line)
    # cleaned = cleaned.split(',')
    # Non-import String Version (faster, but less clean)
    cleaned = line.replace("\n", "").replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(',')
    cleaned = [x.lower() for x in cleaned]
    return cleaned


def gradeHospital(array):
    """Take an array and grade the hospital based on the number of breaches."""
    if type(array) == list:
        numBreaches = len(filter(lambda x: x == 'breach', array))
        if numBreaches == 0:
            return 'Safe'
        elif numBreaches > 3:
            return 'Urgent Inspection'
        else:
            return 'Trouble'
    else:
        print("Error formating text:")
        print(array)
        exit(1)


with open('datafile.txt', 'r') as f:
    content = f.readlines()
# Format hospitals
hospitals = map(formatList, content)
# Grade hospitals
hospitals = map(gradeHospital, hospitals)
# Print results
for i, grade in enumerate(hospitals):
    print('Hospital {}: {}'.format(i+1, grade))
