import database
from database.DB_connect import DBConnect
from database.Aeroporti import Aeroporti


class DAO():
    def __init__(self):
        pass


    def get_nodi(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        #Mi prendo tutte le righe di airports così da poterle aggiungere
        query = """
        SELECT DISTINCT *
        FROM airports
        """
        noid = []
        cursor.execute(query)
        for i in cursor:
            nodo = Aeroporti(**i) #Metodo per spacchettare se i dati della query sono sotto forma di dizionario e la dataclass che uso per salvarli ha i nomi delle variabili uguali alle chiavi del dizionario (che se non uso alias sono i nomi delle righe del database)
            noid.append(nodo)

        cursor.close()
        conn.close()
        return noid

    def get_archi(self, x):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        #Il LEAST e il GREATEST mi permettono di fare in modo che sia indistinto 10->20 o 20->10 in quanto il più grande sarà il nodo u e il più piccolo il nodo v,
        #Prendo direttamente la media della distanza p, raggruppata per nodi di andata e arrivo, aventi distanza media > del parametro che passo
        query ="""
        SELECT LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) as u, 
        GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) as v,
        AVG(DISTANCE) as p
        FROM flights
        GROUP BY u, v
        HAVING AVG(DISTANCE) > %s
        """
        risultato = []
        cursor.execute(query, (x,))
        for row in cursor:
            risultato.append((row["u"], row["v"], row["p"])) #In questo modo ogni dato di risultato sarà una tupla con nodo minore, nodo maggiore e peso(distanza)
        cursor.close()
        conn.close()
        return risultato

