# Python sequence types let us to create a slice.

# we can produce a slice by providing theree numbers separated by colons.
# Thses numbers are called as start, stop and step values.

# ** we are going to look out how to slice without a step.

parrot = "Norwegain Blue"

# If we want to slice sequence 'parrot' upto 'Norweg' do as following.
print(parrot[0:6]) # we are slicing the sequence from index 0 (including) upto index 6(exclusive).

# ** we can also slice a sequence from bignning to preferred point by omitting starting index.
# we can also ommit the stop value if we are slicing the word upto the end.
# ex:
print(parrot[:9]) # Norwegain

# create a slice that return word 'Blue' from variable 'parrot'.

print(parrot[10:])

# prints the value of the variable.
print(parrot[:])


