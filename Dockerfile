#Download Python from DockerHub and use it
#FROM python:3.9.2 as build
FROM python:3.9.2-alpine

#Set the working directory in the Docker container
WORKDIR /code

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

# seond stage
#FROM python:3.9.2-alpine

# copy the required artifacts to from the first build stage
#COPY --from=build /code /

#Run the container
CMD [ "python", "./app.py" ]