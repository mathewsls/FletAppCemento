import flet as ft
from controls.Calendar import calendar
from controls.Navigation import Drawer
def main(page: ft.Page):
    Drawer(page)
    
    
ft.app(target=main)