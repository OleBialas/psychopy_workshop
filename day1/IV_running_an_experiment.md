# IV. Running an Experiment

Now we know all the building blocks to create and run an actual experiment.
In this notebook, we are going to run an our own implementation of a spatial attention cueing task which was originally developed by Michael Posner and is thus often referred to as the Posner task.
We are also going to learn how to create a little command line interface (CLI) for the experiment and how to store experimental data for multiple subjects.

## 1. Fixing errors

The `day1` folder contains a script called `posner_experiment.py` that contains an implementation of the Posner attention cueing task.
Open the script in your editor and have a look at its content.
Don't worry about details, just get a rough idea of what the script is doing - most of the functions and classes in there should feel familiar from the previous sessions.
Once you are done reviewing the code, we can run the experiment.

But wait, there is a catch!
The script contains multiple errors which we have to fix in order to run the experiment.
Before we start debugging, let's look at some the most common errors and their meanings:

- `TypeError`: indicates that a variable has the wrong type for a given operation
- `ValueError`: indicates that the type is correct but the value is invalid
- `FileNotFoundError`:

Now that we have a basic understanding of the most common exceptions in Python, let's start to debug our experiment.
If we run our experimental script with `python posner_experiment.py` it won't take long until we see the first error message pop up.

```
Traceback (most recent call last):
  File "/home/obi/projects/psychopy_workshop/day1/posner_task.py", line 11, in <module>
    with open("posner_task_cfg.json") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'posner_task_cfg.json'
```

The first line tells us that this is where the
 
