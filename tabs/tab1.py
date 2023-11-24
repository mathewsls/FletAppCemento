import flet as ft
from controls.Calendar import calendar
from controller.Registro import agregar


def Tab1(page: ft.Page):
    page.update()
         #--------------Remision--------------------------------------
    remision = ft.TextField(label="Remision", keyboard_type=ft.KeyboardType.NUMBER)
     #--------------Remision--------------------------------------
     #--------------slump--------------------------------------
    slump = ft.TextField(label="Slump", keyboard_type=ft.KeyboardType.NUMBER)
     #--------------slump--------------------------------------

    
     #--------------Metros cubicos m³--------------------------------------
    metrosCubicos = ft.TextField(label="metros cubicos", keyboard_type=ft.KeyboardType.NUMBER, suffix_text="m³")
    #--------------Metros cubicos m³--------------------------------------
    
    
    #--------------Actividades--------------------------------------
    actividades = ft.Dropdown( label="Actividades", options=[
        ft.dropdown.Option("muros"),
        ft.dropdown.Option("loza"),
        ft.dropdown.Option("aticos"),
    ]
    )
    #--------------Actividades--------------------------------------
     #--------------ubicacion--------------------------------------
    ubicacion = ft.TextField(label="ubicacion", keyboard_type=ft.KeyboardType.NUMBER, prefix_text="APT ")
        
    remision = ft.TextField(label="Remision", keyboard_type=ft.KeyboardType.NUMBER)
        #--------------Remision--------------------------------------
        #--------------slump--------------------------------------
    slump = ft.TextField(label="Slump", keyboard_type=ft.KeyboardType.NUMBER)
        #--------------slump--------------------------------------

        
        #--------------Metros cubicos m³--------------------------------------
    metrosCubicos = ft.TextField(label="metros cubicos", keyboard_type=ft.KeyboardType.NUMBER, suffix_text="m³")
        #--------------Metros cubicos m³--------------------------------------
        
        
        #--------------Actividades--------------------------------------
    actividades = ft.Dropdown( label="Actividades", options=[
            ft.dropdown.Option("muros"),
            ft.dropdown.Option("loza"),
            ft.dropdown.Option("aticos"),
        ]
        )
        #--------------Actividades--------------------------------------
        #--------------ubicacion--------------------------------------
    ubicacion = ft.TextField(label="ubicacion", keyboard_type=ft.KeyboardType.NUMBER, prefix_text="APT ")
        #--------------ubicacion--------------------------------------
    calendario = calendar()
    def cerrar(e):
        dlg_modal.open = False
        page.update()
    def enviar(e):
        cerrar(e)
        fecha = calendario.encontrar()
        datos = {
            'ubicacion': ubicacion.value,
            'remision': remision.value,
            'm3': metrosCubicos.value,
            'actividad': ubicacion.value,
            'slump': slump.value,
        }
        datos['fecha'] = fecha
        agregar(datos)
        page.update()
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor confirma"),
        content=ft.Text("quieres enviar este registro?"),
        actions=[
            ft.TextButton("Yes", on_click=enviar),
            ft.TextButton("No", on_click=cerrar),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    submit = ft.ElevatedButton(text="Enviar", on_click=open_dlg_modal)
    

        
    return ft.Column(controls=[remision, slump, metrosCubicos, actividades, ubicacion, calendario, submit])
    




