# Use the official FastAPI image from Tiangolo
FROM tiangolo/uvicorn-gunicorn-fastapi:latest
# Update container
RUN apt-get update -y && \
    apt-get install -y cmake libzbar-dev
# Set ARGs \
ARG APP_CODE=/src
ARG APP_LOCAL_PATH=./humanes_api

# Set the working directory to /app
WORKDIR $APP_CODE

# Copy requirements.txt to the working directory
COPY $APP_LOCAL_PATH/requirements/requirements.txt $APP_CODE/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY $APP_LOCAL_PATH $APP_CODE/application

# Set PYTHONPATH
ENV PYTHONPATH $PYTHONPATH:$APP_CODE/application/:/src/:./


#
## Make port 80 available to the world outside this container
#EXPOSE 80
#
## Use tail -f /dev/null to keep the container running
#CMD ["tail", "-f", "/dev/null"]
#
### Run app.py when the container launches
##CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#
