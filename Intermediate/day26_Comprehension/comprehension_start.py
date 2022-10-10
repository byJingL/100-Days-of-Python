import random

# Todo: 1. List Comprehension
# new_list = [new_item for item in numbers]
numbers = [2, 4, 6, 8]
new_number = [n+1 for n in numbers]
print(new_number)

my_name = "Jenny"
new_list = [letter for letter in my_name if letter == my_name[2]]
print(new_list)
double_list =[2 * num for num in range(1, 5)]
print(double_list)

# Todo: 2. Conditional List Comprehension
# new_list = [new_item for item in numbers if test]
square_list = [num ** 2 for num in range(1, 9) if num > 4]
print(square_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name[0:4] for name in names if len(name) > 4]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)

# Todo: 3. Check same numbers
# readline(), very important: sth in List
with open("file1.txt") as f1:
    data1 = f1.readlines()
with open("file2.txt") as f2:
    data2 = f2.readlines()
result = [int(num) for num in data1 if num in data2]
print(result)

# Todo: 4. Dictionary Comprehension
# just to create a new dict
# new_dict = {new_key:new_value for item in list/string/range...}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(30, 90) for student in names}
passed_students = {name: score for (name, score) in students_score.items() if score >= 60}
print(passed_students)

# !!! Convert a sentence to word list: text.split()
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()
result = {word: len(word) for word in word_list}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items()}
print(weather_f)


