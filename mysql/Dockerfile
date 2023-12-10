# Use an official MySQL image as a parent image
FROM mysql/mysql-server:latest

# Copy the initialization script into the container at /docker-entrypoint-initdb.d/
COPY imageClassifier_prediction_logs.sql /docker-entrypoint-initdb.d/:ro

EXPOSE 3306





