from flask import Flask, request, jsonify
from add import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from divide import divide_numbers

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    a = request.json['a']
    b = request.json['b']
    result = add_numbers(a, b)
    return jsonify({'result': result})

@app.route('/subtracе', methods=['POST'])
def subtract():
    a = request.json['a']
    b = request.json['b']
    result = subtract_numbers(a, b)
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    a = request.json['a']
    b = request.json['b']
    result = multiply_numbers(a, b)
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    a = request.json['a']
    b = request.json['b']
    result = divide_numbers(a, b)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
