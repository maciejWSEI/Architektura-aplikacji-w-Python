## Usage

Add `@log_params` above a function definition.

When the function is called, parameter names and their types are printed to the console.

Types are taken from the actual arguments passed to the function.

Example:

```python
@log_params
def foo(a, b):
    pass

foo(1, "test")
# {'a': 'int', 'b': 'str'}
```
