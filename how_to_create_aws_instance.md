
# How to Create AWS Account

# Features
- [How to Create AWS Account](#how-to-create-aws-account)
- [Features](#features)
	- [Add this Ports to your inbound rules](#add-this-ports-to-your-inbound-rules)
	- [I have to spin more servers, and each time I have to go and configure it, which takes a bit of time for about 7 servers. But on your EC2 dashboard, you can go to;](#i-have-to-spin-more-servers-and-each-time-i-have-to-go-and-configure-it-which-takes-a-bit-of-time-for-about-7-servers-but-on-your-ec2-dashboard-you-can-go-to)

Click on the on the link ([Click to Sign Up](https://signin.aws.amazon.com/signup?request_type=register)) to send you to the AWS website to register if this is your first time or click on the link ([Click to Sign In](https://signin.aws.amazon.com/signin?client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_eu-north-1_810bda85b4093773&page=resolve&code_challenge=_yYnfroR3C6JGf70PMpBTJijEzmJDpDE4cfM8Vo-7V4&code_challenge_method=SHA-256)) if you already have an account

## Add this Ports to your inbound rules
```python
    Security Group/Firewall 
	a. Splunk Web Port - 8000
	b. Splunk Management Port (Splunkd) - 8089
	c. kvstore Port - 8191
	d. Secure Shell (SSH) - 22
	e. Splunk Receiving Port - 9997
```
## I have to spin more servers, and each time I have to go and configure it, which takes a bit of time for about 7 servers. But on your EC2 dashboard, you can go to;
1. Network and Security and click on Security Groups.
2. Click on Create Security Group. 
3. Do your configuration, give it a name, and save. 

Whenever creating a new EC2 instance, the security group section, you can select the existing one and select the new one you created, or you can even select the previous ones you have created.
You can spin them in bulk by increasing the number of instances and change the names after that. Maybe it'll save some time. 