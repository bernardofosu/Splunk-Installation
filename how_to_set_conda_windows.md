# How to set up conda if its not showing after installation on windows
```bash
conda --version
conda init

Output: The command is not recognize
```

## Run this command in your command prompt
Trying to run **conda init** directly from the intallation folder by specifying the full path
```bash
"C:\Users\<YourUsername>\Ananconda\Scripts\conda.exe" init
```
```bash
"C:\Users\<YourUsername>\Miniconda\Scripts\conda.exe" init
```
This Approach forces the conda command to run from its actual location and its may help the PATH issues.

NOTE:
1. Restart the command prompt by closing and opening it again
2. Sometimes You have to Reboot the computer


# Finding the Miniconda Installation Folder on C: Drive

## Open File Explorer
Press Win + E or open File Explorer from the taskbar.

## Search for Miniconda
In the top-right search bar of File Explorer, type Miniconda and press Enter.
File Explorer will search your computer for any folder or files related to Miniconda.

## Manually Navigate to the Default Location
If Miniconda was installed with default settings, you can navigate to the following locations:
```bash
Single-user installation: 
C:\Users\yourusername\Miniconda3
All-user installation: C:\ProgramData\Miniconda3
```
## Use the Address Bar
If you know the path but want to quickly navigate there, you can use the Address Bar at the top of the File Explorer window.
Simply click the Address Bar, type the full path (e.g., C:\Users\yourusername\Miniconda3), and press Enter.

## Copy Path from File Explorer
Once you're inside the Miniconda folder in File Explorer, right-click on the folder name (e.g., Miniconda3), and select Copy address as text.
You can now paste the copied path into other applications like environment variables.

Let me know if you’re able to locate Miniconda, or if you need further assistance!

# Verify Path Addition
Make sure you've added the correct paths to the Path environment variable. The paths you need to add are:

# Manualy adding the Environment varibles
## Steps to Add Miniconda to the PATH Manually
### Open Environment Variables
1. Press Win + R, type **SystemPropertiesAdvanced**, and press Enter.
2. This will open the System Properties window.
3. Click the Environment Variables button at the bottom of the Advanced tab.

### Find the Path Variable
1. In the Environment Variables window, under User variables (for just your account) or System variables (for all users), look for a variable named Path.
2. If Path exists, select it and click Edit. If Path is not listed, click New and name it Path.

### Edit the Path Variable
1. In the Edit Environment Variable window, you should see a list of paths.
2. If the list is empty or you don’t see an option to add a path, click the New button on the right side of the window.
3. If you see a list of paths, click New to add a new entry.

### Add Miniconda Paths
1. Click New and add the following paths (adjust the yourusername part based on your actual username if needed):
```bash
C:\Users\yourusername\Miniconda3
C:\Users\yourusername\Miniconda3\Scripts
C:\Users\yourusername\Miniconda3\Library\bin
```
For System variables, ensure the paths are added in the same way, but note that you may need admin privileges to edit this section.

### Save the Changes
1. Once the paths are added, click OK to save and close the window.
2. Click OK in the Environment Variables window as well.

### Restart Command Prompt
1. Close and reopen Command Prompt (or your terminal of choice).
2. Test if Conda is available by typing:

```bash
conda --version
```

### If you get the problem below: follow the steps below to solve it 
```bash
conda --version
conda init

Output: The command is not recognize
```
## Run this command in your command prompt
Trying to run **conda init** directly from the intallation folder by specifying the full path
```bash
"C:\Users\<YourUsername>\Ananconda\Scripts\conda.exe" init
```
```bash
"C:\Users\<YourUsername>\Miniconda\Scripts\conda.exe" init
```
This Approach forces the conda command to run from its actual location and its may help the PATH issues.

NOTE:
1. Restart the command prompt by closing and opening it again
2. Sometimes You have to Reboot the computer


### Create a New Conda Environment
To create a new Conda environment with specific packages (e.g., Python 3.8), use the following command:
```bash
conda create --name myenv python=3.8
```
### Shortcut command:
```bash
conda create -n myenv python=3.8
```
This will create a new environment called myenv with Python 3.8.
#### In these commands:
1. **--name (or -n)** specifies the name of the environment. Here, it's set to myenv.
2. **python=3.8** specifies the version of Python to install in the environment, which will be Python 3.8.

### Activate the environment with:
```bash
conda activate myenv
```
### You can deactivate the environment with:
```bash
conda deactivate
```

### Managing Environments
You can list all your Conda environments with:
```bash
conda env list
``` 
Output:
```bash
╰─ conda env list                                                            ─╯
# conda environments:
#
base                  *  /opt/anaconda3
bootcamp_for_students     /opt/anaconda3/envs/bootcamp_for_students
geospatial               /opt/anaconda3/envs/geospatial
mysql_streamlit_crud     /opt/anaconda3/envs/mysql_streamlit_crud
```
NB: The * indicate the active or activated environment

### To remove an environment:
```bash
conda remove --name myenv --all
```

### Install Additional Packages
To install packages into an environment, you can use conda install:
```bash
conda install numpy pandas matplotlib
``` 
This will install the specified packages (e.g., numpy, pandas, matplotlib) into your current environment.

### Configure Conda to Automatically Activate (Optional)

If you want Conda to activate automatically when you open a new terminal session, make sure that conda init has been run correctly. You can verify this by checking if the following is added to your ~/.bashrc or ~/.bash_profile:
```bash
# added by Miniconda3 installer
. $HOME/miniconda3/etc/profile.d/conda.sh
conda activate base
```
This ensures that Conda initializes automatically each time you open a terminal.


# The forge channel is an optional third-party channel in conda often used for specialized packages or newer versions of packages not found in the default conda repositories. 

If you’re running conda install numpy pandas matplotlib and seeing a mention of forge, here’s what it means and how to proceed:
## Explanation of Channels
In conda, a channel is a repository where packages are stored and from which they are installed. The default channel provided by conda is called defaults (managed by Anaconda). Other popular channels include conda-forge, which is a community-driven repository hosting many open-source packages.

conda-forge: This is a robust community-maintained channel offering a wide selection of packages that may not always be in the default channels.

## Running conda install with Conda-Forge
**To install packages like numpy, pandas, and matplotlib, you don’t need to specify conda-forge unless a particular package or version isn’t available in the default channel or you need the conda-forge version for compatibility.**

If you prefer using conda-forge for these packages (e.g., for the latest versions), you can specify it explicitly:
```bash
conda install -c conda-forge numpy pandas matplotlib
```
This command tells conda to use the conda-forge channel for these packages.

## Adding Conda-Forge as a Default Channel
If you frequently need to install packages from conda-forge, you can add it as a default channel in your conda configuration:
```bash
conda config --add channels conda-forge
```
After adding it, conda will look in conda-forge when you install packages without needing to specify -c conda-forge.
Basic conda install Command

If you don’t need conda-forge for your installation, you can use the standard command:
```bash
conda install numpy pandas matplotlib
```
This will install numpy, pandas, and matplotlib from the default channels.

If the command prompt is working but powershell is not working after the above configuration

```bash
File C:\Users\PLANNING OFFICE\Documents\WindowsPowerShell\profile.ps1 cannot be loaded because running scripts is disabled on this system. For more information,
 see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:0 char:0
```

```bash
conda : The term 'conda' is not recognized as the name of a cmdlet, function, script file, or operable 
program. Check the spelling of the name, or if a path was included, verify that the path is correct     
and try again.
At line:1 char:1
+ conda --version
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (conda:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

# How to solve the powershell error
> This error indicates that PowerShell’s execution policy is preventing the profile script from running. By default, PowerShell restricts the running of scripts for security reasons. You can enable script execution to allow the Conda initialization to run by changing the execution policy.

## Here’s how to do it:
### Open PowerShell as Administrator
Press Win + S, type PowerShell, right-click on Windows PowerShell, and select Run as Administrator.

### Set the Execution Policy
Run the following command to allow scripts to run in PowerShell:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
When prompted, type Y to confirm or click on Yes to all to confirm and restart powershell

### Explanation:
**RemoteSigned** allows scripts created on your computer to run, but scripts downloaded from the internet must be signed by a trusted publisher.
**-Scope** CurrentUser applies this setting only to your user account, so it won’t affect other users or system-wide security.
1. Restart PowerShell
Close the current PowerShell window and open a new one.
2. Verify Conda

After restarting PowerShell, run:
```powershell
conda --version
```
## How to make it work with git bash
To make Conda work in Git Bash, you need to ensure that Git Bash can locate Conda in its PATH and also set up the environment correctly. Here’s how to configure it:

# Add Conda to Git Bash PATH
Open Git Bash.
Open or create a .bashrc file in your home directory by running:
```bash
nano ~/.bashrc
```
Add the following lines to the end of the .bashrc file, replacing PLANNING OFFICE with your actual path:

```bash
# Add Miniconda to PATH
export PATH="/c/Users/PLANNING OFFICE/miniconda3:/c/Users/PLANNING OFFICE/miniconda3/Scripts:/c/Users/PLANNING OFFICE/miniconda3/Library/bin:$PATH"
```
NB: We can locate this file manually or copy the file path and AI can help us get the full path.

Save the file by pressing CTRL + X, then Y, and Enter.

## Source the .bashrc file to apply the changes:
```bash
source ~/.bashrc
```
## Initialize Conda for Git Bash
After updating the PATH, initialize Conda specifically for Git Bash:
Run the following command in Git Bash:
```bash
conda init bash
```
Close and reopen Git Bash to reload the settings.

## Test Conda
Once you reopen Git Bash, test if Conda is working by running:
```bash
conda --version
``
