numbers = [10, 40, 20, 80, 30, 60, 50, 70]
larger = numbers[0]
for number in numbers:
    if number > larger:
        larger = number
print("Largest number:", larger)