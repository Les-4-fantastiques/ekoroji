from flask import render_template, request, Blueprint
from app.main.forms import SearchForm
from app.models import Waste

# création du Blueprint pour les pages principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Cette fonction est la vue pour la page d'accueil du site web.

    Elle gère une requête GET et POST pour la page d'accueil. Si une requête POST est effectuée, la fonction récupère le
    terme de recherche entré par l'utilisateur et utilise ce terme pour filtrer les déchets dans la base de données.
    La fonction retourne la page d'accueil avec les déchets correspondants au terme de recherche, ou les déchets les plus
    récemment consultés si aucune recherche n'est effectuée.

    :return: la page d'accueil avec les déchets correspondants au terme de recherche, ou les déchets les plus récemment
    consultés si aucune recherche n'est effectuée
    :rtype: str
    """
    
    # Création d'un objet formulaire pour la recherche
    form = SearchForm()
    
    # Récupération du numéro de page et du terme de recherche de la requête GET
    page = request.args.get('page', default=1, type=int)
    search_term = form.search_content.data
    
    # Création de la requête de base pour récupérer tous les déchets de la base de données
    query = Waste.query
    
    # Filtrage des déchets si un terme de recherche est entré
    if search_term:
        query = query.filter((Waste.name.ilike(f'%{search_term}%')) | (Waste.description.ilike(f'%{search_term}%')))
        page = 1

    # Récupération des déchets triés par date de dernière consultation et pagination
    wastes = query.order_by(Waste.last_viewed.desc()).paginate(page=page, per_page=5)
        
    # Renvoi de la page d'accueil avec les déchets correspondants au terme de recherche ou les déchets les plus récemment
    # consultés si aucune recherche n'est effectuée
    return render_template('index.html', wastes=wastes, title='Home', form=form, location='index')