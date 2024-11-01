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

# How to Update Package Managers on Ubuntu
```
sudo apt update && sudo apt upgrade -y
```


# How to Update Package Managers AWS Linux or Centos
```
sudo yum update && sudo yum upgrade -y
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

# How to add the Splunk User to the Sudo group
```
usermod -aG sudo splunk
```

# Download Splunk Enterprise
Change directory to temporary files
```
cd /tmp
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
# How to export varibles
```
export SPLUNK_HOME=/opt/splunk/
```
## How to Save and close the file, then apply the changes:
```bash
source ~/.bashrc
```
This will ensure the variable is set permanently for your user across all sessions. If you need this change to apply system-wide, add it to /etc/profile or /etc/environment instead.

# How to Install the plocate utility - It helps you to locate files easily

```bash
sudo apt-get update && sudo apt install plocate
```

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

# How Enable bootstart (This will let your Splunk Web starts automatically without starting manually)
```
./splunk enable boot-start --accept-license -user splunk
```

# Change the ownership of /opt/splunk at root user after enable boot-start
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
/opt/splunk/bin/splunk start
```
## How to restart splunk web app at the bin directory
```
./splunk restart 
```
```
/opt/splunk/bin/splunk restart
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
sudo systemctl restart splunk
```
```
sudo systemctl status splunk
```
```
sudo systemctl stop splunk
```
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
