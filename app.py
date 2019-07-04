from flask import Flask, jsonify, request, make_response, render_template, redirect
from models.task import *


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task = Task(task_content)
        task.commit()
        return redirect('/')
    else:
        data = get_tasks()
        return render_template('index.html', tasks=data['tasks'])


@app.route('/delete/<id>')
def delete(id):
    task_to_delete = get_task(id)
    if task_to_delete is not None:
        delete_task(id)
    return redirect('/')


@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        task_content = request.form['content']
        update_task(id, task_content)
        return redirect('/')
    else:
        task = get_task(id)
        return render_template('update.html', task=task)


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True) 
