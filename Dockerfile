FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including my_project, telegram_messages, dbt)
COPY . /app

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start FastAPI app (main.py is assumed to have the FastAPI app)
CMD ["uvicorn", "my_project.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including my_project, telegram_messages, dbt)
COPY . /app

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start FastAPI app (main.py is assumed to have the FastAPI app)
CMD ["uvicorn", "my_project.main:app", "--host", "0.0.0.0", "--port", "8000"]
