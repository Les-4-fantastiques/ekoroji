from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev")

# Connexion à la base de données
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Page d'articles sur l'écologie
@app.route('/articles')
def articles():
    # Récupération des articles via NewsAPI
    response = requests.get("https://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey=YOUR_API_KEY")
    articles = response.json()["articles"]
    return render_template('articles.html', articles=articles)

# Page de recherche de déchets
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Récupération du déchet entré par l'utilisateur
        query = request.form.get('query').lower()
        # Recherche du déchet dans la base de données
        c.execute("SELECT * FROM wastes WHERE name=?", (query,))
        waste = c.fetchone()
        if waste:
            # Si le déchet est présent dans la base de données, on affiche les informations stockées
            name, image, description, recycling_methods, count = waste
        else:
            # Si le déchet n'est pas présent, on utilise l'API OpenAI pour récupérer les informations
            headers = {
                'Content-Type': 'application/json',
                'x-rapidapi-host': 'openai80.p.rapidapi.com',
                'x-rapidapi-key': 'YOUR_API_KEY'
            }
            data = '{"input":"' + query + '","model":"text-davinci-002","max_tokens":1024,"temperature":0.5,"top_p":1,"frequency_penalty":0,"presence_penalty":0}'
            response = requests.post('https://openai80.p.rapidapi.com/completions', headers=headers, data=data)
            result = response.json()["choices"][0]["text"]
            # Extraction des informations du résultat retourné par l'API OpenAI
            description, recycling_methods, image = result.split("\n")[0], result.split("\n")[1:-2], result.split("\n")[-2]
            recycling_methods = [method.strip("- ") for method in recycling_methods]
            count = 0
            # Ajout du nouveau déchet dans la base de données
            c.execute("INSERT INTO wastes VALUES (?, ?, ?, ?, ?)", (query, image, description, str(recycling_methods), count))
            conn.commit()
            # Récupération des informations ajoutées pour affichage
            c.execute("SELECT * FROM wastes WHERE name=?", (query,))
            waste = c.fetchone()
            name, image, description, recycling_methods, count = waste
        return render_template('result.html', name=name, image=image, description=description, recycling_methods=recycling_methods, count=count)
    return render_template('search.html')

# Page de la communauté
@app.route('/community')
def community():
    # Récupération des déchets les plus recherchés
    most_searched = Waste.query.order_by(Waste.search_count.desc()).limit(10).all()

    return render_template('community.html', title='Communauté', most_searched=most_searched)

# Page d'erreur 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run()