
# Image-Classifier-Assignment

This provides instructions on setting up and running the AI model, the Flask web service, and the Kubernetes deployment for the application.

## 1. Set Up the AI Model

### Train the Model
1. Run the following command to train the model and save it:
   ```bash
   python model.py
   ```
2. The trained model will be saved in the directory.

## 2. Set Up the Flask Web Service

### Install Dependencies
1. Ensure you have Python and pip installed.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Flask App Locally
1. Run the following command to start the Flask app locally:
   ```bash
   python app.py
   ```
2. The web service will be accessible at `http://localhost:5000`.

## 3. Set Up Kubernetes Deployment

### Prerequisites
1. Ensure you have `kubectl` configured to connect to your Kubernetes cluster.
2. Have a Docker image of your application pushed to a container registry.

### Deploy to Kubernetes
1. Open the `app-deployment.yaml` file.
2. Apply the Kubernetes configuration:
   ```bash
   kubectl apply -f app-deployment.yaml
   ```

### Access the Service
1. Once deployed, get the external IP of the service:
   ```bash
   kubectl get service your-app-service
   ```
2. Access the web service at the provided external IP.

## Additional Notes
- You can scale the deployment using:
   ```bash
   kubectl scale deployment your-app-deployment --replicas=<desired_replica_count>
   ```



