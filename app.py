from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route('/todos', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/todos', methods=['POST'])
def create_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/todos/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.json
    task.update(data)
    return jsonify(task)


@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
