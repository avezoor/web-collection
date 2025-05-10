---
name: JavaScript Arrow Functions
usage: (parameters) => expression
example: |
  // Basic arrow function
  const add = (a, b) => a + b;
  console.log(add(5, 3));  // 8
  
  // With no parameters
  const sayHello = () => console.log("Hello");
  sayHello();  // "Hello"
  
  // With a function body
  const greet = name => {
    const message = `Hello, ${name}!`;
    return message;
  };
  console.log(greet("Alice"));  // "Hello, Alice!"
description: Arrow functions are a concise syntax for writing function expressions in JavaScript. They have implicit returns when using expressions and don't bind their own this value.
tags: JavaScript, Functions, ES6, Arrow Functions
---

# JavaScript Arrow Functions

Arrow functions were introduced in ES6 (ECMAScript 2015) and provide a more concise syntax for writing function expressions in JavaScript.

## Basic Syntax

```javascript
// Basic syntax
(param1, param2, ...) => expression

// Multiple statements require curly braces and a return statement
(param1, param2, ...) => {
  statements;
  return expression;
}
