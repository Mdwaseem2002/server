from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Route for the root URL
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello World!'})

# Route to handle form submissions
@app.route('/save', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        password = data['password']

        # Create a dictionary with the form data
        form_data = {'name': name, 'email': email, 'password': password}

        # Load existing data from JSON file
        existing_data = []
        if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
            with open('data.json', 'r') as file:
                existing_data = json.load(file)

        # Append new form data to existing data
        existing_data.append(form_data)

        # Save the updated data back to the JSON file
        with open('data.json', 'w') as file:
            json.dump(existing_data, file, indent=2)

        return jsonify({'message': 'Data received successfully!'}), 200

    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to process the request.'}), 500

# Route to retrieve data
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Load existing data from JSON file
        existing_data = []
        if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
            with open('data.json', 'r') as file:
                existing_data = json.load(file)

        return jsonify(existing_data), 200

    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to retrieve data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
