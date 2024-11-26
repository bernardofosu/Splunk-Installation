# FISH BUCKET
Splunk uses the fishbucket to track files that are being indexed into Splunk. 
## Which path can you find the fishbucket
```bash
$SPLUNK_HOME/var/lib/splunk/fishbucket
```
## Key Contents:
Inside the fishbucket directory, you will find a subdirectory named splunk_private_db

The fishbucket directory contains both;
- 1. Seek Pointers  
- 2. Cyclic Redundancy Checkers (CRCs)

### Seek Pointers
- **What it is: A seek pointer** is a marker that tells Splunk where it left off in a file when it last indexed data.
- Purpose: It helps Splunk efficiently resume reading a file by skipping over already-processed data instead of starting from the beginning. Which keeps track of how much of your file has been indexed into Splunk.
- How it works: When Splunk reopens a file, it uses the seek pointer to jump directly to the last read position.
The fishbucket is like the memory of Splunk to know whether a log has been ingested already.

### Cyclic Redundancy Checkers (CRCs)
- What it is: CRC is a hash value or checksum generated for a file's content to uniquely identify it.
- Purpose: It ensures Splunk can distinguish between different files or detect when a file has changed (e.g., truncated or rotated logs).
How it works:
- Splunk generates a CRC for the initial few kilobytes of a file to verify its identity.
- If the CRC of a file does not match the recorded value, Splunk treats it as a new file.

To prevent re-indexing a previously-read file Splunk runs a cyclic redundancy check against first and last 256 bytes of a file.

# HOW FISH BUCKET WORKS
- When Splunk is restarted file monitor processor checks if CRC is present in its database.

- If CRC is found and seek pointer is same as previous, then Splunk knows file has already been ingested.

- if CRC is not present or seek pointer is different than Splunk re-ingests whole file again. 

- The fish bucket is not basically for normal humans to investigate. 

- You will not see any content in the latest splunk version. But in older versions you may see some data.

[Read More on Fish Bucket](https://docs.splunk.com/Splexicon:Fishbucket)

[Read More on Fish Bucket form Kinney Group](https://kinneygroup.com/blog/splunk-fishbucket/#:~:text=What%20is%20Fishbucket?,inputstatus%20%5B%2Dinput%20%7C%20%2Dtype%5D)

[Read More on Fish Bucket](https://docs.splunk.com/Documentation/Splunk/latest/Troubleshooting/CommandlinetoolsforusewithSupport?_gl=1*1uuezc0*_ga*MTAwMjEyNDg3My4xNjk2NTE2OTQ1*_ga_GS7YF8S63Y*MTcwMjIyMDk1OS43OC4xLjE3MDIyMjA5NzQuNDUuMC4w*_ga_5EPM2P39FV*MTcwMjIxODE1NS43MC4xLjE3MDIyMjA5NzUuMC4wLjA.&_ga=2.35428706.299005456.1701735897-1002124873.1696516945#btprobe)

# Demo Time – Using BTPROBE TOOL
## Display hex for all monitored files
```bash
/opt/splunk/bin/splunk cmd btprobe -d /opt/splunk/var/lib/splunk/fishbucket/splunk_private_db/ -k ALL –validate
```
## Display Info About a Specific File
```bash
/splunk cmd btprobe -d /opt/splunk/var/lib/splunk/fishbucket/splunk_private_db/ --file /home/splunk/data/sales.log –validate
```
## How to Reset a Specific File
```bash
/splunk cmd btprobe -d /opt/splunk/var/lib/splunk/fishbucket/splunk_private_db/ --file /home/splunk/data/sales.log --reset
```

# FORWARDERS

A Splunk instance that forwards data to another Splunk instance, such as an indexer or another forwarder, or to a third-party system.

# TYPES OF FORWARDERS
There are three (3) types of forwarder:
- 1. Universal Forwarder
- 2. Heavy Forwarder
- 3. Light Forwarder – It is deprecated as of Splunk Enterprise version 6.0.0

# UNIVERSAL FORWARDER
- The universal forwarder is a dedicated, lightweight version of Splunk Enterprise that contains only the essential components needed to forward data.

- The sole purpose of the universal forwarder is to forward data.

- The universal forwarder does not support python. 

- It does not expose a User Interface (UI) or no frontend.

- The universal forwarder does not parse data except in certain limited situations.

# HEAVY & LIGHT FORWARDERS
- Both heavy and light forwarders are full Splunk Enterprise instances with certain features disabled.

- Heavy forwarder parses data before forwarding it.

- Heavy forwarder can route data based on criteria such as source or type of event.

- Heavy forwarder can index data locally, as well as forward data to another Splunk instance.

- Heavy forwarder cannot perform distributed searches.

- The light forwarder has been deprecated but continues to be available mainly to meet legacy needs.

# Demo Time – Install Universal Forwarder
## How Install Universal Forwarder (UF) on Windows
[How Install Universal Forwarder (UF) on Windows](https://docs.splunk.com/Documentation/Forwarder/9.3.1/Forwarder/InstallaWindowsuniversalforwarderfromaninstaller)

[How Install Universal Forwarder (UF) on Linux](https://docs.splunk.com/Documentation/Forwarder/9.3.1/Forwarder/Installanixuniversalforwarder#Next_steps)


# READING TASK
[Read More](https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Typesofforwarders)

[Read More](https://docs.splunk.com/Splexicon:Universalforwarder)

[Read More](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Installtheuniversalforwardersoftware)

### Configure Universal Forwarder (UF) on Windows to send logs to your Splunk Standalone (Enterprise)
[Short video on the Google Drive](https://drive.google.com/drive/u/0/folders/1-6w5dY043Yva4CxdKu8_99OMtuDUPQCZ)





