FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

# ===================== INFORMATION ==================================

#FROM python:3.9-slim-buster
#Base Image: Uses the official Python 3.9 image, specifically the "slim-buster" variant, which is a smaller Debian-based image. It’s optimized for size but includes enough tools to run Python applications.

#RUN apt update -y && apt install awscli -y
#Update and Install AWS CLI:

#apt update -y: Updates the package list.
#apt install awscli -y: Installs the AWS CLI tool, which allows the app to interact with AWS services (e.g., S3, EC2, etc.).

#WORKDIR /app
#Working Directory: Sets the working directory to /app inside the container. All subsequent commands (like COPY, RUN, etc.) will be executed relative to this directory.

#COPY . /app
#Copy Files: Copies everything from your local directory (where the Dockerfile is) into the container’s /app directory.

#RUN pip install -r requirements.txt
#Install Dependencies: Installs all Python packages listed in requirements.txt using pip.

#CMD ["python3", "app.py"]
#Startup Command:
#This line is intended to run the application using Python.

