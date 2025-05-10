---
name: Mathematical Expressions with LaTeX
usage: Embed LaTeX expressions with $ or $$ delimiters
example: |
  # Inline math: $E = mc^2$
  
  # Display math: 
  $$
  \int_{a}^{b} f(x) \, dx = F(b) - F(a)
  $$
description: Learn how to include mathematical equations and expressions in your documentation using LaTeX syntax.
tags: LaTeX, Math, Equations, Documentation
---

# Mathematical Expressions with LaTeX

This guide demonstrates how to include mathematical expressions in documentation using LaTeX syntax, which is now supported in our platform.

## Inline Mathematical Expressions

You can include inline math by surrounding LaTeX code with single dollar signs. For example, Einstein's famous equation $E = mc^2$ can be embedded directly in a sentence.

Other examples of inline math:
- The Pythagorean theorem: $a^2 + b^2 = c^2$
- The quadratic formula: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- Euler's identity: $e^{i\pi} + 1 = 0$

## Display Mathematical Expressions

For more complex equations or to display them as block elements, use double dollar signs:

$$
\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x)
$$

This is the fundamental theorem of calculus.

### Matrices

You can also include matrices:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

### Multi-line Equations

Using the align environment:

$$
\begin{align}
f(x) &= (x+a)(x+b) \\
&= x^2 + (a+b)x + ab
\end{align}
$$

## Common Mathematical Symbols

Here are some common mathematical symbols in LaTeX:

- Fractions: $\frac{1}{2}$
- Square roots: $\sqrt{x}$, $\sqrt[n]{x}$
- Summation: $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
- Product: $\prod_{i=1}^{n} i = n!$
- Integrals: $\int_{a}^{b} x^2 \, dx = \frac{b^3 - a^3}{3}$
- Limits: $\lim_{x \to \infty} \frac{1}{x} = 0$
- Infinity: $\infty$
- Greek letters: $\alpha, \beta, \gamma, \delta, \pi, \sigma, \omega$

## Applications in Different Fields

### Physics

The Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H\Psi(\mathbf{r},t)
$$

### Statistics

The normal distribution probability density function:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

### Computer Science

Time complexity:

$$
O(n \log n)
$$

## Conclusion

With LaTeX support, you can now include complex mathematical expressions in your documentation. This makes it easier to explain algorithms, formulas, and scientific concepts with proper mathematical notation.