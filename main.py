import flet as ft
import flet_contrib.color_picker as ft_color_picker



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
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[   
                        ft.Icon(name=ft.icons.CIRCLE, size=10, color=ft.colors.GREEN),
                        ft.TextButton(text="Device ID"),
                    ]
                    
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
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        create_color_units(ft.colors.RED, [255,0,0]),
                        create_color_units(ft.colors.GREEN, [0,255,0]),
                        create_color_units(ft.colors.BLUE, [0,0,255]),
                        create_color_units(ft.colors.BLACK, [0,0,0]),
                        
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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

    def change_hue():
        pass

    fourth_row = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft_color_picker.HueSlider(on_change_hue=change_hue),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(name=ft.icons.BRIGHTNESS_LOW, color=ft.colors.WHITE),
                        ft.Slider(expand=True),
                        ft.Icon(name=ft.icons.BRIGHTNESS_HIGH, color=ft.colors.WHITE),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(name=ft.icons.FAST_FORWARD_OUTLINED, color=ft.colors.WHITE),
                        ft.Slider(expand=True),
                        ft.Icon(name=ft.icons.FAST_FORWARD, color=ft.colors.WHITE),
                    ]
                ),
            ]
        )
    )

    last_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Dropdown(
                    expand=1,
                    label="Order",
                    value="RGB",
                     options=[
                        ft.dropdown.Option("RGB"),
                    ],
                ),
                
                ft.Dropdown(
                    expand=1,
                    label="IC Type",
                    value="WS2811",
                     options=[
                        ft.dropdown.Option("WS2811"),
                    ],
                ),
                ft.TextField(
                    expand=1,
                    value=300,
                    label="Total Pixels"
                ),
            ]
        )
    )

    main_container = ft.Container(
        width = width,
        height = height,
        bgcolor = ft.colors.GREY_800,
        #border_radius = ft.border_radius.only(top_left=30, top_right=30, bottom_left=0, bottom_right=0),
        margin=ft.margin.symmetric(vertical=10),
        padding = ft.padding.all(10),

        content = ft.Column(
            controls=[
                first_row,
                second_row,
                third_row,
                fourth_row,
                last_row,
            ]
        )
    )


    
    page.add(main_container)

ft.app(main)
