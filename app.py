from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def charger_page(nom_page):
    """Charge le contenu d'une page depuis son fichier JSON"""
    try:
        with open(f'data/{nom_page}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"titre": "Page non trouvée", "contenu": ""}

@app.route('/')
def accueil():
    page_data = charger_page('accueil')
    return render_template('page.html', **page_data)

@app.route('/types-pollution')
def types_pollution():
    page_data = charger_page('types_pollution')
    return render_template('page.html', **page_data)

@app.route('/chiffres')
def chiffres():
    page_data = charger_page('chiffres')
    return render_template('chiffres.html', **page_data)

@app.route('/ia-pollution')
def ia_pollution():
    page_data = charger_page('ia_pollution')
    return render_template('ia_pollution.html', **page_data)

@app.route('/gestes')
def gestes():
    page_data = charger_page('gestes')
    return render_template('gestes.html', **page_data)

@app.route('/gafam')
def gafam():
    page_data = charger_page('gafam')
    return render_template('gafam.html', **page_data)

if __name__ == '__main__':
    app.run(debug=True)