# Interview Questions (Splunk)
### 1. When you want to parse data and you are finding it dificult, where will you go or what website will you website to find app developed by others without starting from scratch
**Answer: Splunk base**

### 2. When onboard data and everything looks good, the indexing port open, you have configured inputs.conf. what is the best tool for troubleshoot to find the problem
**Answer: Btool**

This might be that, there double inputs.conf, one in apps local, system local. This will be conflicting and splunk will find it difficult which one to use, and it will may not use any of them. Deleting one probably the one at systems local and logs will start coming

### 3. What stage of the data ingest flow is when incoming raw data stream is breakdown into individual events based on line breaks (linebreaker).
**Answer: Parsing Pipeline**

### 4. What stage of the data ingest flow is when metadata (e.g., host, source, sourcetype) is extrated from incoming raw data stream
**Answer: Parsing Pipeline**

### 5. What stage of the data ingest flow is when multiple small chunks of data are combined into larger aggregated events to optimize processing (aggregator).
**Answer: Merging Pipeline**

### 6. What stage of the data ingest flow is when regex patterns applies to the data
 

### 7. What stage of the data ingest flow is when data is finalizes, processed and prepares for indexing.
**Answer: Index Pipeline**

### 8. What is the difference between Splunk App and Splunk Add-on

### 9. Which Configuration file is use for accessing user data or managing users and roles
**Answer: authorize.conf**

### 11. What are the two types of indexes and what types data they can stored
- **Metric Index:** A Metric Index is designed to store time-series data such as performance metrics (CPU, memory, latency, etc.)
- **Event Index:** Event Index
An Event Index is the traditional type of Splunk index, used to store unstructured or semi-structured log/event data such as application logs, security logs, or transaction logs.

### 12. Where can you find splunk logs and list some of the internal logs

### 13. What is the name of splunk daemon and what its does


### 14. Where can you find the fishbucket
/opt/splunk/var/lib/splunk/

### 15. What is the purpose of splunk fishbucket
The fishbucket in Splunk is a special directory that keeps track of data inputs. It ensures that Splunk does not re-index the same data and can resume data processing from where it left off in the event of a disruption.

#### Seek Pointers
- **What it is:•• A seek pointer is a marker that tells Splunk where it left off in a file when it last indexed data.
- Purpose: It helps Splunk efficiently resume reading a file by skipping over already-processed data instead of starting from the beginning. Which keeps track of how much of your file has been indexed into Splunk.
- How it works: When Splunk reopens a file, it uses the seek pointer to jump directly to the last read position. The fishbucket is like the memory of Splunk to know whether a log has been ingested already.

#### Cyclic Redundancy Checkers (CRCs)
- What it is: CRC is a hash value or checksum generated for a file's content to uniquely identify it.
- Purpose: It ensures Splunk can distinguish between different files or detect when a file has changed (e.g., truncated or rotated logs). How it works:
- Splunk generates a CRC for the initial few kilobytes of a file to verify its identity.
- If the CRC of a file does not match the recorded value, Splunk treats it as a new file. To prevent re-indexing a previously-read file Splunk runs a cyclic redundancy check against first and last 256 bytes of a file.


### 16. What are the ways splunk ingest data
File Monitoring using Universal Forwarders
API Calls using HTTP Event Collector (HEC) is a feature in splunk that allow you to send data to splunk over HTTP or HTTPS

### 17. What is the management port and when its applicable 
8089, it can be use for distributed search environment,

### 18. What is the default port to communicate with deployment server

### 19. what is the default port for creating search peers

### 20. What is the path splunk store indexes
/opt/splunk/var/lib/splunk

### 21. 

### Splunk Ports
| **Port**             | **Component**                     | **Default/Convention**       | **Description**                                                                                                         |
| -------------------- | --------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **514**              | Syslog                            | Convention - Not Recommended | Syslog (TCP or UDP). Recommended to send Syslog to a Syslog Collector tool like Syslog-NG or rsyslog instead of Splunk. |
| **8000**             | Web Interface                     | Default                      | Splunk Web (HTTP by default).                                                                                           |
| **8080, 9887**       | Indexers                          | Default                      | Port used for Indexer replication.                                                                                      |
| **8081, 8181, 9887** | Search Heads                      | Default                      | Search Head Cluster (SHC) replication.                                                                                  |
| **8088**             | HTTP Event Collector (HEC)        | Default                      | Collects data sent to Splunk over HTTP.                                                                                 |
| **8089**             | Splunk                            | Default                      | Management port.                                                                                                        |
| **8089**             | Indexers                          | Default                      | REST API access for indexers.                                                                                           |
| **8089**             | Deployment Server                 | Default                      | Management port for Splunk deployment server.                                                                           |
| **8089**             | Search Heads                      | Default                      | Management port for Splunk search heads.                                                                                |
| **8191**             | KVStore                           | Default                      | Internal KVStore communication and replication.                                                                         |
| **9997**             | Forwarders                        | Convention                   | Default forwarding port for sending data to indexers.                                                                   |
| **9998**             | Universal Forwarders and Indexers | Default                      | SSL communication between forwarders and indexers.                                                                      |

### 1. What is the difference between server.conf and web.conf
**web.conf** controls splunk web interface, configure settings such as web server ports, SSl, and user themes whiles **sever.conf** controls overall splunk server configuration and operations. Configures settings such as server name, host name and indexing settings

### Explain the Data Ingest Flow Pipeline in splunk
# Splunk Data Ingestion Pipeline 
![](how_index_flow.png)
The top section of the image represents the Typical Ingest Flow in Splunk. It shows how data is processed from ingestion to indexing. Let me break it down into its major stages:

## Input Layer (UF - Universal Forwarder)
This is where data enters the Splunk ecosystem. The Universal Forwarder collects data from various sources:
- **Network:** Data sent over TCP or UDP.
- **Tailing:** Reads logs from files (e.g., /var/log or application logs).
- **Scripted:** Data collected by running custom scripts.

#### The data passes through the **Parsing Queue (ParsingQ)** and is sent to the TcpOut component to forward it to the indexer.

### Indexer (Data Processing Pipelines)
The indexer handles the data's ingestion, processing, and storage. The pipelines shown in the image describe the sequential steps Splunk follows:

### Parsing Pipeline
- Splits the incoming raw data stream into individual events based on line breaks (linebreaker).
- Extracts metadata (e.g., host, source, sourcetype) using headers.

### Merging Pipeline
- Combines multiple small chunks of data into larger aggregated events to optimize processing (aggregator).

### Typing Pipeline
- Applies regex patterns to identify and modify data.
- Annotates events with additional information, such as timestamps, fields, and key-value pairs.

### Index Pipeline
- Finalizes the processed data and prepares it for indexing.
- Sends events to: The indexer, where data is stored.
- Outputs like tcp_out (forwarding) or syslog_out (logging).

### File System Buckets Explanation of Data Ingest Flow
This section transitions into the data storage model of Splunk on the indexer. It shows how processed data is stored in "buckets" with different life cycle stages:
- **Hot:** Actively written-to buckets for real-time data ingestion. ($SPLUNK_HOME/var/lib/splunk/defaultdb/db/*)
- **Warm:** Data moved from "hot" buckets after they are full. ($SPLUNK_HOME/var/lib/splunk/defaultdb/db/*)
- **Cold:** Older data that is no longer frequently accessed. ($SPLUNK_HOME/var/lib/splunk/defaultdb/colddb/*)
- **Frozen:** Data archived to third-party storage systems. its custom specify by the user
- **Thawed:** Archived data brought back for searching. ($SPLUNK_HOME/var/lib/splunk/defaultdb/thaweddb/*)

This process ensures that Splunk efficiently handles large-scale data ingestion while maintaining search and retrieval performance. Each stage optimizes the flow from raw data collection to searchable storage.



