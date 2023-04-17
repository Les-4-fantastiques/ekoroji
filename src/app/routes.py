from flask import render_template, url_for, send_from_directory, flash, redirect
from app import app, db
from app.forms import WasteForm, ArticleForm
from app.models import Waste, Article, wastes, newspapers


@app.route('/')
def index():
    return render_template('index.html', wastes=wastes, title='Home', location='index')


@app.route('/popular')
def popular():
    return render_template('popular.html', wastes=wastes, title='Popular', location='popular')


@app.route('/news')
def news():
    return render_template('news.html', newspapers=newspapers, title='News', location='news')


@app.route('/add-waste', methods=['GET', 'POST'])
def add_waste():
    form = WasteForm()
    if form.validate_on_submit():
        flash(f"Le déchet '{form.waste_name.data}' a été ajouté !", 'success')
        return redirect(url_for('index'))
    return render_template('add-waste.html', title='Add waste', location='add-waste', form=form)


@app.route('/add-new', methods=['GET', 'POST'])
def add_new():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.article_title.data, image=form.article_image.data,
                          link=form.article_link.data, content=form.article_content.data)
        db.session.add(article)
        db.session.commit()
        flash(
            f"L'article '{form.article_title.data}' a été ajouté !", 'success')
        return redirect(url_for('index'))
    return render_template('add-new.html', title='Add news', location='add-news', form=form)


nb = 0


@app.route('/waste/' + str(nb))
def waste():
    return render_template('waste.html', waste=wastes[nb], title=wastes[nb]['name'], location='waste')
