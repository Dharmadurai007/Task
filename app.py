from flask import Flask, request
import uuid
import json

from schema_validation import CreateExpense

# data file
file = open('/mnt/c/Users/user/Pictures/Task/data.json', 'w+')

def create_data_check(data):
    try:
        data = CreateExpense(data)
        return data
    except:
        return {"message":"please provide correct input!"}

def add_data(data):
    # print("*********file", data)
    # existing_data = json.load(open('data.json', 'r'))
    # print(existing_data, "*****************")
    # if existing_data:
    #     print("***************write")
    #     data = existing_data.append(data)
    #     json.dump(data, file, indent=4)
    # print("***************write*")
    print(data)
    json.dump([data], file, indent=4)
    return {"message":"Successfully added!"}

app = Flask(__name__)



@app.route("/expenses", methods=['POST'])

def create_expense():
    if request.is_json:
        data = request.get_json()
        print("**********start", data)
        if not data:
            return {"message":"Empty request pls give data!"}
        #data = create_data_check(data)
        id = uuid.uuid4()
        data.update({"id":str(id)})
        print("****************data", data)
        add_data(data)
        return {"message":"Successfully created expense!"}
    return {"message":"Invalid Request!"}

if __name__ == "__main__":
    app.run(port=8006, debug= True, host= "0.0.0.0")