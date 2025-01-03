import reflex as rx

from .ui.base import base_page
from . import pages, navigation


class SizeNumberState(rx.State):
    size: float = 4.5
    size_str: str = f'{size}vh'
    max_size: float = 11.0
    min_size: float = 2.0
    
    def increase_size(self):
        self.size = min(self.size + 0.5, self.max_size)
        self.size_str = f'{self.size}vh'
    
    def decrease_size(self):
        self.size = max(self.size - 0.5, self.min_size)
        self.size_str = f'{self.size}vh'

class CalculatorState(rx.State):
    display: str = "0"
    result: float = 0  # Cambiamos a float para manejar decimales
    operand1: float = 0
    operand2: float = 0
    operator: str = ""
    decimal_mode: bool = False
    
    def set_operand(self, value: str):
        if value == "." and "." in self.display.split()[-1]:
            return  # Evita múltiples puntos decimales en un número
        
        if self.display == "0" and value != ".":
            self.display = value
        else:
            self.display += value
        
        if self.operator == "":
            if value == ".":
                self.decimal_mode = True
            elif self.decimal_mode:
                self.operand1 += float(value) / (10 ** (len(str(self.operand1).split('.')[-1])))
            else:
                self.operand1 = self.operand1 * 10 + float(value)
            self.result = self.operand1
        else:
            if value == ".":
                self.decimal_mode = True
            elif self.decimal_mode:
                self.operand2 += float(value) / (10 ** (len(str(self.operand2).split('.')[-1])))
            else:
                self.operand2 = self.operand2 * 10 + float(value)
            self.result = self.calculate()

    def set_operator(self, op: str):
        if self.operand1 != 0 or self.display != "0":
            self.operator = op
            self.display += " " + op + " "
            self.decimal_mode = False

    def calculate(self):
        if self.operator == "+":
            return self.operand1 + self.operand2
        elif self.operator == "-":
            return self.operand1 - self.operand2
        elif self.operator == "*":
            return self.operand1 * self.operand2
        elif self.operator == "/":
            return self.operand1 / self.operand2 if self.operand2 != 0 else 0
        return self.operand1

    def clear(self):
        self.display = "0"
        self.result = 0
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ""
        self.decimal_mode = False

    def equals(self):
        self.result = self.calculate()
        self.display = self.format_result(self.result)
        self.operand1 = self.result
        self.operand2 = 0
        self.operator = ""
        self.decimal_mode = '.' in self.display
        if self.display == "":
            self.display = "0"

    def format_result(self, value: float) -> str:
        """Formatea el resultado para el display."""
        if value.is_integer():
            return str(int(value))
        return f"{value:.10f}".rstrip('0').rstrip('.')
    
    
    
def index():
    my_child = rx.vstack(
            rx.link(
                rx.button(
                    rx.text("About"),
                ),
                href=navigation.routes.ABOUT_US_ROUTE
            ),
            rx.link(
                rx.button(
                    rx.text("Pricing"),
                ),
                href=navigation.routes.PRICING_US_ROUTE
            ),
            rx.button('Contact us', ),
            align_items="center",
            spacing="2rem", 
            # width="100%",
        )
    
    return base_page(my_child)

def __index():
    button_number_style = {
        "font_size": SizeNumberState.size_str,  # Tamaño de fuente relativo a la altura del viewport
        "height": "100%",  # Equivalente a 60px si el tamaño de fuente raíz es 16px
        "bg": "#718096",
        "color": "#FFFFFF",
        "_hover": {"bg": "#2D3748"},  # Color más oscuro al pasar el mouse
        "_active": {"bg": "#1A202C"},  # Color aún más oscuro al hacer clic
    }
    button_operator_style = {
        "font_size": SizeNumberState.size_str,  # Tamaño de fuente relativo a la altura del viewport
        "height": "100%",  # Equivalente a 60px si el tamaño de fuente raíz es 16px
        "bg": "#A0AEC0",
        "color": "#FFFFFF",
        "_hover": {"bg": "#2D3748"},  # Color más oscuro al pasar el mouse
        "_active": {"bg": "#1A202C"},  # Color aún más oscuro al hacer clic
    }
    button_charsize_style = {
        "font_size": "2vh",
        "height": "100%",
        "bg": "#A0AEC0",
        "color": "#FFFFFF",
        "_hover": {"bg": "#2D3748"},
        "_active": {"bg": "#1A202C"},
    }
    
    return base_page(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.text(CalculatorState.display, size="9"),
                    border="2px solid black",
                    padding="0.75rem",
                    border_radius="0.5rem",
                    width="100%",
                    bg="#F7FAFC",  # Color de fondo gris claro
                    text_align="right",  # Alinea el texto a la derecha
                    font_family="monospace",  # Usa una fuente monoespaciada
                ),
                width='100%',
            ),
            rx.hstack(
                rx.grid(
                    rx.button("1", **button_number_style, on_click=CalculatorState.set_operand("1")),
                    rx.button("2", **button_number_style, on_click=CalculatorState.set_operand("2")),
                    rx.button("3", **button_number_style, on_click=CalculatorState.set_operand("3")),
                    rx.button("4", **button_number_style, on_click=CalculatorState.set_operand("4")),
                    rx.button("5", **button_number_style, on_click=CalculatorState.set_operand("5")),
                    rx.button("6", **button_number_style, on_click=CalculatorState.set_operand("6")),
                    rx.button("7", **button_number_style, on_click=CalculatorState.set_operand("7")),
                    rx.button("8", **button_number_style, on_click=CalculatorState.set_operand("8")),
                    rx.button("9", **button_number_style, on_click=CalculatorState.set_operand("9")),
                    rx.button("0", **button_number_style, on_click=CalculatorState.set_operand("0")),
                    rx.button(".", **button_number_style, on_click=CalculatorState.set_operand(".")),
                    rx.button("C", **button_operator_style, on_click=CalculatorState.clear),
                    columns='3',
                    spacing='2',
                    width='75%',
                    height='100%',
                ),
                rx.grid(
                    rx.button("+", **button_operator_style, on_click=CalculatorState.set_operator("+")),
                    rx.button("-", **button_operator_style, on_click=CalculatorState.set_operator("-")),
                    rx.button("*", **button_operator_style, on_click=CalculatorState.set_operator("*")),
                    rx.button("/", **button_operator_style, on_click=CalculatorState.set_operator("/")),
                    rx.button("=", **button_operator_style, on_click=CalculatorState.equals),
                    columns='1',
                    spacing='2',
                    width='25%',
                    height='100%',
                ),
                spacing='4',
                width='100%',
                height='30rem',
                
            ),
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.button("-", **button_charsize_style, on_click=SizeNumberState.decrease_size),
                        rx.text(f"Size: {SizeNumberState.size_str}", size="4", font_size="2vh", height="100%"),
                        rx.button("+", **button_charsize_style, on_click=SizeNumberState.increase_size),
                        
                        align_items="center",
                        justify_content="center",
                        spacing="1rem",
                    ),
                    # border="2px solid #A0AEC0",
                    padding="0.75rem",
                    # border_radius="0.5rem",
                    width="100%",
                    text_align="center",
                    font_family="monospace",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ),
                width='100%',
                justify_content="center",
                height='100%'
            ),
            
            width='50%',
            margin='2rem'
        ),
        
        
        
        
        width='100%',
    )

app = rx.App()
app.add_page(index)
app.add_page(
    pages.about_page, 
    route=navigation.routes.ABOUT_US_ROUTE
)
app.add_page(
    pages.pricing_page, 
    route=navigation.routes.PRICING_US_ROUTE
)
# app.add_page(
#     pages.contact_page, 
#     route=navigation.routes.CONTACT_ROUTE
# )