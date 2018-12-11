#Miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
print '#1'
L= range(21,40)
print L
print '\n'
# print the numbers of the list that are even
for numbers in L:
	if numbers%2 == 0:
		print numbers
print'\n'
# print the numbers of the list that are multiples of 3
for numbers in L:
	if numbers%3 == 0:
		print numbers

# Exercise 2
print '\n#2'
# Print the last two elements of L 
print L[-2:] 

# Exercise 3
print '\n#3'
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = [1, 2, 3]
for i in range(0,3):
    if i in L:
    	print 'i is in the list'
    else:
    	print 'i not found'    

# Exercise 4
print'\n#4'
# Read the first line from the sprot_prot.fasta file
f= open('sprot_prot.fasta', 'r')
l= f.readlines()
print l[0]
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 
r= l[0].split('OS=')
print r[1]

# Exercise 5
print'\n#5'
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
s= r[1].split(' ')
print s
print ' '.join(s[0:2])

# Exercise 6
print '\n#6'
# reverse the string 'asor rosa'
string= 'asor rosa'
print string[::-1]

# Exercise 7
print '\n#7'
# Sort the following list: L = [1, 7, 3, 9]
L = [1, 7, 3, 9]
print L
print sorted(L)

# Exercise 8
print '\n#8'
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
L = [1, 7, 3, 9]
l= []
l.append(sorted(L))
print l
# Exercise 9
print '\n#9'
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
F= open('exercise9.txt','w')
table= '2 4\n3 6'
F.write(table)
F.close()
print 'exercise 9 done'
