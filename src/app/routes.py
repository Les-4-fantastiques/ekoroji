from flask import render_template, url_for, send_from_directory, flash, redirect, request
from app import app, db
from app.forms import WasteForm, ArticleForm
from app.models import Waste, Article


@app.route('/')
def index():
    wastes = Waste.query.all()
    return render_template('index.html', wastes=wastes, title='Home', location='index')


@app.route('/popular')
def popular():
    wastes = Waste.query.all()
    return render_template('popular.html', wastes=wastes, title='Popular', location='popular')


@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles, title='Articles', location='articles')


@app.route('/waste/new', methods=['GET', 'POST'])
def waste_new():
    form = WasteForm()
    if form.validate_on_submit():
        name = Waste.query.filter_by(name=form.waste_name.data).first()
        if not name:
            waste = Waste(name=form.waste_name.data, description='Description du déchet',
                          list_recycling_possibilitites='le jeter, le trier')
            db.session.add(waste)
            db.session.commit()
            flash(
                f"Le déchet '{form.waste_name.data}' a été ajouté !", 'success')
            return redirect(url_for('index'))
        else:
            flash(
                f"Le déchet '{form.waste_name.data}' existe déjà !", 'danger')
            return redirect(url_for('waste_new'))
    return render_template('waste-new.html', title='Add waste', location='waste-new', form=form, legend='Ajouter')


@app.route('/article/new', methods=['GET', 'POST'])
def article_new():
    form = ArticleForm()
    if form.validate_on_submit():
        link = Article.query.filter_by(link=form.article_link.data).first()
        if not link:
            article = Article(title=form.article_title.data, image=form.article_image.data,
                              link=form.article_link.data, content=form.article_content.data)
            db.session.add(article)
            db.session.commit()
            flash(
                f"L'article '{form.article_title.data}' a été ajouté !", 'success')
            return redirect(url_for('articles'))
        else:
            flash(
                f"L'article '{form.article_title.data}' existe déjà !", 'danger')
            return redirect(url_for('article-new'))
    return render_template('article-new.html', title='Add article', location='article-new', form=form)


@app.route('/waste/<int:waste_id>')
def waste(waste_id):
    waste = Waste.query.get_or_404(waste_id)
    return render_template('waste.html', waste=waste, title=waste.name, location='waste')


@app.route('/waste/<int:waste_id>/update', methods=['GET', 'POST'])
def update_waste(waste_id):
    waste = Waste.query.get_or_404(waste_id)
    form = WasteForm()
    if form.validate_on_submit():
        name = Waste.query.filter_by(name=form.waste_name.data).first()
        if not name:
            waste.name = form.waste_name.data
            db.session.commit()
            flash('Le déchet a été mis à jour !', 'success')
            return redirect(url_for('waste', waste_id=waste.id))
        else:
            flash(
                f"Le déchet '{form.waste_name.data}' existe déjà !", 'danger')
            return redirect(url_for('waste', waste_id=waste.id))
    elif request.method == 'GET':
        form.waste_name.data = waste.name
    return render_template('waste-new.html', waste=waste, title=waste.name, location='waste-update', form=form, legend='Modifier')


@app.route('/waste/<int:waste_id>/delete', methods=['GET', 'POST'])
def delete_waste(waste_id):
    waste = Waste.query.get_or_404(waste_id)
    return render_template('waste-delete.html', waste=waste, title=waste.name, location='waste')

@app.route("/waste/<int:waste_id>/delete-confirmation", methods=['GET', 'POST'])
def delete_waste_confirmation(waste_id):
    waste = Waste.query.get_or_404(waste_id)
    db.session.delete(waste)
    db.session.commit()
    flash('Le déchet a été supprimé !', 'success')
    return redirect(url_for('index'))