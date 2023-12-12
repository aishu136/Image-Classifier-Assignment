from flask import Flask, render_template, request, redirect, url_for, session
import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import mysql.connector
from datetime import datetime
from werkzeug.utils import secure_filename

# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('static', 'images')
# # Define allowed files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, template_folder='templates', static_folder='static')
# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)

db_connection = mysql.connector.connect(
    host='db',
    port="3306",
    user='root',
    password='root',
    database='imageClassifier'
)

# Load the trained model
model = load_model("mnist_model")

# Define a route for home page
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('predict'))
    return render_template('index.html')

# Define a route for authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'user1' and password == 'password1':
        # Authentication successful, set session and redirect to predict page
        session['username'] = username
        return redirect(url_for('predict'))
    else:
        # Authentication failed, redirect back to home page
        return render_template('index.html', error='Invalid username or password')

# Define a route for predicting images
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the image file from the request
            image = request.files['image']

            # Save the image temporarily
            image_filename = secure_filename(image.filename)

            # Upload file to the configured folder
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

            # Storing uploaded file path in Flask session
            session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

            # Preprocess the image for model prediction
            img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_filename)).convert('L')  # Convert to grayscale
            img = img.resize((28, 28))
            img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

            # Make a prediction using the loaded model
            prediction = model.predict(img_array)
            predicted_class = int(np.argmax(prediction))

            # Log the prediction to the MySQL database
            cursor = db_connection.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO prediction_logs (timestamp, image_input,prediction) VALUES (%s, %s, %s)"
            values = (timestamp, image_filename,str(predicted_class))
            cursor.execute(query, values)
            db_connection.commit()

            # Construct the image URL using url_for
            image_url = url_for('static', filename=f'images/{image_filename}')

            # Display the result page
            return render_template('result.html', image_url=image_url, prediction=predicted_class)

        except Exception as e:
            return render_template('result.html', prediction=f'Error: {str(e)}')

    return render_template('predict.html')
    
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session data
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

