from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from app.articles.forms import ArticleForm
from app.models import Article, datetime

articles_bp = Blueprint('articles', __name__)


@articles_bp.route('/articles')
def articles():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.order_by(
        Article.nb_views.desc()).paginate(page=page, per_page=5)
    return render_template('articles.html', articles=articles, title='Articles', location='articles')


@articles_bp.route('/article/new', methods=['GET', 'POST'])
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
            return redirect(url_for('articles.articles'))
        else:
            flash(
                f"L'article '{form.article_title.data}' existe déjà !", 'danger')
            return redirect(url_for('articles.article-new'))
    return render_template('article-new.html', title='Add article', location='article-new', form=form, legend='Ajouter')


@articles_bp.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    article.nb_views += 1
    article.last_viewed = datetime.utcnow()
    db.session.commit()
    return render_template('article.html', article=article, title=article.title, location='article')


@articles_bp.route('/article/<int:article_id>/update', methods=['GET', 'POST'])
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    form = ArticleForm()
    if form.validate_on_submit():
        link = Article.query.filter_by(link=form.article_link.data).first()
        if not link or link.id == article_id:
            article.title = form.article_title.data
            article.image = form.article_image.data
            article.link = form.article_link.data
            article.content = form.article_content.data
            db.session.commit()
            flash(
                f"L'article '{form.article_title.data}' a été ajouté !", 'success')
            return redirect(url_for('articles.article', article_id=article.id))
        else:
            flash(
                f"Le lien de l'article '{form.article_title.data}' existe déjà !", 'danger')
            return redirect(url_for('articles.article', article_id=article.id)) 
    elif request.method == 'GET':
        form.article_title.data = article.title
        form.article_content.data = article.content
        form.article_image.data = article.image
        form.article_link.data = article.link
    return render_template('article-new.html', article=article, title=article.title, location='article-update', form=form, legend='Modifier')


@articles_bp.route('/article/<int:article_id>/delete', methods=['GET', 'POST'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article-delete.html', article=article, title=article.title, location='article')


@articles_bp.route("/article/<int:article_id>/delete-confirmation", methods=['GET', 'POST'])
def delete_article_confirmation(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Le déchet a été supprimé !', 'success')
    return redirect(url_for('articles.articles'))
