import reflex as rx

from ..ui.base import base_page

def pricing_page() -> rx.Component:
    my_child = rx.vstack(
        rx.text("Pricing")
    )
    
    return base_page(my_child)
