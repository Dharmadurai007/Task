from flask import Flask, request, jsonify
import uuid
import json
from schema_validation import CreateExpense  




app = Flask(__name__)

def create_data_check(data):
    try:
        data = CreateExpense().load(data)
        return data
    except Exception as e:
        return {"message": "Please provide correct input!", "error": str(e)}

def add_data(new_data):
    try:
        read_file = open("data.json", 'r')
        try:
            existing_data = json.load(read_file)
        except json.JSONDecodeError:
            existing_data = []  
        write_file = open("data.json", 'w')
        existing_data.append(new_data)
        json.dump(existing_data, write_file, indent=4)
        return {"message": "Successfully added!"}
    except Exception as e:
        return {"message": "Error adding data", "error": str(e)}

@app.route("/expenses", methods=['POST'])
def create_expense():
    if request.is_json:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Empty request. Please provide data!"}), 400

        validation_result = create_data_check(data)
        if "error" in validation_result:
            return jsonify(validation_result), 400

        data["id"] = str(uuid.uuid4())
        
        response = add_data(data)
        if "error" in response:
            return jsonify(response), 500

        return jsonify({"message": "Successfully created expense!"}), 201
    return jsonify({"message": "Invalid Request! Please send JSON data."}), 400

@app.route("/expenses", methods=['GET'])
def get_expense():
    read_file = open("data.json", 'r')
    try:
        existing_data = json.load(read_file)
    except json.JSONDecodeError:
        existing_data = []  
    return existing_data

if __name__ == "__main__":
    app.run(port=8006, debug=True, host="0.0.0.0")
