# Beginner's Guide to Splunk Installation

## Add this Ports to your inbound rules on the AWS EC2 Instance
```python
    Security Group/Firewall 
	a. Splunk Web Port - 8000
	b. Splunk Management Port (Splunkd) - 8089
	c. kvstore Port - 8191
	d. Secure Shell (SSH) - 22
	e. Splunk Receiving Port - 9997
```

# How to Update Package Managers AWS Linux or Centos
```
sudo yum update && sudo yum upgrade -y
```

# How to Update Package Managers on Ubuntu
```
sudo apt update && sudo apt upgrade -y
```

# How to Switch to Root User home directory
```
sudo su
```
```
cd ~ or cd /home
```

# How to Create Splunk User
```
useradd -m splunk
```

# How to add the Splunk User to the Sudo/wheel group
```
usermod -aG wheel splunk
```
## Why Not sudo?

- The choice to use wheel instead of sudo comes from traditional UNIX practices. The wheel group has historically been used to designate users who can perform administrative tasks, whereas the sudo group approach is more common in **Debian-based distributions like Ubuntu.**
- **Amazon Linux, being based on CentOS and Red Hat** principles, follows the wheel convention instead of creating a sudo group.
  
## If the above command did not work, run this command
```
sudo visudo
```
Put this commands inside the text editor and save it
```bash
## Allows people in group splunk to run all commands
splunk    ALL=(ALL)       ALL
```

# Download Splunk Enterprise
Change directory to temporary files
```
cd /tmp
```
## How to check the mount/space options for /tmp
```bash
df -h /tmp
```
```bash
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           475M     0  475M   0% /tmp
```
the space available cannot download splunk enterprise so we have to switch to /opt
```bash
cd /opt
```
## How to check the mount/space options for /opt
```bash
df -h /opt
```
```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       20G  1.7G   19G   9% /
```
# How to Install Splunk Enterprise
```
tar -xzvf <fileName> -C /opt
```
## Splunk Enterprise 9.3.0 Version
```bash
wget -O splunk-9.3.0-51ccf43db5bd-Linux-x86_64.tgz "https://download.splunk.com/products/splunk/releases/9.3.0/linux/splunk-9.3.0-51ccf43db5bd-Linux-x86_64.tgz"
```

# How to Check Splunk Version
```
./splunk version  
```

# Change the ownership of /opt/splunk at root user
```
sudo chown -Rf splunk:splunk /opt/splunk
```

## How to Save and close the file, then apply the changes:
```bash
source ~/.bashrc
```
This will ensure the variable is set permanently for your user across all sessions. If you need this change to apply system-wide, add it to /etc/profile or /etc/environment instead.

# How to Install the mlocate utility - It helps you to locate files easily

Update package
```bash
sudo yum update -y
```
Install Package
```bash
sudo yum install mlocate -y
```
## How to add to the mlocate to the database
```bash
sudo updatedb
```
## How to check the info of the mlocate
```bash
yum info mlocate
```

## How to check the where mlocate is located
```bash
which mlocate
```

This is expected because plocate is not be available on Amazon Linux by default. Instead, you can use mlocate, which serves a similar purpose.

## How to check mlocate version

# How to find the location of system.conf
```
locate system.conf
```
## You can use this path
```
/etc/systemd/system.conf
```
# How to increase ulimit -- example values in system.conf: - Uncomment and Change these lines
```python
DefaultLimitNOFILE=64000
DefaultLimitNPROC=16000
DefaultTasksMax=80%
```
## What Each Configuration Does
- **DefaultLimitNOFILE=64000:** This sets the maximum number of open file descriptors for the service to 64,000. This is useful for applications that need to handle a large number of files simultaneously, such as database servers.

- **DefaultLimitNPROC=16000:** This sets the maximum number of processes that the service can create to 16,000. This is relevant for services that may spawn many subprocesses.
  
- **DefaultTasksMax=80%:** This sets the maximum number of tasks that can be created by the service, expressed as a percentage of the total available tasks on the system.

# How Enable bootstart (This will let your Splunk Web starts automatically without starting manually)
```
sudo ./splunk enable boot-start --accept-license -user splunk
```

# Change the ownership of /opt/splunk at splunk user after enable boot-start
```
sudo chown -Rf splunk:splunk /opt/splunk
```

## How to check splunk status at the bin directory
```
./splunk status 
```
## How to check splunk status using absolute path
```
/opt/splunk/bin/splunk status
```

## How to start splunk web app at the bin directory
```
./splunk start 
```
```
/opt/splunk/bin/splunk <span style="color:red">start
```

## How to stop splunk web app at the bin directory
```
./splunk stop 
```
## How to the systemctl on splunk
```
sudo systemctl start splunk
```
```
sudo systemctl status splunk
```
```
sudo systemctl stop splunk
```
# Reload and Restart the Service:
```
sudo systemctl daemon-reload
```
```
sudo systemctl restart splunk
```
After making any changes to this configuration file, you should reload the systemd daemon and restart the service for the changes to take effect:

The command sudo systemctl can be executed from anywhere in the terminal, not just from a specific directory like /bin. Here's why:
Key Points
- **Systemd Commands:**
systemctl is a command-line utility for managing systemd services. It is available globally on the system, meaning you can invoke it from any directory without needing to be in a specific location.

- **Path Variable:**
The command is part of the system's PATH environment variable, which allows you to run it without specifying the full path. The typical directories included in PATH (like /usr/bin, /bin, etc.) contain system binaries, including systemctl.

- **Service Management:**
systemctl is used to manage services across the entire system, so you do not need to be in a particular directory where the service files or executables are located to issue commands related to them.
```bash
sudo systemtcl start <service name>
```
NB: without the service name the systemtcl command will not work

# How to Check Splunk Lincense
```
./splunk list licences
```

# How to Check Splunk Web Port (i.e 8000)
```
./splunk show web-port  
```

# How to locate user modified Configuration files
```
cd /opt/splunk/etc/system/local
```

# How to locate system default Configuration files
```
cd /opt/splunk/etc/system/default
```

# The path to system and app Configuration files
```bash
$SPLUNK_HOME/
├── etc/
│   ├── apps/
│   │   ├── my_custom_app/
│   │   │   ├── default/
│   │   │   ├── local/
│   │   │   │   └── inputs.conf
│   │   │   └── README
│   │   └── another_app/
│   ├── system/
│   │   ├── local/
│   │   │   ├── server.conf
│   │   │   ├── inputs.conf
│   │   │   └── outputs.conf
│   │   └── README
│   └── ...
```

# <span style="color:orange">Warning 🟠 :warning:</span>
Never change ownership in the root directory to any user because when the root loses its previllages to any user, user system is more likly corrupted.

```bash
Applications Users        cores        home         sbin         var
Library      Volumes      dev          opt          tmp
System       bin          etc          private      usr
```
## Using Long List (ll) command
```css
drwxrwxr-x+ 39 root  admin   1.2K Oct 29 18:23 Applications
drwxr-xr-x  68 root  wheel   2.1K Aug 28 04:01 Library
drwxr-xr-x@  8 root  wheel   256B Oct 30  2020 System
drwxr-xr-x   7 root  admin   224B Sep 25 18:49 Users
drwxr-xr-x   4 root  wheel   128B Oct 31 18:17 Volumes
drwxr-xr-x@ 38 root  wheel   1.2K Jan  6  2024 bin
drwxr-xr-x   2 root  wheel    64B Jun  5  2020 cores
dr-xr-xr-x   3 root  wheel   4.3K Oct 31 16:21 dev
lrwxr-xr-x@  1 root  admin    11B Jan  5  2024 etc -> private/etc
lrwxr-xr-x   1 root  wheel    25B Oct 31 16:23 home -> /System/Volumes/Data/home
drwxr-xr-x   3 root  wheel    96B Apr  1  2024 opt
drwxr-xr-x   6 root  wheel   192B Jan  6  2024 private
drwxr-xr-x@ 63 root  wheel   2.0K Jan  6  2024 sbin
lrwxr-xr-x@  1 root  admin    11B Jan  5  2024 tmp -> private/tmp
drwxr-xr-x@ 12 root  wheel   384B Jan  5  2024 usr
lrwxr-xr-x@  1 root  admin    11B Jan  5  2024 var -> private/var
```
If you experience permision issues try to add your user to the sudo group (Ubuntu) or to the wheel (AWS Linux) and use sudo permissions. You can also switch to root user to execute some commands to avoid permission issues.

# :sparkling\_heart: Support the project

I open-source almost everything I can and try to reply to everyone needing help using these projects. Obviously,
this takes time. You can use this service for free.

However, if you are using this project and are happy with it or just want to encourage me to continue creating stuff, there are a few ways you can do it:

*   Giving proper credit when you use github-readme-stats on your readme, linking back to it. :D
*   Starring and sharing the project. :rocket:

Thanks! :heart:

***

Credits:
- Sir Prince
- Sir Willy
- AGSDAC - Splunk Training
- [Splunk Docs](https://docs.splunk.com/Documentation)

Contributions are welcome! <3

Made with :heart: and Markdown.

**Powered By Nana Kwasi Ofosu-Duodu** :sparkling\_heart: