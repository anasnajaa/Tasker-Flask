import uuid
import json
from datetime import datetime

FILE_NAME = 'data.json'

def get_tasks():
    data = None
    try:
        with open(FILE_NAME) as json_file:
            data = json.load(json_file)
    except:
        data = {}
        data['tasks'] = []
    return data


def update_tasks(data):
    with open(FILE_NAME, 'w') as outfile:  
        json.dump(data, outfile)


def add_task(id: str, content: str, date_created: str):
    db = get_tasks()

    db['tasks'].append({
        'id': id,
        'content': content,
        'date_created': date_created
    })

    update_tasks(db)


# def delete_task(id: str):
#     db = get_data()
#     for task in db[tasks]:
#         if task['id'] == id:
        


class Task:
    def __init__(self, content):
        self.id = str(uuid.uuid4())
        self.content = content
        self.date_created = datetime.now().strftime("%m/%d/%Y")

    def commit(self):
        add_task(self.id, self.content, self.date_created)
    
