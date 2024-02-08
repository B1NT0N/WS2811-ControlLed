import flet as ft
import flet_contrib.color_picker as ft_color_picker



def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_max_width = 500
    page.theme_mode = ft.ThemeMode.DARK

    global width 
    global height 

    width = 480
    height = 854

    global color_units

    dlg_column = ft.Ref[ft.Column]()
    device_id_text = ft.Ref[ft.Text]()

    
    def close_dlg(e):

        device_id_text.current.value = e.control.data
        dlg_modal.open = False
        page.update()

    device1 = {
        "ID":"test_id1",
    }

    device2 = {
        "ID":"test_id2",
    }

    devices = [device1, device2,]

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Chose Bluetooth Device"),
        content=ft.Column(
            ref=dlg_column,
            height=35,
            controls=[
            ]
        ),
        actions=[
            ft.TextButton("Cancel", on_click=close_dlg, data="Device ID"),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(e):

        dlg_column.current.controls.clear()

        for device in devices:
            dlg_column.current.controls.append(
                ft.TextButton(f"{device['ID']}", on_click=close_dlg, data=f"{device['ID']}")
            )
        
        dlg_column.current.height = 35*len(devices) + 5
        
        dlg_column.current.width = 2*len(devices)

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    first_row = ft.Container(
        margin=ft.margin.only(top=5, left=15,right=15,bottom=15),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.TextButton(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(name="circle",size=15, color="green400"),
                                ft.Text(ref= device_id_text, value="Device ID", size=20, color="white",), 
                            ],
                        ),
                    ),
                    on_click=open_dlg_modal
                ),
                
                ft.Container(
                    ft.Switch(
                        label=" ON/OFF", 
                    value=False, 
                    label_position=ft.LabelPosition.LEFT, 
                    active_track_color="green",
                    
                    )

                ),
                
                
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
        margin=ft.margin.all(15),
        content=ft.GridView(
                runs_count=3,
                max_extent=width/4,
                padding=ft.padding.only(left=40, right=40),
                controls=[
                    create_color_units("red",[255,255,255]),
                    create_color_units("green",[255,255,255]),
                    create_color_units("blue",[255,255,255]),
                    create_color_units("orange",[255,255,255]),
                    create_color_units("teal",[255,255,255]),
                    create_color_units("cyan",[255,255,255]),
                    create_color_units("white",[255,255,255]),
                    create_color_units("yellow",[255,255,255]),
                    create_color_units("pink",[255,255,255]),
                    ]
            )

        )


    third_row = ft.Container(
        margin=ft.margin.all(15),
        padding=ft.padding.only(left=40, right=40),
        content= ft.Row
        (
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
               ft.ElevatedButton(
                expand = True,
                height = width/5,
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
        margin=ft.margin.all(15),
        padding=ft.padding.only(left=40, right=40),
        content=ft.Column(
            
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    
                    controls=[
                        ft_color_picker.HueSlider(on_change_hue=change_hue),
                    ],
                    
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(name=ft.icons.BRIGHTNESS_LOW, color=ft.colors.WHITE70),
                        ft.Slider(expand=True, active_color=ft.colors.WHITE),
                        ft.Icon(name=ft.icons.BRIGHTNESS_HIGH, color=ft.colors.WHITE),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(name=ft.icons.FAST_FORWARD_OUTLINED, color=ft.colors.WHITE),
                        ft.Slider(expand=True, active_color=ft.colors.WHITE),
                        ft.Icon(name=ft.icons.FAST_FORWARD, color=ft.colors.WHITE),
                    ]
                ),
            ]
        )
    )

    last_row = ft.Container(
        margin=ft.margin.only(top=15, left=15,right=15,bottom=5),
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
        #bgcolor = ft.colors.GREY_800,
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
