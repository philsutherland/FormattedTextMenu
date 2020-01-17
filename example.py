from src.text_menu_formatting import TextMenuFormatting as TMF
from src.text_menu import TextMenu

print("\n" + TMF.main_title("Welcome to Example Menu"))

about_us = """
    - Version 0.9.1
    - This package was designed and built by 
      Phil Sutherland on 2019-06-15"""

test_menu_1_text = """
    You could put a bunch of text here..."""

test_menu_2_text = """
    You could but even more text here..."""

about = TextMenu(
    title="About", message=about_us)


test_menu_1 = TextMenu(title="Test Menu 1", message=test_menu_1_text)

test_menu_2 = TextMenu(title="Test Menu 2",  message=test_menu_2_text)


main_menu = TextMenu(title="Main Menu", options={'Test Menu 1': test_menu_1.navigate,
                                                 'Test Menu 2': test_menu_2.navigate, 'About': about.navigate, 'Exit': 'exit'})


main_menu.navigate(None)
