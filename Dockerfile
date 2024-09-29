# Use the official Python image as a parent image
FROM python:3.10

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /frontend

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv

# Copy the current directory contents into the container at /frontend
COPY . /frontend

# Copy the .env file
# COPY .env /frontend/.env


# Run Django migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Expose the port that the Django app runs on
EXPOSE 8000

# Run the Django development server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
