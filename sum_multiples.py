result = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(f"The sum of all multiples of 3 or 5 below 1000 is: {result}")