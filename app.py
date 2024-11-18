from flask import Flask, request,jsonify

app = Flask(__name__)

todos = []
todo_id = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route ('/todos', methods=['POST'])
def create_todo():
    global todo_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    todo = {'id': todo_id, 'title': data['title'], 'completed': False}
    todos.append(todo)
    todo_id += 1
    return jsonify(todo),201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            if 'title' in data:
                todo['title'] = data['title']
            if 'completed' in data:
                todo['completed'] = data['completed']
            return jsonify(todo), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)