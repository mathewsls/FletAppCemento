import flet as ft
from controls.cards import Tarjeta
from controller.Registro import consultar


listdata = []


def Tab2():
    cursor = consultar()
    list = []
    for document in cursor:
        fecha = document['fecha']
        remision = document['remision'] 
        m3 = document['m3'] 
        actividad = document['actividad'] 
        ubicacion = document['ubicacion'] 
        slump = document['slump']
        #fecha, remision, m3, actividad, ubicacion, slump
        carta = Tarjeta.build(Tarjeta,fecha, remision, m3, actividad, ubicacion, slump)
        carta.id = remision
        list.append(carta)
        
    listdata.append(remision)
        
    

    return ft.Column(list)

