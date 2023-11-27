import flet as ft
from controller.Registro import consultar

cursor = consultar()

def Tab3():
    data = []
    contador = 0
    for i in cursor:
        x = float(i['slump'])
        data.insert(0, ft.LineChartDataPoint(contador, x-4))
        contador += 1
        
    data_1 = [
        ft.LineChartData(
            data_points=data
            ,
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
            
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("6.0", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("7.0", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("9.0", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("y", size=20, weight=ft.FontWeight.BOLD),
                ),
               
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Container(
                        ft.Text(
                            "1",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=15,
                    label=ft.Container(
                        ft.Text(
                            "15",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=30,
                    label=ft.Container(
                        ft.Text(
                            "30",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=6,
        min_x=0,
        max_x=30,
        # animate=5000,
        expand=True,
    )
    return chart