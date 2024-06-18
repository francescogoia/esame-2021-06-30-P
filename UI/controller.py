import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def fillDDLocalizations(self):
        self._model.crea_grafo()
        localizzazioni = self._model._nodes
        if len(localizzazioni) == 0:
            print("Errore no localizzazione trovate")
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Errore: nessuna localizzazione trovata"))
            self._view.update_page()
            return
        self._view.txt_result.controls.clear()
        for l in localizzazioni:
            self._view._ddLocalizzazione.options.append(ft.dropdown.Option(data=l, text=l, on_click=self.selectLocation))
            self._view.update_page()

    def selectLocation(self, e):
        if e.control.data is None:
            self._choiceLocation = None
        else:
            self._choiceLocation = e.control.data

    def handle_statistiche(self, e):
        result = self._model.getnNeighboors(self._choiceLocation)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a {self._choiceLocation}:"))
        for v in result:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]} : {v[1]}"))
        self._view.update_page()



    def handle_cammino(self, e):
        cammino, peso_cammino = self._model.handlePath(self._choiceLocation)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Cammino che parte da {self._choiceLocation} con peso: {peso_cammino}"))
        self._view.txt_result.controls.append(ft.Text(f"{self._choiceLocation}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"{c[1]}"))
        self._view.update_page()




