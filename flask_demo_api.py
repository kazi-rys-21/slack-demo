#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/io', methods=['GET'])
def get_tasks():

    if 1 == 1:
        print('Yes')
    else:
        print('no')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')
        print('Yes')

    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)