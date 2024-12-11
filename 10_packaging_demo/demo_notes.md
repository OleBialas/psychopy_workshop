# Packaging and Continuous Integration Demo

## 1. Overview of the Experiment
- Run the experiment (they may already be familiar with it from session 3)

- Revisit key topics from day 1:
- Modular organization of code into functions
- One function does one thing
- Type hints for self documenting code
- proper function naming
- separating the code and mechanism
- Configuration file
- Command line interface
- Passing the config file via the CLI
- Revisit Topics from day2:
- testing
- pytest
- fixtures
- mocking
- Talk about testing strategy: Which parts should you focus your efforts on?
- Running an automated experiment
  
  ## 2. Make experiment into an installable package

  - create a new folder for the packaging demo and moce the content from session 10 there
  - Put experiment.py in src folder
  - add pyproject.toml
  - do pip install -e .
  - test that this is working
  - now push the folder to a new github repo
  - do a pip install from git --> now we can install and run our experiment anywhere