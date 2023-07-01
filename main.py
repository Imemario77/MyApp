from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


class WidgetExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('1')
    slider_val_txt= StringProperty('50')
    def click(self):
        if self.count_enabled == True:
            self.count  +=1
            self.my_text  = str(self.count)
        else:
            pass
    def toggle(self,widget):
        if widget.state =="normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    def my_switch2(self, widget):
        print('switch: '+ str(widget.active))
        
    def on_slide(self, widget):
        self.slider_val_txt = str(int(widget.value))
        
class BoxLayoutExample(BoxLayout):
     pass
'''   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3= Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
'''
class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass


TheLabApp().run()