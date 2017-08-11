
score = input("Enter score: ")
score = int(score)
if score > 90 or score == 90:
    grade = 'A'
elif score > 80 or score == 80:
    grade = 'B'
elif score > 75 or score == 75:
    grade = 'C'
elif score > 68 or score == 68:
    grade = 'Pass'
else:
    grade = 'F'
print ("\n\nCongrats!, your grade is: " + grade)



