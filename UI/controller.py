import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def calcola_distanza(self, e):
        x = self._view.distance.value
        if x is None or x == "":
            self._view.create_alert("Errore dato inserito")
            return
        grafo = self._model.crea_archi(x)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con {len(grafo.nodes)} nodi e {len(grafo.edges)} archi."))
        archi = grafo.edges(data=True) #Rende i dati leggibili
        #Archi restituisce i dati organizzato come tuple aventi tre dati, il primo dato è il nodo di partenza (salvato DA ME come oggetto)
        #Il secondo dato è il nodo di arrivo (analogo a quello di partenza)
        #Il terzo dato è un dizionario che sotto il nome di data[weight] (chiave) mi restituisce il dato specifico richiesto (il peso in questo caso)
        for u, v, data in archi: #Uso questa dicitura perché sto estrando delle tuple (data è un dizionario che contiene vari dati associati al grafo, weight è il peso che abbiamo impostato alla sua creazione
            distanza = data['weight']
            self._view.txt_result.controls.append(
            ft.Text(f"Rotta: {u.IATA_CODE} -> {v.IATA_CODE} | Distanza media: {distanza} miglia")
            )
        self._view.update_page()

