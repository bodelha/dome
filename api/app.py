from flask import Flask, jsonify
from schema import HelloWorldSchema

app = Flask(__name__)



@app.route('/', methods=['GET'])
def hello_world():
    response_data = {"message": "Hello, World!"}
    
    schema = HelloWorldSchema()
    result = schema.dump(response_data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
