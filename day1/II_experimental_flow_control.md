# II. Experimental Flow Control

## 1. Iterating Trials

```python
from random import shuffle
```

### Reference Table
| Code                                 | Description                                                   |
| ---                                  | ---                                                           |
| `for x in list_of_x:`                | Execute the indented code for each element `x` in `list_of_x` |
| `shuffle(list_of_x)`                 | Randomize the order of elements (overwrites `list_of_x`)      |
| `list_of_x.append(x)`                | Append the variable `x` to the end of `list_of_x`             |
| `min()`, `max()`                     | Return the minimum and maximum of a collection                |
| `input()`                            | Wait for user input from the command line                     |
| `print(f"x is {x}")`                 | Convert everything inside {} to a string an print it          |

### Key Exercises
1. Write a for loop that makes the user guess a number on every iteration
2. Nest the for loop inside another for loop

## 2. Conditional Expressions

```python
from random import shuffle
```

### Reference Table

| Code            | Description                                                                 |
| ---             | ---                                                                         |
| `if x > 1:`     | Executes the indented code if the condition `x>1` is True                   |
| `elif x < 0:`   | Executes the indented code when the `if` block skipped but `x<0` is True    |
| `else:`         | Executes the indented code when the `if` and all `elif` blocks were skipped |
| `x.isdecimal()` | Check whether the string `x` is a number                                    |
| `int(x)`        | Convert the variable `x` to an integer                                      |

### Key Exercises
1. Write an if statement that converts the input to 1 if it is a decimal and sets it to 0 otherwise
2. Include an elif statements that convert the letters q, w, and e to 1, 2 and 3

## 3. Generating Trial Sequences

```python
import pandas as pd
```

### Reference Table

| Code                                         | Description                                                          |
| ---                                          | ---                                                                  |
| `[1,2,3] * n`                                | Multiplying a list by an integer `n` will repeat the list n times    |
| `df = pd.DataFrame({"x":[1,2,3], "y":None})` | Create a data frame from a dictionary (the "y" column will be empty) |
| `df["x"]`                                    | Get the column "x"                                                   |
| `df.iloc[0, "x"]`                            | Get the data frame value in the 1st row in the column "x"            |
| `df.to_csv("table.csv")`                     | Write the data frame to a file called "table.csv"                    |
| `for i in df.index:`                         | Iterates the indices (i.e. row numbers) of the data frame            |

### Key Exercises
1. Create a pandas data frame that contains a randomized sequence of trials
2. Use that data frame to store the responses and save them


## 4. Analyzing responses

```python
import pandas as pd
```

### Reference Table

| Code                                         | Description                                                          |
| ---                                          | ---                                                                  |
| `df = pd.read_csv("path//to//table.csv")`    | Read data frame from a file                                          |
| `df.head(3)`                                 | Print the first 3 rows of the data frame                             |
| `df.value_counts()`                          | Count how often every unique value occurs in the data frame          |
| `mask = df['x'] == 2`                        | Generate a mask that is True where the value of "x" equals 2         |
| `df[mask]`                                   | Filter the rows of the data frame where the mask is True             |
| `sum(mask)`                                  | Sum the mask to count the number of elements that are True           |
| `df.iloc[4:10]`                              | Get the data frame rows 5 through 10                                 |
| `for i in df.index:`                         | Iterates the indices (i.e. row numbers) of the data frame            |

### Key Exercises
1. Load the previously stored data frame and check whether all conditions appear the same number of times
2. Calculate the hit rate for the first and second half of trials
