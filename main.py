import kivy
kivy.require('1.11.1')


from helpers import screen_helper

from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import Button, MDFillRoundFlatButton,MDFloatingActionButton, MDRectangleFlatButton, MDFloatingActionButtonSpeedDial, MDFlatButton, MDRoundFlatButton
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
from kivymd.uix.textfield import MDTextField
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
        if not self.choose_dialog:
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
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class MotivationScreenMe(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def test_name(self):
        subor = open("package.txt", "w")
        subor.write(self.ids.nazov_testu.text)


class MotivationScreenTeam(Screen):
    nazov = ObjectProperty(None)
    nazov_testu = ObjectProperty(None)
    created= ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def test_name(self):
        subor = open("package.txt", "w")
        subor.write(self.ids.nazov_testu.text)

class MotivationScreenWe(Screen):
    nazov = ObjectProperty(None)
    nazov_testu = ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def test_name(self):
        subor = open("package.txt", "w")
        subor.write(self.ids.nazov_testu.text)

class TestConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, choice):
        choice.active = True
        check_list = choice.get_widgets(choice.group)
        for check in check_list:
            if check != choice:
                check.active = False

class TestScreenV(Screen):
    snackbar = None
    p = 0
    r = 0
    def show_example_snackbar(self):
        if not self.snackbar:
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
        if not self.snackbar:
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
    pass
class TeamContent(MDBoxLayout):
    pass
class WeContent(MDBoxLayout):
    pass

class GoalsScreen(Screen):
    def on_enter(self):
        self.ids.mecard.add_widget(
            MDExpansionPanel(on_open=self.panel_open,
                on_close=self.panel_close,
                icon="human-greeting",content=MeContent(),
                panel_cls=MDExpansionPanelOneLine(text="Ja (definuj si ciele)"),))

        self.ids.teamcard.add_widget(
            MDExpansionPanel(on_open=self.panel_open,
                             on_close=self.panel_close,
                             icon="human-capacity-increase", content=TeamContent(),
                             panel_cls=MDExpansionPanelOneLine(text="Tím (definuj si ciele)"), ))

        self.ids.wecard.add_widget(
            MDExpansionPanel(on_open=self.panel_open,
                             on_close=self.panel_close,
                             icon="human-male-female", content=WeContent(),
                             panel_cls=MDExpansionPanelOneLine(text="Vzťah (definuj si ciele)"), ))


    def panel_open(self, *args):
        self.panel_is_open = True

    def panel_close(self, *args):
        self.panel_is_open = False


    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class Content(MDBoxLayout):
    pass
    
class CustomItem(ThreeLineAvatarIconListItem):

    def delete_item(self, item):
        self.parent.get_screen('history')
        self.panel.content.remove_widget(item)
        self.panel.height -= item.height
        for index, val in enumerate(self.panel.content.children[::-1]):
            val.secondary_text = str(index + 1)

    icon = StringProperty('')


class HistoryScreen(Screen):
    panel_is_open = False
    def on_enter(self):
        self.ids.panel_container.clear_widgets()  # to avoid re-adding panel each time


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

    def show_bottom_sheet(self,):
        bottom_sheet_menu = MDListBottomSheet(
            bg_color=[1, 1, 1, 1],
            radius_from="top",)

        for i in range(1, 22):
            bottom_sheet_menu.add_item(

                f"d {i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"d {y}"
                ),
            )
        bottom_sheet_menu.open()

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


        screen = Builder.load_string(screen_helper)
        return screen



MainApp().run()
