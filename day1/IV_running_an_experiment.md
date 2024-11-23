# IV. Running an Experiment


## 1. Writing and Reading the Configuration
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


TODO: 
- This seems like a loose collection of several topics 
- There should be one script per error


## 2. Adding a command-line interface
TODO: Make sure eveyone at least knows how to use a CLI

```python
import argparse
```

### Reference Table
| Code                                   | Description                                     |
| ---                                    | ---                                             |
| `parser = argparse.ArgumentParser()`   | Create a parser for command line arguments      |
| `parser.add_argument("--id" type=int)` | Add a argument called "id" of type int          |
| `args = parser.parse_args()`           | Parse the command line input                    |
| `args.id`                              | Value passed to the "id" argument               |
| `python scipt.py --id 7`               | Run "script.py" and pass 7 to the "id" argument |

### Key Exercises 
1. Create a script that takes in a command line argument and prints it out
2. Add a CLI to the experimental script to pass in the subject name and dynamically adjust the name of the stored file


 
