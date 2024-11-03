import reflex as rx

from ..ui.base import base_page
from .. import navigation

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Contact Us", size="8", margin_bottom="1em"),
        rx.text("Get in touch with us!", margin_bottom="2em"),
        rx.vstack(
            rx.input(placeholder="Name", width="100%"),
            rx.input(placeholder="Email", width="100%"),
            rx.text_area(placeholder="Your message", width="100%", height="150px"),
            rx.button("Send Message", width="100%"),
            spacing="1em",
            width="100%",
            max_width="500px",
            padding="2em",
            border="1px solid #eaeaea",
            border_radius="8px",
        ),
        width="100%",
        align_items="center",
        spacing="2em",
        padding="2em",
    )
    
    return base_page(my_child)
