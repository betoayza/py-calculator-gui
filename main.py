import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# el parametro es la clase de la cual hereda


class Calculator(App):

    def build(self):
        base_layout = GridLayout(cols=1, rows=6)  
        buttons_layout = GridLayout(cols=4)      

        self.result = Label(text="0", font_size=15,
                            halign='right', valign='middle')
        base_layout.add_widget(self.result)

        # botones
        buttons = ["AC", "7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   ".", "0", "/", "="]

        for button in buttons:
            if button == "=":
                btn = Button(text=button, font_size=30,
                             background_color=("cyan"))
            elif button in ["+", "-", "*", "/"]:
                btn = Button(text=button, font_size=30,
                             background_color="yellow")
            elif button == "AC":
                btn = Button(text=button, font_size=30,
                             background_color=("red"))
            else:
                btn = Button(text=button, font_size=30)
            
            btn.bind(on_press=self.press_button) # relaciona el boton a una funcion/evento
            
            buttons_layout.add_widget(btn) # adjunta al diseño

        # agregar al diseño base el de los botones
        base_layout.add_widget(buttons_layout)

        return base_layout

    def press_button(self, instance):  # instance es eñ botón específico que se presionó
        pass


# Dunder main para apps complejas
if __name__ == "__main__":
    # Corre la app
    Calculator().run()
