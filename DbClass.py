class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {"host": "localhost", "user": "root" , "passwd": "root", "db": "project1"}

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

    def standFilter(self):
        # Query zonder parameters
        sqlQuery = "SELECT Filter FROM Aquarium WHERE AquariumNaam = 'Tropical'"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def VeranderFilter(self,value1):
        sqlQuery = "UPDATE Aquarium SET Filter = '{param1}' WHERE AquariumNaam = 'Tropical'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def CheckAquarium(self,voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT COUNT(1) FROM Aquarium WHERE AquariumNaam = '{param1}'"

        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def GekozenAquarium(self, voorwaarde):

    # Query met parameters
        sqlQuery = "SELECT * FROM Aquarium WHERE AquariumNaam = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AlleAquariums(self):
        # Query zonder parameters
        sqlQuery = "SELECT AquariumNaam FROM Aquarium"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def AquariumToevoegen(self,value1):
        # Query met parameters
        sqlQuery = "INSERT INTO Aquarium (Filter,Verlichting,AquariumNaam) VALUES (0,0,'{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def VeranderVerlichting(self, value1):
        sqlQuery = "INSERT INTO Aquarium (Verlichting) VALUES ({param1})"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()



    def VerwijderExtraGebruiker(self, value1):
        # Query met parameters
        sqlQuery = "UPDATE Aquarium SET ExtraHoofdgebruiker = '' WHERE ExtraHoofdgebruiker = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()
    def HaalVissenOp(self):
        #  Query zonder parameters
        sqlQuery = "SELECT * FROM vissen ORDER BY Soort"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

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