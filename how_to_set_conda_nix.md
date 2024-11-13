# How to set up conda on Unix and Linux

# How to Set Up Conda on Unix/Linux

Setting up **Conda** on Unix (Linux and macOS) is a straightforward process, but it does require a few specific steps. Below are the instructions to install and configure Conda, whether you're using **Miniconda** or **Anaconda**.

## Steps to Set Up Conda on Unix/Linux

### 1. Download Miniconda or Anaconda
You can choose to install either **Miniconda** (lightweight version) or **Anaconda** (full version with many pre-installed packages).

- **Miniconda** is recommended if you want a smaller initial installation and to install only the packages you need.
- **Anaconda** is a larger distribution that includes many pre-installed scientific packages, which might be useful if you need a full data science environment right away.

#### Download Miniconda:
- Go to the official Miniconda download page: [Miniconda Downloads](https://docs.conda.io/en/latest/miniconda.html)
- Choose the version for your architecture (Linux 64-bit or ARM) and Python version (usually Python 3.x).

For example, you can download Miniconda with `wget` like this:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
``` 
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2024.07-Linux-x86_64.sh
``` 
On macOS, the wget command may not be installed by default. Instead, you can use curl, which is pre-installed on macOS. Here's how you can download the Miniconda installation script using curl:
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
``` 
### Verify the download: Once the download is complete, you can list the contents of your current directory to ensure the script is there:
```bash
ls
```

### Run the Miniconda installation script: After the script is downloaded, run the following command to install Miniconda:
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```
```bash
bash Anaconda3-2024.07-Linux-x86_64.sh
```

### Follow the prompts:

1. Press Enter to review the license agreement.
2. Type yes to accept the terms.
3. Choose the installation directory (default is ~/miniconda3 or ~/anaconda3).
4. Confirm the installation location.
5. Allow the installer to initialize Conda by running conda init.

After the installation finishes, the installer will add Conda to your ~/.bashrc or ~/.bash_profile (depending on your shell). This will automatically initialize Conda when you start a terminal session.

### Activate Conda in Your Shell
To enable Conda, you will need to restart your terminal or manually source the shell configuration file.
#### Restart your terminal or run:
```bash
source ~/.bashrc
```
This will activate Conda in your current terminal session.

### Test the Installation
Once you have installed Conda, you can verify that it’s set up correctly by running:
```bash
conda --version
```
This should print the installed version of Conda.

### Update Conda (Optional but Recommended)
You can update Conda to the latest version using the following command:
```bash
conda update conda
```

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

