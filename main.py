import flet as ft




def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_max_width = 500

    global width 
    global height 

    width = 480
    height = 854

    global color_units

    first_row = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    ft.TextButton(text="Device ID"),
                ),
                
                ft.Container(
                    ft.Switch(label=" ON/OFF", value=False, label_position=ft.LabelPosition.LEFT)
                )
                
            ]
        )
    )

    def create_color_units(color, color_rgb):

        color_units = ft.Container(
        bgcolor = color,
        width=width/6,
        height=width/6,
        border_radius=ft.border_radius.all(5),
        on_click=lambda e: print(f"{color_rgb}"),
        )

        return color_units


    second_row = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        create_color_units(ft.colors.RED, [255,0,0]),
                        create_color_units(ft.colors.GREEN, [0,255,0]),
                        create_color_units(ft.colors.BLUE, [0,0,255]),
                        create_color_units(ft.colors.BLACK, [0,0,0]),
                        
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        create_color_units(ft.colors.RED, [255,0,0]),
                        create_color_units(ft.colors.GREEN, [0,255,0]),
                        create_color_units(ft.colors.BLUE, [0,0,255]),
                        create_color_units(ft.colors.BLACK, [0,0,0]),

                    ]
                ),

            ]
        )

    )

    third_row = ft.Container(
        content= ft.Row
        (
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
               ft.ElevatedButton(
                expand = True,
                height = width/6,
                style=ft.ButtonStyle(
                    bgcolor = ft.colors.WHITE,
                    elevation = 0,
                    surface_tint_color = ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=5),
                )
                
            ),

            ]
    ))

    main_container = ft.Container(
        width = width,
        height = height,
        bgcolor = ft.colors.GREY_800,
        #border_radius = ft.border_radius.only(top_left=30, top_right=30, bottom_left=0, bottom_right=0),
        margin=ft.margin.symmetric(vertical=10,),

        content = ft.Column(
            controls=[
                first_row,
                second_row,
                third_row
            ]
        )
    )


    
    page.add(main_container)

ft.app(main)
