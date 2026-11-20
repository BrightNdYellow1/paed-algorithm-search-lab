print("Starting program")
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
operations = 0
for number in numbers:
    print(number)
    operations += 1 

print("Total items:", len(numbers))
print("Total loop operations", operations)
numbers = [10, 20, 30, 40, 50]
target = 50 
for number in numbers: 
    if number == target: 
        print ("found")
        break 