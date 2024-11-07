# IF SECTION !!!!!!!!!:

# QUESTION NUMBER 5:

num1: int = int(input('enter a number, 1,000-9,999: q5'))
if 1_000 <= num1 <= 9_999:
    first_dig = num1 % 10
    print(first_dig)

# QUESTION NUMBER 6:

num2: int = int(input('enter a number, 1,000-9,999: q6'))
if 1_000 <= num2 <= 9_999:
    second_dig = (num2 //10 ) % 10
    print(second_dig)

# QUESTION NUMBER 7:

number: int = int(input('enter a number: q7'))
asarot: int = number // 10
print(number //10)
ahadot: int = number % 10
print(number % 10)
print(f"{asarot + ahadot}")
print ()

# QUESTION NUMBER 8:

number = int(input('Enter a number: q8'))
dig1 = number // 10
dig2 = number % 10
reversed_number = dig2 * 10 + dig1
print(reversed_number)

# QUESTION NUMBER 9:

number9: int = int(input('Enter a number: q9'))
if number9 % 2 == 0:
    print('zugi / even')
else:
    print('e-zugi / odd')

# QUESTION NUMBER 11

age11 = int(input('Enter age: Q11 '))
height11 = int(input('Enter height : '))
if 8 <= age11 <= 18 and height11 >= 115:
    print('You can enter the ride.')
elif age11 >= 18 and height11 >= 110:
    print('You are still eligible for the ride.')
else:
    print('Your height/age is NOT eligible for the ride!!!')


# END

































































