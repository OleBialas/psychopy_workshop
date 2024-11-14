# II. Experimental Flow Control

Experiments consist of different elements, like the presentation of a stimulus or the recording of a response. 
These elements are organized in a certain flow that determines when and under which conditions certain behaviors are executed.
In this notebook, we will learn how to turn this experimental flow into code by using expressions like loops and conditional statements.
We will also see how to store and evaluate trial sequences and response data using the Pandas package.
To explore these concepts, we are going to implement a little numbers guessing game.
While this is going to be a toy example, it will contain many of the core features of an actual experiment and produce response data that we can analyze.

## 1. Iterating Experimental Trials

Let's start simple by creating a list of numbers and randomizing it with the `shuffle()` function from Python's built-in `random` module.
Then, let's go trough that list one-by-one and ask the participant to guess each number.
To this end, we'll use a `for` loop, which repeats a block of code `for` every element in a sequence.
In each iteration, we ask the participant to guess the current number using the `input()` function.
This function pauses the program until the participants typed something and confirmed by pressing enter.
The described program may look like this:

```python
from random import shuffle

numbers = [1,2,3]
shuffle(numbers) # randomize
responses = [] # list for storing responses
s
for number in numbers: 
    # get response
    print(f"guess a number between {min(numbers)} and {max(numbers)}")
    response = input()
    responses.append(response)
# print results
print(f"The numbers were: {numbers}")
print(f"Your responses were: {responses}")
```

First, we create and `shuffle()` a list of `numbers`.
Next, we create an empty list for the `responses`.
Then, a `for` loop iterates our list of `numbers` .
The indented code following the `for` statement makes up the body of the loop and will be repeated for every `number` in the list.
In each iteration, the `input()` function obtains a `response` and appends it to the `responses` list which is displayed at the end, together with the actual `numbers`.
When we save the code above to a script called `numbers_game.py` and run it with `python numbers_game.py`, we'll see something like this:

```sh
guess a number between 1 and 3
2
guess a number between 1 and 3
1
guess a number between 1 and 3
3
The numbers were: [1, 3, 2]
Your responses were: ['2', '1', '3']
```

The lines that only contain a single number show the participants response.
Because the program will only exit the loop after reaching last `number` in `numbers`, the two `print()` statements at the end of the script are only executed once.

### Exercises
1. Modify the script so that it iterates a different set of numbers
3. What is the data type of the responses returned by `input()`? Use type casting to store `numbers` and `responses` in the same data type. What problems could this cause?
4. Let's assume that the script above runs a single block of the numbers game. Modify the script so that it runs three blocks of the experiment (Tip: you can wrap another `for` loop around the existing one).

## 2. Conditional Expressions

So far, our `numbers_game.py` script will always do exactly the same thing, irrespective of the participant's behavior.
However, certain behaviors may require our program to respond differently.
For example, we may want to convert the string returned by the `input()` function to an integer so that we can compare it to the target number.
This is fine when the input is a number, but it will throw a `ValueError` when the input contains letters.
To avoid this, we can adjust our program's response to the kind of input using an `if` statement:

```python
from random import shuffle

numbers = [1,2,3]
shuffle(numbers) # randomize
responses = [] # list for storing responses

for number in numbers: 
    # get response
    print(f"guess a number between {min(numbers)} and {max(numbers)}")
    response = input()
    if response.isdecimal(): # check if response is a number
        response = int(response)
    else:  # replace non-numbers with 0
        response = 0
    responses.append(response)
# print results
print(f"The numbers were: {numbers}")
print(f"Your responses were: {responses}")
```
The `if` statement takes an expression that can be either `True` or `False`.
If it is `True`, the indented code following the `if` is executed.
If it is `False`, the program skips ahead to the `else` block and executes that code.
Here, we use the use the `.isdecimal()` to test if the string only contains numbers.
If it does, we convert it to an integer and append it to the list of `responses`.
If not, we append zero instead.

The `if` statement could also contain an `elif` block that would be executed when the `if` condition is false but some other condition is true.
For example, let's assume that, by accident, sometimes participants press the letter e instead of 3.
To count all responses that are e as 3, we could modify our `if` statement like this:

```python
if response.isdecimal(): # check if response is a number
    response = int(response)
elif response == 'e':
    response = 3
else:  # replace non-numbers with 0
    response = 0
```

The `elif` block will be only be executed if the response is not a number and if it is equal to e.
To test that our code works as expected, let's run the current version of `number_game.py` and input some letters as well.

The result should look like this:

```sh
guess a number between 1 and 3
2
guess a number between 1 and 3
hello
guess a number between 1 and 3
1
The numbers were: [3, 2, 1]
Your responses were: [2, 0, 1]
```

Now all elements in `responses` are integers and the non-numeric input got replaced with zero.

### Exercises
1. Modify the script so that the participant receives feedback on whether the response was correct after every trial. How does this change the experiment? Do you think this modification would increase or decrease the participant's success rate?
2. Add `elif` blocks to convert the letters q, w, and e in the response to the numbers 1, 2 and 3. How could we deal with upper and lower case letters?

## 3. Generating Trial Sequences

So far, our script uses each number only once.
If we wanted to present numbers multiple times, we would have to edit the list of `numbers`.
This is not ideal - we should be able to separately define the experimental conditions (i.e. the different numbers) and the number of experimental trials.
Let's edit `numbers_game.py` so that it repeats the list of `numbers` to make a sequence for the desired number of trials:

```python
from random import shuffle

# create trial sequence
numbers = [1,2,3]
n_trials = 8
n_repeats = int(n_trials/len(numbers))
trials = numbers * n_repeats
shuffle(trials)

responses = [] # list for storing responses
for number in trials:
    print(f"guess a number between {min(numbers)} and {max(numbers)}")
    # get response
    response = input()
    if response.isdecimal(): # check if response is a number
        response = int(response)
    else:  # replace non-numbers with 0
        response = 0
    responses.append(response)
# print results
print(f"The numbers were: {numbers}")
print(f"Your responses were: {responses}")
```
Dividing the desired number of trials by the length of our list of `numbers` gives us the number of times we have to repeat the list.
To repeat the list we can make use of the fact that multiplying a list by an integer repeats that list.
To make the task a little easier, we can add a print statement that lets the participants know whether their response was correct.
Now we can set the number of trials independently from our list of conditions!

### Exercises
1. Modify the script so that it loads in the config file stored at `day1/config.json` and replace the hard-coded values of `numbers` and `n_trials` with the values from that config.
2. If `n_trials` is not divisible by `len(numbers)`, the resulting `trials` list may differ from the desired length. Modify the script to deal with this problem.
3. How could we change the program to ensure that the trial sequence does not contain any immediate repetition of the same number? Think about possible strategies rather than the concrete implementation (you are welcome to try though).

## 4. Saving Data

Currently, our script just prints out all responses.
However, we need to store our experimental data so we can analyze them later.
To this end we will use the `DataFrame` provided by the Pandas module.
This structure allows us to store different types of data in an intuitive tabular format and provides convenient methods to read and write them.
We can create a `DataFrame` from a dictionary where the keys will be used as column names.
In the dictionary, we can add a key for our responses and assign the value `None`.
This way, we won't have to change non-decimal characters to zero - we can simply leave the `None` value.
Also, instead of hard-coding the different numbers and the number of trials at the beginning of the script, we can load `day1/config.json` and use the parameters from that file.
The modified version of `numbers_game.py` looks like this:

```python
from random import shuffle
import json
import pandas as pd

# load configuration
with open('config.json', 'r') as f:
    cfg = json.load(f)

# create data frame
n_repeats = int(cfg['n_trials']/len(cfg['numbers']))
trials = cfg['numbers'] * n_repeats
shuffle(trials)
df = pd.DataFrame({'number':trials, 'response':None})

responses = []
for i in df.index:
    print(f"guess a number between {min(cfg['numbers'])} and {max(cfg['numbers')}")
    number = df.loc[i, "number"] # get current number
    # get response
    response = input()
    if response.isdecimal():
        response = int(response)
        df.loc[i, "response"] = response  # store response
        
df.to_csv("numbers_game_response.csv", index=False) # save data
```

Now, the `for` loop iterates the index of the data frame which contains the row numbers.
For each index `i`, we use `df.loc[i]` to get the corresponding row and access the number or store the response.
Instead of printing the response, we now save it to a file.
Let's run this version of `numbers_game.py` (make sure you are in the `day1` folder, otherwise the script won't find the config).
After the program ran, we should not see a response printed out - instead, there should be a file called `numbers_game_response.csv` in the current folder.

### Exercises
1. Discuss what may be advantages and downsides of storing data in the csv format.
2. In the `print` statement, why must we use single quotations for `cfg['numbers']`?
3. Assume you are worrying the experiment may crash at some point. Modify the script so that the data frame is stored after every trial.
4. Rerun the experiment but change the number of trials to 12 and save the result in a file with a different name.

## 5. Analyzing responses

Aside from providing a way to store our data, Pandas offers convenient methods for data analysis and visualization.
Let's create a new script called `analyze_responses.py` that loads the data stored in `numbers_game_response.csv` and analyzes them.
To start off, lets just print out the first lines of the data frame:

```python
import pandas as pd
df = pd.read_csv('numbers_game_response.csv')
print(df.head(3))
```
If we run this script with `python analyze_responses.py` (make sure you are in the `day1` directory or otherwise it won't find the csv file), we should see something like this:

```sh
   number  response
0       4         2
1       3         1
2       4         3
```

The numbers on the left represent the row index and the two named columns contain each trials number, as well as the participant's response.
The `.head()` method prints out the first rows of a data frame but we can also get rows at specific indices using the `.loc` attribute.
For example, we could edit the last line of `analyze_response.py` to print out rows 5 to 10:

```python
print(df.loc[5:10])
```

Note that `.loc` takes square, not round, brackets because it is not a class method but an attribute.
We can also use a mask to filter out all rows that satisfy a certain condition.
For example, to get all trials where the target number was 2, we could write the following:

```python
mask = df['number'] == 2
df2 = df[mask]
print(df2)
```

The first line used the comparison operator `==` to find all lines where `number` equals 2.
This returns a `mask` that is True for all rows where this conditions is met and False otherwise.
We can use this to index the data frame and get all rows where the `mask` is True.
Another convenient and useful method is `.value_counts()` which counts how often each unique value appears.
We edit the last line of `analyze_responses.py` to count how often each value appears in the trial sequence:

```python
print(df['number'].value_counts())
```

If our code for generating the trial sequences works as intended, all numbers should appear with the same frequency and the above line should print out this:

```sh
number
4    5
3    5
2    5
1    5
Name: count, dtype: int64
```

The left column shows the different unique values for the variable `number` and the right column shows the count for each value.
We can also compute the participants hit rate as the fraction of trials where the `response` equals `number`:

```python
n_correct = sum(df['number'] == df['response'])
percent_correct = (n_correct / len(df)) * 100
print(f"{percent_correct}% of all trials were answered correctly")
```

The first line computes the sum of correct responses.
The comparison operator `==` will return True for every columns where `number` and `response` are the same and False for every column where they are not.
Because the integer representation of True and False are 1 and 0, we can simply `sum()` the result to get the total number of correct responses.
To get the percentage of correct trials, we simply divide this number by the `len()` of the data frame and multiply by 100.

### Exercises
1. Do a value count on the responses. Is this information relevant for evaluating the participants behavior?
2. Modify the code that prints the percentage of correct trials so that it prints out the percentage of incorrect trials.
3. Calculate the hit rate for the first and second half of the response data. What could be reasons for changes in the hit rate over the course of an experiment?
4. Calculate the hit rate for each of the four numbers


## Project 

Write a new script that implements a game of rock, paper, scissors.
In on each trial, the program should choose randomly between one of the options, get the participants response and then print out the result and who won. Think about how to deal with responses other than "rock", "paper" or "scissors". Store all responses in a csv file.
