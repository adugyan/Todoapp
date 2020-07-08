from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:97kwadwo@127.0.0.1:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

#the route that listens to the form action /todos/create from index.html
@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    #create a todo item from the description value in index
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
     'description': todo.description
    })

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all()
    )
