# How to create and manage Python environments without using Conda
You can use venv, a built-in Python tool for creating virtual environments. This method works on all platforms (Linux, macOS, and Windows) and is commonly used for isolating project dependencies.

# Steps to Create a Python Virtual Environment
## Ensure Python is Installed
First, make sure Python is installed on your system. You can check by running:

```bash
python --version
```
```bash
python3 --version
```
If Python is not installed, you can download it from the official website: python.org.

## Create a Virtual Environment
The basic syntax for creating a virtual environment is as follows:

```bash
python3 -m venv <name_of_environment>
```
Replace <name_of_environment> with the name you want to give your environment.
1. **-m:** This option stands for "module." It allows you to run a library module as a script, in this case, venv.
2. **venv:** The module being run, which is Python’s built-in module for creating virtual environments.
3. **myenv:** This is the name of the directory where the virtual environment will be created.

For example, to create a virtual environment called myenv, you can run:

```bash
python3 -m venv myenv
```
This command will create a new directory called myenv containing the virtual environment's files.

**Note:** On Linux or macOS, you might need to use python3 instead of python, depending on your system's configuration.

## Activate the Virtual Environment
After creating the environment, you need to activate it. The activation command depends on your operating system:

### Windows:
```bash
.\myenv\Scripts\activate
```
### Linux/macOS:
```bash
source myenv/bin/
```
When activated, the terminal prompt will change to indicate the name of the virtual environment (e.g., (myenv)).

How to check if the terminal is activated
### Windows:
```bash
where python
```
### Linux/macOS:
```bash
which python
```

## Install Packages
With the virtual environment active, you can install packages using pip. For example, to install requests, you can run:

```bash
pip install requests
```
Any packages installed using pip will be isolated to this environment and won't affect your global Python installation.

## Deactivating the Virtual Environment
Once you're done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```
This will return you to your system’s global Python environment.

## Verify Installation
To verify that the packages were installed in the virtual environment and not globally, run:

```bash
pip list
```
This will show the list of installed packages in the active environment.
