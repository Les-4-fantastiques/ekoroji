from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

wastes = [
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

newspapers = [
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


@app.route('/')
def index():
    return render_template('index.html', wastes=wastes, title='Home', location='index')


@app.route('/popular')
def popular():
    return render_template('popular.html', wastes=wastes, title='Popular', location='popular')


@app.route('/news')
def news():
    return render_template('news.html', newspapers=newspapers, title='News', location='news')

nb = 0
@app.route('/waste/' + str(nb))
def waste():
    return render_template('waste.html', waste=wastes[nb], title=wastes[nb]['name'], location='waste')