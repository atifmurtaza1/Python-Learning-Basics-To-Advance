# Internal Working of Python Imports

In this lecture, I learned about the internal working of Python when we import something from different files.

For example:

**basic_1.py**
```python
print('Hello World')

def val(n):
    print(n)

val(10)
```

**basic_2.py**
```python
from basic_1 import val

val("Ginger Tea")
```

### When I run `basic_2.py`

I might think that only `Ginger Tea` will be printed because that is the function call in `basic_2.py`.

But the actual output is:

```text
Hello World
10
Ginger Tea
```

Then I did some research and found out how Python handles imports internally.

### How does it work?

**1. Python starts executing `basic_2.py`.**

It encounters `from basic_1 import val`. Python needs to load `basic_1.py` to access the `val` function.

**2. Python executes `basic_1.py` from top to bottom.**

First, it executes:

```python
print('Hello World')
```

Output:
```text
Hello World
```

Then Python defines the `val(n)` function. Defining a function does not execute its body until the function is called.

**3. Python reaches `val(10)` in `basic_1.py`.**

This function call executes immediately.

```python
val(10)
```

The parameter `n` receives the value `10`, so `print(n)` prints:

```text
10
```

**4. Python finishes loading `basic_1.py`.**

Now the `val` function is available in `basic_2.py`. Python does not copy the entire source file into `basic_2.py`; it makes the imported function available for use.

**5. Python continues executing `basic_2.py`.**

Now it executes:

```python
val("Ginger Tea")
```

The parameter `n` receives the string `"Ginger Tea"`, and the function prints:

```text
Ginger Tea
```

### What I learned

When we import something from another Python file, Python normally executes that file's top-level code during the first import.

This is why `print('Hello World')` and `val(10)` execute before `val("Ginger Tea")`.

To avoid executing `val(10)` when importing `basic_1.py`, we can use:

```python
if __name__ == "__main__":
    val(10)
```

This condition ensures that `val(10)` runs only when `basic_1.py` is executed directly, not when it is imported by another file.