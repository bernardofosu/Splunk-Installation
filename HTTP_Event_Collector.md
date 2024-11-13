# HTTP EVENT COLLECTOR (HEC)

- The HTTP Event Collector (HEC) lets you send data and application events to a Splunk deployment over the HTTP and Secure HTTP (HTTPS) protocols.

- HEC uses a token-based authentication model.

- HEC eliminates the need for a Splunk forwarder when you send application events.

[Read More on HEC](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector)

# Demo Time – Ingesting Data Via HEC
[How to Create HEC Token](https://docs.splunk.com/Documentation/Splunk/9.3.1/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Enterprise)

```bash
NOTE: Open port 8088 in your AWS Security Group
```
# Use CURL command to send data to your Splunk 
curl = client url

[Read More on CURL Command](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#Send_data_to_HTTP_Event_Collector)

```bash
curl –k https://publicIP:8088/services/collector/event -H "Authorization: Splunk TokenHere" -d '{"event": "hello world"}’
```
NB: You will run this command in a terminal from your local computer or another serevr


