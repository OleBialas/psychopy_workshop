# Notebook 1 [28 minutes]

## Section 1 [15 minutes excluding exercise 5]

Copy pasting the code given gives a different output than one in the markdown (Probably because you changed numbers during testing but I am adding it here just in case.)

```bash
This variable is a <class 'float'>. 

As a string, it looks like this: 23.7
As an integer, it looks like this: 23
As a boolean, it looks like this: 23
As a float, it looks like this: 23.7

Lets try some arithmetic!
If we multiply the variable by three, we get: 71.1
If subtract 10 from the variable, we get: 13.7
```

#### 3. Rename the variable x. Can you choose any name or are there certain restrictions?

I was not clear what I was supposed to do. The options in my mind were
- change x to y in all instances of x
- use an integer as variable name
- use some python keywords as variable name (but if people are not aware of keywords, they would not know what to look for I guess)

Maybe the exercise could be split into multiple exercises exploring these options? 

#### 5. Consider a single trial of the [attention cueing task](https://en.wikipedia.org/wiki/Posner_cueing_task). Which inputs or parameters does the trial require? What outputs are generated? Discuss the appropriate data type for each input and output variable.

The wikipedia page was quite long and I decided to move on to next exercise because I was not sure if I could comprehend the article enough to decide what was applicable for the exercise. (But I think I will get back to it after I am done with all the exercises because this is super interesting!)

## Section 2 (7 minutes excluding the last exercise)

## Intro text
- **list**: mutable, ordered collections of values, defined with square brackets e.g. `x =[1, 2, 3]`
- **tuple**: immutable, ordered collection of values, defined with round braces e.g. `x = (1, 2, 3)`
- **set**: immutable, unordered collection of unique values, defined with curly braces e.g. `x={1, 2, 3}`

Maybe a brief explanation of mutable and immutable might help

#### 2. Test the arithmetic operators `+`, `-`, `*`, and `/` on the different collection types. Which operators work on which types and what do they do?

What I did was:

*type list*
```python
x = [1, 2, 3]
y = [4, 5, 6]
print(x + y)
```

*type tuple*
```python
x = (1, 2, 3)
y = (4, 5, 6)
print(x + y)
```

Is that what you wanted? 

#### 4. Discuss which collection would be best suited to store our experimental parameters.

Is this from the exercise 5 of previous session or the participants own experiments?

## Section 3

#### 1. Add an additional field to the dictionary that contains the experimental conditions "left" and "right".

```python (6 minutes)
config = { 
    "fix_dur": 0.75,
    "cue_dur": 0.5,
    "n_trials": 20,
    "n_blocks": 2,
    "p_valid": 0.8,
    "left": True,
    "right": False
} 
```
Is this what you wanted?
