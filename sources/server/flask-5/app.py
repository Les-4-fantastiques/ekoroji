from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from datetime import datetime
from sqlalchemy import or_
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'secret_key'  # clé secrète pour les messages flash
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'sources/server/flask-5/static/images/tasks'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    views = db.Column(db.Integer, default=0)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    due_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Task {self.id}>'


class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Submit')


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    q = request.args.get('q', '')  # récupère le paramètre de recherche
    sort_by = request.args.get('sort_by', 'due_date')
    if sort_by not in ['title', 'due_date', 'views']:
        sort_by = 'due_date'
    if q:
        tasks = Task.query.filter(Task.title.like(f'%{q}%')).order_by(sort_by)
    else:
        tasks = Task.query.order_by(sort_by)
    # ajout de la variable flash_messages
    return render_template('index.html', tasks=tasks, search_term=q, sort_by=sort_by, flash_messages=get_flashed_messages())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime(
            request.form['due_date'], '%Y-%m-%dT%H:%M')

        new_task = Task(title=title, description=description,
                        due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        # Récupération des 3 dernières tâches ajoutées
        new_tasks = Task.query.order_by(Task.id.desc()).limit(3).all()
        return render_template('index.html', new_tasks=new_tasks)
    return render_template('add.html', title='Ajouter une tâche')


@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = True
    db.session.commit()
    flash('Task completed successfully!', 'success')
    return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.complete = 'complete' in request.form

        # Vérifie si un fichier est envoyé avec la demande
        if 'file' in request.files:
            file = request.files['file']
            # Vérifie si le fichier est un fichier image autorisé
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                task.image_file = filename

        db.session.commit()
        return redirect(url_for('view', task_id=task.id))

    return render_template('edit.html', task=task)


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/task/<int:task_id>')
def view(task_id):
    task = Task.query.get(task_id)
    task.views += 1  # ajoute une vue à la tâche
    db.session.commit()
    return render_template('view.html', task=task)


@app.route('/search', methods=['GET', 'POST'])
def search_filter(value, search_str):
    if not search_str:
        return True
    pattern = re.compile('.*{}.*'.format(search_str), re.IGNORECASE)
    return pattern.search(value) is not None


app.jinja_env.filters['search'] = search_filter


@app.route('/sort-by-views')
def sort_by_views():
    # Trie les tâches en fonction du nombre de vues
    tasks = Task.query.order_by(Task.views.desc()).all()
    return render_template('index.html', tasks=tasks)


@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400


if __name__ == '__main__':
    app.run()
