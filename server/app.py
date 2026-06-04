#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print route (also prints to console)
@app.route('/print/<parameter>')
def print_param(parameter):
    print(parameter)
    return parameter

# 3. Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    return ''.join(f"{i}\n" for i in range(parameter))

# 4. Math route
@app.route('/math/<int:a>/<op>/<int:b>')
def math(a, op, b):
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == '*':
        return str(a * b)
    elif op == 'div':
        return str(a / b)
    elif op == '%':
        return str(a % b)
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(port=5555, debug=True)