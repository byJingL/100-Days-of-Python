import pandas
student_dict = {
    "student": ["Alex", "James", "Emma"],
    "score": [56, 67, 78],
}
# Todo: 1. Looping through DataFrame
student_df = pandas.DataFrame(student_dict)
for (key, value) in student_df.items():
    pass
# Todo: 2. Looping through rows of DataFrame
# Keyword Method with iterrows()
for (index, row) in student_df.iterrows():
    # Access index and row
    # Access row.student or row.score
    print(row)
    if row.score > 70:
        print(f"Excellent student: {row.student}")
# Todo: 3. DataFrame comprehension
# {new_key:new_value for (index, row) in df.iterrows()}
new_dic = {row.student: row.score for (index, row) in student_df.iterrows()}
print(new_dic)

# Todo: 4. Looping through dictionary
# important: items()
for (key, value) in student_dict.items():
    # Access key and value
    pass

