# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /flaskdocker
WORKDIR /flaskdocker

# add the current directory to the container as /flaskdocker
ADD . /flaskdocker

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "jsonHandler.py"]


