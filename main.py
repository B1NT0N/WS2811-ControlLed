import flet as ft




def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    first_row = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    ft.TextButton(text="Text button"),
                ),
                
                ft.Container(
                    ft.Switch(label="", value=False)
                )
                
            ]
        )
    )

    main_container = ft.Container(
        width = 480,
        height = 854,
        bgcolor = ft.colors.BLACK87,
        border_radius = ft.border_radius.only(top_left=20, top_right=20, bottom_left=0, bottom_right=0),
        padding=20,

        content = ft.Column(
            controls=[
                first_row
            ]
        )
    )



    page.add(main_container)

ft.app(main)
