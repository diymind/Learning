__author__ = 'Nick'

# variables and lists to use
firstnames = ['Lizlo','Nicklo']
lastnames = [' Pink',' Brown']
bothnames = firstnames + lastnames
name = "Nicholas Fazzolari"

# basic if/else statement checking a condition of the variable names.
if name is not "nick":
    print "Name is not nick!"
else:
    print "Name stored is %s" %name

# adding the first names and last names together from the respective lists
print bothnames
print firstnames[1] + lastnames[1]
print firstnames[0] + lastnames[0]