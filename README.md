# Ers-perfdata-parser
This is a Flask based web-application built with a purpose to analyze db_perf_dataitems and servicecall_perf_dataitems JSON objects, received directly from the Kibana logs.

Application hosted on: https://ers-perfdata-parser-qa.us-west-2.nonprod.cnqr.delivery (Kubernetes deployment)

Maintainer: aniruddh.nathani@sap.com



## Functionalities:
1. The application parses appropriate JSON objects and populates details in a tabular form which can then be sorted in an ascending or a descending order with respect to its columns/attributes.
2. The application will also allow users to display the total duration of every unique db call as well as help us analyze the count of each db call.

## Run the application on docker (localhost):

### Application Requirements:

<a> Command line/Terminal</a>

<a href="https://docs.docker.com/get-docker/">Docker</a> installed on the system

### Steps to follow:
1. Clone the repository: 

```
git clone https://github.concur.com/inception/ers-perfdata-parser.git
cd ers-perfdata-parser
```

2. Run the following docker commands:

	a. Inside the cloned folder:
	```
	docker build -t [image_name] .
	```
		
	This will create an image of the application on docker.

	b. Checking the docker image just created:

	```
	docker image ls
	```

	c. Running the docker image on the local host:

	```
	docker run -p 5000:80 --volume=/ers-perfdata-parser [image_name]
	```
	
	d. Surf the application running on your local host (using port 5000):
	
		https://0.0.0.0:5000
		
## Run the application on PyCharm (virtual environment):

### Application Requirements:

Python Version 2/3

Install <a href="https://flask.palletsprojects.com/en/0.12.x/installation/">Flask</a>
```
pip install Flask
```
or 
```
python2/3 -m pip install flask (based on the python version)

```
### Steps to follow:
1. Clone the repository: 
```
git clone https://github.concur.com/inception/ers-perfdata-parser.git
```
2. Open the folder in PyCharm:
	Make sure you are inside the project directory. On the PyCharm terminal:
	
	a. Set up the Flask application:

	```
	export FLASK_APP=jsonHandler.py
	```

	b. Set up the Flask environment to development:

	```
	export FLASK_ENV=development
	```
	c. Run the flask application on your local host:
	
	```
	flask run
	```
	d. Surf the application running on your local host (using port 5000):
	
		http://127.0.0.1:5000/ 


## Relevant Links:
1. Understanding the application Build-hub process flow:https://wiki.concur.com/confluence/pages/viewpage.action?pageId=144527414

2. Docker image on quay: https://quay.cnqr.delivery/repository/inception/ers-perfdata-parser. To pull docker image from quay:
	```
	docker pull quay.cnqr.delivery/inception/ers-perfdata-parser
	```
	
3. Buildhub Jenkins (for debugging purpose) : https://buildhub.cnqr.delivery/job/inception/job/ers-perfdata-parser/job/ers-perfdata-parser/job/develop/

#### Thanks. Hope this helps!
