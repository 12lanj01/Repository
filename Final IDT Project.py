#! python 3
# This program: (1) Takes a list of students who are signed up for workshops, (2) Takes a list of all students in the school,
# (3) Produces a list of students who have not signed up, (4)

import random
import re
import csv
from collections import Counter

# compare students who signed up and students who didnt


# Assign students who didn't sign up to sessions

IDT_Sessions = ['Mass Incarceration','Example Session','Gratitidue is the Attitude', 'Another One', 'test', 'hello']

NUM_COURSES = 4


def Assigner(i):
    temp = IDT_Sessions.copy()
    random.shuffle(temp)
    for i in range(0, NUM_COURSES):
        temp[i] = str(i + 1) + " - " + temp[i]
        #if counts[str(temp[i])] >= 16:
         #   for x in temp[i]:
          #      temp[i] = [j for j in temp if j!=x]
           #     print(temp)
    return temp[:NUM_COURSES]
	
def excelify(final):
	excel = ""
	for i in range(0,len(final)):
		# is a name
		if (i%2) == 0:
			excel = excel + str(final[i])
			excel = excel + '\t'
		# is a class list
		else:
			classList = final[i]
			for j in range(0,len(classList)):
				excel = excel + classList[j] + '\t'
			excel = excel + '\n'
			
	return excel
	
def readIn(file):
    file = open(file,'r')
    file = file.readlines()
    return [i.rstrip('\n') for i in file]
	
	
# Data Input
Signed_Up_List = readIn('SignedUp.txt')
All_Students_List = readIn('AllStudents.txt')
Not_Signed_Up_List = list(set(All_Students_List).difference(Signed_Up_List))

with open('IDT Example.csv') as data:
    file = csv.reader(data)
    c = [line for line in file]
counts = Counter()
for line in c:
    
    counts.update(line)

print(counts['1 - Mass Incarceration'])

def main():
	
	Final = []
	for i in range(0,len(Not_Signed_Up_List)):
		Final.append(Not_Signed_Up_List[i])
		Final.append(Assigner(i))
		
	Final = excelify(Final)
	
	print(Final)
  
if __name__== "__main__":
	main()
    
# git
# classes
# DO capacity by getting csv
# dictionary
