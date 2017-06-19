import os
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
        db1=DbClass()
        HuidigeTemp = db1.getTemp(aqua2)
        HuidigeTemp = str(HuidigeTemp)
        HuidigeTemp = HuidigeTemp.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",
                                                                                                              "").replace(
            "'", "")
        print(HuidigeTemp)
        db2 = DbClass()
        stand = db2.standVerlichting(aqua)
        db3 = DbClass()
        stand2 = db3.standFilter(aqua)
        db4=DbClass()
        kleur=db4.HuidigeKleur(aqua)
        kleur=str(kleur)
        kleur = kleur.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
        print(kleur)
        mail = session['mail']
        print(mail)
        db6 = DbClass()
        ID = db6.GebruikersIDHuidig(mail)
        print(ID)
        ID = str(ID)
        ID = ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "")
        print(ID)
        db5 = DbClass()
        global indexnummer
        indexnummer = db5.Index(ID, aqua2)
        print(indexnummer)


        return render_template('index.html',HuidigeTemp=HuidigeTemp,stand=stand,stand2=stand2,kleur=kleur)

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
        mail = session['mail']
        print(mail)
        db2 = DbClass()
        ID = db2.GebruikersIDHuidig(mail)
        ID = str(ID)
        ID = ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
            "'", "")
        aquaria = db.SelectionAquaria(ID)
        print(aquaria)
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
    return redirect(url_for('aanmelden'))


@app.route('/aquariums/toevoegen',methods=['GET', 'POST'])
def AquariumToevoegen():
    if 'mail' in session:
        db = DbClass()
        aquaria = db.Aquariums()
        if request.method =='POST':
            mail = session['mail']
            print(mail)
            db2 = DbClass()
            ID = db2.GebruikersIDHuidig(mail)
            ID = str(ID)
            ID= ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
                "'", "")
            print(ID)
            Gekozen=request.form['aquarium']
            print(Gekozen)

            db3=DbClass()
            AquaID=db3.AquariumID(Gekozen)
            AquaID = str(AquaID)
            AquaID = AquaID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
                "'", "")
            print(AquaID)
            db7=DbClass()
            Naam=db7.AquariumNamen(AquaID)
            Naam = str(Naam)
            Naam = Naam.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",                                                                                    "").replace(
                "'", "")
            print(Naam)
            db4=DbClass()
            Check=db4.CheckAquarium(AquaID)

            print(Check)
            if Check==[(0,)]:
                db5=DbClass()
                db5.Gebruikerhasaqua(ID,AquaID,0,Naam)
            else:
                db6=DbClass()
                db6.Gebruikerhasaqua(ID, AquaID, 2,Naam)
            return redirect(url_for('aquariums'))
        return render_template('AquariumToevoegen.html',aquaria=aquaria)

@app.route('/aquariums/verwijderen',methods=['GET', 'POST'])
def AquariumVerwijderen():
    if 'mail' in session:
        db = DbClass()
        mail = session['mail']
        print(mail)
        db2 = DbClass()
        ID = db2.GebruikersIDHuidig(mail)
        ID = str(ID)
        ID = ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
            "'", "")
        print(ID)
        aquaria = db.SelectionAquaria(ID)
        print(aquaria)
        if request.method == 'POST':
            Gekozen = request.form['aquarium']
            Gekozen=str(Gekozen)
            Gekozen = Gekozen.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
            "'", "")
            print(Gekozen)
            db3=DbClass()
            db3.Verwijderaqua(ID,Gekozen)

            return redirect(url_for('aquariums'))
        return render_template('AquariumVerwijderen.html',aquaria=aquaria)


    # werk hie met checkboxen en zet dan later om naar een knop




@app.route('/filter',methods=['GET', 'POST'])
def filter():
    if 'mail' in session:
        if indexnummer ==[(0,)] or indexnummer==[(1,)]:
            print('je bent binnen')
            if request.method == 'POST':
                db=DbClass()

                Knop = request.form['1']
                print(Knop)
                db.VeranderFilter(Knop,aqua)
            db2 = DbClass()
            stand = db2.standFilter(aqua)
            print(stand)

            return render_template('Filter.html', stand=stand)
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')



    # werk hie met checkboxen en zet dan later om naar een knop

@app.route('/temperatuur',methods=['GET', 'POST'])
def temperatuur():
    # in plaats van grafiek heater kunnen we weergeven hoe lang de heater heeft aangelegen en we kunnen de temperatuur weergeven in een grafiek,
    # verder kan de gebruiker de gewenste temperatuur voor het aquarium instellen. en de huidige temperatuur waarnemen.
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            db=DbClass()
            Gewenst=db.GewensteTemperatuur(aqua)
            Gewenst = str(Gewenst)
            Gewenst = Gewenst.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "")
            print(Gewenst)
            db3 = DbClass()
            db4 = DbClass()
            db5 = DbClass()
            db6 = DbClass()
            db7 = DbClass()
            db8= DbClass()
            db9=DbClass()
            db1=DbClass()

            dag = db3.dayAvg()
            week = db4.weekAvg()
            maand = db5.chartOneMonth()
            weekgraph = db6.chartOneWeek()
            daggraph = db7.chartOneDay()
            maandAvg = db8.monthAvg()
            Heater=db9.getCurrent()
            HuidigeTemp=db1.getTemp(aqua2)
            HuidigeTemp = str(HuidigeTemp)
            HuidigeTemp = HuidigeTemp.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
            print(HuidigeTemp)
            print(Heater)
            if request.method == 'POST':
                db2 = DbClass()
                GewensteTemp=request.form['temperatuur']
                print(GewensteTemp)
                db2.VeranderTemperatuur(GewensteTemp,aqua)
                db = DbClass()
                Gewenst = db.GewensteTemperatuur(aqua)
                Gewenst = str(Gewenst)
                Gewenst = Gewenst.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "")
                print(Gewenst)

                return render_template('Temperatuur.html',Gewenst=Gewenst,dag=dag, week=week, maand=maand, weekgraph=weekgraph, daggraph=daggraph,
                               maandAvg=maandAvg,Heater=Heater,HuidigeTemp=HuidigeTemp)

            return render_template('Temperatuur.html',Gewenst=Gewenst,dag=dag, week=week, maand=maand, weekgraph=weekgraph, daggraph=daggraph,
                               maandAvg=maandAvg,Heater=Heater,HuidigeTemp=HuidigeTemp)
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/verlichting',methods=['GET', 'POST'])
def verlichting():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
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
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/verlichting/kleur',methods=['GET', 'POST'])
def Kleur():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
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
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/Schakelaar',methods=['GET', 'POST'])
def LichtSchakelaar():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            if request.method == 'POST':
                db = DbClass()

                Knop = request.form['2']
                print(Knop)
                db.VeranderVerlichting(Knop,aqua)
            db2 = DbClass()
            stand = db2.standVerlichting(aqua)
            print(stand)

            return render_template('LichtSchakelaar.html', stand=stand)
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')


@app.route('/vissen/Toevoegen',methods=['GET', 'POST'])
def VisToevoegen():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            if request.method == 'POST':
                db=DbClass()
                Name=request.form['NaamVis']
                Kind=request.form['SoortVis']
                db.VoegVisToe(Name,Kind,aqua2)
                return redirect(url_for('home'))

            return render_template('VisToevoegen.html')
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/vissen/Verwijderen',methods=['GET', 'POST'])
def VerwijderenVis():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            db = DbClass()
            vissen = db.VissenLijstje()
            if request.method == 'POST':
                Name = request.form['vissenLijst']
                print(Name)
                db2=DbClass()
                db2.VerwijderVis(Name)
                return redirect(url_for('home'))
            return render_template('VerwijderenVis.html',vissen=vissen)
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')


@app.route('/Vissen',methods=['GET', 'POST'])
def vissen():

    # We geven een lijst terug met alle vissen geordend volgens soort (zoek op hoe we gegevens in een lijst kunnen zetten
    # vissen = db.HaalVissenOp()
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            db = DbClass()
            soorten = db.SoortVis()
            if request.method == 'POST':
                Gekozen=request.form['3']
                print(Gekozen)

                db2 = DbClass()
                vissen = db2.HaalVissenOp(Gekozen)
                return render_template('VisBekijken.html', vissen=vissen)

            return render_template('Vissen.html', soorten=soorten)
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/vissen/bekijken')
def bekijken():
    if 'mail' in session:
        if indexnummer == [(0,)] or indexnummer == [(1,)]:
            return render_template('VisBekijken.html')
        if indexnummer == [(2,)]:
            return render_template('GeenToegang2.html')

@app.route('/instellingen')
def instellingen():
    #Hier kijken we voor de instellingen te kunnen aanpassen van de gebruiker, men kan namelijk bepalen of een gebruiker alle rechten heeft of niet,
    # Pas wel op enkel de eerste gebruiker kan deze instellingen raadplegen ! Voor de gebruikers met beperkte toelating zal men
    # moeten kijken voor het verbergen van zelf in te vullen gegevens (knoppen, formulieren,... )
    # (maak mss apparte klasse aan zodat je alles drect kan verbergen van dezelfde klasse.
    if 'mail' in session:
        if indexnummer == [(0,)] :
            return render_template('Gebruiker.html')
        if indexnummer == [(2,)] or indexnummer == [(1,)]:
            return render_template('GeenToegang2.html')

@app.route('/instellingen/Toevoegen',methods=['GET', 'POST'])
def GeefRechten():
    if 'mail' in session:
        if indexnummer == [(0,)] :
            if request.method == 'POST':
                Gebruiker=request.form['toevoegen']
                db=DbClass()
                ID=db.GebruikersIDHuidig(Gebruiker)
                ID = str(ID)
                ID = ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",
                                                                                                          "").replace(
                    "'", "")
                print(ID)
                db2=DbClass()
                db2.GeefRechten(ID)
                return redirect(url_for('instellingen'))
            return render_template('GeefRechten.html')
        if indexnummer == [(2,)] or indexnummer == [(1,)]:
            return render_template('GeenToegang2.html')

@app.route('/instellingen/Verwijderen',methods=['GET', 'POST'])
def VerwijderRechten():
    if 'mail' in session:
        if indexnummer == [(0,)] :
            if request.method == 'POST':
                Gebruiker=request.form['toevoegen']
                db=DbClass()
                ID=db.GebruikersIDHuidig(Gebruiker)
                ID = str(ID)
                ID = ID.replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",
                                                                                                          "").replace(
                    "'", "")
                db2=DbClass()
                db2.VerwijderRechten(ID)
                return redirect(url_for('instellingen'))
            return render_template('VerwijderRechten.html')

        if indexnummer == [(2,)] or indexnummer == [(1,)]:
            return render_template('GeenToegang2.html')

@app.route('/afmelden')
def afmelden():
    session.pop('mail', None)
    return redirect(url_for('onboarding'))

#Error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html', error=error), 404


@app.errorhandler(403)
def page_not_found(error):
    return render_template('error/403.html', error=error), 403

@app.errorhandler(405)
def page_not_found(error):
    return render_template('error/405.html', error=error), 405

@app.errorhandler(500)
def page_not_found(error):
    return render_template('error/500.html', error=error), 500


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    port=int(os.environ.get("PORT",8080))
    host='0.0.0.0'
    app.run(host=host,port=port,debug=True)

