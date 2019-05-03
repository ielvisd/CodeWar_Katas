""" Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F """

def abbrevName(name):
    # initialize return as an empty string
    abbrev = ''

    # first letter of passed in name gets added to string and capitalized
    abbrev += name[0].upper()

    # looks for first space in name and then adds the capitalized letter following that space
    for i in range(0, len(name)):
      if (name[i] == ' '):
        abbrev += '.'
        abbrev += name[i+1].upper()
    return abbrev

print(abbrevName("Sam Harris")) # "S.H"
print(abbrevName("Patrick Feenan")) # "P.F"
print(abbrevName("Evan Cole")) # "E.C"
print(abbrevName("P Favuzzi")) # "P.F"
print(abbrevName("David Mendieta")) # "D.M"

# Best Practice Solution
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()