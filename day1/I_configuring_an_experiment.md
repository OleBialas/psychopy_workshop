# I. Configuring an Experiment

## 1. Running Scripts
TODO: make this the "first exercise" in the kickoff meeting

### Reference Table
| Code                               | Description                                                                    |
| ---                                | ---                                                                            |
| `cd psychopy_workshop`             | Move to a a folder called "psychopy_workshop" within the current folder        |
| `cd /path/to/psychopy_workshop`    | Does the same with an absolute path, independent of the current folder         |
| `cd C://path/to/psychopy_workshop` | Windows: Does the same with an absolute path, independent of the current folder         |
| `python script.py`                 | Execute a Python script called `script.py` within the current directory        |
| `print("Hello!")`                  | Print out a string                                                             |

### Key Exercises
1. Open a terminal and move to the `day1` folder in the `psychopy_workshop` directory.
2. Write and run a script that prints out a message.


## 2. Data Types and Variables


### Reference Table
| Code                | Description                                                      |
| ---                 | ---                                                              |
| `x = 3`             | Assign the integer number 3 to the variable x                    |
| `x = 3.14`          | Assign the floating number 3.14 to the variable x                |
| `x = "hi"`          | Assign the string "hi" to the variable x                         |
| `x = True`          | Assign the boolean value True to the variable x                  |
| `print(f"x = {x})"` | Print message and convert output inside `{}` to strings          |
| `type(x)`           | Get the data type of variable x                                  |
| `int(x)`          | Convert the variable x to an integer                             |
| `float(x)`        | Convert the variable x to a float                                |
| `str(x)`          | Convert the variable x to a string                               |
| `bool(x)`         | Convert the variable x to a bool                                 |

### Key Exercises
1. Write a script that defines a variable `x` and then converts `x` to an boolean, string, integer and float and prints out the variable after each conversion. Run this script while assigning an integer, float, boolean and string value to `x` 
2. Consider an experiment that estimates the participants hearing threshold by presenting pure tones and lowering their level until they are detected in 50% of cases. Some tones are omitted to catch false alarms. For a single trial of this experiment, which input parameters are required and what outputs are produced? Which type would you choose to represent each of those?

## 3. Operators

### Reference Table
| Code                 | Description                                              |
| ---                  | ---                                                      |
| `3 + 5`              | Adds two integers, result: `8`                           |
| `"Hello" + "!"`      | Concatenates two strings, result: `"Hello!"`             |
| `5.5 - 3`            | Subtracts from a float, result: `2.5`                    |
| `7 * 1.5`            | Multiplies float, result: `10.5`                         |
| `"Ha" * 3`           | Repeats string, result: `"HaHaHa"`                       |
| `10 / 2`             | Divides integers, result: `5.0`                          |
| `x > 5`              | Returns `True` if `x` is greater than `5`                |
| `x <= 6`             | Returns `True` if `x` is smaller or equal to `6`         |
| `x == "oh"`          | Retruns `True` if `x` is exactly the string `"oh"`         |
| `x != "oh"`          | Retruns `True` if `x` is not exactly the string `"oh"` |

### Key Exercises
1. Create a script that defines a variable x and then multiplies x, adds to it and subtracts from x, divides x and checks if x smaller or larger than a given value. Print out the result of each operation
2. Find float integer and boolean values that are all equal to each other (i.e. the comparison `==` returns True)


## 4. Collections

### Reference Table
| Code                         | Description                                                                                                |
| ---                          | ---                                                                                                        |
| `x = [1, "a", 3.1]`          | Assign a list an integer, a string and a float to the variable `x`                                         |
| `x = (True, False)`          | Assign a tuple containing two booleans to the variable `x`                                                 |
| `x = []`                     | Assign an empty list to the variable `x`                                                                   |
| `x[0]`                       | Acess the first value of list or tuple `x`                                                                 |
| `x[-1]`                      | Acess the last value of list or tuple `x`                                                                  |
| `list(x)`                    | Convert `x` to the data type list                                                                          |
| `tuple(x)`                   | Convert `x` to the data type tuple                                                                         |
| `len(x)`                     | Returns the number of elements in `x`                                                                      [|](|)
| `x = {"a": 1, "b": 2}`       | Defines a dictionary with keys `"a"`, and `"b"` and values `1` and `2`                                     |
| `x["a"]`                     | Acess the value(s) stored under the key `"a"` in the dictionary `x`                                        |
| `x.keys()`, `x.values()`     | Return all keys and values of the dictionary `x`                                                           |

### Key Exercises
1. Write a script that defines a list, prints out it's length and assigns a new value to the last element. Replace the list with a tuple - how can you modify the script so that it will not throw an error

TODO: make it less vague, give feedback --> it should be clear when the exercise is done and they can move on

2. Discuss which type of collection you would use to store your experimental parameters
3. Make a collection for my three subjects: Nick, Ole, and Atle, and another Nick
4. 


## 5. Writing and Reading the Configuration
TODO: This is a critical component, move it to an earlier point here or in the next notebook
```python
import json
```

### Reference Table
| Code                           | Description                                                |
| ---                            | ---                                                        |
| `f = open("config.json", "w")` | Open a file called `"config.json"` in `"w"` (writing) mode |
| `f = open("config.json", "r")` | Open a file called `"config.json"` in `"r"` (reading) mode |
| `f.close()`                    | Close the file `f`                                         |
| `json.dump(x, f)`              | Write the dictionary `x` to the (opened) file `f`          |
| `json.load(f)`                 | Read a dictionary from the (opened) JSON file `f`          |

### Key Exercises
1. Consider an oddball task where we play tones of frequency 800, 1000 and 1200 Hz and occasionally omit tones with a probability of 15 percent. Write a config file that stores the tone frequencies, omission probability and number of trials for this experiment. Discuss the appropriate data type for representing each of these parameters.
2. Read this config file and print it's keys and values
(TODO: prepare a file for this)

