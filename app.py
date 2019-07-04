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


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True) 
