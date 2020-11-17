


score = input('enter a score: ')
score = int(score)

# score = int(input('enter a score: '))

# result = ''
# if score >= 90:
#     result = 'A'
# elif score >= 80 and score <= 89:
#     result = 'B'
# elif score >= 70 and score <= 79:
#     result = 'C'
# elif score >= 60 and score <= 69:
#     result = 'D'
# else:
#     result = 'F'

# result = ''
# if score >= 90:
#     result = 'A'
# elif 80 <= score <= 89:
#     result = 'B'
# ...

# result = ''
# if score >= 90:
#     result = 'A'
# elif score >= 80:
#     result = 'B'
# ...

result = ''
if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

# 65%10 == 5
# 97%10 == 7
# 70%10 == 0

ones_digit = score%10
plus_minus = ''
if ones_digit >= 6:
    plus_minus = '+'
elif ones_digit <= 4:
    plus_minus = '-'

print(result + plus_minus)


