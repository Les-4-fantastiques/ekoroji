from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
moment = Moment(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now())
    completed_date = db.Column(db.DateTime)
    views = db.Column(db.Integer, default=0)
    last_viewed_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task %r>' % self.name


@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_date).all()
    return render_template('index.html', tasks=tasks)


@app.route('/popular')
def popular():
    tasks = Task.query.order_by(Task.views.desc()).all()
    return render_template('popular.html', tasks=tasks)


@app.route('/search')
def search():
    query = request.args.get('q')
    results = []
    if query:
        results = Task.query.filter(Task.name.contains(query)).all()
    return render_template('search.html', results=results)


@app.route('/task/<int:task_id>')
def view_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.views += 1
    task.last_viewed_date = datetime.datetime.now()
    db.session.commit()
    return render_template('task.html', task=task)


@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.form['image']
        task = Task(name=name, description=description, image=image)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_task.html')


@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.name = request.form['name']
        task.description = request.form['description']
        task.image = request.form['image']
        task.completed = 'completed' in request.form
        if task.completed:
            task.completed_date = datetime.datetime.now()
        else:
            task.completed_date = None
        db.session.commit()
        return redirect(url_for('view_task', task_id=task.id))
    return render_template('edit_task.html', task=task)


@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
