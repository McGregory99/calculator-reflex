import reflex as rx

from ..ui.base import base_page

def about_page() -> rx.Component:
    my_child = rx.vstack(
        rx.text("About")
    )
    
    return base_page(my_child)
