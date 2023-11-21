# DIExample. 
Using profiles with Dependency Injection

## Introduction
This application illustrates Profiles (Modes) usage with [Injector](https://github.com/python-injector/injector)
library. This technique can be handy to build few environments like: development, test, production (default).

## Run
This application supports two running profiles: 
- default
- development

To run application execute one of the:
```
injector_example_main.py --Profile default
injector_example_main.py --Profile development
```
the profile name argument here will define classes implementations accordingly.

## Installation
To create a virtual environment, go to your project’s directory and run venv.
```
python3 -m venv venv
```
Venv will create a virtual Python installation in the venv folder.
Note You should exclude your virtual environment directory from your version control system using .gitignore or similar.
Activate the venv
```
source venv/bin/activate
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter:
```
which python
```
If you want to switch projects or otherwise leave your virtual environment, simply run:
```
deactivate
```
Pip can export a list of all installed packages and their versions using the freeze command:
```
pip freeze > requirements.txt
```
Then you can tell pip to install all the packages in `requrements.txt` using the -r flag:
```
python3 -m pip install -r requirements.txt
```
See more at [python.org](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)