"""Demonstrate cubic O(n^3) iteration using three independent loops."""

numbers = [1, 2, 3, 4]

for i in numbers:
    for j in numbers:
        for f in numbers:
            print(i, j, f)
