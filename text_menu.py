from sys import exit
from text_menu_formatting import TextMenuFormatting as TMF


class TextMenu:
    def __init__(self, title, message="", options={'Return': 'return', 'Exit': 'exit'}):
        self.title = title
        self.message = message
        self.options = options

    def navigate(self, previous_menu, returning=False):
        # If the return button has not been selected, store the previous menu location
        if not returning:
            if previous_menu is None:
                self.previous_menu = self
            else:
                self.previous_menu = previous_menu

        # Print out title of the menu
        print(TMF.sub_title(self.title))

        # If there is a menu message, print it out
        if self.message:
            print(TMF.body_content(self.message))

        # Print the menu options out as a list
        print(TMF.options_menu(list(self.options)))

        # If a value other than an integer is entered, display error and show menu again
        try:
            selection = int(input("Select Option: "))
            selection = selection - 1
        except(BaseException):
            TMF.clear()
            print(TMF.error_title("Please only enter an integer!"))
            self.navigate(self, True)

        # Convert menu option values into a list for comparison to user selected option
        nav_map = list(self.options.values())

        # If an incorrect option is chosen, display error and show menu again
        if 0 <= selection < len(nav_map):
            if nav_map[selection] == "return":
                TMF.clear()
                self.previous_menu.navigate(self, True)
            elif nav_map[selection] == "exit":
                TMF.clear()
                print(TMF.main_title("Goodbye!"))
                exit(0)
            else:
                TMF.clear()
                nav_map[selection](self)
        else:
            TMF.clear()
            print(TMF.error_title("That option does not exist!"))
            self.navigate(self, True)
