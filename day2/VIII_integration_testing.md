# VIII. Integration testing

## 1. Patching and Mocking

```python
from unittest.mock import patch
import pytest
```

### Reference Table
| Code                                                                                                                                                                                                                                                              | Description                                                                                  |
| ---                                                                                                                                                                                                                                                               | ---                                                                                          |
| `def sayhi():` <br> ;&nbsp;&nbsp; `print("hi")`                                                                                                                                                                                                        | Define a function that says hi                                                               |
| `def mockprint(msg):` <br> &nbsp;&nbsp; `pass`                                                                                                                                                                                                                    | Define a function that stakes in an argument and does nothing                                |
| `with patch("builtins.print", side_effect=p)` <br> &nbsp;&nbsp; `sayhi()`                                                                                                                                                                             | Execute the `sayhi()` function while replacing the builtin `print` function with `mockprint` |
| `@pytest.fixture` <br> `def mockprint(msg):` <br> &nbsp;&nbsp; `with patch("builtins.print", side_effect=p):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `yield`                                                   | Define a `@pytest.fixture` that yields a mock function                                       |

### Key Exercises
1. Use patching to call the prepared function while changing it's behavior
2. Do the same thing using a Pytest fixture

## 2. Running an Integration Test

```python
import pytest
```

### Code References

### Key Exercises
1. Write a test 


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


