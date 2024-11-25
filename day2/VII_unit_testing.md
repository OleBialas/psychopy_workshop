# VII. Unit Testing

## 1. Assert Statements

### Reference Table
| Code                 | Description                                     |
| ---                  | ---                                             |
| `assert True`        | Will never raise an Error                       |
| `assert False`       | Will always raise an Error                      |
| `assert len(x)==3`   | Will raise an Error if the length of x is not 3 |
| `isinstance(x, int)` | Returns True if x is an integer                 |

### Key Exercises
1. Write a function to assert that the value of the variable x is between 0 and 1
2. Write a function to assert that the variable x is a string

## 2. Writing a Test Function


### Key Exercises
1. Write a test function that makes sure that loading a configuration file worked
2. Write another test that asserts a `FileNotFound` error is raised when the configuration file could not be found

## 3. Automate Testing with Pytest

### Key Exercises
1. Run the test functions with Pytest and observe the outputs
2. Determine the test-coverage using Pytest
