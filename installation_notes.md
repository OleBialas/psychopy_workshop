## Git Installation and Cloning Repo

```bash
git --version
```

[x] Works in command prompt? </br>
[x] Works in powershell? </br>
[x] Works in Anaconda Prompt? </br>
    [ ] Setting PATH instructions? **Did not check**</br> 
    [ ] Configure git username? **Did not check**</br>
    [ ] Configure git email? **Did not check**</br>


[x] Cloning repo? </br>

---
## Python

```bash
conda --version
```

Without adding PATH

    [ ] In command prompt?</br>
    [x] Anaconda Prompt? </br>
    [ ] Powershell? </br>
    [ ] VSCode Terminal </br>


**What worked in VS Code without adding PATH (git bash)**
```bash
source ~/anaconda3/Scripts/activate
```

Easiest way I found was to open VS Code from anaconda prompt

---

## Environment

```bash
conda env install --file environment.yml
```

<span style="color:red">
ERROR: 

$conda env install --file environment.yml 

usage: conda-script.py env [-h] command ...

conda-script.py env: error: argument command: invalid choice: 'install' (choose from 'config', 'create', 'export', 'list', 'remove', 'update')

</span>


**What worked**
```bash
conda env create -f environment.yml
```