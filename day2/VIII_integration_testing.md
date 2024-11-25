# VIII. Integration testing
TODO: No need to talk about integration testing, the benefit here is the ability to mock components of the experiment

## 1. Patching and Mocking

```python
from unittest.mock import patch
import pytest
```

### Reference Table

```python
def sayhi():
    print("hi!")
```
Defines a function that says `"hi!`

```python
def mock_print(msg):
    pass
```
Defines a function that takes in an argument and does nothing

```python
with patch("builtins.print", side_effect=mock_print):
    sayhi()
```
Execute the function `sayhi()` while replacing the builtin `print` function with `mock_print()`

```python
@pytest.fixture
def mock_print_fix():
    with patch("builtins.print", side_effect=mock_print):
        yield
```
Create a fixture that yields the `mock_print` function

```python
def test_sayhi(mock_print_fix):
    sayhi()
```
The test function can take a fixture as argument and Pytest will do the patching for us

### Key Exercises
1. Use patching to call the prepared function while changing it's behavior
2. Do the same thing using a Pytest fixture

## 2. Running an Integration Test

```python
import pytest
```

### Code References


### Key Exercises
1. Write a fixture to patch PsychoPy's `event.waitKeys()`  function
2. Use the fixture to run the whole experiment in an automated test


## 3. Adding a Test Option to the CLI

### Reference Table
| Code                                                     | Description                                                  |
| ---                                                      | ---                                                          |
| `parser = argparse.ArgumentParser()`                     | Create a parser for command line arguments                   |
| `parser.add_argument("--test" type=bool, default=False)` | Add a boolean argument that defaults to `False`              |
| `args = parser.parse_args()`                             | Parse the command line input                                 |
| `args.test`                                              | Value passed to the `.test` argument                         |
| `python experiment.py --test`                            | Run `"experiment.py"` and set the `.test` argument to `True` |

### Key Exercises
1. Add an optional argument to the experiment's command line interface that indicates whether you want to run it in test-mode.
2. Modify the code so that, if the experiment runs automatically when executed in test-mode


