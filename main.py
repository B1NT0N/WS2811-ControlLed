import flet as ft
import flet_contrib.color_picker as ft_color_picker
import asyncio
from bleak import BleakScanner
from sp110e.driver import Driver



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
    status_indicator = ft.Ref[ft.Icon]()
    order = ft.Ref[ft.Dropdown]()
    ic_type = ft.Ref[ft.Dropdown]()
    pixel_num = ft.Ref[ft.Text]()
    mode = ft.Ref[ft.Text]()

    selected_device = Driver()

    async def disconnect2device():
        if selected_device.is_connected() != False:
            await selected_device.disconnect()
            print("disconected")
        else:
            print("Device already disconected")


    async def connect2device(mac_address):

        
        await disconnect2device()
        await selected_device.connect(f'{mac_address}')
        selected_device.print_parameters()
        
        
    def close_dlg(e):

        device_id_text.current.value = e.control.data[0]
        if e.control.data[1] != "":
            asyncio.run(connect2device(e.control.data[1]))
            status_indicator.current.color = ft.colors.GREEN_400
        dlg_modal.open = False
        page.update()


    def open_dlg_modal(e):

            dlg_column.current.controls.clear()

            dlg_column.current.controls.append(ft.Row([ft.ProgressRing(width=16, height=16, stroke_width = 2), ft.Text("Scanning Devices")]),)
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

            try:
                devices = asyncio.run(scan_devices())
            except:
                devices = []

            if devices != []:

                dlg_column.current.controls.clear()

                for device in devices:
                    dlg_column.current.controls.append(
                        ft.TextButton(f"{device['ID']}", on_click=close_dlg, data=[f"{device['ID']}",f"{device['address']}"])
                    )
                
                dlg_column.current.height = 35*len(devices) + 5

                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
            
            else:
                dlg_column.current.controls.clear()
                dlg_column.current.controls.append(ft.Text("No Devices Found"))
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()

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
            ft.TextButton("Cancel", on_click=close_dlg, data=[f"Connect Device",f""]),
            ft.TextButton("Re-Scan", on_click=open_dlg_modal,),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        #on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    async def scan_devices():

        device_list = []

        devices = await BleakScanner.discover()
        if devices != None:
            for d in devices:
            #print(d.address)

                device_item = {
                    "ID":f"{d.name}",
                    "address":f"{d.address}"
                }

            device_list.append(device_item)
    
        return device_list

    first_row = ft.Container(
        margin=ft.margin.only(top=5, left=15,right=15,bottom=15),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.TextButton(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ref = status_indicator, name="circle",size=15, color="red400"),
                                ft.Text(ref= device_id_text, value="Connect Device", size=20, color="white",), 
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
                    ref = order,
                    expand=1,
                    label="Order",
                    value="GBR",
                     options=[
                        ft.dropdown.Option("GBR"),
                    ],
                ),
                
                ft.Dropdown(
                    ref = ic_type,
                    expand=1,
                    label="IC Type",
                    value="WS2811",
                     options=[
                        ft.dropdown.Option("WS2811"),
                    ],
                ),
                ft.TextField(
                    ref = pixel_num,
                    expand=1,
                    value=600,
                    label="Total Pixels"
                ),
                ft.TextField(
                    ref = mode,
                    expand=1,
                    value=0,
                    label="Mode"
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
