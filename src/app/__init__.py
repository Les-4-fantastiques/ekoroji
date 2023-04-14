from flask import Flask, render_template, url_for

app = Flask(__name__)

wastes = [
    {
        'id': 1,
        'name': 'Plastic',
        'description': 'Plastic is a material consisting of any of a wide range of synthetic or semi-synthetic organic compounds that are malleable and so can be molded into solid objects. Plasticity is the general property of all materials which can deform irreversibly without breaking but, in the class of moldable polymers, this occurs to such a degree that their actual name derives from this specific ability. Plastics are typically organic polymers of high molecular mass, but they often contain other substances. They are usually synthetic, most commonly derived from petrochemicals, but many are partially natural. Depending on their chemical structure, plastics can be either amorphous or semi-crystalline and may be amorphous or crystalline. Plastics are usually organic polymers of high molecular mass, but they often contain other substances. They are usually synthetic, most commonly derived from petrochemicals, but many are partially natural. Depending on their chemical structure, plastics can be either amorphous or semi-crystalline and may be amorphous or crystalline.',
        'image': '',
        'list_recycling_possibilitites': [

        ],
        'nb_views': 0,
        'last_viewed': '2020-01-01 00:00:00',
    },
    {
        'id': 2,
        'name': 'Glass',
        'description': 'Glass is a non-crystalline amorphous solid that is often transparent and has widespread practical, technological, and decorative use in, for example, window panes, tableware, and optoelectronics. The most familiar, and historically the oldest, types of manufactured glass are "silicate glasses" based on the chemical compound silica (silicon dioxide, or quartz), the primary constituent of sand. The term glass, in popular usage, is often used to refer only to this type of material. However, glass can refer to other non-crystalline amorphous solids, such as sheet glass, which is made of a variety of non-silicate materials. The term glass, in popular usage, is often used to refer only to this type of material. However, glass can refer to other non-crystalline amorphous solids, such as sheet glass, which is made of a variety of non-silicate materials.',
        'image': '',
        'list_recycling_possibilitites': [

        ],
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
    return render_template('index.html', title='Home')


@app.route('/popular')
def popular():
    return render_template('popular.html', wastes=wastes, title='Popular')


@app.route('/news')
def news():
    return render_template('news.html', newspapers=newspapers, title='News')
