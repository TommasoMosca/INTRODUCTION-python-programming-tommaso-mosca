# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

v1= input('input a 10 numbers vector: ')
def average_vector(x):
	for i in x:
		return float((sum (x))/len(x))
print 'average of the values of the vector:'
print average_vector(v1)


'''
pseudo-code:
define a function (average_vector)
that for each number inside the vector (x)
returns the mean (sum of each element/number of elements)
of the values inside the vector
'''
