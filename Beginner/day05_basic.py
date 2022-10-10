
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

sum = 0
for number in range(1, 101, 1): #[1,101)
    if number % 2 == 0:
        sum += number
print(sum)


#Calculate the average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
num = 0
sum_height = 0

for height in student_heights:
    num += 1
    sum_height += height

aver_height = round(sum_height / num, 2)
print(aver_height)
print(sum(student_heights) / len(student_heights))#easy function

#High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0 #

for score in student_scores:
    if score > highest_score:
        highest_score  = score

print(f"The highest score in the class is: {highest_score}")
print(max(student_scores), min(student_scores))