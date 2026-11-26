# Nested Loops in Python: Quadratic and Cubic Complexity

## Learning objective

I explored how independently nested loops affect the number of operations as input size grows. The exercises use four numbers and compare two loops with three loops.

## Quadratic: O(n²)

Run `python quadratic_pairs.py`.

```python
numbers = [1, 2, 3, 4]
for i in numbers:
    for j in numbers:
        print(i, j)
```

Each of four outer iterations runs the inner loop four times: **4 × 4 = 16** printed ordered pairs. The output begins with `1 1` and ends with `4 4`. For input length n, the inner print runs **n²** times.

## Cubic: O(n³)

Run `python cubic_triples.py`.

```python
numbers = [1, 2, 3, 4]
for i in numbers:
    for j in numbers:
        for f in numbers:
            print(i, j, f)
```

Each of the four outer iterations runs four middle iterations, and each middle iteration runs four inner iterations: **4 × 4 × 4 = 64** printed ordered triples. The output begins with `1 1 1` and ends with `4 4 4`. For input length n, the print executes **n³** times.

| Example | Nested loops | Output lines (n=4) | Time complexity |
| --- | ---: | ---: | --- |
| Quadratic pairs | 2 | 16 | O(n²) |
| Cubic triples | 3 | 64 | O(n³) |

## Debugging and learning reflection

I encountered an `IndentationError` because the `print` statement was not indented inside the inner loop. I corrected the indentation, ran the programs again, and verified the first and last outputs. I also practised checking the case of variable names (`j` and `J` are different in Python). I learned to predict operations mathematically before running the code and then verify the prediction against the program output.

**Important nuance:** The number of nested loops does not always determine Big O by itself. These examples are O(n²) and O(n³) because *each* loop independently traverses *all n elements*. Conditional branches, dependent loop bounds, and early exits can change complexity.

**Space:** Apart from the existing list and printed output, the loops use O(1) auxiliary memory. If the input list is counted, it occupies O(n) memory.

## Next exercise

Change the numbers list to contain five items. Before running, predict the number of quadratic pairs and cubic triples, then compare with the terminal output.
