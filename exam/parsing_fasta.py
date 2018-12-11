# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 

def type_of_organism(f):
	f= open('sprot_prot.fasta','r')
	g= open('not_human.txt','w')
	for line in f:
		if line[0] == '>':			
			if line.find('Homo sapiens') == -1:
				g.write(line)
				

'''
Pseudo-code:
open the file
read it lin by line
if the line starts with '>' and does not contain 'homo sapiens'('find' it)
print the record ('>'line + lines form 'M' to the next '>') into a new file.txt
and print its organism and sequence lenght
'''


