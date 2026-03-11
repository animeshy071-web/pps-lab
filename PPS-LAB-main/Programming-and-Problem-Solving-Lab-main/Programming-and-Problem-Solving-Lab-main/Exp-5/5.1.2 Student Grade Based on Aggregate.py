m1, m2, m3, m4 = map(int, input().split())

total = m1 + m2 + m3 + m4
percentage = total / 4

if percentage > 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Division"
elif percentage >= 50:
    grade = "Second Division"
elif percentage >= 40:
    grade = "Third Division"
else:
    grade = "Fail"

print(total)
print(f"{percentage:.2f}")
print(grade)