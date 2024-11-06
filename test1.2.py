# SECTION LOOPS !!!!!!!!!!!!

# QUESTION NUMBER 1:

top_number = int(input('enter your top number: q1'))

for num in range(1, top_number + 1):
    print(num, end= " ")

# QUESTION NUMBER 2:

top_num1 = int(input('enter the 1st number: q2'))
top_num2 = int(input('enter the 2nd number: q2'))
for num in range(top_num1, top_num2 + 1):
    print(num, end= " ")


# DATA COMPREHENSION!!!!!!!!:

# QUESTION NUMBER 1:

total = 0

sentinel = -99
while True:
    number1 = int(input('enter a number:q1'))
    if number1 == sentinel:
        break
    if number1 > sentinel:
        total += number1
print('the total is ',total)

# QUESTION NUMBER 2:

total = 0
sentinel = -99
largest = None
smallest = None

while True:
    number1 = int(input('Enter a number: q2'))
    if number1 <= 0:
        break
    total += number1
    if largest is None or number1 > largest:
        largest = number1
    if smallest is None or number1 < smallest:
        smallest = number1
print('The total is', total)

if largest is not None and smallest is not None:
    print('The largest number is', largest)
    print('The smallest number is', smallest)
else:
    print('No valid numbers were entered.')


# QUESTION NUMBER 3:

big_num: int = 0
index_num: int = -1
for i in range(5):
    num = int(input("Enter a number :q3 "))
    if big_num is None or num > big_num:
        big_num = num
        index_num = i
print(f"The largest number is {big_num} at index {index_num}")



# ADVANCED-LOOPS!!!!!!!!!

# QUESTION NUMBER 1:

temp = []
zero_count = 0
for i in range(12):
    try:
        temp_input = float(input('Enter temp: '))
        if temp_input == 0:
            zero_count += 1
            if zero_count == 2:
                print("You entered 0 twice.")
                break
            print("You entered 0.")
            continue
        if -5.0 <= temp_input <= 40.0:
            temp.append(temp_input)
            print(f'{temp_input} , correct data :)')
        else:
            print(f'{temp_input} , wrong data :(')
    except ValueError:
        print('Wrong data')
print(f"Temps entered: {temp}")

if temp:
    average_temp = sum(temp) / len(temp)
    min_temp = min(temp)
    max_temp = max(temp)

    print(f"The average is: {average_temp:.2f}")
    print(f"The minimum temp is: {min_temp:.2f}")
    print(f"The maximum temp is: {max_temp:.2f}")
else:
    print("No valid temps entered")







































