import flet as ft
from tabs.tab1 import Tab1
from tabs.tab2 import Tab2
from tabs.tab3 import Tab3
def Drawer(page: ft.Page):
    tab1 = Tab1()
    def probar(e):
        page.controls.clear()
        if e.control.selected_index == 0:
            tab1 = Tab1()
            page.add(tab1)
            page.update()
        elif e.control.selected_index == 1:
            tab2 = Tab2()
            page.add(tab2)
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