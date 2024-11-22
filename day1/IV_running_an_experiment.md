# IV. Running an Experiment

## 1. Debugging and running an experiment

### Reference Table
| Code                       | Description                                                                |
| ---                        | ---                                                                        |
| `TypeError`                | Indicates that a variable has the wrong type for a given operation         |
| `ValueError`               | Indicates that the variable has the correct type but and invalid value     |
| `FileNotFoundError`        | Indicates that a directory or file could not be found                      |
| `KeyError`                 | Indicates that the dictionary or object does not contain the requested key |
| `raise ValueError("oops")` | Raises an Exception (e.g. `ValueError`) and prints out a message           |

### Key Exercises 
1. Read the prepared script and identify different sections (e.g. configuration, sequence, trials, storage)
2. Raise an error message if the config file is missing a key


## 2. Adding a command-line interface

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

## 3. Folder and file management

```python
from pathlib import Path
```

### Reference Table
| Code                       | Description                                                   |
| ---                        | ---                                                           |
| `path = Path(".")`         | Get the relative path to the current directory                |
| `path = path/"foo"`        | Append a directory called "foo" to the path                   |
| `path.resolve()`           | Get an absolute version of this path                          |
| `path.parent`              | The path's parent (i.e. the directory containg the path)      |
| `path.exists()`            | Check if a file or folder at this path exists                 |
| `path.mkdir(parents=True)` | Create a new directory at this path (and it's parents)        |
| `__file__`                 | Variable containing the path to the currently executed script |

### Key Exercises
1. Create a script that create a new folder with several subfolders within the current directory
2. Add a routine that checks whether a folder for the current subject exists and, if not, creates one

 
