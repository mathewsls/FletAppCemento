import flet as ft
from tabs.tab1 import Tab1
from tabs.tab2 import Tab2
from time import sleep
import tabs.tab2 as taba2
from tabs.tab3 import Tab3
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from controller.Registro import eliminar

    
    
def Drawer(page: ft.Page):
    page.remove()
    tab1 = Tab1(page)
        
    
    def probar(e):
        page.controls.clear()
        if e.control.selected_index == 0:
            tab1 = Tab1(page)
            page.add(tab1)
            page.update()
        elif e.control.selected_index == 1:
            tab2 = Tab2()
            def quitar(a):
                borrar = str(remisionborrar.value)
                eliminar(borrar)
                if tab2 in page.controls:
                    page.controls.clear
                    probar(e) 
                print("lo que salio fue: ", borrar)
            remisionborrar = ft.TextField(hint_text="Ingrese el numero de remision para borrar")

            borrador = ft.ElevatedButton(text="Borrar", icon=ft.icons.DELETE, on_click=quitar)
            page.add(tab2, remisionborrar,borrador)
            page.update() 
        elif e.control.selected_index == 2:
            tab3 = Tab3()
            page.add(tab3)
            page.update()

    page.title = "AppBeta"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.ADD_CHART, label="Agregar registros", ),
            ft.NavigationDestination(icon=ft.icons.TABLE_CHART, label="Ver registros"),
            ft.NavigationDestination(icon=ft.icons.BAR_CHART, label="Resumen de este mes",
            ),
        ], on_change=probar
    )   
    

    page.add(tab1)