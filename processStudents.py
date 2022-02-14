""" 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


"""


import csv


# create a file object to open the file in read mode

students = open("students.csv", "r")

# create a csv object from the file object

students_file = csv.reader(students, delimiter=",")

# skip the header row

next(students_file)

# create an outfile object for the pocessed record


def add_dict():
    outfile = open("students.csv", "w")


# create a new dictionary named 'student_dict'

student_dict = {
    "123456789": "3.00",
    "124567890": "2.70",
    "234567890": "3.50",
    "345678901": "2.80",
    "456789012": "3.20",
    "567890123": "3.60",
    "678901234": "3.30",
    "789012345": "2.50",
    "876543210": "4.00",
    "890123456": "2.20",
    "901234567": "3.80",
}

# use a loop to iterate through each row of the file

# check if the GPA is below 3.0. If so, write the record to the outfile


# append the record to the dictionary with the student id as the Key
# and the value as the GPA


# print the entire dictionary


# Print the student id


# print out the corresponding GPA from the dictionary


# close the outfile
