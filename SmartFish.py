from flask import Flask
from flask import render_template

from DbClass import DbClass

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def onboarding():
    return render_template('Onboarding.html')

@app.route('/registreren')
def registreren():
    return render_template('Registreren.html')

@app.route('/aanmelden')
def aanmelden():
    return render_template('Aanmelden.html')

@app.route('/aquariums')
def aquariums():
    return render_template('Aquariums.html')

@app.route('/filter')
def filter():
    return render_template('Filter.html')

@app.route('/temperatuur')
def temperatuur():
    return render_template('Temperatuur.html')

@app.route('/verlichting')
def verlichting():
    return render_template('Verlichting.html')

@app.route('/vissen')
def vissen():
    return render_template('Vissen.html')

if __name__ == '__main__':
    app.run()

