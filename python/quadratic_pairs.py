"""Demonstrate quadratic O(n^2) iteration using two independent loops."""

numbers = [1, 2, 3, 4]

for i in numbers:
    for j in numbers:
        print(i, j)
