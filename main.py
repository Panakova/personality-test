import kivy
kivy.require('1.11.1')

from db import MYDataBase
#from database import DataBase
from helpers import screen_helper

from result import BehaviorModel1, BehaviorModel2, BehaviorModel3, BehaviorModel4

from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton,MDFloatingActionButton, MDRectangleFlatButton, MDFloatingActionButtonSpeedDial, MDFlatButton, MDRoundFlatButton
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.menu import MDDropdownMenu, RightContent
from kivy.uix.dropdown import DropDown
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelOneLine
from kivymd.uix.list import StringProperty,ThreeLineAvatarIconListItem


from kivy.properties import BooleanProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.factory import Factory
from kivymd.toast import toast
from kivy.animation import Animation
from kivymd.uix.bottomsheet import MDCustomBottomSheet


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, choice):
        choice.active = True
        check_list = choice.get_widgets(choice.group)
        for check in check_list:
            if check != choice:
                check.active = False

class HomeScreen(Screen):
    choose_dialog= None
    choice = None
    help_dialog= None

    def show_ChooseDialog(self):
        self.choose_dialog = MDDialog(title="Test zameraný pre:", type="confirmation",
                size_hint=[0.9, 0.5], auto_dismiss=False,
                items=[ItemConfirm(text="osobné zlepšenie",on_release= self.next_page_me,
                                   on_press= self.close_choose_dialog,),
                        ItemConfirm(text="prácu v tíme", on_release= self.next_page_team,
                                    on_press= self.close_choose_dialog, ),
                        ItemConfirm(text="osobné vzťahy",on_release= self.next_page_we,
                                    on_press= self.close_choose_dialog,)],)
        self.choose_dialog.open()


    def close_choose_dialog(self, obj):
        self.choose_dialog.dismiss()
        print(self.choose_dialog.items)

    def next_page_me (self,obj):
        self.manager.current = "motivationme"
    def next_page_team (self,obj):
        self.manager.current = "motivationteam"
    def next_page_we (self,obj):
        self.manager.current = "motivationwe"

    def show_HelpDialog(self):
        ok_button = MDRectangleFlatButton (text= "Rozummiem",on_release=self.close_help_dialog)
        self.help_dialog = MDDialog(title="O čo v teste ide?", text="obkec",
                              size_hint=[0.8, 0.5], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog.open()

    def close_help_dialog(self,obj):
        self.help_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class MotivationScreenMe(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("package.txt", "w")
        file.write(self.ids.nazov_testu.text)


class MotivationScreenTeam(Screen):
    nazov_testu = ObjectProperty(None)
    created= ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("package.txt", "w")
        file.write(self.ids.nazov_testu.text)

class MotivationScreenWe(Screen):
    nazov_testu = ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("package.txt", "w")
        file.write(self.ids.nazov_testu.text)

class TestConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, choice):
        choice.active = True
        check_list = choice.get_widgets(choice.group)
        for check in check_list:
            if check != choice:
                check.active = False

class TestScreenV(Screen):
    d= 0
    i= 0
    s=0
    k=0
    n=0
    snackbar = None
    p = 0
    r = 0
    def d(self,d):
        self.d= d+1
        print(d)
    def i(self,i):
        self.i=i+1
        print(i)
    def s(self,s):
        self.s=s+1
        print(s)
    def k(self,k):
        self.k=k+1
        print(k)
    def n(self,n):
        self.n=n+1
        print(n)
    def show_example_snackbar(self):
        self.snackbar = Snackbar(text="Pokračovať na druhý test?",
                                    snackbar_x="10dp",
                                    snackbar_y="10dp",
                                 bg_color= (0.96,0.79,0.09, 1),)
        self.snackbar.size_hint_x = ( Window.width -
                                      (self.snackbar.snackbar_x * 2)) / Window.width
        self.snackbar.buttons = [MDFlatButton(text="Áno",text_color=(1, 1, 1, 1),
                                              on_release=self.evaluate,
                                              on_press= self.snackbar.dismiss),]
        self.snackbar.open()

    def evaluate (self,obj):
        self.manager.current= "testm"
        self.manager.transition.direction = 'left'

    def plus(self):
        self.p = self.p +4.16
        self.ids.progress.value = self.p

class TestScreenM(Screen):
    snackbar = None
    p = 0
    r = 0
    def show_example_snackbar(self):

        self.snackbar = Snackbar(text="Naozaj ukončiť ?",
                                    snackbar_x="10dp",
                                    snackbar_y="10dp",
                                 bg_color= (0.96,0.79,0.09, 1),)
        self.snackbar.size_hint_x = ( Window.width -
                                      (self.snackbar.snackbar_x * 2)) / Window.width
        self.snackbar.buttons = [MDFlatButton(text="Uložiť",text_color=(1, 1, 1, 1),
                                              on_release=self.evaluate,
                                              on_press= self.snackbar.dismiss),]
        self.snackbar.open()

    def evaluate (self,obj):
        self.manager.current= "history"
        self.manager.transition.direction = 'left'

    def plus(self):
        self.p = self.p +4.16
        self.ids.progress.value = self.p

class MeContent(MDBoxLayout):
    model = ObjectProperty(None)
    ciel1 = ObjectProperty(None)

    def submit(self):
        if self.ids.model.text != "":
            file = open("package.txt", "w")
            file.write(self.ids.model.text)
            self.reset()

class TeamContent(MDBoxLayout):
    pass
class WeContent(MDBoxLayout):
    pass
class AContent(MDBoxLayout):
    pass
class MyGoalsScreen (Screen):

    def main_navigate(self, button):

        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class GoalsScreen(Screen):
    model = ObjectProperty (None)
    panel_is_open = False
    ciel1= ObjectProperty(None)

    def submit(self):
        if self.ids.model.text != "":

            file = open("package.txt", "w")
            file.write(self.ids.model.text)
            self.reset()

    def on_enter(self):
        self.ids.cards.clear_widgets()
        self.panel0 = MDExpansionPanel(icon="flash",content=AContent(),
                                       panel_cls=MDExpansionPanelOneLine(text="Definuj si ciele"), )

        self.ids.cards.add_widget(self.panel0)
        self.panel0.bind(on_open=self.panel_open, on_close=self.panel_close)

        self.panel1 = MDExpansionPanel(icon="human-greeting",content=MeContent(),
                panel_cls=MDExpansionPanelOneLine(text="Ja"),)

        self.ids.cards.add_widget(self.panel1)
        self.panel1.bind(on_open=self.panel_open, on_close=self.panel_close)

        self.panel2 = MDExpansionPanel(icon="human-capacity-increase", content=TeamContent(),
                                       panel_cls=MDExpansionPanelOneLine(text="Tím"), )

        self.ids.cards.add_widget(self.panel2)
        self.panel2.bind(on_open=self.panel_open, on_close=self.panel_close)

        self.panel3 = MDExpansionPanel(icon="human-male-female", content=WeContent(),
                                       panel_cls=MDExpansionPanelOneLine(text="Vzťah"), )

        self.ids.cards.add_widget(self.panel3)
        self.panel3.bind(on_open=self.panel_open, on_close=self.panel_close)

    def panel_open(self, *args):
        self.panel_is_open = True

    def panel_close(self, *args):
        self.panel_is_open = False

    def show_smart(self):
        self.smart_dialog = MDDialog(title="Technika SMART", text="Tvoj cieľ mousí byť: \n\n"
                                                                  "S- špecifický, pretože musíme vedieť čo\n"
                                                                  "M- merateľný, aby sme vedeli definovať pokrok\n"
                                                                  "A- akceptovaný, pre istotu, že všetic relevantí vedia a súhlasia\n"
                                                                  "R- realistický, aby bolo jasné, že stojíme nohami na zemi\n"
                                                                  "T– termínovaný, určený do kedy má byť splnený\n"
                                                                  "\n\n"
                                                                  "Mal by zodpovedať tieto otázky:\n\n"
                                                                  "- Čo potrebuje zmenu?\n"
                                                                  "- Aká zmena je potrebná?\n"
                                                                  "- Na koho je zmena zameraná?\n"
                                                                  "- Kde sa zmena uplatní?\n"
                                                                  "- Kedy sa zmena uplatní?\n",
                                    size_hint=[0.8, None], auto_dismiss=True,)
        self.smart_dialog.open()


    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class Content(MDBoxLayout):
    pass

class CustomItem(ThreeLineAvatarIconListItem):

    def sh_delete_item(self):
        yes_button = MDFillRoundFlatButton (text="Zmazať", on_release=self.close_del_dialog
                                            ,on_press= self.delete_item)
        no_button = MDRoundFlatButton (text= "Zrušiť", on_release= self.close_del_dialog)
        self.del_dialog = MDDialog(title="Naozaj zmazať test?",
                                    size_hint=[0.8, 0.5], auto_dismiss=False,
                                    buttons=[ no_button,yes_button])
        self.del_dialog.open()

    def close_del_dialog(self, obj):
        self.del_dialog.dismiss()

    def delete_item(self, item):
        self.parent.get_screen('history')
        self.panel.content.remove_widget(item)
        self.panel.height -= item.height
        for index, val in enumerate(self.panel.content.children[::-1]):
            val.secondary_text = str(index + 1)

    icon = StringProperty('')


class HistoryScreen(Screen):
    panel_is_open = False
    custom_sheet = None
    def on_enter(self):
        self.ids.panel_container.clear_widgets()
        self.panel= MDExpansionPanel(icon="all.png", panel_cls=MDExpansionPanelOneLine(
                        text="Moje testy",),
                    content=Content())

        self.ids.panel_container.add_widget(self.panel)
        self.panel.bind(on_open=self.panel_open, on_close=self.panel_close)

    def panel_open(self, *args):
        self.panel_is_open = True

    def panel_close(self, *args):
        self.panel_is_open = False

    def delete_item(self, item):
        self.panel.content.remove_widget(item)
        self.panel.height -= item.height
        for index, val in enumerate(self.panel.content.children[::-1]):
            val.secondary_text = str(index + 1)

    def add_into_panel(self, Názov, interval):
        item = CustomItem(text=f"{len(self.panel.content.children) + 1} Názov",
                          secondary_text="ukazovatel",tertiary_text="datoum" ,icon="book-outline")
        self.panel.content.add_widget(item)
        if self.panel_is_open and len(self.panel.content.children) > 1:
            self.panel.height += item.height
        elif self.panel_is_open and len(self.panel.content.children) == 1:
            self.panel.height -= (self.panel.height - item.height) - self.panel.panel_cls.height

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("Model správania", lambda x: x,icon='account-group-outline')
#for y in 1,2,3,4,12,13,14,21,23,24,31,32,34,41,42,43,123,124,134,234:
#   bs.add_item(f"{len(self.bs.children) + y} osobnosť",lambda x: self.behavior1(),icon='account-group-outline')
        bs.add_item("1", lambda x: self.behavior1(), icon='account-group-outline')
        bs.add_item("2", lambda x: self.behavior2(), icon='account-group-outline')
        bs.add_item("3", lambda x: self.behavior3(),icon='account-group-outline' )
        bs.add_item("4", lambda x: self.behavior4(),icon='account-group-outline' )
        bs.add_item("12", lambda x: self.behavior12(),icon='account-group-outline' )
        bs.add_item("13", lambda x: self.behavior13(), icon='account-group-outline')
        bs.add_item("14", lambda x: self.behavior14(), icon='account-group-outline')
        bs.add_item("21", lambda x: self.behavior21(), icon='account-group-outline')

        bs.open()

    def behavior1(self):
        self.manager.current = "1"
    def behavior2(self):
        self.manager.current = "2"
    def behavior3(self):
        self.manager.current = "3"
    def behavior4(self):
        self.manager.current = "4"
    def behavior12(self):
        self.manager.current = "12"
    def behavior13(self):
        self.manager.current = "13"
    def behavior14(self):
        self.manager.current = "14"
    def behavior21(self):
        self.manager.current = "21"


    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel12(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel13(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel14(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel21(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel23(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel24(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel31(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel32(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel34(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel41(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel42(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel43(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel123(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel124(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel134(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel234(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"



class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"


        db= MYDataBase()

        screen = Builder.load_string(screen_helper)
        return screen

MainApp().run()
