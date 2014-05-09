__author__ = 'Nick'

# variables and lists to use
firstnames = ['Lizlo','Nicklo']
lastnames = [' Pink',' Brown']
bothnames = firstnames + lastnames
name = "Nicholas Fazzolari"
nameInput = raw_input('Type ur name biotch!')
if nameInput == 'nick' or nameInput == 'Nick':
    print nameInput
else:
    print 'Fuck off!'


# basic if/else statement checking a condition of the variable names.
if name is not "nick":
    print 'The name is ' + name + ' , which is not nick'

# adding the first names and last names together from the respective lists
print bothnames
print firstnames[1] + lastnames[1]
print firstnames[0] + lastnames[0]
print "My name is %s , and I need to get better at this shit..." % name