class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "perrine" , "passwd": "domilou128", "db": "project1"}

        self.__connection= connector.connect(**self.__dsn)
        self.__cursor =self.__connection.cursor()

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def CheckUser(self,voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT COUNT(1) FROM gebruiker WHERE mail = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def GetUser(self,voorwaarde ):
        # Query met parameters
        sqlQuery = "SELECT Hash FROM gebruiker WHERE mail='{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def registreer(self, value1, value2, value3, value4):
        # Query met parameters

        sqlQuery = "INSERT INTO gebruiker(Voornaam,Naam,mail,Hash) VALUES ('{param1}','{param2}', '{param3}','{param4}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1, param2=value2, param3=value3, param4=value4)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def standFilter(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT Filter FROM aquarium WHERE AquariumNaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def VeranderFilter(self,value1,value2):
        sqlQuery = "UPDATE aquarium SET Filter = '{param1}' WHERE AquariumNaam = '{param2}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1,param2=value2)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()



    def VeranderKleur(self,value1,value2):
        sqlQuery = "UPDATE aquarium SET Kleur = '{param1}' WHERE AquariumNaam = '{param2}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1,param2=value2)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def HuidigeKleur(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT Kleur FROM aquarium WHERE AquariumNaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=value1)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def standVerlichting(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT Verlichting FROM aquarium WHERE AquariumNaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=value1)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def VeranderVerlichting(self, value1,value2):
        sqlQuery = "UPDATE aquarium SET Verlichting = '{param1}' WHERE AquariumNaam = '{param2}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1,param2=value2)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def VoegVisToe(self,value1,value2,value3):
        #  Query zonder parameters
        sqlQuery = "INSERT INTO vis (Naam,Soort,aquarium_AquariumID) VALUES ('{param1}','{param2}','{param3}')"

        sqlCommand = sqlQuery.format(param1=value1,param2=value2,param3=value3)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def VerwijderVis(self,value1):

        sqlQuery = "Delete from vis where Naam = '{param1}'"

        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def AquariumID(self,value1):
        sqlQuery = "SELECT AquariumID FROM aquarium WHERE AquariumNaam= '{param1}'"

        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def SoortVis(self):
        sqlQuery = "SELECT DISTINCT Soort FROM vis ORDER BY Soort"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def VissenLijstje(self):
        #  Query zonder parameters
        sqlQuery = "SELECT Naam FROM vis "

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def HaalVissenOp(self,voorwaarde):
        #  Query zonder parameters
        sqlQuery = "SELECT Naam FROM vis WHERE Soort='{param1}'"
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def Visjes(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT Naam FROM vis WHERE Soort= '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def Aquariums(self):
        sqlQuery = "SELECT DISTINCT AquariumNaam FROM aquarium ORDER BY AquariumNaam"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def HuidigeTemperatuur(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT HuidigeTemperatuur FROM aquarium WHERE AquariumNaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=value1)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def GewensteTemperatuur(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT GewensteTemperatuur FROM aquarium WHERE AquariumNaam = '{param1}'"
        sqlCommand = sqlQuery.format(param1=value1)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result


    def getCurrent(self):
        # Query zonder parameters
        sqlQuery = "SELECT Heater FROM temperatuur ORDER BY DateTime DESC LIMIT 1"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def VeranderTemperatuur(self, value1, value2):
        sqlQuery = "UPDATE aquarium SET GewensteTemperatuur = '{param1}' WHERE AquariumNaam = '{param2}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1, param2=value2)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def VoegMetingToe(self,value1,value2,value3,value4):
        sqlQuery = "INSERT INTO temperatuur (Temperatuur,DateTime,aquarium_AquariumID,Heater) VALUES ('{param1}','{param2}','{param3}','{param4}')"

        sqlCommand = sqlQuery.format(param1=value1, param2=value2, param3=value3,param4=value4)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def GebruikersIDHuidig(self,voorwaarde):
        sqlQuery = "SELECT GebruikersID FROM gebruiker WHERE mail = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AquariumIDHuidig(self,voorwaarde):
        sqlQuery = "SELECT AquariumID FROM aquarium WHERE AquariumNaam = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AquariumNamen(self,voorwaarde):
        sqlQuery = "SELECT AquariumNaam FROM aquarium WHERE AquariumID = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def Index(self,voorwaarde,voorwaarde2):
        sqlQuery = "SELECT GebruikersIndex FROM gebruiker_has_aquarium WHERE gebruiker_GebruikersID = '{param1}' and aquarium_AquariumID='{param2}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde,param2=voorwaarde2)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def SelectionAquaria(self,voorwaarde):
        sqlQuery = "SELECT NaamAquarium FROM gebruiker_has_aquarium WHERE gebruiker_GebruikersID = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def Gebruikerhasaqua(self,value1,value2,value3,value4):
        sqlQuery = "INSERT INTO gebruiker_has_aquarium (gebruiker_GebruikersID,aquarium_AquariumID,GebruikersIndex,NaamAquarium) VALUES ('{param1}','{param2}','{param3}','{param4}')"

        sqlCommand = sqlQuery.format(param1=value1, param2=value2, param3=value3,param4=value4)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def Verwijderaqua(self, value1,value2):
        sqlQuery = "DELETE FROM gebruiker_has_aquarium WHERE gebruiker_GebruikersID='{param1}' AND NaamAquarium='{param2}' "

        sqlCommand = sqlQuery.format(param1=value1, param2=value2)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def CheckAquarium(self,voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT COUNT(1) FROM aquarium WHERE AquariumNaam = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result


    def GekozenAquarium(self, voorwaarde):

    # Query met parameters
        sqlQuery = "SELECT * FROM aquarium WHERE AquariumNaam = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AlleAquariums(self):
        # Query zonder parameters
        sqlQuery = "SELECT AquariumNaam FROM aquarium"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AquariumToevoegen(self,value1):
        # Query met parameters
        sqlQuery = "INSERT INTO aquarium (Filter,Verlichting,AquariumNaam) VALUES (0,0,'{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def CheckAquarium(self,voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT COUNT(1) FROM gebruiker_has_aquarium WHERE aquarium_AquariumID = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result



    def GeefRechten(self, value1):
        # Query met parameters
        sqlQuery = "UPDATE gebruiker_has_aquarium SET GebruikersIndex = '1' WHERE gebruiker_GebruikersID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def VerwijderRechten(self, value1):
        # Query met parameters
        sqlQuery = "UPDATE gebruiker_has_aquarium SET GebruikersIndex = '2' WHERE gebruiker_GebruikersID = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()


    # def getDataFromDatabase(self):
    #     # Query zonder parameters
    #     sqlQuery = "SELECT * FROM tablename"
    #
    #     self.__cursor.execute(sqlQuery)
    #     result = self.__cursor.fetchall()
    #     self.__cursor.close()
    #     return result
    #
    # def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
    #     # Query met parameters
    #     sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
    #     # Combineren van de query en parameter
    #     sqlCommand = sqlQuery.format(param1=voorwaarde)
    #
    #     self.__cursor.execute(sqlCommand)
    #     result = self.__cursor.fetchall()
    #     self.__cursor.close()
    #     return result
    #
    # def setDataToDatabase(self, value1):
    #     # Query met parameters
    #     sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
    #     # Combineren van de query en parameter
    #     sqlCommand = sqlQuery.format(param1=value1)
    #
    #     self.__cursor.execute(sqlCommand)
    #     self.__connection.commit()
    #     self.__cursor.close()

        # Metingen inlezen
        # Grafieken
    def chartTwoHours(self):
        # Query zonder parameters
        sqlQuery = "SELECT TemperatuurID, Temperatuur " \
                   "UNIX_TIMESTAMP(DateTime) FROM ( select * from temperatuur ORDER BY TemperatuurID DESC LIMIT 120) sub order by DateTime ASC"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def chartOneMonth(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1),unix_timestamp(DateTime) FROM temperatuur WHERE datetime >= (NOW() - interval 1 month) " \
                   "and datetime <= NOW() GROUP BY dayofmonth(datetime) order by dateTime"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def chartOneWeek(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1), unix_timestamp(DateTime) FROM temperatuur WHERE datetime >= (NOW() - interval 1 week) " \
                   "and datetime <= NOW() GROUP BY dayofweek(datetime) order by dateTime"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def chartOneDay(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1), unix_timestamp(DateTime) FROM temperatuur WHERE datetime >= (NOW() - interval 1 day) and " \
                   "datetime <= NOW() GROUP BY hour(datetime) order by dateTime"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

        # buttons
    def getLastMonth(self):
        # Query zonder parameters
        sqlQuery = "select format(avg(Temperatuur),1) from temperatuur " \
                   "where DateTime <= (NOW() - INTERVAL 1 MONTH)"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getHoursHeat(self):
        # Query zonder parameters
        sqlQuery = "select count(*) from ( select Heater from temperatuur where Heater = 1 and DateTime >= CURDATE() group by " \
                   "hour(DateTime)) As Count;"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    # cards
    def getCurrent(self):
        # Query zonder parameters
        sqlQuery = "SELECT Heater FROM temperatuur ORDER BY DateTime DESC LIMIT 1"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getTemp(self,value1):
        # Query zonder parameters
        sqlQuery = "SELECT Temperatuur FROM temperatuur  WHERE aquarium_AquariumID='{param1}' ORDER BY DateTime DESC LIMIT 1"
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def dayAvg(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1) FROM temperatuur WHERE dayofyear(DateTime)=dayofyear(NOW());"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def weekAvg(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1) FROM temperatuur WHERE weekofyear(DateTime)=weekofyear(NOW());"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def monthAvg(self):
        # Query zonder parameters
        sqlQuery = "SELECT format(avg(Temperatuur),1) FROM temperatuur WHERE month(DateTime)=month(NOW());"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result