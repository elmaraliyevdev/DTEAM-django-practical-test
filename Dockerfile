# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Expose the port Django runs on
EXPOSE 8000

# Run the Django server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]