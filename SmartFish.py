from flask import Flask
from flask import render_template
from flask import redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash



from DbClass import DbClass

app = Flask(__name__)



@app.route('/')
def onboarding():
    return render_template('Onboarding.html')

@app.route('/registreren', methods=['GET', 'POST'])
def registreren():

    if request.method == 'POST':
        db = DbClass()

        Voornaam= request.form['Voornaam']
        Achternaam = request.form['Achternaam']
        Email = request.form['Email']
        Wachtwoord = request.form['Wachtwoord']
        hash = generate_password_hash(Wachtwoord)
        db.registreer(Voornaam,Achternaam,Email,hash)
        print("hash: " + hash)
        return redirect(url_for('home'))
    return render_template('Registreren.html')

@app.route('/aanmelden', methods=['GET', 'POST'])
def aanmelden():
    error = None
    db = DbClass()
    db2 =DbClass()
    if 'mail' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        mail=request.form['Email']
        password=request.form['Wachtwoord']
        check = db.CheckUser(mail)
        if check[0]:
            get= db2.GetUser(mail)
            for row in get:
                if check_password_hash(row[0], password) == True:
                    session['mail'] = request.form['Email']
                    return redirect(url_for('home'))
                else:
                    error ='Verkeerde gegevens, probeer het opnieuw.'

    return render_template('Aanmelden.html', error=error)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/aquariums',methods=['GET', 'POST'])
def aquariums():
    # Verder controle want bad request (voorlopig misschien 1 aquarium aanmaken want anders problemen met ip-adres raspberry pi)
    # db=DbClass()
    # Gebruiker=session['GebruikersID']
    # aquarium = request.form['AquariumToevoegen']
    # if request.method == 'POST':
    #     if db.CheckAquarium(aquarium) ==1:
    #         print("Aquarium bestaat al")
    #     else:
    #         print("Dit is een nieuw aquarium")
    return render_template('Aquariums.html')


@app.route('/filter',methods=['GET', 'POST'])
def filter():
    db=DbClass()
    stand=db.standFilter
    Knop=request.form[1]
    print(stand)
    # werk hie met checkboxen en zet dan later om naar een knop
    if request.method == 'POST':

        if stand==1:
            db.VeranderFilter(1)
            print("Filter staat uit")
        else:
            db.VeranderFilter(0)
            print("Filter staat aan")


    return render_template('Filter.html')

@app.route('/temperatuur')
def temperatuur():
    # in plaats van grafiek heater kunnen we weergeven hoe lang de heater heeft aangelegen en we kunnen de temperatuur weergeven in een grafiek,
    # verder kan de gebruiker de gewenste temperatuur voor het aquarium instellen. en de huidige temperatuur waarnemen.
    return render_template('Temperatuur.html')

@app.route('/verlichting')
def verlichting():
    # Hier moet de gebruiker een kleur kunnen instellen en de verlichting uitschakelen (GPIO's allemaal afleggen. ofwel hexwaarde 000000 doorsturen
    return render_template('Verlichting.html')

@app.route('/Vissen')
def vissen():
    # We geven een lijst terug met alle vissen geordend volgens soort (zoek op hoe we gegevens in een lijst kunnen zetten
    return render_template('Vissen.html')

@app.route('/instellingen')
def instellingen():
    #Hier kijken we voor de instellingen te kunnen aanpassen van de gebruiker, men kan namelijk bepalen of een gebruiker alle rechten heeft of niet,
    # Pas wel op enkel de eerste gebruiker kan deze instellingen raadplegen ! Voor de gebruikers met beperkte toelating zal men
    # moeten kijken voor het verbergen van zelf in te vullen gegevens (knoppen, formulieren,... )
    # (maak mss apparte klasse aan zodat je alles drect kan verbergen van dezelfde klasse.
    return render_template('Gebruiker.html')


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')

