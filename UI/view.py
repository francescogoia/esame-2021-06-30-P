import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 30-06-2021 Pomeriggio", color="blue", size=24)
        self._page.controls.append(self._title)



        self._ddLocalizzazione = ft.Dropdown(label="Localizzazione")
        self.btn_statistiche = ft.ElevatedButton(text="Statistiche", on_click=self._controller.handle_statistiche)
        row2 = ft.Row([self._ddLocalizzazione, self.btn_statistiche],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)





        self.btn_ricercaCammino = ft.ElevatedButton(text="Cerca cammino", on_click=self._controller.handle_cammino)
        row3 = ft.Row([self.btn_ricercaCammino],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)

        self._controller.fillDDLocalizations()

        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
