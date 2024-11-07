# LOOP SECTION:

# QUESTION NUMBER 3:

n: int = int(input('enter n: Q3 '))
for i in  range (0, n + 1):
    if i % 2 == 0:
        print(f"{i} is zugi/even")
    else:
        print(f"{i} is e-zugi/odd")


# DATA COMPREHENSION:

# QUESTION NUMBER 8

list_prime = []
for x in range(1, 100 + 1):
    if x < 1:
        continue
    else:
        if x == 1:
            continue
        elif x == 2:
            list_prime.append(x)
        elif x % 2 == 0:
            continue
        else:
            divider: int = 3
            found_divider: bool = False
            while divider <= x ** 0.5 + 1:
                if x % divider == 0:
                    found_divider = True
                    break
                divider += 2
            if not found_divider:
                list_prime.append(x)
print(list_prime)


# IF SECTION:

# QUESTION NUMBER 10:

income = float(input("Enter the income: "))
tax = 0
if income > 6_000:
    if income <= 12_000:
        tax += (income - 12_000) * 0.10
    else:
        tax += (12_000 - 6_000) * 0.10
if income > 12_000:
    if income <= 18_000:
        tax += (income - 12_000) * 0.20
    else:
        tax += (18_000 - 12_000) * 0.20
if income > 18_000:
    if income <= 25_000:
        tax += (income - 18_000) * 0.30
    else:
        tax += (25_000 - 18_000) * 0.30

if income > 25_000:
    if income <= 35_000:
        tax += (income - 25_000) * 0.40
    else:
        tax += (35_000 - 25_000) * 0.40
if income > 35_000:
    if income <= 50_000:
        tax += (income - 35_000) * 0.45
    else:
        tax += (50_000 - 35_000) * 0.45
if income > 50000:
    tax += (income - 50000) * 0.51
print(f"The total tax {income} is {tax:.2f}")









































