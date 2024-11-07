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








































