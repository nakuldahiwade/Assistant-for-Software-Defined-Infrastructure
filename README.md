# Chat Assistant for Software Defined Infrastructure
This chatbot currently supporting **OpenStack**, can be used in software defined infrastructure such as an OpenStack cloud, Kubernetes to create, delete, list cloud resources by typing commands in plain English as a chat messages to the chat bot. It understands the English and converts into respective OpenStack client commands. 

## What does this Bot solve?
The main idea here to reduce the complexity in using an OpenStack cloud for novices and experts alike. No need to remember all those pesky command line words and the confusing Horizon dashboard. Just chat away your cloud needs to this bot. It will do it for you.

## Installation:

1. Clone repo.	
   ```https://github.com/shank7485/OpenStack-Hackathon-OSIC.git```
2. Edit `endpoint.conf` to add OpenStack Keystone endpoint IP.
3. Create Virtual Environment.	
	```virtualenv venv```
4. Source it.	
	```source venv/bin/activate/```
5. Install requirements.txt.	
	```cd OpenStack-Hackathon-OSIC; pip install -r requirements.txt```
6. For deployment, add private key with name `deploy_key.pem` in `/home/ubuntu/` to deploy another OpenStack cloud on another server. The other server should be SSH'able using the `deploy_key.pem`.
7. Run the API server.	
	```python api.py```
8. Open the API IP/URL in web brower by going to `http://<IP>:8081` to see a login page. Login with OpenStack credentials.
9. Now you have an assistant waiting to recieve your commands. Just chat with it and it will reply back.

## System Diagram
![Diagram](https://raw.githubusercontent.com/shank7485/OpenStack-Hackathon-OSIC/master/docs/Diagram.png)
