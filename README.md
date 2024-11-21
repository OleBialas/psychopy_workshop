# Building Robust Neuroscience Experiments with Python and PsychoPy

## Welcome
This is the repository for a three-day online workshop hosted by the [open technology support Platform of the iBehave research network](https://ibehave.nrw/ibots-platform/about-ibots/).
In this workshop, we are going to learn how to implement neuroscience experiments in Python using the PsychoPy package.
We are going to leverage modern software engineering tools like automated testing, data validation and continuous integration to create robust applications that work exactly as intended. An example of such an application can be found [in this repository](https://github.com/OleBialas/posner_task).

Each day consists of four units, each of those units centers on a particular topic surrounding building experiments. Here is a brief outline of the days and topics:

### Day 1
- I. [Configuring an Experiment](day1/I_configuring_an_experiment.md)
- II. [Experimental Flow Control](day1/II_experimental_flow_control.md)
- III. [Introduction to PsychoPy](day1/III_psychopy.md)
- IV. Running an Experiment
### Day 2
- V. Modularizing an experiment
- VI. Type-based data validation
- VII. Automated unit testing
- VIII. Integration testing
### Day 3
- IX. Integrating external devices
- X. Packaging an experiment
- XI. Continuous Integration
- XII. Feedback

## Notebooks
For each unit, there is a markdown notebook in the folder corresponding to the respective day (e.g. the notebook for session II can be found at `day1/II_experimental_flow_control.md`.
Each notebook is composed of multiple sections.
These sections start with explanations and code examples and end with a set of exercises that test your understanding of the covered topic.
The exercises are typically ranked in order of increasing difficulty - while the first exercises require only small modifications on the code presented in the examples, the latter exercises go beyond those materials and may require some independent research.
Don't worry if you can't complete all exercises - if you find yourself stuck, just move on.

It is still recommended that you at least take a look at all of the exercises and then check the solutions that will be uploaded to the `solutions` folder, after the workshop.
At the end of every notebook (except the first one), you'll find a project.
The projects provide opportunities to rehearse and deepen your understanding of the materials outside of the course hours.

While some notebooks build on each other thematically, they are self sufficient in the sense that the examples do not require any code or data from other notebooks.
However, the notebooks do assume that you installed the required dependencies and downloaded the contents from this repository.

## Installation

In order to run all of the code presented in the notebooks, you need to clone this repository and set up the correct Python environment.
Always use this environment when working on the course contents!
If you use VSCode you can either start VSCode from the Command Prompt by simply typing `code` (after activating the environment ) simply or [select the environment in VSCode](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment).

If you experience any trouble while following installation, you can post your problem the [issues](https://github.com/OleBialas/psychopy_workshop/issues) section (make sure that you list the steps for reproducing your problem.

### Windows
First, we need to install the version control software git and the Python package manager uv.
You can do this by using Window's builtin package manager winget.
Simply open the Command Prompt (type "cmd" in the search window) and run
```sh
winget install -e --id Git.Git
```
to install git as well as
```sh
winget install -e --id astral-sh.uv
```
to install the uv package manager.
Once the installation is complete, close and re-open the Command Prompt.
To test, that the installation of git and uv was successful, type
```sh
git --version
uv --version
```
which should return the versions of the respective installation.
Now, we can clone the repository for this course.
Move to a folder of your choice using the `cd` command or stay in your user directory and run
```sh
git clone https://github.com/OleBialas/psychopy_workshop.git
```
which will download the course contents to a new folder called psychopy_workshop.
Next, we `cd` into the new folder and install the Python environment with uv
```sh
cd psychopy_workshop
uv sync --python 3.8
```
You can also use a newer Python version but this may require manual installation of additional dependencies.
Now, uv should have created a new folder called .venv (you can list the contents of your current directory by typing `dir`).
To activate the new environment type
```sh
.venv\Scripts\activate
```
Now you should see the name of the environment "psychopy_workshop" appear in brackets on the left side of your command line.
You are good to go!

### Linux

Setting up PsychoPy on Linux requires a few additional steps.
First, install the necessary dev libraries and git using the `apt` package manager (on Debian-based distributions like Ubuntu) by executing
```sh
sudo apt-get install libusb-1.0-0-dev portaudio19-dev libasound2-dev git-all
```
and install the uv package manager by typing
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Next, move to a directory of your choice using the `cd` command and clone the course repository by running
```sh
git clone https://github.com/OleBialas/psychopy_workshop.git
```
which will download the course contents to a new folder called psychopy_workshop.
Then, move to that new folder and create a virtual Python environment:
```sh
uv venv --python 3.10
```
which will create a new sub-directory in `psychopy_workshop` called `.venv`.
To activate the virtual environment type
```sh
source .venv/bin/activate
```
which should show you the name of the environment "psychopy_workshop" in brackets on the left side of your command line.
Next, download WxPython4 for your Linux distribution from [this website](https://extras.wxpython.org/wxPython4/extras/linux/gtk3/).
Note that there are multiple files in each directory that correspond to different versions of Python.
For example, `wxPython-4.2.2-cp310-cp310-linux_x86_64.whl` is the version compatible with Python 3.10.
For some distributions, like Debian 11, WxPython4 does not offer wheels for Python 3.10.
If you are using such a distribution, you must use a different Python version when creating the virtual environment.
Once the download finished, install the wheel by running something like
```sh
uv pip install ~/Downloads/wxPython-4.2.2-cp310-cp310-linux_x86_64.whl
```
depending on your download location and version of WxPython.
Once WxPython is installed you can install all remaining dependencies by simply running
```sh
uv pip install .
```
Now, you are good to go!

## Resources

### Packages

- [PsychoPy](https://psychopy.org/documentation.html) 
  
### Books

- **Robust Python: Write Clean and Maintainable Code** - this book by Patrick Viafore covers many of the core concepts from this workshop, like type-hinting, modularization and testing.
- **Python Testing with Pytest** - this book by Brian Okken elaborates all the things one can d withing the pytest framework, going far beyond this course.

### Papers

- **Bridges et al. (2020): The timing mega-study: comparing a range of experiment generators, both lab-based and online** - this paper compares response and stimulus timing across different programs and setups and provides detailed discussions on various aspects of experimental timing
- **Posner (1980): Orienting of Attention - this paper describes the attention cueing task this course uses as an example.
