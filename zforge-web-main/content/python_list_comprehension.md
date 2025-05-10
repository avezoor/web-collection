---
name: Python List Comprehension
usage: [expression for item in iterable if condition]
example: |
  # Create a list of squares
  squares = [x**2 for x in range(10)]
  print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  
  # List comprehension with conditional logic
  even_squares = [x**2 for x in range(10) if x % 2 == 0]
  print(even_squares)  # [0, 4, 16, 36, 64]
description: List comprehensions provide a concise way to create lists based on existing iterables. They can replace loops and map/filter combinations with a single line of code.
tags: Python, List, Comprehension, Iteration
---

# Python List Comprehension

List comprehensions in Python provide a concise way to create lists based on existing lists or other iterables. They combine the `for` loop and the creation of new elements into a single line, making code more readable and often faster.

## Basic Syntax

```python
[expression for item in iterable]
