---
name: Python Decorators
usage: "@decorator\ndef function():"
example: |
  # Simple timing decorator
  import time
  
  def timer(func):
      def wrapper(*args, **kwargs):
          start = time.time()
          result = func(*args, **kwargs)
          end = time.time()
          print(f"Function {func.__name__} took {end-start:.6f} seconds to run")
          return result
      return wrapper
  
  @timer
  def slow_function():
      time.sleep(1)
      return "Function completed"
  
  print(slow_function())
description: Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their code directly.
tags: Python, Decorators, Functions, Advanced
---

# Python Decorators

Python decorators are a powerful way to modify or extend the behavior of functions or methods without directly changing their source code. They're a form of metaprogramming that lets you wrap a function with another function.

## Basic Concept

A decorator is a callable that takes a function as an input and returns a new function as output. The syntax uses the `@` symbol placed above a function definition.

## Basic Syntax

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before the function runs
        result = func(*args, **kwargs)
        # Do something after the function runs
        return result
    return wrapper

@decorator
def my_function():
    pass
