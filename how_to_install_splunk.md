# Click on the Links Below Based on What you need
# Features
- [Click on the Links Below Based on What you need](#click-on-the-links-below-based-on-what-you-need)
- [Features](#features)
- [Open your terminal and navigate to the directory that contains your AWS instance key.](#open-your-terminal-and-navigate-to-the-directory-that-contains-your-aws-instance-key)
- [How to Update Package Managers](#how-to-update-package-managers)
- [How to Switch to Root User home directory](#how-to-switch-to-root-user-home-directory)
- [How to Create a user on your Linux System](#how-to-create-a-user-on-your-linux-system)
- [How to create the Splunk User using 'adduser' command](#how-to-create-the-splunk-user-using-adduser-command)
- [How to create the Splunk User using 'useradd' command](#how-to-create-the-splunk-user-using-useradd-command)
	- [How to Create/Update User Password on the Linux System](#how-to-createupdate-user-password-on-the-linux-system)
	- [How to Create Custom Directory](#how-to-create-custom-directory)
- [How to Delete the User only without the home directory or all other files associated with the user](#how-to-delete-the-user-only-without-the-home-directory-or-all-other-files-associated-with-the-user)
	- [How to check if home directory exists](#how-to-check-if-home-directory-exists)
	- [**Interpret the Output**:](#interpret-the-output)
	- [Delete the Home Directory:](#delete-the-home-directory)
	- [If you want to force deletion without prompts, you can use the -f option as well:](#if-you-want-to-force-deletion-without-prompts-you-can-use-the--f-option-as-well)
- [Where to find users password when you have switch to the User](#where-to-find-users-password-when-you-have-switch-to-the-user)
- [How to set ownership for the home directory.](#how-to-set-ownership-for-the-home-directory)
- [How to add the Splunk User to the Sudo group](#how-to-add-the-splunk-user-to-the-sudo-group)
	- [How to check the user groups](#how-to-check-the-user-groups)
	- [How to check if the user belongs to the sudo group](#how-to-check-if-the-user-belongs-to-the-sudo-group)
	- [How to check sudo previllages](#how-to-check-sudo-previllages)
- [Download Splunk Enterprise](#download-splunk-enterprise)
- [How to Install Splunk Enterprise](#how-to-install-splunk-enterprise)
	- [Splunk Enterprise 9.3.0 Version](#splunk-enterprise-930-version)
	- [Splunk Enterprise 9.1.6 Version](#splunk-enterprise-916-version)
	- [Splunk Universal Forwarder 9.3.0 Version](#splunk-universal-forwarder-930-version)
	- [Splunk Universal Forwarder 9.1.6 Version](#splunk-universal-forwarder-916-version)
- [Change the ownership of under root /opt/splunk (Switch to the splunk user)](#change-the-ownership-of-under-root-optsplunk-switch-to-the-splunk-user)
- [How to set $SPLUNK\_HOME to be equal to /opt/splunk](#how-to-set-splunk_home-to-be-equal-to-optsplunk)
	- [How to check if the export command has worked](#how-to-check-if-the-export-command-has-worked)
	- [How to change ownership individually by specify the sub directory](#how-to-change-ownership-individually-by-specify-the-sub-directory)
- [How to Install the plocate utility - It helps you to locate files easily](#how-to-install-the-plocate-utility---it-helps-you-to-locate-files-easily)
	- [if the plocate is giving error (unable to locate packages plocate)](#if-the-plocate-is-giving-error-unable-to-locate-packages-plocate)
- [How to find the location of system.conf](#how-to-find-the-location-of-systemconf)
	- [You can use this path](#you-can-use-this-path)
- [How to increase ulimit -- example values in system.conf: - Uncomment and Change these lines](#how-to-increase-ulimit----example-values-in-systemconf---uncomment-and-change-these-lines)
	- [What Each Configuration Does](#what-each-configuration-does)
- [How Enable bootstart (This will let your Splunk Web starts automatically without starting manually)](#how-enable-bootstart-this-will-let-your-splunk-web-starts-automatically-without-starting-manually)
	- [ls root](#ls-root)
- [If you get get server error and cannot login to the splunk web will run this security check command.](#if-you-get-get-server-error-and-cannot-login-to-the-splunk-web-will-run-this-security-check-command)
	- [After the above command then you restart splunk enterprise](#after-the-above-command-then-you-restart-splunk-enterprise)
- [How to Change Splunk Web Admin Password](#how-to-change-splunk-web-admin-password)
- [:sparkling\_heart: Support the project](#sparkling_heart-support-the-project)
# Open your terminal and navigate to the directory that contains your AWS instance key.
Run the command below to connect to the remote server

```
ssh -i your_key.pem ubuntu@<public ip address>
```
# How to Update Package Managers
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

# How to Create a user on your Linux System
There are two ways to create a user on linux box
- adduser
- useradd

With the adduser option, you will get a prompt to create your password and add your personal information, and the home directory for the user will be created automatically. 

# How to create the Splunk User using 'adduser' command
```
adduser splunk
```
The adduser is the command, and the splunk is the username. You can give any name of your choice, but Splunk is more preferable for the bootcamp. 
NB: Use lower case letters for naming variables in this bootcamp.

# How to create the Splunk User using 'useradd' command
```
adduser splunk
```
# Create a Splunk User (using adduser)
## echo "Creating Splunk user..."
```bash
sudo adduser --disabled-password --gecos "" splunk
```
### Explanation:
```bash
sudo adduser --disabled-password --gecos "" splunk
```
- **--disabled-password:** This option prevents the adduser command from prompting for a password.
- **--gecos** "": Skips the interactive prompts for full name and other details.
- This creates the splunk user without requiring any user input.
  
# Step 4a: Set a password for the Splunk user (automatically)
echo "Setting password for Splunk user..."
```bash
echo "splunk:splunkpassword" | sudo chpasswd  # Replace "splunkpassword" with your desired password
```
Automatically sets the password for the splunk user. Replace "splunkpassword" with the password you wish to set.

## How to Create/Update User Password on the Linux System
```
passwd splunk
```
If it ask for password, and you don’t know or you don’t remember, type exit twice to return to root user and run the command above.

With the useradd option, you have to create your password and the home directory for manually. 

If you run the command below, the home directory will be created automatically. 

```
useradd -m splunk
```
The **-m** option creates the home directory if it does not already exist.

## How to Create Custom Directory
```
useradd -m -d /home/splunk <username>
```
- The -m option creates the home directory if it does not already exist.
- The -d option specifies the path to the new home directory.
Replace /home/splunk with the actual path you want to use (e.g., /home/splunk).
Replace username with the desired username for the new user.


# How to Delete the User only without the home directory or all other files associated with the user

```
userdel splunk
```
```
sudo userdel splunk
```
## How to check if home directory exists
```
cat /etc/passwd | grep splunk
```
```
getent passwd splunk
```
## **Interpret the Output**: 
If the user exists, you should see a line similar to this:
NB: If the user is the first user created aside the default ubuntu and you also named the user splunk, if not the username and the id will change
```
splunk:x:1001:1001::/home/splunk:/bin/sh
```
## Delete the Home Directory: 
If the home directory exists, you can delete it 	using the rm command:
```
sudo rm -r /home/splunk
```
The **-r** option allows for recursive deletion, which means it will delete the directory and all its contents.

## If you want to force deletion without prompts, you can use the -f option as well:
```
sudo rm -rf /home/splunk
```
Important Notes:
- Caution with rm **-rf**: Be very careful when using **rm -rf**, as it will delete files and directories without any confirmation. Double-check the path to ensure you’re deleting the correct directory.
- Data Loss: Deleting the home directory will permanently remove all files and data stored there.

# Where to find users password when you have switch to the User
```
cd /opt/etc/passwd
```
# How to set ownership for the home directory.
```
sudo chown splunk:splunk /home/splunk  
```
when you see permission denied, then it maybe ownership issues, which means you have to change permission from the root to splunk using the above code.

# How to add the Splunk User to the Sudo group
```
usermod -aG sudo splunk
```
## How to check the user groups
```
id splunk
```
## How to check if the user belongs to the sudo group 

```
grep ’sudo’ /etc/group 
```

## How to check sudo previllages 

```
sudo cat /etc/sudoers
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

## Splunk Enterprise 9.1.6 Version
```bash
wget -O splunk-9.1.6-a28f08fac354-Linux-x86_64.tgz "https://download.splunk.com/products/splunk/releases/9.1.6/linux/splunk-9.1.6-a28f08fac354-Linux-x86_64.tgz"
```

## Splunk Universal Forwarder 9.3.0 Version
```bash
wget -O splunkforwarder-9.3.0-51ccf43db5bd-Linux-x86_64.tgz "https://download.splunk.com/products/universalforwarder/releases/9.3.0/linux/splunkforwarder-9.3.0-51ccf43db5bd-Linux-x86_64.tgz"
```

## Splunk Universal Forwarder 9.1.6 Version
```bash
wget -O splunkforwarder-9.1.6-a28f08fac354-Linux-x86_64.tgz "https://download.splunk.com/products/universalforwarder/releases/9.1.6/linux/splunkforwarder-9.1.6-a28f08fac354-Linux-x86_64.tgz"
```

# Change the ownership of under root /opt/splunk (Switch to the splunk user)
```bash
su - splunk
sudo chown -Rf splunk:splunk /opt/splunk
```
Breakdown of the Command
- chown: This command is used to change the ownership of files and directories in Linux.
- splunk:splunk: This specifies the new owner and group for the directory:
- splunk (before the colon) is the username of the new owner.
- splunk (after the colon) is the group name that the directory will belong to.
- /opt/splunk: This is the path to the directory whose ownership you are changing.
  
Explanation of Options
- -R (Recursive): This option tells the command to change the ownership of not just the specified directory but also all files and subdirectories inside it. This is important when you want to apply the ownership change to everything within that directory.
- -f (Force): This option suppresses most error messages and overrides certain restrictions. It can be used to avoid errors about files that do not exist or cannot be changed for some reason. For example, if there are files that you do not have permission to change, using -f would prevent those errors from being displayed.

# How to set $SPLUNK_HOME to be equal to /opt/splunk
```
export SPLUNK_HOME=/opt/splunk
```

## How to check if the export command has worked 
```
echo $SPLUNK_HOME
```

## How to change ownership individually by specify the sub directory

```
chown splunk:splunk /home/splunk/.bashrc  #one 
```
Multiple:
```
chown splunk:splunk /home/splunk/.bash_logout /home/splunk/.profile #two
```

# How to Install the plocate utility - It helps you to locate files easily
```bash
sudo apt install plocate
```

## if the plocate is giving error (unable to locate packages plocate)
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
## What Each Configuration Does
- **DefaultTasksMax=80%:** This sets the maximum number of tasks that can be created by the service, expressed as a percentage of the total available tasks on the system.

- **DefaultLimitNOFILE=64000:** This sets the maximum number of open file descriptors for the service to 64,000. This is useful for applications that need to handle a large number of files simultaneously, such as database servers.

- **DefaultLimitNPROC=16000:** This sets the maximum number of processes that the service can create to 16,000. This is relevant for services that may spawn many subprocesses.
# How Enable bootstart (This will let your Splunk Web starts automatically without starting manually)
```
# How to turn off THP (THP means transparent huge pages)
```
echo 'never' > /sys/kernel/mm/transparent_hugepage/enabled
echo 'never' > /sys/kernel/mm/transparent_hugepage/defrag
```

# Navigate or change directory to bin directory to run the commands for the binaries or the executables 
```
cd /opt/splunk/bin
```
Why changing to the bin folder to run the commands bellow
- Because the bin folder contains all the binary and executable files of splunk

# How Enable bootstart (This will let your Splunk Web starts automatically without starting manually)
```
sudo ./splunk enable boot-start --accept-license -user splunk
```
# How to check if enable bootstart was succesful
```bash
 sudo systemctl is-enabled splunk
sudo ./splunk display boot-start
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

## How to stop splunk web app at the bin directory
```
./splunk stop 
```

# How to change ownership of /opt/splunk 
```
sudo chown -Rf splunk:splunk /opt/splunk
```

# How to Check Splunk Version
```
./splunk version  
```

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

## ls root
```css
lrwxrwxrwx   1 root root     7 Apr 22  2024 bin -> usr/bin/
drwxr-xr-x   2 root root  4096 Feb 26  2024 bin.usr-is-merged/
drwxr-xr-x   5 root root  4096 Oct 31 08:35 boot/
drwxr-xr-x  16 root root  3240 Nov  2 19:12 dev/
drwxr-xr-x 108 root root  4096 Oct 31 08:35 etc/
drwxr-xr-x   4 root root  4096 Oct 31 01:13 home/
lrwxrwxrwx   1 root root     7 Apr 22  2024 lib -> usr/lib/
drwxr-xr-x   2 root root  4096 Apr  8  2024 lib.usr-is-merged/
lrwxrwxrwx   1 root root     9 Apr 22  2024 lib64 -> usr/lib64/
drwx------   2 root root 16384 Sep 27 08:38 lost+found/
drwxr-xr-x   2 root root  4096 Sep 27 08:36 media/
drwxr-xr-x   2 root root  4096 Sep 27 08:36 mnt/
drwxr-xr-x   3 root root  4096 Oct 31 01:17 opt/
dr-xr-xr-x 201 root root     0 Nov  2 19:12 proc/
drwx------   5 root root  4096 Oct 31 01:47 root/
drwxr-xr-x  28 root root   900 Nov  2 19:17 run/
lrwxrwxrwx   1 root root     8 Apr 22  2024 sbin -> usr/sbin/
drwxr-xr-x   2 root root  4096 Mar 31  2024 sbin.usr-is-merged/
drwxr-xr-x   7 root root  4096 Nov  2 19:17 snap/
drwxr-xr-x   2 root root  4096 Sep 27 08:36 srv/
dr-xr-xr-x  13 root root     0 Nov  2 19:12 sys/
drwxrwxrwt  12 root root  4096 Nov  2 19:19 tmp/
drwxr-xr-x  12 root root  4096 Sep 27 08:36 usr/
drwxr-xr-x  13 root root  4096 Oct 31 00:55 var/
```
# If you get get server error and cannot login to the splunk web will run this security check command.
```
sudo -u splunk echo -e "[settings]\nstartwebserver = True\nenableSplunkWebSSL = True\nsslVersions = tls1.2\n" >> /opt/splunk/etc/system/local/web.conf
```
## After the above command then you restart splunk enterprise
```
./splunk restart
```
if you are not in the bin directory, then you have to run this command (absolute path)
```
/opt/splunk/bin/splunk restart
```
# How to Change Splunk Web Admin Password
Click here [youtube video](https://www.youtube.com/watch?v=kkX0XwPpX2A&t=614s "Please Subscribe to her Channel") to change the splunk web admin password and username.

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
