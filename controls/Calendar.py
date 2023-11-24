import flet as ft
import datetime


class calendar(ft.UserControl):
    def build(self):
        self.fecha = ft.TextField(label="Fecha", read_only=True, value="YYYY-MM-DD")
        self.date_picker = ft.DatePicker(
        on_change=self.change_date,
        on_dismiss=self.date_picker_dismissed,
        first_date=datetime.datetime(2023, 11, 17)
        )

        self.date_button = ft.ElevatedButton(
        "Seleccione la fecha",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: self.date_picker.pick_date(),
        )
        return ft.Column(controls=[self.fecha, self.date_button, self.date_picker])
    def change_date(self, e):
        self.fechastr = str(self.date_picker.value)
        self.fecha.value = self.fechastr[0:10]
        self.fecha.update()
    
        
    def date_picker_dismissed(self, e):
        self.fechastr = str(self.date_picker.value)
        self.fecha.value = self.fechastr[0:10]
        self.fecha.update()
        
    def encontrar(self):
        fecha = self.fecha.value

        return fecha
    
    
