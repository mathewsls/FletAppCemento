import flet as ft
from controls.Calendar import calendar

def Tab1():
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
    submit = ft.TextButton(text="Enviar")
    calendario = calendar()
    return ft.Column(controls=[remision, slump, metrosCubicos, actividades, ubicacion, calendario, submit])
        
        