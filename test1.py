# QUESTION NUMBER 1:

#  IF SECTION:

num1: float = float(input('enter the 1ST number: q1'))
num2: float = float(input('enter the 2ND number: q1'))

if num1 > num2:
    smaller_number = num2
else:
    smaller_number = num1

for _ in range(3):
    print(smaller_number)

# QUESTION NUMBER 2

number1: int = int(input('enter the 1st number: q2'))
number2: int = int(input('enter the 2nd number: q2'))

average_number = (number1 + number2) / 2

print('avg is', average_number)

# QUESTION NUMBER 3

num4: int = int(input('enter the 1st number: q3'))
num5: int = int(input('enter the 2nd number: q3'))
num6: int = int(input('enter the 3rd number: q3'))

if num4 >= num5 and num4 >= num6:
    bigger_number = num4
elif num5 >= num4 and num5 >= num6:
    bigger_number = num5
else:
    bigger_number = num6

print('the bigger number is',bigger_number)


# QUESTION NUMBER 4

movie_length = int(input('how long is the movie? q4'))
long: int = 60

hour = movie_length // 60
minutes = movie_length % 60

print (f"the movie length is {hour} hour and {minutes} minutes")
























