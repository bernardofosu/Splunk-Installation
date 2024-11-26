# Splunk Admin Class Labs

## Labs One
### 1. Splunk Web(GUI) 		

1. create a new role in Splunk --> name the role as bootcamp						
[documentation](https://docs.splunk.com/Documentation/Splunk/latest/Security/Addandeditroles)						
- New role (bootcamp) should inherit power and user roles (Take a screenshot)											
                                                
1a. create a new user in Splunk --> name of the user should be your firstname
[documentation](https://docs.splunk.com/Documentation/Splunk/latest/Security/Addandeditusers)						
Assign new_role (bootcamp) created in 1 should be assigned to the new user (your firstname), Take a screenshot											
                                                
1. use the CLI (authorize.conf) to create a role in Splunk --> name the role as atlanta
[documentation](https://docs.splunk.com/Documentation/Splunk/latest/Security/Addandeditroleswithauthorizeconf)
New role (atlanta) should inherit admin roles			restart splunk to effect changes									
- example of creating a role using authorize.conf						
```bash
[role_atlanta]
importRoles = admin	
```						
```bash
cd to /opt/splunk/etc/system/local
```
and add the example stanza to it Take a screenshot											
                                                
                                                
### 1. use the cli to create a user  -->name of the user should be your lastname
[documentation](https://docs.splunk.com/Documentation/Splunk/latest/Security/ConfigureuserswiththeCLI)
- Assign new_role (atlanta) created in 1 should be assigned to the new user (your lastname)												
- restart splunk to reflect changes
- To add a new user (lastname) with the password "qwerty123":						
- run the command in /opt/splunk/bin directory -->			
```bash
./splunk add user lastname -password qwerty123 -role atlanta
```						
Take a screenshot											
                                                
                                                
                                                
### Assigment due: Friday	 											
Please post four(4) screenshots in the admin group when you done with the assignment												
1. 1 screenshot for step1												
2. 1 screenshot for step2												
3. 1 screenshot for step3												
4. 1 screenshot for step4                                              
5. NOTE: Feel free to post your questions on the Slack channel for help.	

## Lab two (2)	
### 1. Create the first index (my_first_index) from the web GUI(front end )			
Note: do not make any changes to my_first_index leave all attributes as default			
            
### 2. Create a second index called my_second_index from the backend and specify the home, warm, and cold paths			
add a data retention period of 90 days to my_second_index			
            
HINTS			
3. Use nano to create your indexes.conf file at /opt/splunk/etc/system/local			
#### Sample of indexes.conf stanza
```bash			
[georgia]			
coldPath = $SPLUNK_DB/georgia/colddb			
homePath = $SPLUNK_DB/georgia/db			
maxTotalDataSizeMB = 512000			
thawedPath = $SPLUNK_DB/georgia/thaweddb			
```            
[Download the sample log from Datasets folder](https://drive.google.com/drive/u/0/folders/11uqJEUTeIFacAf5wLvyWmgPDOpPhh5AA)			
3b. Secure Copy (scp) the downloaded file from your personal computer to the remote server running Splunk			
HINT: Watch this video in the How-Tos Folder --> https://drive.google.com/file/d/189IiffxvllTHm7dM8HKcNS2vG44MSJ0y/view?usp=drive_link			
            
            
### 4. Create an inputs.conf file at /opt/splunk/etc/system/local to monitor the sample log you scp (uploaded) to your splunk server			
#### Sample of the inputs.conf		
```bash	
[monitor:///home/splunk/theNameOfTheSampleLogFile]			
index = my_second_index	
```
## Lab Three (3)
### 1a. Create two (2) new servers in AWS.																			
### 1b. One (1) server should be AWS Linux & One server should be a Windows Server																			
### 2. Set up a  universal forwarder on the Linux server.				
#### Install a *nix universal forwarder - Splunk Documentationm/Documentation/Forwarder/latest/Forwarder/

#### InstallaWindowsuniversalforwarderfromaninstaller															
### 3a. [Set up a  universal forwarder on the Windows Server](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/)
### 3b. [Install a Windowsuniversalforwarderfromaninstaller](https://docs.splunk.com/Documentation/Forwarder/9.1.2/Forwarder/InstallaWindowsuniversalforwarderfromaninstaller)														Configure your two new servers running a universal forwarder to contact one of your old servers already running Splunk (use the private ip of that server) - That old server becomes an Indexer												

Command to run of the new Linux Server - run the command at 

```bash
/opt/splunkforwarder/bin
```	

```bash				
./splunk add forward-server PUT THE PRIVATE IP OF THE OLD SERVER:9997
```

Example	
```bash
./splunk add forward-server 172.16.0.0:9997
```
### Submissions
#### 1. Take a screenshot of the outputs.conf that splunk created on your new Linux server																			
#### 1b. Run this command to display the outputs.conf - nano /opt/splunkforwarder/etc/system/local/outputs.conf

#### 2a. Take a screenshot of the outputs.conf that splunk created on your new Windows server																			
#### 2b. Run this command to display the outputs.conf
open the file explorer on the Windows server
```bash
Click on This PC												Click on Windows (C:)
Click on Programs Files
Click on splunkforwarder-->etc-->system-->local	Open the outputs file with notepad
```
                       
#### 3b. Install the Splunk Add-on for Microsoft Windows onto the Windows Server 
[Link to the add-on](https://splunkbase.splunk.com/app/742)

#### Ingest windows Application, Security, and Events logs
##### Example of the logs
```bash
###### OS Logs ######
[WinEventLog://Application]
disabled = 0
start_from = oldest
current_only = 0
checkpointInterval = 5
renderXml=false
index = windows

[WinEventLog://Security]
disabled = 0
start_from = oldest
current_only = 0
evt_resolve_ad_obj = 1
checkpointInterval = 5
blacklist1 = EventCode="4662" Message="Object Type:(?!\s*groupPolicyContainer)"
blacklist2 = EventCode="566" Message="Object Type:(?!\s*groupPolicyContainer)"
renderXml=false
index = windows

[WinEventLog://System]
disabled = 0
start_from = oldest
current_only = 0
checkpointInterval = 5
renderXml=false
index = windows
```

Finally, take a screenshot after running index=name_Of_Index_You_Store_The_Logs

### Challenge Lab
#### a. What is the purpose of the fishbucket?																			
#### b. What are two (3) main mechanism the fishbucket use to track an index file?

## Lab Four (4)
### Note: For this lab, we will spin up two new AWS Linux instances.
TASK ONE (1)																	
### Spin with two (2) AWS Linux instances with at least 20Gb storage capacity.																	
### 1b. Make sure port 8088 is open in your security group.																	
### 1. Install full splunk enterprise on server A.																	
### 2. On server B, you will not install any splunk component on it. 																	
### 2a. It is recommended to use the recorded class video as a guide																	
### 1. Set up and configure HTTP Event Collector (HEC) on server A using the guide in the documentation below:
[Documentation](https://docs.splunk.com/Documentation/Splunk/9.1.2/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Enterprise)				
#### Take screenshot 1 after setting up HEC on server A.															       
#### TASK TWO (2): Use server B to send data to server A using HTTP Event Collector (HEC)
##### On server B, run this command:
```bash
curl -k https://serverA_private_ip:8088/services/collector/event -H "Authorization: Splunk B5A79AAD-D822-46CC-80D1-819F80D7BFB0" -d '{"event": "hello world"}
```	
**Note:** **B5A79AAD-D822-46CC-80D1-819F80D7BFB0** should be replaced with your token.
**Note:** **serverA_private_ip** should be the private ip of server A

#### 2. If you used main index as the default index, run this search to see the event you sent via HEC
```bash
index=main
```

#### Take screenshot 2 for the search results.
**TASK THREE (3)**

**Note:** For this session, we will be ingesting data via Application Programming Interface (API)

Use the recorded class video as a guide.
[Download the Python script from here](https://drive.google.com/drive/u/0/folders/11uqJEUTeIFacAf5wLvyWmgPDOpPhh5AA)

#### Create an index called movie_idx using either Splunk web or the backend

#### On server A, create an app called movie under /opt/splunk/etc/

#### Within the movie app, create a subdirectory called bin
#### 1. Copy and paste the content of the python file you downloaded to a file called main.py
#### 2. Create an inputs.conf in your app local directory --> /opt/splunk/etc/apps/movie/local
##### example of the inputs.conf
```bash
[script://$SPLUNK_HOME/etc/apps/movie/bin/main.py]
disabled = false
index = movie_idx
interval = 5
sourcetype = _json"
```
##### Restart your splunk server
##### 1. Search in your movie_idx for newly ingest data --- Take a screenshot


## Lab Five (5)	
#### 1. Spin up 7 AWS instances with 6 Linux servers as 1 windows server 

#### Install Splunk full instance on 4 of the Linux servers and Splunk light weight instance on the 2 Linux and windows servers

#### Configure these components
1 Search Head, 2 Indexers, 1 DS/MC/LM and 3 Ufs (Using the global banner and later use the MC)

#### Create/install Apps and TAs and deploy to Ufs, SH and indexers via DS 
* all_deploymentclient_app push this to all servers reporting 
* all_fwd_outputs - push this to the UFs
* all_based_indexes - push this to the indexers 
* install Install 2 Apps from Splunk Base (Splunk Add-on for windows and Splunk Add-on for Unix and Linux) on the DS and move these apps to the $SPLUNK_HOME/etc/deployment-apps/

#### Create Serverclass
- all_deploymentclient
  clients - all hosts
- all_uf_outputs
  clients - UFs
- all_base_indexer
  clients - indexers
- all_windows_host
  App - Splunk Add-on for windows
  clients - windows host
- all_linux_host 
  apps - Splunk Add-on for Unix and Linux
  clients - linux hosts

#### Setup Distributed search 
DS and SH (only add indexers)

#### Monitoring Console to Monitor environment
DS - also edit the server roles and add the forwarder monitoring "										
                                                
## Lab Six (6)	
### LDAP Configuration and Active Directory Configuration on the windows Server

## Lab Seven (7)	
### Db Connect Configuration


# Personal Addition
### Props and Transform Configuration

### Splunk AWS Add-on Configuration 