"""
Ce module contient les routes relatives à la gestion des déchets.

Routes :
-------
/popular :
    Page qui affiche les déchets les plus populaires.

/waste/new :
    Permet l'ajout d'un nouveau déchet dans la base de données.

/waste/<int:waste_id> :
    Page qui affiche les détails d'un déchet spécifique.

/waste/<int:waste_id>/update :
    Permet la mise à jour d'un déchet existant.

/waste/<int:waste_id>/delete :
    Page de confirmation de suppression d'un déchet.

/waste/<int:waste_id>/delete-confirmation :
    Confirme la suppression d'un déchet existant dans la base de données.

/waste/<int:waste_id>/details :
    Affiche les détails d'un déchet spécifique.
"""

from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from app.wastes.forms import WasteForm
from app.models import Waste, datetime
from app.wastes.utils import rename_waste_image, get_waste_info, os, current_app

# création du Blueprint pour les déchets
wastes_bp = Blueprint('wastes', __name__)


@wastes_bp.route('/popular')
def popular():
    """
    Cette route affiche les déchets les plus populaires.
    """
    page = request.args.get('page', 1, type=int)
    wastes = Waste.query.order_by(
        Waste.nb_views.desc()).paginate(page=page, per_page=10)
    return render_template('popular.html', wastes=wastes, title='Popular', location='popular')


@wastes_bp.route('/waste/new', methods=['GET', 'POST'])
def waste_new():
    """
    Cette route permet l'ajout d'un nouveau déchet dans la base de données.
    """
    form = WasteForm()
    if form.validate_on_submit():
        # Vérifie si le déchet existe déjà dans la base de données
        name = Waste.query.filter_by(name=form.waste_name.data.lower()).first()
        if not name:
            # Si le déchet n'existe pas, on récupère les informations et on l'ajoute à la base de données
            """flash(
                    f"Requête en cours... !", 'warning')"""
            description, list_recycling_possibilitites = get_waste_info(
                form.waste_name.data.lower())
            waste = Waste(name=form.waste_name.data.lower(), description=description,
                          list_recycling_possibilitites=list_recycling_possibilitites)
            db.session.add(waste)
            db.session.commit()
            if description == "" or list_recycling_possibilitites == "":
                flash(
                    f"Le déchet '{form.waste_name.data}' a été ajouté mais une erreur a eu lieu avec openai !", 'warning')
            else:
                flash(
                    f"Le déchet '{form.waste_name.data}' a été ajouté !", 'success')
            return redirect(url_for('wastes.waste', waste_id=waste.id))
        else:
            flash(
                f"Le déchet '{form.waste_name.data}' existe déjà !", 'danger')
            return redirect(url_for('wastes.waste_new'))
    return render_template('waste-new.html', title='Add waste', location='waste-new', form=form, legend='Ajouter')


@wastes_bp.route('/waste/<int:waste_id>')
def waste(waste_id):
    """
    Cette route affiche les détails d'un déchet spécifique.
    """
    waste = Waste.query.get_or_404(waste_id)
    waste.nb_views += 1
    waste.last_viewed = datetime.utcnow()
    db.session.commit()
    return render_template('waste.html', waste=waste, title=waste.name, location='waste')


@wastes_bp.route('/waste/<int:waste_id>/update', methods=['GET', 'POST'])
def update_waste(waste_id):
    """
    Cette route permet de modifier les informations d'un déchet.
    """
    waste = Waste.query.get_or_404(waste_id)
    form = WasteForm()
    if form.validate_on_submit():
        name = Waste.query.filter_by(name=form.waste_name.data.lower()).first()
        if not name:
            # Si le déchet n'existe pas, on modifie le nom et le fichier image correspondant
            rename_waste_image(waste.name, form.waste_name.data.lower())
            waste.name = form.waste_name.data.lower()
            db.session.commit()
            flash('Le déchet a été mis à jour !', 'success')
            return redirect(url_for('wastes.waste', waste_id=waste.id))
        else:
            flash(
                f"Le déchet '{form.waste_name.data}' existe déjà !", 'danger')
            return redirect(url_for('wastes.waste', waste_id=waste.id))
    elif request.method == 'GET':
        form.waste_name.data = waste.name
    return render_template('waste-new.html', waste=waste, title=waste.name, location='waste-update', form=form, legend='Modifier')


@wastes_bp.route('/waste/<int:waste_id>/delete', methods=['GET', 'POST'])
def delete_waste(waste_id):
    """
    Cette route permet de supprimer un déchet de la base de données.
    """
    waste = Waste.query.get_or_404(waste_id)
    return render_template('waste-delete.html', waste=waste, title=waste.name, location='waste')


@wastes_bp.route("/waste/<int:waste_id>/delete-confirmation", methods=['GET', 'POST'])
def delete_waste_confirmation(waste_id):
    """
    Cette route permet de confirmer la suppression d'un déchet de la base de données.
    """
    waste = Waste.query.get_or_404(waste_id)
    filename = waste.name.lower() + '.png'
    if os.path.exists(os.path.join(current_app.root_path,
                      'static/uploads/wastes', filename)):
        os.remove(os.path.join(current_app.root_path,
                               'static/uploads/wastes', filename))
    db.session.delete(waste)
    db.session.commit()
    flash('Le déchet a été supprimé !', 'success')
    return redirect(url_for('main.index'))


@wastes_bp.route("/waste/<int:waste_id>/details")
def waste_details(waste_id):
    """
    Cette route affiche les détails d'un déchet spécifique.
    """
    waste = Waste.query.get_or_404(waste_id)
    return render_template('waste-details.html', waste=waste, title=waste.name, location='waste')
