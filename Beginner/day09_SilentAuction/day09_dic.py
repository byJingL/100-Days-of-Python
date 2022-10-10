#format more than one element properly
#cap off all entries in your dictionary or list with a comma by convention
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    12345: "A piece of code that you can easily call over and over again.",
    }

#retrive the dictionary
#fetching somthing out of dictionary
#spell the key correct or "keyError"/Using the right data type of the key
programming_dictionary["Bug"]

#when key not exist: adding new items to dictionary
#when key not exist: edit an item in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
programming_dictionary ["Bug"] = "A mouth in the programming"

#empty dictionary

empty_dictionary = {}

#loop through the dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

for value in programming_dictionary:
    print(programming_dictionary[value])


#wipe an existing dictionary

programming_dictionary = {}
print(programming_dictionary)


#Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding" #Add new item
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

