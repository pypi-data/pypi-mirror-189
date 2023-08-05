# Running Static Code Analysis Locally

## Linter and static type checker 

Install the following python packages `flake8`, `pylint`, `mypy` and `pytest`. 

`mypy` (see [here](https://plugins.jetbrains.com/plugin/11086-mypy
)) and `pylint` (see [here](https://plugins.jetbrains.com/plugin/11084-pylint
)) are available as convenient plugins for pycharm. In order to use them, the executables need to be part of the `PATH`. They can be for example loacated at `C:\Users\eschnaub\AppData\Local\Programs\Python\Python39\Scripts`. To test it, run `pylint.exe` in a `cmd` window. If all is configured correctly, this should run `pylint`. 

Similarly, `flake8` has to be run manually calling `flake8.exe`. 

## Code quality checker

The code quality and security checkers, i.e., the Gitlab-integrated one and `Sonarqube`, will for now only be run from the remote side. 
