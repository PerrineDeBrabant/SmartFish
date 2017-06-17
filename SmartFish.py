

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
        return redirect(url_for('aquariums'))
    return render_template('Registreren.html')

@app.route('/aanmelden', methods=['GET', 'POST'])
def aanmelden():
    error = None
    db = DbClass()
    db2 =DbClass()
    if 'mail' in session:
        return redirect(url_for('aquariums'))
    if request.method == 'POST':
        mail=request.form['Email']
        password=request.form['Wachtwoord']
        check = db.CheckUser(mail)
        if check[0]:
            get= db2.GetUser(mail)
            for row in get:
                if check_password_hash(row[0], password) == True:
                    session['mail'] = request.form['Email']
                    return redirect(url_for('aquariums'))
                else:
                    error ='Verkeerde gegevens, probeer het opnieuw.'

    return render_template('Aanmelden.html', error=error)


@app.route('/home')
def home():
    if 'mail' in session:
        db=DbClass()
        huidig=db.HuidigeTemperatuur(aqua)
        huidig=str(huidig)
        huidig=huidig.replace("(","").replace(")","").replace(",","").replace("[","").replace("]","")
        print(huidig)
        db2 = DbClass()
        stand = db2.standVerlichting(aqua)
        db3 = DbClass()
        stand2 = db3.standFilter(aqua)
        db4=DbClass()
        kleur=db4.HuidigeKleur(aqua)
        kleur=str(kleur)
        kleur = kleur.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
        print(kleur)

        return render_template('index.html',huidig=huidig,stand=stand,stand2=stand2,kleur=kleur)

@app.route('/aquariums',methods=['GET', 'POST'])
def aquariums():
    # Verder controle want bad request (voorlopig misschien 1 aquarium aanmaken want anders problemen met ip-adres raspberry pi)
    # global variabele aquarium

    # db=DbClass()
    # Gebruiker=session['GebruikersID']
    # aquarium = request.form['AquariumToevoegen']
    # if request.method == 'POST':
    #     if db.CheckAquarium(aquarium) ==1:
    #         print("Aquarium bestaat al")
    #     else:
    #         print("Dit is een nieuw aquarium")
    if 'mail' in session:
        db = DbClass()
        aquaria = db.Aquariums()
        if request.method == 'POST':
            global aqua
            aqua = request.form['aquarium']
            print(aqua)
            db2=DbClass()
            global aqua2
            aqua2=db2.AquariumID(aqua)
            aqua2=str(aqua2)
            aqua2=aqua2.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
            print(aqua2)

            return redirect(url_for('home'))
        return render_template('Aquariums.html',aquaria=aquaria)


@app.route('/filter',methods=['GET', 'POST'])
def filter():
    if 'mail' in session:

        if request.method == 'POST':
            db=DbClass()

            Knop = request.form['1']
            print(Knop)
            db.VeranderFilter(Knop,aqua)
        db2 = DbClass()
        stand = db2.standFilter(aqua)
        print(stand)

        return render_template('Filter.html', stand=stand)


    # werk hie met checkboxen en zet dan later om naar een knop

@app.route('/temperatuur')
def temperatuur():
    # in plaats van grafiek heater kunnen we weergeven hoe lang de heater heeft aangelegen en we kunnen de temperatuur weergeven in een grafiek,
    # verder kan de gebruiker de gewenste temperatuur voor het aquarium instellen. en de huidige temperatuur waarnemen.
    return render_template('Temperatuur.html')

@app.route('/verlichting',methods=['GET', 'POST'])
def verlichting():
    # Hier moet de gebruiker een kleur kunnen instellen en de verlichting uitschakelen (GPIO's allemaal afleggen. ofwel hexwaarde 000000 doorsturen

        # if request.method =='POST':
        #     db=DbClass()
        #     Kleur=request.form['kleur']
        #     print(Kleur)
        #     Knop = request.form['1']
        #     print(Knop)
        #     db.VeranderVerlichting(Knop,Kleur)
        # db3 = DbClass()
        # stand2 = db3.standFilter()
        # print(stand2)
        return render_template('Verlichting.html')

@app.route('/verlichting/kleur',methods=['GET', 'POST'])
def Kleur():
    if 'mail' in session:
        db2 = DbClass()
        kleur = db2.HuidigeKleur(aqua)
        kleur = str(kleur)
        kleur = kleur.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
        print(kleur)
        if request.method == 'POST':
            db = DbClass()
            Kleur = request.form['kleur']
            print(Kleur)
            db.VeranderKleur(Kleur,aqua)
            db3 = DbClass()
            kleur = db3.HuidigeKleur(aqua)
            kleur = str(kleur)
            kleur = kleur.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
            print(kleur)
            return render_template('Kleur.html',kleur = kleur)

        return render_template('Kleur.html',kleur = kleur)

@app.route('/Schakelaar',methods=['GET', 'POST'])
def LichtSchakelaar():
    if 'mail' in session:

        if request.method == 'POST':
            db = DbClass()

            Knop = request.form['2']
            print(Knop)
            db.VeranderVerlichting(Knop,aqua)
        db2 = DbClass()
        stand = db2.standVerlichting(aqua)
        print(stand)

        return render_template('LichtSchakelaar.html', stand=stand)


@app.route('/vissen/Toevoegen',methods=['GET', 'POST'])
def VisToevoegen():
    if 'mail' in session:
        if request.method == 'POST':
            db=DbClass()
            Name=request.form['NaamVis']
            Kind=request.form['SoortVis']
            db.VoegVisToe(Name,Kind,aqua2)
            return redirect(url_for('home'))

    return render_template('VisToevoegen.html')

@app.route('/vissen/Verwijderen',methods=['GET', 'POST'])
def VerwijderenVis():
    if 'mail' in session:
        db = DbClass()
        vissen = db.VissenLijstje()
        if request.method == 'POST':
            Name = request.form['vissenLijst']
            print(Name)
            db2=DbClass()
            db2.VerwijderVis(Name)
            return redirect(url_for('home'))
        return render_template('VerwijderenVis.html',vissen=vissen)


@app.route('/Vissen',methods=['GET', 'POST'])
def vissen():

    # We geven een lijst terug met alle vissen geordend volgens soort (zoek op hoe we gegevens in een lijst kunnen zetten
    # vissen = db.HaalVissenOp()
    if 'mail' in session:
        db = DbClass()
        soorten = db.SoortVis()
        if request.method == 'POST':
            Gekozen=request.form['3']
            print(Gekozen)

            db2 = DbClass()
            vissen = db2.HaalVissenOp(Gekozen)
            return render_template('VisBekijken.html', vissen=vissen)

        return render_template('Vissen.html', soorten=soorten)

@app.route('/vissen/bekijken')
def bekijken():

    return render_template('VisBekijken.html')

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

