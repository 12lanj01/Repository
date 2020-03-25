#! python 3
# This program: (1) Takes a list of students who are signed up for workshops, (2) Takes a list of all students in the school,
# (3) Produces a list of students who have not signed up, (4)

import random
import re

# compare students who signed up and students who didnt


# Assign students who didn't sign up to sessions

IDT_Sessions = ['Mass Incarceration','Example Session','Gratitidue is the Attitude', 'Another One', 'test', 'hello']

NUM_COURSES = 4

def Assigner(student):
	temp = IDT_Sessions.copy()
	random.shuffle(temp)
	for i in range(0, NUM_COURSES):
		temp[i] = str(i + 1) + " - " + temp[i]
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
    return file.read()
	
	

Signed_Up = readIn('SignedUp.txt')
Signed_Up_List = Signed_Up.replace('\n',' , ').split(' , ')
All_Students = readIn('AllStudents.txt')
All_Students_List = All_Students.replace('\n',' , ').split(' , ')
Not_Signed_Up_List = list(set(All_Students_List).difference(Signed_Up_List))

def main():
	
	
	Final = []
	for i in range(0,len(Not_Signed_Up_List)):
		Final.append(Not_Signed_Up_List[i])
		Final.append(Assigner(i))
		
	Final = excelify(Final)
	
	print(Final)

if __name__== "__main__":
	main()
