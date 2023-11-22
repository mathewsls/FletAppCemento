import flet as ft
from controls.cards import Tarjeta
remision = 10321
fecha = 3220
m3 = 10
slump = 10231
actividad = "cualquiera"
ubicacion = "APT - cualquiera"
def Tab2():
    tabla1 = Tarjeta().build(fecha, remision, m3, actividad, ubicacion, slump)
    tabla2 = Tarjeta().build(fecha, remision, m3, actividad, ubicacion, slump)
    

    return ft.Column([
            tabla1,
            tabla2
        ])


