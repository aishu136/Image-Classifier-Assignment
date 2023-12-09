# Use an official MySQL image as a parent image
FROM mysql:latest

# Copy the initialization script into the container at /docker-entrypoint-initdb.d/
COPY imageClassifier_prediction_logs.sql /docker-entrypoint-initdb.d/

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=imageClassifier
ENV MYSQL_ROOT_HOST= localhost


EXPOSE 3306
