# Getting the base image
FROM apache/airflow:2.7.1

# Copying the requirements
COPY requirements.txt /opt/requirements.txt

# Upgrade the latest pip
RUN pip install --no-cache-dir --upgrade pip

# Install the latest dependencies
RUN pip install --no-cache-dir -r /opt/requirements.txt