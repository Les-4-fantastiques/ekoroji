from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import TaskForm
from app.models import Task


@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        tasks = Task.query.filter(Task.name.like(f'%{search}%')).all()
    else:
        tasks = Task.query.order_by(Task.created_at.asc()).all()
    return render_template('index.html', tasks=tasks)


@app.route('/popular')
def popular():
    tasks = Task.query.order_by(Task.views.desc()).all()
    return render_template('popular.html', tasks=tasks)


@app.route('/task/<int:id>')
def task(id):
    task = Task.query.get_or_404(id)
    task.views += 1
    task.last_viewed = datetime.utcnow()
    db.session.commit()
    return render_template('task.html', task=task)


@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            name=form.name.data,
            description=form.description.data,
            image=form.image.data,
            is_done=form.is_done.data
        )
        db.session.add(task)
        db.session.commit()
        flash('La tâche a été créée avec succès !', 'success')
        return redirect(url_for('index'))
    return render_template('edit_task.html', form=form, title='Nouvelle tâche')


@app.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    form = TaskForm()
    if form.validate_on_submit():
        task.name = form.name.data
        task.description = form.description.data
        task.image = form.image.data
        task.is_done = form.is_done.data
        db.session.commit()
        flash('La tâche a été mise à jour avec succès !', 'success')
        return redirect(url_for('task', id=task.id))
    elif request.method == 'GET':
        form.name.data = task.name
        form.description.data = task.description
        form.image.data = task.image
        form.is_done.data = task.is_done
    return render_template('edit_task.html', form=form, title='Modifier la tâche')


