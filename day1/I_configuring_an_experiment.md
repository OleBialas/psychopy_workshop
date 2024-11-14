# I. Configuring an Experiment

## 0. Running Scripts

In this course, we will create applications for running experiments.
These applications will be run from the command line so that, once developed, they can be run many times without having to open the code in an editor.
If you are unfamiliar with this way of operating, don't worry - running scripts is easy!
Just open a new file, let's call it `experiment.py`, and add the following line of code:

```python
print("Run, experiment!")
```

Now, open your terminal and move to the folder where the script is located by using the command `cd` (change directory), for example: `cd C:\Users\Posner\Psychopy_Course` (adjust the path so that it points to the folder where `experiment.py` is stored on your machine). 
Then run the script by typing `python experiment.py` which means "execute the file 'experiment.py' as a Python script".
Now you should see the content of the `print()` statement appear in your terminal.
Congratulations, you just ran your first script!

## 1. Data Types and Variables

Programs receive, create and operate on data.
For example, the script above created a string of characters and displayed it with the `print()` command.
There are many different types (in fact, you can invent your own) but a few **essential** ones can be found in most programming languages. In Python, they are called:

- **int**: integers or non-decimal numbers, example -7, 0, 101
- **float**: floating-point numbers with a limited number of decimal places, for example: 0.1, pi, 1/3
- **str**: a string of characters, marked by quotations, for example "a", "13", "hello"
- **bool**: boolean logical values, can be either True or False

The type determines the range of **values** the data can take on as well as the set of **operations** that can be performed on them.
These operations can come in the shape of functions (like `print()`) or specific **operators** such as the arithmetic operators `+`, `-`, `*`, and `/`.
What's more, each mentioned type has a function with the same name that converts data to that type - this is known as **type casting**.

To practice our intuitions about data types by running another script.
Create a new file, let's call it `test_type.py`, and add the following code:

```python
x = 1
print(f"This variable is a {type(x)}. \n")
print(f"As a string, it looks like this: {str(x)}")
print(f"As an integer, it looks like this: {int(x)}")
print(f"As a boolean, it looks like this: {int(x)}")
print(f"As a float, it looks like this: {float(x)}")

print("\nLets try some arithmetic!")
print(f"If we multiply the variable by three, we get: {x*3}")
print(f"If subtract 10 from the variable, we get: {x-10}")
```

This script creates a **variable** by assigning `x=1`.
A variable simply is a placeholder that we can use to store and address data.
After creating the variable, we cast it to different data types and perform some arithmetic operations on it.
The expressions that look like this `f"{}"` are called f-strings and they are a way to tell Python to format everything enclosed in the curly brackets as a string.

Let's run the script by using `cd` to move to the directory where it is stored and typing `python test_type.py`.
You should see this output:

```sh
This variable is a <class 'int'>.

As a string, it looks like this: 1
As an integer, it looks like this: 1
As a float, it looks like this: 1.0

Lets try some arithmetic!
If we multiply the variable by three, we get: 3
If subtract 10 from the variable, we get: -9
```

Now, let's modify our script!
Instead of assigning an integer, we'll assign our variable a string by changing the first line to:

```python
x = "1"
```

If we save the change and rerun our script by typing `python test_string.py`, we'll see a similar output as before followed by a menacing error message: `TypeError: unsupported operand type(s) for -: 'str' and 'int'`.
This tells us that subtraction is not a valid operation for a string and an integer.
Also, notice how multiplying the variable by three did not give us "39" but instead "131313".
This shows that the same operation may have a different meaning (or none at all), depending on the data type!

### Exercises
1. Rerun the `test_types.py` script and assign a boolean and a float value to the variable `x`.
2. Find a [string](string) value for `x` that produces a different error than the one we saw before.
3. Rename the variable x. Use upper and lower case letters, numbers and special characters. Are there certain names forbidden?
4. Observe the different type casting operations that have been performed. Can you spot certain behaviors that may result in errors?
5. There may be cases where multiple data types will be equivalent with respect to a programs behavior. For example, `x=1`, `x=True` and `x=1.0` can be equivalent in many scenarios. If that is the case, h:wow would you decide which type to use?
6. Consider an experiment that estimates the participants hearing threshold by presenting pure tones and lowering their level until they are detected in 50% of cases. Some tones are omitted to catch false alarms. For a single trial of this experiment, which input parameters are required and what outputs are produced? Which type would you choose to represent each of those?
   
## 2. Type hints
Python is a dynamically typed language which means that you don't have to explicitly declare the type of a variable.
Instead a variables type is inferred from the assigned value.
This allows us to code faster because we don't have to spend time thinking about and declaring data types.
However, this also means that Python won't know that an operation (e.g. multiplying two strings) is invalid before it ran and crashed.

In statically typed languages, you must explicitly declare the type of every variable you create.
While this is additional  effort it allows your program to be checked for logical consistency before it runs.
In version 3.5, Python introduced type hints for static type checking.
Let's edit `test_types.py` to add a type declaration for our variable `x`:

```python
x: str = "1"
```
Once made this edit, you should see a new message appear in your editor which warns you that the `-` operator is not supported for these data types.
This is the power of static typing: it can catch mistakes before they even happen.
Note however, that type hints are entirely voluntary and have no effect when we actually run the program - they just help us to write correct code

### Exercise
1. Assign an integer, boolean and float value to `x`. For each type, add a type hint and observe the resulting warnings.
2. What happens if at some point in `test_types.py`, we cast `x` to a different type, like `x = int(x)`?
3. Discuss potential upsides and downsides of using type hints.

## 2. Collections

In the previous section, we learned how to operate on variables containing a single value of a certain data type.
Often however, it is useful to operate on multiple values.
This is what Collections are for: they are special data types that act as containers for storing **multiple values**.
Python knows several kinds of collections:

- **list**: mutable, ordered collections of values, defined with square brackets e.g. `x =[1, 2, 3]`
- **tuple**: immutable, ordered collection of values, defined with round braces e.g. `x = (1, 2, 3)`
- **set**: immutable, unordered collection of unique values, defined with curly braces e.g. `x={1, 2, 3}`

If a collection is ordered, we can extract specific elements by their indices.
Assume we define a tuple `x = (1, 2, 3)`.
We can obtain the first element of the list by typing `x[0]` (Python starts counting at 0).
We can obtain the first two elements of the list by typing `x[0:2]`.
Note that the last element (i.e. `x[2]`) is not included here.
One may also use negative number to count backwards from the last element of the collection, e.g. `x[-2]` will return the second to last element of x.
Another important operation is the `len()` function which returns the number of elements in a collection.

Let's create another script, called `test_collections.py` and include the following code:

```python
x = [1, 1.0, "a", True]
print(f"This variable is a {type(x)}.")
print(f"It contains {len(x)} elements. \n")

print(f"As a list, it looks like this: {list(x)}")
print(f"As a tuple, it looks like this: {tuple(x)}")
print(f"As a set, it looks like this: {set(x)} \n")

print(f"The first and last elements are {x[0]} and {x[-1]}")
print("Let's set the first element to zero!")
x[0] = 0
print(f"Now, it looks like this: {x}")
```

If we run the script with `python test_collections.py` we'll see the following:

```sh
This variable is a <class 'list'>.
It contains 4 elements.

As a list, it looks like this: [1, 1.0, 'a', True]
As a tuple, it looks like this: (1, 1.0, 'a', True)
As a set, it looks like this: {1, 'a'}

The first and last elements are 1 and True
Let's set the first element to zero!
Now, it looks like this: [0, 1.0, 'a', True]
```

There is one important collection that we haven't discussed yet - dictionaries.
Dictionaries differ from the other collections in that they store two kinds of data, keys and values.
Each value has an associated unique key that can be used to access it.
Let's edit the first line of `test_collections.py` so that x is assigned a dictionary:

```python
x = {"a": 1, "b": [1.0, 1.1, 1.2], "c": True}
```

When we save the changes and rerun our scripts we can notice two things. First, if we cast the dictionary to a list, tuple or set we only get the keys not the values and second, trying to access the first element with `x[0]` raises a `KeyError`.
The latter happens because, in a dictionary, elements are accessed by their key instead of their position. Thus, when trying to access `x[0]`, Python searches for a key in x called 0 which raised a `KeyError` since that key does not exist.


### Exercises

1. Edit `test_collections.py` so that x is assigned a set and a tuple, then rerun the script. What does the output tell you about the properties of sets and tuples?
2. Add a type hint for each type of collection.
3. Test the arithmetic operators `+`, `-`, `*`, and `/` on the different collection types. Which operators work on which types and what do they do?
4. Determine the number of duplicate items in the list `x=[1, 2, 3, 1, 2, 1, 3, 5]` (Hint: use the `set()` and `len()` functions).
5. Which type of collection would you use to store your experimental configuration (e.g. number of trials, conditions, stimulus duration etc.) and why?

## 3. Writing and Reading the Configuration

Now we learned about different ways to store different kinds of data in Python.
However, once a script is done, all it's variables are deleted.
If we want to preserve specific data, we must write them to a file.

Let's assume we are running an experiment that estimates the participants hearing threshold for pure tones using a staircase procedure.
This means the sound level is lowered until the participant can't hear the tone anymore at which point the level is increased until the participants can hear the tone again and so on.
The threshold is obtained by averaging across the reversal points where the staircase changed from decrease to increase or vice versa.
Some percentage of tones are omitted to catch false alarms.
A config for this experiment could look like this:

```python
config = {
    "frequencies": [800, 1600, 3200],
    "start_intensity": 60,
    "step_size": 1.5,
    "p_omission": 0.2,
    "n_reversals": 8
    }
```

Let's create a file that stores our experimental parameters!
We'll use JSON which stands for JavaScript Object Notation and is a widely used standard for data storage and exchange.
We can define a dictionary in Python and then use the `dump()` function from Pythons built-in `json` library, which must be imported.
Let's create a script called `write_config.py` that does exactly that and looks like this:


```python
import json

config = {
    "frequencies": [800, 1600, 3200],
    "start_intensity": 60,
    "step_size": 1.5,
    "p_omission": 0.2,
    "n_reversals": 8
    }

f = open("config.json", mode="w")
json.dump(config, f)
f.close()
```

The expression `open("config.json", mode="w")` means "open a file called 'config.json' in writing mode" and it returns a file object that the `dump()` function can use to save the `config` dictionary.
If we run the script with `python write_config.py`, it will create a file called `config.json` in our current directory.
Now, let's create another script called `read_config.py` that reads the config from the file:

```python
import json
f = open("config.json", "r")
config = json.load(f)
f.close()
print(config)
```

Running `python read_config.py` should load and print our stored configuration.
We can now run this code at the beginning of our experiment to configure the experiment using a file!


### Exercises
1. Add an additional field to the dictionary called "n_trials" that contains the total number of trials.
2. One advantage of JSON is that it is stored in plain text. Open your `config.json` in your editor and change it. Then save it and rerun `python read_config.py`. Can you make some change that prevents your file from being read?
3. Discuss possible benefits and risks of storing your configuration as JSON and loading it as a Python dictionary.
4. Assume you want to store the keys that the participants use to indicate whether they head a tone or not in the config. How would you encode them?
