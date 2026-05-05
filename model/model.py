from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {} #Creo una idMap dove associo ad ogni id degli aeroporti (chiave) il relativo oggetto (valore)
        self._dao = DAO()

    def crea_nodi(self):
        nodi = self._dao.get_nodi()
        self.grafo.add_nodes_from(nodi) #Con questo comando posso aggiungere ad un grafo come nodi tutti i valori di una data lista.
        for nodo in nodi:
            self.idMap[nodo.ID] = nodo #Aggiungo i nodi alla idMap

    def crea_archi(self, x):
        self.grafo.clear() #Pulisco il grafo ogni volta così da non aggiungerci roba sempre
        archi = self._dao.get_archi(x) #Mi prendo la queri del dao, ogni elemento della lista archi conterrà una tupla (che quindi potrò spacchettare
        #Contenente al suo interno nodo minore, maggiore e peso
        for u, v, p in archi:#archi è una lista di tuple, pertanto uso questa dicitura per spacchetarli, u nodo partenza, v nodo arrivo, p peso dell'arco
            self.grafo.add_edge(self.idMap[u], self.idMap[v], weight = p) #Uso la idMap così da poter dall'ID dell'aeroporto risalire all'oggetto aeroporto, che ho precedentemente impostato come nodo del grafo (e quindi per aggiungere gli archi dovrò far riferimento a tutto l'oggetto e non al solo ID)
        return self.grafo

