from flask import render_template, request, Blueprint
from app.main.forms import SearchForm
from app.models import Waste

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    page = request.args.get('page', default=1, type=int)
    search_term = form.search_content.data
    query = Waste.query
    
    if search_term:
        query = query.filter((Waste.name.ilike(f'%{search_term}%')) | (Waste.description.ilike(f'%{search_term}%')))
        page = 1

    wastes = query.order_by(Waste.last_viewed.desc()).paginate(page=page, per_page=5)
        
    return render_template('index.html', wastes=wastes, title='Home', form=form, location='index')