from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/","*","+","-"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color = "white",foreground_color = "black",
                                  multiline=False, halign="right", font_size=55, readonly=True)
        
        main_layout.add_widget(self.solution)
        buttons=[
            ["/","7","8","9"],
            ["*","4","5","6"],
            ["+","1","2","3"],
            ["-",".","0","C"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if label=="C":
                    color = "red"
                else:
                    color= "cyan"
                
                button = Button(
                    text = label, font_size=30, background_color=color,
                    pos_hint={"centre_x": 0.5, "centre_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        eq_button = Button(
            text = "=", font_size=30, background_color="cyan",
                    pos_hint={"centre_x": 0.5, "centre_y": 0.5}
        )
        eq_button.bind(on_press=self.on_solution)
        main_layout.add_widget(eq_button)
        coperayt = Label(
            text="Cette App est développée par ZERZOUR Salmane.", 
        )
        main_layout.add_widget(coperayt)
        return main_layout
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text=="C":
            self.solution.text = ""
            
        else:
            if current=="ZeroDivisionError" or current=="NameError" or current=="SyntaxError":
                self.solution.text = ""
                new_text = button_text
                self.solution.text = new_text
            elif current and (
                    self.last_was_operator and button_text in self.operators):
                return
            elif current=="" and button_text in self.operators:
                return
            else:
                new_text = current +button_text
                self.solution.text = new_text
            self.last_button=button_text
            self.last_was_operator = self.last_button in self.operators
    
    def on_solution(self, instance):
        text = self.solution.text
        if text=="ZeroDivisionError" or text=="NameError" or text=="SyntaxError":
            self.solution.text = ""
        else:
            try:
                if text:
                    solution = str(eval(self.solution.text))
                    self.solution.text = solution
            except SyntaxError:
                self.solution.text="SyntaxError"
            except NameError:
                self.solution.text="NameError"
            except ZeroDivisionError:
                self.solution.text="ZeroDivisionError"
        
        
        
if __name__ == "__main__":
    app = MainApp()
    app.run()

