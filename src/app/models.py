from datetime import datetime
from app import db


wastes_list = [
    {
        'id': '0',
        'name': 'Bois',
        'description': 'Le bois est arbre ...',
        'image': '',
        'list_recycling_possibilitites': "-Compost\n-Chipping pour mulch\n-Bois-énergie\n-Papier\n-Plastique\n-Verre\n-Métal",
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    },
    {
        'id': '1',
        'name': 'Carton',
        'description': 'Un carton est une boîte en carton ...',
        'image': '',
        'list_recycling_possibilitites': '',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    },
    {
        'id': '2',
        'name': 'Fer',
        'description': 'Une feraille est un déchet métallique ...',
        'image': '',
        'list_recycling_possibilitites': '',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    },
    {
        'id': '3',
        'name': 'Plastique',
        'description': 'Les plastiques sont faits de matériaux naturels comme la cellulose, le charbon...',
        'image': '',
        'list_recycling_possibilitites': '',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    },
    {
        'id': '4',
        'name': 'Papier',
        'description': 'Un papier blanc est un support vierge utilisé pour écrire ou dessiner ...',
        'image': '',
        'list_recycling_possibilitites': '',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    }
]


class Waste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    list_recycling_possibilitites = db.Column(db.Text, nullable=False)
    nb_views = db.Column(db.Integer, nullable=False, default=0)
    last_viewed = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f"Waste('{self.name}', '{self.description}', '{self.image}', '{self.list_recycling_possibilitites}', '{self.nb_views}', '{self.last_viewed}')"


articles_list = [
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    },
    {
        'id': 2,
        'title': "Code de l'environnement",
        'date': '2020-01-01 00:00:00',
        'image': 'https://www.legifrance.gouv.fr/contenu/logo-rf',
        'link': 'https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074220/LEGISCTA000006143752/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'Version en vigueur au 14 avril 2023'
    },
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    },
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    },
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    },
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    },
    {
        'id': 1,
        'title': 'Bien trier ses déchets',
        'date': '2020-01-01 00:00:00',
        'image': 'https://web.citeo.guidedutri.fr/assets/images/citeo_retouch.jpg',
        'link': 'http://www.siredom.com/vos-dechets-au-quotidien/bien-trier-ses-dechets/',
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
        'content': 'D’une commune à l’autre, les dispositifs et modes de collecte des déchets changent.'
    }
]


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime) #nullable=False
    image = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(300), unique=True, nullable=False)
    nb_views = db.Column(db.Integer, nullable=False, default=0)
    last_viewed = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Article('{self.title}', '{self.date}', '{self.image}', '{self.link}', '{self.nb_views}', '{self.last_viewed}', '{self.content}')"
