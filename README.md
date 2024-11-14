# Building Robust Neuroscience Experiments with Python and PsychoPy

## Welcome
This is the repository for a three-day online workshop hosted by the [open technology support Platform of the iBehave research network](https://ibehave.nrw/ibots-platform/about-ibots/).
In this workshop, we are going to learn how to implement neuroscience experiments in Python using the PsychoPy package.
We are going to leverage modern software engineering tools like automated testing, data validation and continuous integration to create robust applications that work exactly as intended. An example of such an application can be found [in this repository](https://github.com/OleBialas/posner_task).

Each day consists of four units, each of those units centers on a particular topic surrounding building experiments. Here is a brief outline of the days and topics:

### Day 1
- I. [Configuring an Experiment](day1/I_configuring_an_experiment.md)
- II. [Experimental Flow Control](day1/II_experimental_flow_control.md)
- III. Introduction to PsychoPy
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
This section goes through the different installation steps that are required to run all of the code presented in the notebooks.
Setting these things up for the first time can be a bit of a pain but you will only have to do it once!
If you experience any trouble while following these instructions, you can post your problem the [issues](https://github.com/OleBialas/psychopy_workshop/issues) section (make sure that you list the steps for reproducing your problem.


### Git
To install the Git, follow the instructions for your operating system on [the git webiste](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
After installing, open a terminal (on Windows, you can use the builtin Command Prompt) and check if git is detected by typing:

```sh
git --version
```

This should print out the version of your Git installation.
If it doesn't, that means that the terminal does not know the location of Git.
In this case, you'll have to add it to your PATH environment variable.
This is simply a list of all the places where a program should look for things - if you type `git` in your terminal, the program will search trough this list for a command called `git`, and throw and error if it can't find any.

On Windows, you can [follow this guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) for editing PATH using the graphical interface.
You'll have to add the path to you Git installation, which should be something like `C:\Program Files\Git\cmd\git.exe`, to PATH. Once you did that, restart the Terminal and try if the `git` command is recognized now.

Once git is working, you can configure your email and username by running the following while replacing the text inside the quotation marks with your actual user name and email.

```sh
git config --global user.name "example"
git config --global user.email "example@mail.com"
```

Then, move to the directory where you wish to store the content for this course using the `cd`(change directory) command.
Once you are in the correct director, clone this repository:

```sh
git clone https://github.com/OleBialas/psychopy_workshop.git
```

This should create a new subfolder called `psychopy_workshop` within your current directory.

### Python
You will also need an installation of Python 3.
You can download and [Anaconda](https://docs.anaconda.com/anaconda/install/) which is a Python distribution with a built-in package and environment manage system.
During the installation, you can opt to add Anaconda to your system's PATH.
To test that your conda installation is working, open a terminal (on Windows you can use the "Anaconda Prompt" that is part of the Anaconda distribution.

```sh
conda --version
```

If this throws an error, try adding conda to your PATH variable as described in the previous section.

### Environment

Once you installed Git and Python, you can install the required packages using the `environment.yml` file found in this repository.
Move to the directory that contains the workshop materials by typing something like:

```sh
cd <Path to>/psychopy_workshop
```

While substituting `<Path to>` with the directory where you stored the repository.
Then, type:

```sh
conda env create -f environment.yml
```

This will create a new environment and install all the required packages.
PsychoPy has a lot of dependencies so this may take a while.
Once the installation is finished you can activate your new environment by typing:

```sh
conda activate psychopy
```

All of the code presented in the notebooks should be executable with this environment.
If you are experiencing issues when installing the environment, this is most likely due to PsychoPy.
Check out their [installation section](https://www.psychopy.org/download.html) and, if that did not help, consult the [issues](https://github.com/OleBialas/psychopy_workshop/issues) section.

## Resources

### Packages

- [PsychoPy](https://psychopy.org/documentation.html) 
  
### Books

- **Robust Python: Write Clean and Maintainable Code** - this book by Patrick Viafore covers many of the core concepts from this workshop, like type-hinting, modularization and testing.
- **Python Testing with Pytest** - this book by Brian Okken elaborates all the things one can d withing the pytest framework, going far beyond this course.

### Papers

- **Bridges et al. (2020): The timing mega-study: comparing a range of experiment generators, both lab-based and online** - this paper compares response and stimulus timing across different programs and setups and provides detailed discussions on various aspects of experimental timing
- **Posner (1980): Orienting of Attention - this paper describes the attention cueing task this course uses as an example.
