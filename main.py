from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# إعدادات الشاشة (خلفية كحلي ملكي)
Window.clearcolor = (0.02, 0.05, 0.15, 1)

class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.85, 0.65, 0.13, 1) # ذهبي
        self.color = (1, 1, 1, 1)
        self.font_size = '18sp'
        self.bold = True

class MainMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # العنوان
        title = Label(text="AL-HISN 26\nSUPER ELITE", font_size='40sp', 
                      color=(0.85, 0.65, 0.13, 1), bold=True, halign='center')
        
        # الأزرار الرئيسية
        btn_play = StyledButton(text="إدارة الفريق (My Team)")
        btn_play.bind(on_release=lambda x: setattr(self.manager, 'current', 'squad'))
        
        btn_transfer = StyledButton(text="سوق الانتقالات (Transfers)")
        btn_transfer.bind(on_release=lambda x: setattr(self.manager, 'current', 'transfers'))
        
        layout.add_widget(title)
        layout.add_widget(btn_play)
        layout.add_widget(btn_transfer)
        self.add_widget(layout)

class SquadScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20)
        
        header = Label(text="تشكيلة الحصن الذهبية", font_size='25sp', color=(0.85, 0.65, 0.13, 1))
        layout.add_widget(header)

        # عرض اللاعب الأسطوري
        legend_card = Label(text="CAPTAIN: YOUNIS MAHMOUD\nRating: 99 | Pos: CF\nStatus: LEGENDARY", 
                            size_hint_y=None, height=200, color=(1, 1, 1, 1))
        layout.add_widget(legend_card)

        btn_back = Button(text="العودة", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        
        layout.add_widget(btn_back)
        self.add_widget(layout)

class TransferScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        players = [
            {"name": "Lionel Messi", "rating": "97", "pos": "RW"},
            {"name": "C. Ronaldo", "rating": "95", "pos": "ST"},
            {"name": "Neymar Jr", "rating": "93", "pos": "LW"}
        ]
        
        layout.add_widget(Label(text="سوق النجوم", font_size='25sp', color=(0.85, 0.65, 0.13, 1)))
        
        for p in players:
            btn = StyledButton(text=f"{p['name']} | {p['pos']} | OVR: {p['rating']}")
            layout.add_widget(btn)
            
        btn_back = Button(text="العودة", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class AlHisnApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(SquadScreen(name='squad'))
        sm.add_widget(TransferScreen(name='transfers'))
        return sm

if __name__ == '__main__':
    AlHisnApp().run()