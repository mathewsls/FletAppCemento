import flet as ft


class Tarjeta():
    def build(self,  fecha, remision, m3, actividad, ubicacion, slump):
        self.cartas = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text(f"Remision: {remision}"),
                            subtitle=ft.Text(
                                f"fecha: {fecha}, m3: {m3}, actividad: {actividad}, ubicacion: {ubicacion}, slump {slump}."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Eliminar")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        return self.cartas
    