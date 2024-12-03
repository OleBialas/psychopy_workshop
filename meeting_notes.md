Notebook density (how many % of students complete 80% of the notebooks)

Day 1:
I. Introduction to Python
Additional section for "surprising stuff"
Move dictionary introduction to session IV
Score: 100-80
II. Experimental Flow Control
Don't use list comprehension
Don't use range outside of a loop
enumerate and zip are not essential -> move to bonus section  (no one is going to see)
separate if and while
drop pandas from this section
Score: 0 go to 60
III. Introduction to Psychopy
Show how to get documentation on lazy imported modules
Technical issues with PsychoPy could get in the way
Score: 100 (could add more)
IV. Configuring an Experiment
Score: 20
Dense because it introduces two concepts at once: CLI and configuration
--> rearrange III and IV so there is one section on keyboard/sound+CLI and one one visual+configuration

Day 2:
I. Modularization:
Functions -> Break Down existing Script -> Complexity Measures with Radon
Introduce assert as a feedback mechanism together with functions
Variable scope / global variablesjk
Some examples of this use: https://github.com/nickdelgrosso/CodeTeachingMaterials/blob/main/notebooks/Python%20Functions.ipynb
II. Static Typing:
type hints ->   ->  ->
III. Testing
Assert Statements -> Pytest -> IPytest -> Test Coverage
IV.  Simulating an Experiment
Mock -> Patch -> w/ PsychoPy -> Fixtures -> Analyzing Simulated Data
Black Sheep:
Pydantic & Static Typing

Proposal:
Functions:
Write functions to satisfy assert statements
4 sections around teaching aspects of functions
Last (bonus section): Static Annotations of Functions for human- and machine-readable documentation, Show example of IDE warning
Testing:
Write assert statements to tests already-written functions
Mock & Patching (not with Pytest)
Project: Patch Psychopy to simulate a subject.