## BankAccount

`BankAccount` represents a simple bank account with basic operations:
depositing money, withdrawing money, and checking the current balance.

The class raises exceptions when an invalid amount is provided or when
a withdrawal exceeds the available balance.

## Tests

Unit tests are implemented using the `unittest` module.

Tests cover:

- account creation with initial balance
- deposits and withdrawals
- balance updates
- error handling for invalid operations

Tests are located in `test_task5.py` and can be run with:

```bash
python -m unittest
```
